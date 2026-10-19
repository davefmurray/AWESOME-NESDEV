---
name: nes-ppu-rendering
description: "NES PPU rendering: frame timing, nametables, attributes, palettes, OAM sprites, scrolling, NMI/vblank budget, sprite 0, and the usual black-screen and glitch failures. Use when writing or debugging PPU code, enabling rendering, scrolling a level, drawing sprites, or diagnosing corrupt graphics."
---

# NES PPU rendering

The PPU draws tiles, not pixels, from its own 16 KB address space. The CPU never sees that space directly; it writes through `$2006`/`$2007` during vblank, or DMA's sprite data through `$4014`. Almost every rendering bug is one of: wrong address, wrong time, or wrong enable order.

## Frame timing (NTSC)

| Thing | Value |
|---|---|
| Dots per scanline | 341 |
| Scanlines per frame | 262 (240 visible) |
| Dots per frame | 89,342 |
| Frame rate | 60.0988 Hz |
| CPU cycles per frame | ~29,780 |
| Vblank | scanlines 241–260, ~2,273 CPU cycles |
| NMI | start of vblank, scanline 241 dot 1 |

PAL: 312 scanlines, ~106,496 dots, 50.007 Hz, ~33,247 CPU cycles/frame. Do not hardcode 60 Hz for music or timers.

## Bring-up order that works

1. Disable NMI and rendering (`$2000 = 0`, `$2001 = 0`).
2. Wait for two vblanks after power-on (see `nes-memory-map`).
3. Set the VRAM address with `$2006` (read `$2002` first to reset the latch).
4. Upload palette, nametable, attributes, and CHR-RAM tiles through `$2007`.
5. Set scroll: `$2005` X, `$2005` Y, then nametable bits in `$2000`.
6. Enable background/sprites in `$2001`.
7. Enable NMI in `$2000` if you want per-frame updates.

`$2006` and `$2005` share the write toggle. Any `$2006` write invalidates the scroll you set; set scroll **after** VRAM updates.

## Background

- Nametable: 32×30 tile indices at `$2000 + nt*$400 + y*32 + x`.
- Attribute table: 64 bytes at `+$3C0`; 2 bits per 16×16 px region, 4 regions per 32×32 px block.

```
attr_addr  = base + $3C0 + (y/4)*8 + (x/4)
attr_shift = ((y%4)/2)*4 + ((x%4)/2)*2
```

- Pattern table: 256 tiles × 16 bytes. Tile `t` at `table*$1000 + t*16`.
- CHR-RAM: you must upload tiles before enabling rendering, and every time you change them.

## Palettes

- `$3F00–$3F0F` background, `$3F10–$3F1F` sprites.
- `$3F00` is the universal background color and the transparent color.
- `$3F10/$3F14/$3F18/$3F1C` mirror the first four background entries. A sprite using palette color 0 shows the background color.
- Palette RAM is only writable through `$2006`/`$2007`. While rendering is on, writing is unreliable; do it in vblank or forced blank.
- Palette changes mid-frame are possible but need cycle-exact timing; see the wiki's "Palette change mid frame".

## Sprites (OAM)

64 entries, 4 bytes each: Y, tile, attributes, X.

| Byte | Notes |
|---|---|
| Y | Top minus 1; `$EF–$FF` hides. Sprites never appear on line 0 |
| Tile | 8×8: pattern table from `$2000` bit 3. 8×16: bit 0 selects table, low bit cleared |
| Attr | Palette 0–3 (bits 1–0), priority (5), flip H (6), flip V (7) |
| X | Left edge; `$F9–$FF` pushes it off the right |

- DMA: write the page number to `$4014` (usually `$02` for `$0200`). Costs 513 cycles, 514 on odd cycles. Do it in vblank.
- Limits: 8 sprites per scanline, 64 total. More causes flicker/dropout.
- Priority: lower OAM index wins between sprites; sprite priority bit decides against the background.
- 8×16 mode: the tile index's bit 0 selects the pattern table, not the table bit in `$2000`.
- Sprite overflow flag (`$2002` bit 5) is buggy; do not use it for logic.

### Sprite 0 hit

Set when an opaque sprite-0 pixel overlaps an opaque background pixel. Used for split-screen timing.

It does **not** trigger when:

- rendering is disabled,
- either pixel is transparent (CHR index 0),
- the overlap is in the left 8 px and clipping is enabled,
- the overlap is at x=255,
- it already happened this frame.

It is independent of priority, palette and color. Read `$2002` bit 6, then clear it by reading `$2002` (the flag clears at pre-render).

## Scrolling

The common case:

1. Compute 9-bit X/Y of the camera.
2. Write X low 8 bits to `$2005`.
3. Write Y low 8 bits to `$2005`.
4. Write X bit 8 and Y bit 8 to `$2000` bits 0–1 (base nametable).

Rules:

- Do it before the end of vblank; scroll is latched at the end of vblank.
- Do it after all `$2006` VRAM writes for the frame.
- Keep NMI short: most games upload ≤64 bytes per NMI. More needs a plan.
- For a scrolling seam, write the incoming column/row during vblank, then set scroll.
- Split screens: change scroll mid-frame with sprite 0 or a mapper IRQ (MMC3), not with a naive NMI.

The PPU's internal `v`/`t`/`x`/`w` registers and their exact copy points (dot 256, 257, 280–304) matter only for raster effects; see `references/scrolling.md` before attempting one.

## NMI

- Enable with `$2000` bit 7; fires at vblank start.
- The handler must finish PPU writes and scroll before vblank ends (~2,273 cycles).
- `$2002` read clears the vblank flag and the write latch. Reading it at the exact start of vblank can miss the flag; wait loops should not have a period that divides the frame length (a Dendy issue).
- Do not do heavy logic in NMI; set a flag and do it in the main loop.

## Checks

- Did you read `$2002` before the first `$2006` write?
- Is rendering disabled while uploading?
- Is the palette entry for the background color distinct from everything else?
- Does the nametable point at a tile that exists in CHR?
- Are you uploading CHR-RAM before enabling rendering?
- Did you set scroll after the last `$2006` write?
- Is OAM DMA in vblank, and is the source page correct?
- Are you testing at 120+ frames, not 2?

## Failure modes

| Symptom | Likely cause |
|---|---|
| Black screen | Rendering never enabled, palette all black, CHR-RAM empty, PPU warmup not respected |
| Garbage tiles | Wrong pattern table, wrong tile index, CHR bank not switched |
| Wrong colors | Attribute byte wrong, palette mirror (`$3F10`), emphasis bits |
| Sprites flicker | >8 per scanline; reorder or multiplex |
| Scroll jumps | `$2006` written after `$2005`, or NMI overran vblank |
| Split screen tears | Scroll changed at the wrong dot, or sprite 0 hit missed |
| Writes ignored | Rendering on, or PPU still in warmup |

## References

- [PPU](https://www.nesdev.org/wiki/PPU) · [PPU registers](https://www.nesdev.org/wiki/PPU_registers)
- [PPU palettes](https://www.nesdev.org/wiki/PPU_palettes) · [PPU OAM](https://www.nesdev.org/wiki/PPU_OAM)
- [PPU scrolling](https://www.nesdev.org/wiki/PPU_scrolling) · [The frame and NMIs](https://www.nesdev.org/wiki/The_frame_and_NMIs)
- `references/rendering-tables.md` · `references/scrolling.md`
