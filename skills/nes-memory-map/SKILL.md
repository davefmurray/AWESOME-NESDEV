---
name: nes-memory-map
description: "NES/Famicom CPU and PPU address spaces, mirroring, vectors, zero page, stack, OAM buffer, and the reset/warmup sequence. Use when placing variables, reading a memory dump, debugging a stray write, computing an address, or explaining where code and data live on the NES."
---

# NES memory map

Two address spaces, not one. The CPU sees 64 KB with holes and mirrors; the PPU sees 16 KB of pattern tables, nametables and palettes. They meet only through the PPU registers at `$2000–$2007` and OAM DMA at `$4014`.

## CPU map

| Range | Size | Contents |
|---|---|---|
| `$0000–$07FF` | 2 KB | Internal RAM |
| `$0800–$1FFF` | 6 KB | Mirrors of `$0000–$07FF`, every `$0800` |
| `$2000–$2007` | 8 B | PPU registers |
| `$2008–$3FFF` | — | Mirrors of `$2000–$2007`, every 8 bytes |
| `$4000–$4017` | 24 B | APU and I/O (controllers, DMA) |
| `$4018–$401F` | 8 B | Normally disabled (CPU test mode) |
| `$4020–$5FFF` | — | Cartridge expansion |
| `$6000–$7FFF` | 8 KB | Cartridge WRAM / PRG-RAM, often battery-backed |
| `$8000–$FFFF` | 32 KB | PRG ROM and mapper registers |

Consequences that bite:

- Writing `$0800` writes `$0000`. There is no separate second kilobyte.
- `$2000` and `$2008` are the same register.
- Reading an unmapped address returns **open bus**, not zero. Do not rely on it.
- The cartridge can observe every CPU read/write except reads of `$4015` (APU status is internal to the CPU).

## Zero page, stack, OAM buffer

| Range | Conventional use |
|---|---|
| `$0000–$00FF` | Zero page: pointers, hot variables. `LDA $00,X` is one byte shorter and one cycle faster than absolute |
| `$0100–$01FF` | Stack, descending from `$01FF` |
| `$0200–$02FF` | OAM shadow buffer, DMA'd with `$4014` each frame |
| `$0300–$07FF` | General RAM |

Zero-page indexed addressing wraps inside `$00–$FF`; absolute indexed does not. A pointer table that crosses a page needs care.

## Vectors

| Address | Vector |
|---|---|
| `$FFFA–$FFFB` | NMI |
| `$FFFC–$FFFD` | RESET |
| `$FFFE–$FFFF` | IRQ / BRK |

Supplied by the cartridge, little-endian. On banked carts, either the vector area is in a fixed bank or every bank must contain a stub.

## PPU map

| Range | Contents |
|---|---|
| `$0000–$0FFF` | Pattern table 0 (256 tiles) |
| `$1000–$1FFF` | Pattern table 1 (256 tiles) |
| `$2000–$23FF` | Nametable 0 (960 B tiles + 64 B attributes) |
| `$2400–$27FF` | Nametable 1 |
| `$2800–$2BFF` | Nametable 2 |
| `$2C00–$2FFF` | Nametable 3 |
| `$3000–$3EFF` | Mirrors of `$2000–$2EFF`; not rendered |
| `$3F00–$3F1F` | Palettes (16 BG + 16 sprite) |
| `$3F20–$3FFF` | Mirrors of `$3F00–$3F1F` |

The PPU has 2 KB of internal nametable RAM, so only two logical nametables are usually distinct; the cartridge's mirroring decides which. Palette `$3F10/$3F14/$3F18/$3F1C` mirror `$3F00/$3F04/$3F08/$3F0C` — sprite color 0 is background color 0.

## Registers at a glance

| Address | Name | Job |
|---|---|---|
| `$2000` | PPUCTRL | NMI enable, sprite size, pattern table select, VRAM increment, nametable base |
| `$2001` | PPUMASK | Rendering enable, left-column clipping, emphasis, greyscale |
| `$2002` | PPUSTATUS | Vblank, sprite 0 hit, overflow; read clears the write latch |
| `$2003` | OAMADDR | OAM write pointer |
| `$2004` | OAMDATA | OAM read/write |
| `$2005` | PPUSCROLL | Scroll X then Y |
| `$2006` | PPUADDR | VRAM address high then low |
| `$2007` | PPUDATA | VRAM data; buffered reads |
| `$4014` | OAMDMA | Copy 256 bytes from CPU page to OAM |
| `$4015` | APUSTATUS | Channel enable/status |
| `$4016`/`$4017` | JOY1/JOY2 | Controller strobe/read; APU frame counter on `$4017` write |

Full bitfields: `references/registers.md`.

## Reset and PPU warmup

The PPU ignores writes to `PPUCTRL`, `PPUMASK`, `PPUSCROLL` and `PPUADDR` for roughly the first 29,658 CPU cycles. The standard wait:

```asm
  bit $2002        ; clear a possible power-on vblank flag
vwait1:
  bit $2002
  bpl vwait1
vwait2:
  bit $2002
  bpl vwait2       ; PPU is ready
```

Do RAM clear and mapper init between the two waits. Keep the loop length from dividing the frame length exactly (Dendy famiclones can otherwise livelock).

## Checks

- Does the variable address fall in `$0000–$07FF`, `$6000–$7FFF`, or ROM? A "variable" in `$8000+` is a bug.
- Is the stack pointer initialized (`LDX #$FF / TXS`) before any `JSR`?
- Does OAM DMA read from the page you think (`$4014` takes the page number in A)?
- Are you writing PPU data with rendering on? Stop rendering first.
- On a banked cart, is the vector bank currently switched in?

## Failure modes

- **Phantom writes**: `$0800` mirrors `$0000`; a stray absolute write can corrupt zero page.
- **Open bus**: reading `$4015` disconnects the external bus; the value is not what the cartridge sees.
- **OAM decay**: OAM contents are undefined at power-on and during long rendering-off periods.
- **PPU write latch**: a read of `$2002` resets the `$2005`/`$2006` toggle; interleaving writes without accounting for it corrupts the address.

## References

- [CPU memory map](https://www.nesdev.org/wiki/CPU_memory_map)
- [PPU memory map](https://www.nesdev.org/wiki/PPU_memory_map)
- [PPU power up state](https://www.nesdev.org/wiki/PPU_power_up_state)
- [Registers](https://www.nesdev.org/wiki/Registers)
- `references/address-space.md` · `references/registers.md`
