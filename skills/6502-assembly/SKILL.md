---
name: 6502-assembly
description: "6502 assembly from the programming model to working code: registers, flags, all 13 addressing modes, the full official 151-opcode instruction set, 8/16-bit arithmetic, pointers, jump tables, macros, ca65/asm6/dasm syntax, cycle counting, and testing against py65, Klaus and 65x02. Use for 6502, 65C02, 2A03/2A07 (NES), or 6510 (C64) code, or when debugging flags, timing, or assembler syntax."
---

# 6502 assembly

One skill for the whole 6502 family. The core ISA is small: **56 mnemonics, 151 official opcodes, 13 addressing modes**. The hard parts are not the instructions — they are flags, carry chains, page crossings, and picking the right pointer shape.

Use the references for depth:

| Reference | Read it for |
|---|---|
| [opcodes.md](references/opcodes.md) | Full opcode matrix, cycles, flags |
| [addressing-modes.md](references/addressing-modes.md) | Every mode, effective address, page-cross rules |
| [programming-patterns.md](references/programming-patterns.md) | 8/16-bit math, arrays, strings, jump tables, stack frames, macros |
| [toolchains.md](references/toolchains.md) | ca65, asm6, dasm, ACME, build and symbol files |
| [testing.md](references/testing.md) | py65, Klaus, 65x02, perfect6502, cycle tests |
| [platforms.md](references/platforms.md) | 6502 vs 65C02 vs 2A03 vs 6510 |
| [sources.md](references/sources.md) | Every resource this skill was built from |

## The machine in one page

- **8-bit** accumulator and index registers, **16-bit** program counter, **8-bit** stack pointer.
- **64 KB** address space, little-endian words (`$1234` is stored `34 12`).
- **Memory-mapped I/O**: there are no `IN`/`OUT` instructions; hardware registers are just addresses.
- **No multiply, no divide, no native 16-bit registers.** You build those from shifts, adds and carry.
- **Stack is fixed** at `$0100–$01FF`. The stack pointer is an offset, not a full address. It grows down and wraps inside page 1.
- **Interrupt vectors** live at the top of memory: `$FFFA` NMI, `$FFFC` RESET, `$FFFE` IRQ/BRK.

## Registers and flags

| Register | Width | Job |
|---|---|---|
| `A` | 8 | arithmetic, loads, stores, most data |
| `X` | 8 | index, counter, second scratch |
| `Y` | 8 | index, counter, second scratch |
| `PC` | 16 | next instruction |
| `SP` | 8 | offset into `$0100` page |
| `P` | 8 | flags |

| Flag | Bit | Meaning |
|---|---|---|
| `N` | 7 | negative (bit 7 of the result) |
| `V` | 6 | signed overflow |
| `B` | 4 | break; only meaningful in a pushed status byte |
| `D` | 3 | decimal mode (ignored by the 2A03/2A07) |
| `I` | 2 | IRQ disable |
| `Z` | 1 | zero result |
| `C` | 0 | carry / unsigned borrow / shift-out bit |

`P` has no `B` bit in the register; `PHP`/`BRK` push a copy with `B` set, and `PLP`/`RTI` ignore it.

## Addressing modes

| Mode | Syntax | Example | Effective address |
|---|---|---|---|
| Implied | — | `INX` | none |
| Accumulator | `A` | `ASL A` | `A` |
| Immediate | `#` | `LDA #$10` | operand byte |
| Zero page | `zp` | `LDA $10` | `$0010` |
| Zero page,X/Y | `zp,X` | `LDA $10,X` | `($10+X) & $FF` |
| Absolute | `abs` | `LDA $1234` | `$1234` |
| Absolute,X/Y | `abs,X` | `LDA $1234,X` | `$1234+X` (may cross page) |
| Relative | `rel` | `BNE loop` | `PC+2+signed8` |
| Indirect | `(abs)` | `JMP ($1234)` | pointer at `$1234` (JMP only) |
| Indexed indirect | `(zp,X)` | `LDA ($10,X)` | pointer table at `$10+X` |
| Indirect indexed | `(zp),Y` | `LDA ($10),Y` | pointer at `$10`, plus `Y` |

