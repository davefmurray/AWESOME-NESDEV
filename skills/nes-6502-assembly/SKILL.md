---
name: nes-6502-assembly
description: "6502 assembly for the NES: registers, flags, addressing modes, cycle counts, zero page, stack, jump tables, the RTS trick, synthetic instructions, and size/speed optimizations. Use when writing or reading NES assembly, hand-optimizing a routine, or explaining 6502 behavior and timing."
---

# 6502 assembly for the NES

The NES uses a 6502 variant (2A03 NTSC / 2A07 PAL) at ~1.79 MHz. It has no decimal mode, no multiply, no divide, and a 256-byte fast-access zero page. Code that respects the cycle rules is code that fits in vblank.

## Registers

| Register | Width | Use |
|---|---|---|
| A | 8 | accumulator, arithmetic |
| X | 8 | index, counter |
| Y | 8 | index, counter |
| SP | 8 | stack pointer, page `$0100`, descending |
| PC | 16 | program counter |
| P | 8 | flags |

Flags: `N` negative, `V` overflow, `-` unused, `B` break, `D` decimal (ignored on NES), `I` IRQ disable, `Z` zero, `C` carry.

No decimal mode: `SED` does not make `ADC`/`SBC` do BCD on the 2A03.

## Addressing modes

| Mode | ca65 syntax | Example |
|---|---|---|
| Implied | — | `RTS`, `INX` |
| Accumulator | `A` | `ASL A` |
| Immediate | `#value` | `LDA #$10` |
| Zero page | `$nn` | `LDA $10` |
| Zero page,X | `$nn,X` | `LDA $10,X` |
| Zero page,Y | `$nn,Y` | `LDX $10,Y` |
| Absolute | `$nnnn` | `LDA $2002` |
| Absolute,X | `$nnnn,X` | `LDA $2000,X` |
| Absolute,Y | `$nnnn,Y` | `LDA $2000,Y` |
| Indirect | `($nnnn)` | `JMP ($FFFC)` |
| Indexed indirect | `($nn,X)` | `LDA ($10,X)` |
| Indirect indexed | `($nn),Y` | `LDA ($10),Y` |
| Relative | `label` | `BNE loop` |

Traps:

- Zero-page indexed wraps inside `$00–$FF`; absolute indexed does not.
- `JMP ($xxFF)` has a page-boundary bug: the high byte comes from `$xx00`, not the next page.
- Branches are −128…+127 bytes.
- `(indirect)` is only available for `JMP`.

## Common instructions and cycles

`+` means add 1 if a page boundary is crossed (reads only).

| Instruction | Modes and cycles |
|---|---|
| `LDA` | imm 2 · zp 3 · zp,X 4 · abs 4 · abs,X 4+ · abs,Y 4+ · (zp,X) 6 · (zp),Y 5+ |
| `LDX` | imm 2 · zp 3 · zp,Y 4 · abs 4 · abs,Y 4+ |
| `LDY` | imm 2 · zp 3 · zp,X 4 · abs 4 · abs,X 4+ |
| `STA` | zp 3 · zp,X 4 · zp,Y 4 · abs 4 · abs,X 5 · abs,Y 5 · (zp,X) 6 · (zp),Y 6 |
| `ADC`/`SBC` | same as `LDA` |
| `AND`/`ORA`/`EOR` | same as `LDA` |
| `CMP` | same as `LDA`; `CPX`/`CPY` like `LDX` |
| `INC`/`DEC` | zp 5 · zp,X 6 · abs 6 · abs,X 7 · `INX`/`INY`/`DEX`/`DEY` 2 |
| `ASL`/`LSR`/`ROL`/`ROR` | A 2 · zp 5 · zp,X 6 · abs 6 · abs,X 7 |
| `BIT` | zp 3 · abs 4 |
| `JMP` | abs 3 · (ind) 5 |
| `JSR` / `RTS` / `RTI` | 6 / 6 / 6 |
| `BRK` | 7 |
| Branches | 2, +1 if taken, +1 more if the branch crosses a page |
| `PHA`/`PHP` / `PLA`/`PLP` | 3 / 4 |
| `TAX`/`TAY`/`TXA`/`TYA`/`TSX`/`TXS` | 2 |
| `CLC`/`SEC`/`CLI`/`SEI`/`CLD`/`CLV` | 2 |

