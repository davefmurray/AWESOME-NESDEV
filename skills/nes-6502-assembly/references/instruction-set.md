# 6502 instruction notes

## Flags

| Flag | Set by | Cleared by | Used by |
|---|---|---|---|
| C carry | `SEC`, `ADC`, `SBC`, shifts, compares | `CLC` | add/subtract, rotate, branches |
| Z zero | any load/logic/arithmetic result | same | `BEQ`/`BNE` |
| N negative | result bit 7 | same | `BMI`/`BPL` |
| V overflow | `ADC`/`SBC`, `BIT` | `CLV` | `BVC`/`BVS` |
| I IRQ disable | `SEI` | `CLI` | interrupt mask |
| D decimal | `SED` | `CLD` | **no effect on NES** |
| B break | `BRK`/`PHP` | `PLP`/`RTI` | software only |

## Branch rules

- Range −128…+127 from the byte after the branch.
- 2 cycles not taken, 3 taken, 4 if taken across a page.
- `BIT` sets Z from `A & mem`, N/V from the memory byte; useful for polling `$2002`.

## Interrupts

- NMI: `$FFFA`, cannot be masked, fires at vblank when enabled.
- IRQ: `$FFFE`, masked by I; sources are mapper IRQ, APU frame IRQ, DMC IRQ.
- BRK: software interrupt, pushes PC+2, sets B.
- RTI restores P and PC; RTS restores PC only.
- NMI/IRQ entry does not save registers; do it yourself.

## Unofficial opcodes

The 2A03 executes many undocumented opcodes. They are stable on real hardware but not on all emulators and not portable to 65C02. Avoid them in code that must run everywhere, or isolate them behind a feature check.

## Full reference

- [Instruction reference](https://www.nesdev.org/wiki/Instruction_reference) — per-instruction opcodes, flags, cycles
- [CPU unofficial opcodes](https://www.nesdev.org/wiki/CPU_unofficial_opcodes) — full matrix
- [6502 cycle times](https://www.nesdev.org/wiki/6502_cycle_times) — table by addressing mode