The two pointer forms are not interchangeable:

```
(zp,X)   ; X selects a pointer from a table in zero page
(zp),Y   ; one pointer in zero page, Y is the index into the data
```

`JMP ($xxFF)` has the NMOS page-boundary bug: the high byte comes from `$xx00`, not `$xx+1:00`. The 65C02 fixes it. Zero-page indexed modes wrap inside page zero; absolute indexed modes carry into the next page and may cost a cycle.

## The instruction families

| Family | Instructions | Notes |
|---|---|---|
| Load/store | `LDA LDX LDY STA STX STY` | `STX`: `zp`, `zp,Y`, `abs`; `STY`: `zp`, `zp,X`, `abs` (neither has `abs,Y`) |
| Transfer | `TAX TAY TXA TYA TSX TXS` | `TXS` does not set flags |
| Arithmetic | `ADC SBC` | carry is input and output; `CLC`/`SEC` first |
| Logic | `AND ORA EOR` | bit masking, setting, toggling |
| Shifts | `ASL LSR ROL ROR` | `A` or memory; `C` is the bit shifted out/in |
| Compare | `CMP CPX CPY` | unsigned; `C=1` means `reg >= operand` |
| Inc/dec | `INC DEC INX DEX INY DEY` | memory forms are read-modify-write |
| Branch | `BCC BCS BEQ BMI BNE BPL BVC BVS` | signed 8-bit range only |
| Jump | `JMP JSR RTS RTI BRK` | `JSR` pushes return address minus 1 |
| Stack | `PHA PLA PHP PLP` | `PLA` sets N/Z; `PHA` does not |
| Flags | `CLC SEC CLI SEI CLD SED CLV` | no `CLB`; use `CLV` for overflow |

## The 6502 style

1. **Zero page is your register file.** `$00–$FF` is faster (3 cycles vs 4) and shorter (2 bytes vs 3). Reserve a block for pointers, counters and scratch.
2. **Pointers are two zero-page bytes.** `LDA (ptr),Y` reads the little-endian address at `ptr`, then adds `Y`. Set `ptr`/`ptr+1` explicitly; there is no 16-bit load.
3. **Carry is the 16-bit glue.** Add low bytes with `CLC`/`ADC`, then high bytes with `ADC` (no `CLC` between). Subtract with `SEC`/`SBC`, then `SBC`.
4. **Dispatch with a jump table**, not a chain of `CMP`/`BEQ`, when the index is dense.
5. **The RTS trick** pushes `address-1` and executes `RTS` to jump without a `JMP (ptr)` setup.
6. **Unroll small fixed loops.** The 6502 has no cache; speed comes from fewer instructions and fewer branches.
7. **Self-modifying code only in RAM.** It works on the 6502 (no instruction cache), but not in NES PRG ROM; use it for patching RAM routines, not cartridge code.

## The patterns you will actually write

### 8-bit add and subtract

```asm
; sum = a + b
CLC
LDA a
ADC b
STA sum

; diff = a - b
SEC
LDA a
SBC b
STA diff
```

### 16-bit add

```asm
CLC
LDA a_lo
ADC b_lo
STA sum_lo
LDA a_hi
ADC b_hi
STA sum_hi
```

### 16-bit compare (unsigned)

```asm
LDA a_hi
CMP b_hi
BNE .done
LDA a_lo
CMP b_lo
.done:
; C=1 => a >= b, Z=1 => equal
```

### Pointer walk

```asm
; copy 256 bytes from (src),Y to (dst),Y
LDY #0
.loop:
LDA (src),Y
STA (dst),Y
INY
BNE .loop
```

### Jump table

```asm
; table_lo/table_hi are parallel byte tables
LDX index
LDA table_lo,X
STA ptr
LDA table_hi,X
STA ptr+1
JMP (ptr)
```