Full opcode matrix: [Instruction reference](https://www.nesdev.org/wiki/Instruction_reference) · [CPU unofficial opcodes](https://www.nesdev.org/wiki/CPU_unofficial_opcodes).

## Stack and calls

- `JSR` pushes return address − 1; `RTS` pulls and adds 1.
- `BRK` pushes PC + 2 and sets the B flag; IRQ/NMI push PC and clear B. `RTI` restores P and PC.
- Interrupt handlers must preserve A/X/Y if the main code uses them.
- The stack is only 256 bytes; deep recursion and large pushes overflow into `$0100`.

## Synthetic instructions

Common idioms the assembler or the programmer builds from other opcodes:

| Want | Write |
|---|---|
| `A = 0` | `LDA #0` (2 bytes, 2 cycles) |
| `A = $FF` | `LDA #$FF` |
| Multiply by 2 | `ASL A` |
| Divide by 2 | `LSR A` |
| Negate | `EOR #$FF / CLC / ADC #1` |
| Clear / set carry | `CLC` / `SEC` |
| 16-bit increment | `INC lo / BNE + / INC hi` |
| 16-bit add | `CLC / ADC lo / STA lo / LDA hi / ADC hi / STA hi` |

The wiki's [Synthetic instructions](https://www.nesdev.org/wiki/Synthetic_instructions) page has the full catalogue of aliases and multi-instruction idioms.

## Control flow

### Jump table (split low/high)

```asm
  ldx index
  lda table_lo,x
  sta ptr
  lda table_hi,x
  sta ptr+1
  jmp (ptr)

table_lo: .byte <routine0, <routine1
table_hi: .byte >routine0, >routine1
```

Avoid `JMP (ptr)` when `ptr` ends in `$FF` (page-boundary bug).

### RTS trick

```asm
  ldx index
  lda table_hi,x
  pha
  lda table_lo,x
  pha
  rts
```

`RTS` pulls the address and adds 1, so the table must contain `target - 1`. Saves the indirect jump and its page bug; costs stack traffic.

## Optimizations that pay

- Put hot variables and pointers in zero page: shorter and faster.
- Use `INC`/`DEC` memory instead of load-add-store.
- Prefer `ASL A` over `CLC/ADC A` for ×2.
- Tail-call with `JMP` instead of `JSR` + `RTS` (saves 9 cycles, 1 byte).
- Split pointer tables into low/high bytes to avoid `ASL` and 16-bit loads (saves ~4 cycles).
- Unroll small loops only when the cycle budget matters; code size is also a constraint.
- Count cycles on paper for vblank and raster code; an extra branch can cost a scanline.
- Avoid `JMP` chains in hot paths; fall through.

## Checks

- Is the routine using zero page where it could?
- Does any branch exceed ±127 bytes? The assembler will tell you.
- Is a 16-bit pointer crossing a page in an indexed read?
- Does an interrupt handler save/restore A/X/Y?
- Is the stack balanced on every path?
- Are you relying on decimal mode? It does not exist.
- Did you account for page-cross penalties in a timed loop?

## References

- [Instruction reference](https://www.nesdev.org/wiki/Instruction_reference) · [6502 instructions](https://www.nesdev.org/wiki/6502_instructions)
- [6502 cycle times](https://www.nesdev.org/wiki/6502_cycle_times) · [Cycle reference chart](https://www.nesdev.org/wiki/Cycle_reference_chart)
- [6502 assembly optimisations](https://www.nesdev.org/wiki/6502_assembly_optimisations) · [Synthetic instructions](https://www.nesdev.org/wiki/Synthetic_instructions)
- [Jump table](https://www.nesdev.org/wiki/Jump_table) · [RTS trick](https://www.nesdev.org/wiki/RTS_trick)
- `references/instruction-set.md` · `references/techniques.md`
