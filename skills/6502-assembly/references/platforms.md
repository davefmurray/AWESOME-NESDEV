# 6502 family and platform differences

The instruction mnemonics are shared; the machines are not. The same `LDA #$10` can hit RAM, a hardware register, or a banked ROM depending on the address.

## CPU variants

| CPU | Used in | Official opcodes | Decimal | Key differences |
|---|---|---|---|---|
| **NMOS 6502** | Apple II, Atari, C64 (6510), NES (2A03 core) | 151 | yes | `JMP ($xxFF)` bug; 105 undocumented opcodes |
| **65C02** | Apple IIc, modern SBCs | 151 + additions | yes | `STZ`, `BRA`, `PHX/PHY`, `TRB/TSB`, `WAI/STP`; fixes JMP bug |
| **2A03 / 2A07** | NES / Famicom | 151 | **no** | APU/PPU on-die; `SED` has no effect on ADC/SBC |
| **6510** | C64 | 151 | yes | 6-bit I/O port at `$0000/$0001` |
| **65SC02** | some embedded | 65C02 subset | yes | no bit instructions |
| **65CE02** | C65 | extended | yes | `Z` index, 16-bit stack relative |
| **65816** | Apple IIgs, SNES | 16-bit | yes | 24-bit address, different mode system |

"6502" in a tutorial usually means NMOS 6502. If the target is NES, the 2A03 differences matter; if the target is C64, the 6510 I/O port matters.

## NMOS 6502

- 8-bit data, 16-bit address, 1 MHz-ish (1.023 MHz Apple II, 1.79 MHz NES, 0.985 MHz C64).
- Decimal mode works: `SED` makes `ADC`/`SBC` operate on packed BCD.
- `JMP ($xxFF)` page bug.
- No `STZ`, `BRA`, `PHX/PHY`, `TRB/TSB`, `INC A`, `DEC A`, `BIT #`.
- Undocumented opcodes exist and are stable on NMOS; they are not part of the official 151.

## 65C02

Additions that matter:

| Instruction | Effect |
|---|---|
| `STZ addr` | store zero without touching A |
| `BRA rel` | unconditional branch |
| `PHX/PHY/PLX/PLY` | push/pull X/Y |
| `TRB/TSB addr` | test-and-reset/set bits |
| `INC A` / `DEC A` | accumulator increment/decrement |
| `BIT #imm` | immediate bit test (Z only) |
| `JMP (abs,X)` | indexed indirect jump |
| `WAI` / `STP` | wait for interrupt / stop |
| `RMB/SMB/BBR/BBS` | Rockwell/WDC bit ops (variant-dependent) |

The 65C02 fixes the `JMP ($xxFF)` bug and changes some undocumented opcode behavior. Code written for 65C02 may not run on NES.

## 2A03 / 2A07 (NES)

The NES CPU is a 6502 core with:

- **No decimal mode.** `SED` sets D, but `ADC`/`SBC` stay binary. Do not use BCD routines on NES.
- **1.7897725 MHz** NTSC, **1.662607 MHz** PAL.
- **APU** registers at `$4000–$4013`, status at `$4015`, joypads at `$4016/$4017`.
- **PPU** registers at `$2000–$2007`, mirrored through `$3FFF`.
- **2 KB RAM** at `$0000–$07FF`, mirrored through `$1FFF`.
- **PRG** at `$8000–$FFFF` (16 KB or 32 KB windows), **SRAM** at `$6000–$7FFF`.
- **Vectors** at `$FFFA` NMI, `$FFFC` RESET, `$FFFE` IRQ/BRK.
- **NMI** is the vblank interrupt; **IRQ** comes from the mapper, DMC, or APU frame counter.

The 2A03 has no `WAI`; use a `JMP *` or a tight loop with `BIT`/`NOP` for idle.

## 6510 (C64)

The 6510 adds a 6-bit I/O port:

- `$0000` = data direction register (1 = output).
- `$0001` = port data; bits 0–2 bank BASIC/KERNAL/I/O, bits 3–5 control cassette/serial.
- `$37` maps BASIC, KERNAL and I/O in (the usual default); `$35` maps both ROMs out (RAM at `$A000`/`$E000`) with I/O in; `$36` maps BASIC out, KERNAL and I/O in.
- The port is not available on the 6502; code that writes `$0000/$0001` is C64-specific.

C64 memory map highlights: `$A000` BASIC ROM, `$D000` VIC-II, `$D400` SID, `$DC00` CIA1, `$DD00` CIA2, `$E000` KERNAL ROM, vectors at `$FFFA`.

## Apple II

- 6502 at 1.023 MHz (IIe/IIc).
- `$0000–$BFFF` RAM (48 KB), `$C000–$C0FF` I/O and soft switches, `$C100–$C7FF` slot ROM, `$C800–$CFFF` expansion ROM, `$E000–$FFFF` ROM.
- Text screen at `$0400`, hi-res at `$2000`/`$4000`.
- Reset vector at `$FFFC`.

## Interrupts

The 6502 has three hardware vectors plus `BRK`:

| Event | Vector | Maskable | Pushed PC | Notes |
|---|---|---|---|---|
| NMI | `$FFFA` | no | current PC | vblank on NES |
| RESET | `$FFFC` | — | — | initial PC |
| IRQ | `$FFFE` | yes (I flag) | current PC | mapper/DMC/APU |
| BRK | `$FFFE` | no (software) | PC+2 | skips signature byte |

On interrupt: push PCH, PCL, P (with B clear for IRQ/NMI, set for BRK), set I, load PC from vector. `RTI` pulls P, PCL, PCH.

`NMI` can interrupt an `IRQ` handler. If both touch the same state, disable NMI or use a flag. `SEI` blocks IRQ but not NMI. `CLI` re-enables IRQ.

## Undocumented opcodes

The NMOS 6502 has 105 undocumented encodings. Some are stable and widely used:

```
LAX  LDA + LDX        SAX  store A & X
DCP  DEC + CMP        ISC  INC + SBC
SLO  ASL + ORA        RLA  ROL + AND
SRE  LSR + EOR        RRA  ROR + ADC
ANC  AND + carry      ALR  AND + LSR
ARR  AND + ROR        SBX  compare and decrement
```

Unstable ones (`XAA`, `AHX`, `TAS`, `SHY`, `SHX`, `LAS`) depend on the value in A/X and the high byte of the address; avoid them in portable code. The 2A03 implements most undocumented opcodes, but behavior can differ from NMOS parts; do not use them in NES code you want to run on all emulators.

## What changes when you change platform

1. **Memory map** — where RAM, ROM and I/O live.
2. **Decimal mode** — present on NMOS/65C02, absent on 2A03.
3. **Clock** — cycle budgets differ (1.79 MHz NES vs 1.023 MHz Apple II).
4. **Interrupt sources** — NMI timing, IRQ sources, vectors.
5. **I/O port** — 6510's `$0000/$0001`, NES PPU/APU registers.
6. **Undocumented opcodes** — stable on NMOS, variable on 2A03, absent on 65C02.
7. **Assembler target** — `ca65 -t nes` vs `-t c64` vs `-t apple2`; the CPU core is the same, the platform config is not.

## References

- [Wilson Mines: NMOS-CMOS differences](http://wilsonminesco.com/NMOS-CMOSdif/)
- [Wilson Mines: 6502 interrupts](http://wilsonminesco.com/6502interrupts/)
- [NESdev wiki: CPU](https://www.nesdev.org/wiki/CPU)
- [NESdev wiki: PPU registers](https://www.nesdev.org/wiki/PPU_registers)
- [NESdev wiki: APU registers](https://www.nesdev.org/wiki/APU_registers)
- [C64 Wiki: 6510](https://www.c64-wiki.com/wiki/6510) · [C64 memory map](https://www.c64-wiki.com/wiki/Memory_Map)
