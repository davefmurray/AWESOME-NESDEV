# Scrolling internals

The PPU keeps four fields:

| Field | Meaning |
|---|---|
| `v` | current VRAM address (15 bits) |
| `t` | temporary VRAM address / top-left tile |
| `x` | fine X scroll (3 bits) |
| `w` | write toggle (1 bit) |

`v` layout: `yyy NN YYYYY XXXXX` — fine Y, nametable, coarse Y, coarse X.

## Writes

| Action | Effect |
|---|---|
| `$2000` write | `t` nametable bits 10–11 ← data bits 0–1 |
| `$2005` first | `t` coarse X ← data bits 3–7; `x` ← data bits 0–2; `w`=1 |
| `$2005` second | `t` fine Y ← data bits 0–2; `t` coarse Y ← data bits 3–7; `w`=0 |
| `$2006` first | `t` bits 8–13 ← data bits 0–5; `t` bit 14=0; `w`=1 |
| `$2006` second | `t` bits 0–7 ← data; `v` ← `t`; `w`=0 |
| `$2002` read | `w`=0; clears vblank flag |
| `$2007` access | increments `v` by 1 or 32 (outside rendering) |

## Automatic copies during rendering

- Dot 256: increment vertical position in `v`.
- Dot 257: copy horizontal bits from `t` to `v`.
- Pre-render dots 280–304: copy vertical bits from `t` to `v`.
- Dots 328–336 and 8–256: increment horizontal position for fetches.

## Practical rules

1. Set scroll at the end of vblank, after VRAM writes.
2. Write X then Y to `$2005`, then nametable bits to `$2000`.
3. Reading `$2002` resets the latch; do it before `$2006` when starting a VRAM upload.
4. A split screen needs a second scroll write mid-frame, timed by sprite 0 or a mapper IRQ.
5. If the split is at the top of the screen, use `$2006` to set the nametable and skip the status bar.

## Split-screen recipe (sprite 0)

1. Put sprite 0 at the split line, over an opaque background tile.
2. In the main loop, wait for `$2002` bit 6.
3. Read `$2002` to clear the hit.
4. Write the new scroll (`$2005`/`$2000`) or a new `$2006` address.
5. Restore the scroll next frame in NMI.

The wait loop must not be interrupted by NMI doing PPU writes; disable NMI or keep the handler from touching `$2006`.
