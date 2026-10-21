# 6502 learning path

Full curated list: [`docs/6502.md`](../../../docs/6502.md).

1. **Easy 6502** — <https://skilldrick.github.io/easy6502/> — interactive book + simulator.
2. **Wilson Mines 6502 Primer** — <https://wilsonminesco.com/6502primer/> — practical primer.
3. **Obelisk guide + instruction reference** — <https://www.nesdev.org/obelisk-6502-guide/> · <https://www.nesdev.org/wiki/Instruction_reference>.
4. **Nerdy Nights** — <https://nerdy-nights.nes.science/> — NES course.
5. **8bitworkshop** — <https://8bitworkshop.com/> — browser IDE with NES examples.
6. **Nova the Squirrel** — <https://github.com/NovaSquirrel/NovaTheSquirrel> — read a full NES game.
7. **py65 / Klaus tests / 65x02** — write a routine, assemble it, assert it in a simulator.

## Assemblers

`ca65` (cc65), `asm6f` (simple NES), `dasm`, `acme`. Pick one; ca65 is what NES homebrew and romdev use.

## Cautions

- 65C02-only instructions do not run on NES.
- 2A03 has no decimal mode.
- Undocumented opcodes are not portable across emulators.
