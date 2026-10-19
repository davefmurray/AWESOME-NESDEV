---
name: nes-cart-mappers
description: "Read and write iNES/NES 2.0 headers, choose a mapper, and implement NROM, UxROM, CNROM, MMC1, MMC3 or AxROM banking. Use when parsing a ROM, fixing a bad header, adding PRG/CHR banks, dealing with mirroring or battery saves, or debugging a bank-switch crash."
---

# NES cartridges and mappers

A `.nes` file is a 16-byte header plus PRG ROM, CHR ROM, and optionally a trainer. The header tells the emulator which mapper hardware to emulate. A wrong header is indistinguishable from a broken game.

## iNES header

| Byte | Meaning |
|---|---|
| 0–3 | `4E 45 53 1A` ("NES" + EOF) |
| 4 | PRG size in 16 KB units |
| 5 | CHR size in 8 KB units (0 = CHR-RAM) |
| 6 | bit 0 mirroring (0 horizontal, 1 vertical) · bit 1 battery · bit 2 trainer · bit 3 four-screen · bits 4–7 mapper low nibble |
| 7 | bits 0–1 console type · bits 2–3 `10` = NES 2.0 · bits 4–7 mapper high nibble |
| 8 | iNES: PRG-RAM size in 8 KB units (0 ≈ 8 KB) |
| 9 | iNES: bit 0 TV system (1 = PAL) |
| 10–15 | iNES: unofficial / padding |

Mapper number = `(flags7 & 0xF0) | (flags6 >> 4)`.

### NES 2.0 differences

- Byte 7 bits 3–2 = `10` marks NES 2.0.
- Byte 8: low nibble = mapper bits 8–11; high nibble = submapper.
- Byte 9: low nibble = PRG size MSB; high nibble = CHR size MSB.
- Byte 10: PRG-RAM (low nibble) / PRG-NVRAM (high nibble), size = `64 << value` bytes (0 = none).
- Byte 11: CHR-RAM / CHR-NVRAM, same encoding.
- Byte 12: TV system / timing (0 NTSC, 1 PAL, 2 dual, 3 Dendy).

Prefer NES 2.0 for new homebrew; it can express CHR-RAM and RAM sizes that iNES cannot.

## Choosing a mapper

| Mapper | Name | PRG | CHR | Use |
|---|---|---|---|---|
| 0 | NROM | 16/32 KB fixed | 8 KB ROM or RAM | Small games, first project |
| 2 | UxROM | 16 KB switchable, last fixed | 8 KB RAM | Simple large games; cheap boards |
| 3 | CNROM | 32 KB fixed | 8 KB switchable | Graphics variety, no PRG banking |
| 1 | MMC1 | 16 KB switchable + fixed | 4/8 KB switchable | Saves, flexible banking |
| 4 | MMC3 | 8 KB switchable | 1 KB switchable | Scanline IRQ, larger games |
| 7 | AxROM | 32 KB switchable | 8 KB RAM | Single-screen mirroring |

Start with NROM. Move to UxROM/MMC1 for size, MMC3 only when you need the IRQ or fine CHR banking.

## NROM

- 16 KB PRG mirrored at `$8000` and `$C000`, or 32 KB at `$8000`.
- 8 KB CHR-ROM or CHR-RAM.
- Vectors at `$FFFA`; no banking init.
- Header: `.byte 2, 1, 0, 0` for 32 KB PRG + 8 KB CHR.

## UxROM / UNROM

- 16 KB switchable at `$8000–$BFFF`; last bank fixed at `$C000–$FFFF`.
- Write the bank number to `$8000–$FFFF`. Bus conflicts require the written value to match the ROM byte at the destination — use a lookup table in ROM.
- CHR-RAM: copy tiles from the switched PRG bank, then enable rendering.

```asm
; bank table in the fixed bank
banktable: .byte $00,$01,$02,$03,$04,$05,$06

bankswitch_y:
  tya
  sta banktable,y    ; read-modify-write the table; value matches ROM
  rts
```

## MMC1

Serial interface: five writes to `$8000–$FFFF`, LSB first. A write with bit 7 set resets the shift register and sets fixed-$C000 mode.