### RTS dispatch

```asm
; jump to routine without JMP (ptr)
LDA #>routine
PHA
LDA #<routine-1
PHA
RTS
```

`RTS` pulls the address and adds 1, so push `target-1`.

### Save and restore registers

```asm
PHA
TXA
PHA
TYA
PHA
; ... body ...
PLA
TAY
PLA
TAX
PLA
RTS
```

## Assembler syntax at a glance

| Thing | ca65 | asm6 | dasm |
|---|---|---|---|
| Origin | linker config / `.segment` | `ORG $8000` | `ORG $8000` |
| Byte | `.byte $EA` | `DB $EA` | `DC.B $EA` |
| Word | `.word $1234` | `DW $1234` | `DC.W $1234` |
| Immediate | `#$10` | `#$10` | `#$10` |
| Comment | `;` | `;` | `;` |
| Include | `.include "file"` | `INCLUDE "file"` | `INCLUDE "file"` |
| Local label | `@loop` / `:` | `@loop` | `.loop` |

ca65 adds segments, `.proc`, `.macro`, `.import`/`.export`; asm6 is deliberately minimal. Pick one and learn its directives — mixing syntax is the most common beginner error.

## Build and test loop

```bash
# ca65 + ld65
ca65 -t nes src/main.s -o build/main.o
ld65 -C nes.cfg build/main.o -o build/game.nes

# asm6
asm6 src/main.asm build/game.nes

# 8bitworkshop, from its checkout
npm run cli -- build --platform nes src/main.s -o build/game.nes --symbols
npm run cli -- run --platform nes --frames 240 --png shot.png build/game.nes
```

Keep a **symbol file** and load it in the emulator debugger. A disassembly without labels is a puzzle; a symbol file makes it a map.

## Debugging checklist

- Did you `CLC` before `ADC`, or `SEC` before `SBC`?
- Is the branch within `-128..+127` bytes of the next instruction?
- Did a pointer calculation cross a page and cost a cycle you did not budget?
- Did `INY` wrap from `$FF` to `$00` inside a 256-byte loop?
- Is the stack balanced on every path? `JSR` and `PHA` must be matched.
- Did an interrupt fire between a 16-bit read and its high byte?
- Are you comparing signed values with unsigned `CMP` semantics?
- Did `JMP ($xxFF)` bite you?
- On NES: is decimal mode assumed? It is disabled on the 2A03.
- On 65C02: are you using an opcode the target does not have?

## Platform matrix

| CPU | Official opcodes | Decimal | Notable extras | Use |
|---|---|---|---|---|
| NMOS 6502 | 151 | yes | — | Apple II, C64 (6510), NES (2A03 core) |
| 65C02 | 151+ | yes | `STZ`, `BRA`, `PHX/PHY`, `TRB/TSB`, `WAI/STP` | Apple IIc, modern SBCs |
| 2A03/2A07 | 151 | **no** | APU/PPU on-die | NES/Famicom |
| 6510 | 151 | yes | 6-bit I/O port at `$0000/$0001` | C64 |

The 2A03 is not "6502 with extra instructions"; it is a 6502 core with **no decimal mode** and hardware glued on. Code that relies on `SED` will silently produce binary results.

## References

- [Full opcode matrix and cycles](references/opcodes.md)
- [Addressing modes in detail](references/addressing-modes.md)
- [Programming patterns](references/programming-patterns.md)
- [Toolchains and syntax](references/toolchains.md)
- [Testing and verification](references/testing.md)
- [Platform differences](references/platforms.md)
- [Annotated sources](references/sources.md)

## Companion skills

- [NES 6502 optimizations](../nes-6502-assembly/SKILL.md) — NES-specific timing and code-size tricks.
- [NES memory map](../nes-memory-map/SKILL.md) · [PPU](../nes-ppu-rendering/SKILL.md) · [APU](../nes-apu-audio/SKILL.md)
