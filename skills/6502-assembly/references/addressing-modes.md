# 6502 addressing modes

The 6502 has **13 addressing modes**. The mode is encoded in the opcode, not in a separate field, so `LDA $10` and `LDA $1000` are different instructions with different sizes and cycles.

| Mode | Syntax | Bytes | Effective address | Example |
|---|---|---|---|---|
| Implied | — | 1 | none | `INX` |
| Accumulator | `A` | 1 | `A` | `ASL A` |
| Immediate | `#oper` | 2 | operand | `LDA #$10` |
| Zero page | `oper` | 2 | `$00oper` | `LDA $10` |
| Zero page,X | `oper,X` | 2 | `($00oper+X) & $FF` | `LDA $10,X` |
| Zero page,Y | `oper,Y` | 2 | `($00oper+Y) & $FF` | `LDX $10,Y` |
| Absolute | `oper` | 3 | `oper` | `LDA $1234` |
| Absolute,X | `oper,X` | 3 | `oper+X` | `LDA $1234,X` |
| Absolute,Y | `oper,Y` | 3 | `oper+Y` | `LDA $1234,Y` |
| Relative | `label` | 2 | `PC+2+signed8` | `BNE loop` |
| Indirect | `(oper)` | 3 | pointer at `oper` | `JMP ($1234)` |
| Indexed indirect | `(oper,X)` | 2 | pointer at `($00oper+X)` | `LDA ($10,X)` |
| Indirect indexed | `(oper),Y` | 2 | pointer at `$00oper`, plus `Y` | `LDA ($10),Y` |

## Immediate

`#` means the operand is the value, not an address.

```asm
LDA #$10    ; A = $10
LDA $10     ; A = memory[$0010]
```

Immediate is only available for `LDA LDX LDY ADC SBC AND ORA EOR CMP CPX CPY` (and `BIT #` on 65C02).

## Zero page

The high byte is forced to `$00`, so the instruction is 2 bytes and usually one cycle faster.

```asm
LDA $10     ; 2 bytes, 3 cycles
LDA $0010   ; 3 bytes, 4 cycles (assembler may optimize to zp)
```

Indexed zero-page modes **wrap inside page zero**:

```asm
LDX #$FF
LDA $10,X   ; reads $000F, not $010F
```

This is useful for circular buffers and dangerous for arrays that cross a page.

## Absolute

Full 16-bit address, 3 bytes. The assembler chooses zero page automatically when the address is a constant `< $100`; force it when needed:

| Assembler | Force zero page | Force absolute |
|---|---|---|
| ca65 | `z:$10` | `a:$0010` |
| asm6 | `$10` (auto) | `a:$0010` |

If a label is defined in zero page, ca65/ld65 can relax it automatically. If you move a variable out of zero page, recheck the generated listing.

## Absolute,X / absolute,Y

`oper,X` adds X to the 16-bit base. If the addition carries out of the low byte, the read takes one extra cycle:

```asm
LDA $12FF,X   ; X=1 -> $1300, page crossed, +1 cycle
STA $12FF,X   ; stores never take the page-cross penalty
```

`abs,Y` is available for `LDA`, `STA`, `ADC`, `SBC`, `AND`, `ORA`, `EOR`, `CMP`, and `LDX` (not `STX`).
`abs,X` is available for those plus `LDY`, `STY`, `INC`, `DEC`, `ASL`, `LSR`, `ROL`, `ROR`.

## Relative

Branches take a signed 8-bit offset from the byte **after** the operand:

```
target = PC + 2 + offset
offset = target - (PC + 2), range -128..+127
```

If the target is too far, invert the branch and add a `JMP`:

```asm
BEQ nearby
JMP far_target
nearby:
```

## Indirect: `JMP (abs)`

Only `JMP` has a true indirect mode. The two bytes at `abs` are the low/high target.

```asm
JMP ($1234)   ; PC = memory[$1234] | memory[$1235]<<8
```

**NMOS bug:** if `abs` ends in `$FF`, the high byte is fetched from `abs & $FF00` instead of the next page. `JMP ($12FF)` reads low from `$12FF`, high from `$1200`. The 65C02 fixes this; NES code must avoid the page boundary.

## Indexed indirect: `(zp,X)`

X selects a **pointer from a table** in zero page. The pointer is read from `zp+X` (low) and `zp+X+1` (high), with zero-page wrap.

```asm
; pointers at $10,$12,$14...
LDX #2
LDA ($10,X)   ; pointer at $12/$13
```

Use this for a table of buffers or strings. It is 2 bytes, 6 cycles.

## Indirect indexed: `(zp),Y`

One pointer in zero page; Y is added to the pointer to form the effective address.

```asm
; ptr = $20 (low), $21 (high)
LDY #5
LDA ($20),Y   ; reads memory[ptr+5]
```

The pointer itself wraps inside zero page: if `zp=$FF`, the high byte comes from `$00`. The `+Y` addition carries into the high byte normally; reads take +1 cycle on a page cross, stores do not.

This is the workhorse for arrays, strings, framebuffers, and copying.

## Stack "addressing"

`PHA`, `PLA`, `PHP`, `PLP`, `JSR`, `RTS`, `BRK`, `RTI` use the stack at `$0100–$01FF`. There is no general `(SP),Y` addressing mode on the 6502; the 65C02 adds `(zp)` but not stack-relative.

## Mode availability

Not every mnemonic supports every mode. The assembler will reject invalid combinations. The important gaps:

- `STX` has no `abs,X`; `STY` has no `abs,Y`.
- `LDX` has `abs,Y` but no `abs,X`; `LDY` has `abs,X` but no `abs,Y`.
- `CPX`/`CPY` have immediate, zero page, absolute only.
- `INC`/`DEC` have no immediate or accumulator mode on NMOS 6502 (`INC A` is 65C02).
- `BIT` has zero page/absolute on NMOS (`BIT #` is 65C02).
- `JMP` has absolute and indirect only; `JSR` has absolute only.

## Cycle penalties

| Situation | Extra cycle |
|---|---|
| `abs,X` / `abs,Y` read crosses page | +1 |
| `(zp),Y` read crosses page | +1 |
| Branch taken | +1 |
| Branch taken across page | +1 more |
| `abs,X` / `abs,Y` store | 0 |
| Zero-page indexed wrap | 0 |

`STA abs,X` is fixed at 5 cycles; `LDA abs,X` is 4 or 5 depending on the page crossing. This asymmetry matters in raster code.

## Common mistakes

- Using `$10,X` for an array that can cross a page: it wraps at `$FF`.
- Forgetting that `(zp),Y` needs the pointer's high byte set.
- Assuming `JMP ($xxFF)` works like a 16-bit pointer.
- Using `abs,Y` with `STX`/`STY` (not encodable).
- Forgetting the branch range; the assembler errors, but hand-written bytes do not.