Registers:

| Write # | Bits | Meaning |
|---|---|---|
| 1 | 0–1 | mirroring: 0 one-screen lower, 1 one-screen upper, 2 vertical, 3 horizontal |
| 2 | 2–3 | PRG mode: 0/1 = 32 KB at $8000, 2 = fix first at $C000, 3 = fix last at $C000 |
| 2 | 4 | CHR mode: 0 = 8 KB, 1 = two 4 KB |
| 3 | 0–4 | CHR bank |
| 4 | 0–4 | PRG bank (low bit ignored in 32 KB mode) |

Init for UNROM-like behavior (fixed last bank, 8 KB CHR):

```asm
  lda #$0E        ; vertical mirroring, fixed $C000, 8 KB CHR
  sta $8000
  lsr a
  sta $8000
  lsr a
  sta $8000
  lsr a
  sta $8000
  lsr a
  sta $8000
```

Put a reset stub and vectors in **every** 16 KB bank: some MMC1 revisions power up in an unknown mode. If an NMI can interrupt a serial write, either retry the write or reset the shift register before switching.

## MMC3

Registers:

| Address | Purpose |
|---|---|
| `$8000` | bank select: bits 0–2 register, bit 6 PRG mode, bit 7 CHR A12 inversion |
| `$8001` | bank data for selected register |
| `$A000` | mirroring: bit 0 (0 vertical, 1 horizontal) |
| `$A001` | PRG-RAM protect |
| `$C000` | IRQ latch |
| `$C001` | IRQ reload |
| `$E000` | IRQ disable + acknowledge |
| `$E001` | IRQ enable |

- R0–R5: CHR banks (1 KB each, with 2 KB modes for R0/R1).
- R6/R7: PRG banks (8 KB). With PRG mode 0, R6 maps `$8000`, `$C000` is second-last fixed; mode 1 swaps.
- The last 8 KB (`$E000–$FFFF`) is always fixed. Vectors live there.
- Scanline IRQ uses PPU A12; clock it during init by toggling `$2006` (commercial init sequence) to avoid a spurious first IRQ.
- Bank writes are write-only; keep a shadow copy for NMI/IRQ restore.

## AxROM

- 32 KB switchable at `$8000`; 8 KB CHR-RAM.
- Write bank to `$8000–$FFFF`; bit 4 selects one-screen mirroring.
- Bus conflicts apply on some boards.

## Rules that prevent crashes

- Vectors and reset code must be in a fixed bank, or in every bank.
- Never switch the bank you are currently executing from unless the switch takes effect after the next fetch — put the switch routine in the fixed bank.
- If NMI changes banks, restore the previous bank before `RTI`.
- Bank numbers are not always contiguous; use a table if the board maps them oddly.
- Bus conflicts: on discrete boards, the value written must equal the ROM byte at that address.
- CHR-RAM starts undefined; upload tiles before enabling rendering.
- Battery saves need a magic header and checksum; do not assume WRAM is zeroed.

## Checks

- Does the header's mapper match the board behavior you implemented?
- Is PRG size a multiple of 16 KB and CHR a multiple of 8 KB?
- Is the last bank fixed and does it contain the vectors?
- After a bank switch, is the code that continues executing still mapped?
- Does the IRQ/NMI handler restore the bank it changed?
- Is `$6000–$7FFF` actually RAM on this board, or open bus?

## References

- [iNES](https://www.nesdev.org/wiki/INES) · [NES 2.0](https://www.nesdev.org/wiki/NES_2.0)
- [Mapper](https://www.nesdev.org/wiki/Mapper) · [Bus conflict](https://www.nesdev.org/wiki/Bus_conflict)
- [Programming NROM](https://www.nesdev.org/wiki/Programming_NROM) · [Programming UNROM](https://www.nesdev.org/wiki/Programming_UNROM)
- [Programming MMC1](https://www.nesdev.org/wiki/Programming_MMC1) · [Programming MMC3](https://www.nesdev.org/wiki/Programming_MMC3)
- `references/ines-header.md` · `references/mapper-recipes.md`
