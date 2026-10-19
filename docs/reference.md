# Reference

The tables you will look up ten times a day. All values are NTSC unless noted. Authoritative source: [NESdev wiki](https://www.nesdev.org/wiki/).

## CPU memory map

| Range | Contents |
|---|---|
| `$0000–$07FF` | 2 KB internal RAM |
| `$0800–$1FFF` | Mirrors of `$0000–$07FF` (every `$0800`) |
| `$2000–$2007` | PPU registers |
| `$2008–$3FFF` | Mirrors of `$2000–$2007` (every 8 bytes) |
| `$4000–$4017` | APU and I/O (controllers, DMA) |
| `$4018–$401F` | Normally disabled |
| `$4020–$5FFF` | Cartridge expansion |
| `$6000–$7FFF` | Cartridge RAM / WRAM (often battery-backed) |
| `$8000–$FFFF` | PRG ROM (banked on most mappers) |

Stack: `$0100–$01FF`, descending from `$01FF`. Zero page `$00–$FF` is the fast-access area — use it for pointers and hot variables.

## PPU registers

| Address | Name | Bits |
|---|---|---|
| `$2000` | PPUCTRL | 7 NMI enable · 5 sprite size (8×16) · 4 BG pattern table · 3 sprite pattern table · 2 VRAM increment (1/32) · 1–0 base nametable |
| `$2001` | PPUMASK | 7–5 emphasis · 4 sprites · 3 background · 2 left-column sprites · 1 left-column BG · 0 greyscale |
| `$2002` | PPUSTATUS | 7 vblank · 6 sprite 0 hit · 5 sprite overflow · 4–0 open bus |
| `$2003` | OAMADDR | OAM write address |
| `$2004` | OAMDATA | OAM read/write |
| `$2005` | PPUSCROLL | write X, then Y |
| `$2006` | PPUADDR | write high byte, then low |
| `$2007` | PPUDATA | read/write PPU memory (buffered reads) |
| `$4014` | OAMDMA | copy 256 bytes from CPU page to OAM |

Two rules that cause most bugs:

- Reading `$2002` clears the write latch for `$2005`/`$2006`. Read it before setting scroll or address.
- Do not write `$2007` while rendering is enabled unless you know exactly what you are doing; it corrupts the address and can glitch the screen.

## PPU memory map

| Range | Contents |
|---|---|
| `$0000–$0FFF` | Pattern table 0 (256 tiles) |
| `$1000–$1FFF` | Pattern table 1 (256 tiles) |
| `$2000–$23FF` | Nametable 0 (32×30 tiles + attributes) |
| `$2400–$27FF` | Nametable 1 |
| `$2800–$2BFF` | Nametable 2 |
| `$2C00–$2FFF` | Nametable 3 |
| `$3000–$3EFF` | Mirrors of `$2000–$2EFF` |
| `$3F00–$3F1F` | Palettes (16 BG, 16 sprite) |
| `$3F20–$3FFF` | Mirrors of `$3F00–$3F1F` |

Palette notes:

- `$3F00` is the universal background color, also used for transparency.
- `$3F10/$3F14/$3F18/$3F1C` mirror `$3F00/$3F04/$3F08/$3F0C` — a common source of "why is my sprite background wrong".
- Values are 6-bit NES palette indices (`$00–$3F`), not RGB.

## OAM

64 sprites, 4 bytes each, at `$0200` in most homebrew (then DMA'd to `$4014`):

| Byte | Meaning |
|---|---|
| 0 | Y position (top minus 1) |
| 1 | Tile index |
| 2 | Attributes: palette (bits 1–0), priority (5), flip H (6), flip V (7) |
| 3 | X position |

Y = `$F0`–`$FF` hides a sprite. Only 8 sprites per scanline and 64 per screen; more causes flicker or dropout.

## CHR tile format

Each 8×8 tile is 16 bytes: 8 bytes for bitplane 0 (LSB), then 8 for bitplane 1 (MSB). For each pixel, the two bits select one of four palette colors. Row `y` is `plane0[y]` then `plane1[y]`.

## iNES header

| Offset | Size | Meaning |
|---|---|---|
| 0–3 | 4 | `4E 45 53 1A` ("NES" + MS-DOS EOF) |
| 4 | 1 | PRG ROM size in 16 KB units |
| 5 | 1 | CHR ROM size in 8 KB units (0 = CHR-RAM) |
| 6 | 1 | bit 0 mirroring (0 horizontal, 1 vertical) · bit 1 battery · bit 2 trainer · bit 3 four-screen · bits 4–7 mapper low nibble |
| 7 | 1 | bits 0–1 console type · bits 2–3 NES 2.0 marker (`10`) · bits 4–7 mapper high nibble |
| 8 | 1 | PRG RAM size in 8 KB units (NES 2.0: mapper high bits + submapper) |
| 9 | 1 | bit 0 TV system (1 = PAL) |
| 10 | 1 | unofficial TV system / PRG RAM / bus conflicts |
| 11–15 | 5 | padding (should be zero) |

Mapper number = `((byte7 >> 4) << 4) | (byte6 >> 4)`.

### NES 2.0 in one paragraph

If byte 7 bits 3–2 are `10`, the file is NES 2.0. It adds extended mapper bits, submapper, exponent-multiplier ROM sizes and explicit RAM sizes in bytes 8–10. Most emulators accept both; when writing a header, prefer NES 2.0 for new homebrew and iNES for maximum compatibility. Spec: <https://www.nesdev.org/wiki/NES_2.0>.

## Vectors

| Address | Vector |
|---|---|
| `$FFFA–$FFFB` | NMI |
| `$FFFC–$FFFD` | RESET (entry point) |
| `$FFFE–$FFFF` | IRQ / BRK |

Little-endian. In ca65:

```asm
.segment "VECTORS"
    .word nmi, reset, irq
```

## Common mappers

| # | Name | PRG | CHR | Typical use |
|---|---|---|---|---|
| 0 | NROM | 16/32 KB fixed | 8 KB ROM or RAM | launch titles, small homebrew |
| 1 | MMC1 | 16 KB switchable | 4/8 KB switchable | 80s carts, battery saves, Zelda/Metroid |
| 2 | UxROM | 16 KB switchable | 8 KB RAM | Contra, Mega Man; cheap and common |
| 3 | CNROM | 32 KB fixed | 8 KB switchable | graphics-heavy simple games |
| 4 | MMC3 | 8 KB switchable | 1 KB switchable | the workhorse; scanline IRQ |
| 5 | MMC5 | complex | complex | Castlevania III, expansion audio |
| 7 | AxROM | 32 KB switchable | 8 KB RAM | single-screen mirroring |
| 9 | MMC2 | 8 KB | 4 KB | Punch-Out!! |
| 69 | FME-7 | 8 KB | 1 KB | Famicom-only, expansion audio |

Full list: <https://www.nesdev.org/wiki/Mapper>. Mapper 0, 1, 2, 3 and 4 cover most of the library and almost all homebrew.

## Address math

For a flat 32 KB NROM (mapper 0, no banking):

```
CPU address = 0x8000 + (file offset - 16)
file offset = (CPU address - 0x8000) + 16
```

For a 16 KB NROM mapped at `$C000`:

```
CPU address = 0xC000 + (file offset - 16)
```

For banked carts, the CPU address depends on which bank is currently switched in. Do not trust a single linear formula; use the disassembler's mapper support or the debugger's live mapping.

## 6502 quick reference

Registers: `A` accumulator, `X`/`Y` index, `SP` stack pointer, `PC`, `P` flags.

Flags: `N` negative, `V` overflow, `-` unused, `B` break, `D` decimal, `I` IRQ disable, `Z` zero, `C` carry.

| Opcode | Mnemonic | Notes |
|---|---|---|
| `A9` | `LDA #imm` | load immediate |
| `A5`/`AD` | `LDA zp` / `LDA abs` | load from memory |
| `85`/`8D` | `STA zp` / `STA abs` | store |
| `20` | `JSR abs` | call subroutine |
| `60` | `RTS` | return |
| `4C` | `JMP abs` | jump |
| `D0`/`F0` | `BNE`/`BEQ rel` | branch on zero flag |
| `C9` | `CMP #imm` | compare |
| `E6`/`C6` | `INC`/`DEC zp` | increment/decrement |
| `EA` | `NOP` | 2 cycles; the classic patch |
| `48`/`68` | `PHA`/`PLA` | push/pull A |
| `78`/`58` | `SEI`/`CLI` | disable/enable IRQ |

Cycle counts matter in NMI handlers and raster tricks. A taken branch costs an extra cycle; page crossings cost an extra cycle on indexed reads.

## CDL (code/data log)

Coverage files record, per PRG byte, whether it was executed or read as data. FCEUX-style `.cdl` uses one byte per PRG byte, with bit 0 = code and bit 1 = data; emulators differ, so check the file size against the PRG size before trusting it.

Use it to:

- Split code from data in a disassembler (`retrodisasm -cdl`).
- Find unreached code (dead routines, unused banks).
- Confirm a patch region actually executes.

## Timing

| Thing | NTSC value |
|---|---|
| CPU clock | 1.7897725 MHz |
| PPU clock | 5.3693175 MHz |
| Frame rate | 60.0988 Hz |
| Cycles per frame | ~29,780 CPU cycles |
| Scanlines | 262 (240 visible) |
| Cycles per scanline | 113.67 CPU / 341 PPU |

PAL: 50.007 Hz, 312 scanlines, different music pitch and frame budget. A 60 Hz game on a PAL console runs ~17% slow.

## Further reference

- [CPU memory map](https://www.nesdev.org/wiki/CPU_memory_map)
- [PPU registers](https://www.nesdev.org/wiki/PPU_registers)
- [PPU OAM](https://www.nesdev.org/wiki/PPU_OAM)
- [iNES](https://www.nesdev.org/wiki/INES) · [NES 2.0](https://www.nesdev.org/wiki/NES_2.0)
- [Mappers](https://www.nesdev.org/wiki/Mapper)
- [APU](https://www.nesdev.org/wiki/APU)
- [Emulator tests](https://www.nesdev.org/wiki/Emulator_tests) — useful when your emulator and your code disagree
---

Part of [AWESOME NESDEV](../README.md) · [Start here](start-here.md) · [MCP servers](mcp-servers.md) · [Skills](agent-skills.md) · [Homebrew](homebrew.md) · [ROM hacking](romhacking.md)
