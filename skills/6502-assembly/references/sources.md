# Sources and further reading

This skill synthesizes the resources below. They were read in October 2026; the opcode reference was generated from Masswerk's instruction table and cross-checked against py65's cycle data. Where the two disagreed, the per-instruction cycle table won.

## Tutorials and books

| Source | What it contributed |
|---|---|
| [Easy 6502](https://skilldrick.github.io/easy6502/) by Nick Morgan | The zero-to-code path: registers, addressing modes, stack, branching, the Snake example, game structure. CC BY 4.0 |
| [Wilson Mines 6502 Primer](https://wilsonminesco.com/6502primer/) by Garth Wilson | Practical programming, memory maps, stacks, interrupts, NMOS/CMOS differences, self-modifying code |
| [Wilson Mines: 6502 stacks](http://wilsonminesco.com/stacks/) | The stack as a data structure, not just `PHA`/`PLA` |
| [Wilson Mines: 6502 interrupts](http://wilsonminesco.com/6502interrupts/) | IRQ/NMI/BRK sequence, vectors, latency, handler design |
| [Wilson Mines: NMOS-CMOS differences](http://wilsonminesco.com/NMOS-CMOSdif/) | 65C02 additions and behavior changes |
| [Obelisk 6502 Guide](https://www.nesdev.org/obelisk-6502-guide/) | Instruction-by-instruction reference and examples |
| [NESdev: Instruction reference](https://www.nesdev.org/wiki/Instruction_reference) | Official opcode/flag/cycle tables |
| [Masswerk 6502 Instruction Set](https://www.masswerk.at/6502/6502_instruction_set.html) | Opcode matrix, addressing modes, flags, cycle counts used to build `opcodes.md` |
| [Nerdy Nights](https://nerdy-nights.nes.science/) | NES-specific assembly course: PPU, APU, mappers, controllers |
| [ChibiAkumas 6502 series](https://www.chibiakumas.com/6502/) | Multi-platform 6502 tutorials and worked examples |
| [Codebase64](https://codebase64.net/) | C64 6502 algorithms, raster and memory tricks |
| [8bitworkshop](https://8bitworkshop.com/) | Browser IDE, debugger, examples, CLI |
| [6502.org tutorials](http://www.6502.org/tutorials/) | Bruce Clark's classic tutorials (site availability varies) |

Out-of-print books worth finding in a library or archive:

- *6502 Assembly Language Programming* — Lance Leventhal.
- *Programming the 6502* — Rodnay Zaks.
- *Machine Language for Beginners* — Compute! Books.

## Repos

| Repo | What it contributed |
|---|---|
| [skilldrick/easy6502](https://github.com/skilldrick/easy6502) | Source of the Easy 6502 book |
| [skilldrick/6502js](https://github.com/skilldrick/6502js) | JavaScript assembler/simulator behind Easy 6502 |
| [8bitworkshop/8bitworkshop](https://github.com/8bitworkshop/8bitworkshop) | IDE, CLI, toolchains, examples, debugger workflow |
| [NovaSquirrel/NovaTheSquirrel](https://github.com/NovaSquirrel/NovaTheSquirrel) | Real NES game structure (C + assembly, banking, input, camera) |
| [sebastianromerocruz/Game-Programming-In-Assembly](https://github.com/sebastianromerocruz/Game-Programming-In-Assembly) | NES game-dev lecture: data movement, branching, animation, controller input |
| [jefftranter/6502](https://github.com/jefftranter/6502) | Monitor, BASIC, hardware examples for 6502 machines |
| [cc65/cc65](https://github.com/cc65/cc65) | `ca65`/`ld65`, segments, macros, NES target |
| [freem/asm6f](https://github.com/freem/asm6f) | Simple NES assembler, iNES directives, symbol output |
| [dasm-assembler/dasm](https://github.com/dasm-assembler/dasm) | Macro assembler syntax and Atari heritage |
| [meonwax/acme](https://github.com/meonwax/acme) | ACME syntax and cross-platform directives |
| [mnaberez/py65](https://github.com/mnaberez/py65) | Python simulator, instruction cycles, test harness |
| [mist64/perfect6502](https://github.com/mist64/perfect6502) | Transistor-level reference simulation |
| [Klaus2m5/6502_65C02_functional_tests](https://github.com/Klaus2m5/6502_65C02_functional_tests) | Functional opcode, interrupt and decimal tests |
| [SingleStepTests/65x02](https://github.com/SingleStepTests/65x02) | Per-instruction JSON state/cycle tests |
| [christopherpow/nes-test-roms](https://github.com/christopherpow/nes-test-roms) | NES CPU/PPU/APU test ROMs |
| [bruddog/Tecmo_Super_Bowl_NES_Disassembly](https://github.com/bruddog/Tecmo_Super_Bowl_NES_Disassembly) | A full commercial-game disassembly to read |

## Documentation used for syntax and directives

- [ca65 Users Guide](https://cc65.github.io/doc/ca65.html) — segments, macros, scopes, `.proc`, address-size prefixes.
- [ld65 Users Guide](https://cc65.github.io/doc/ld65.html) — memory areas, segments, config files, label/debug output.
- [asm6f readme](https://github.com/freem/asm6f/blob/master/readme.txt) — `ORG`, `DB`/`DW`, `MACRO`, `INESPRG`/`INESCHR`/`INESMAP`, symbol options.
- [DASM documentation](https://dasm-assembler.github.io/) — `processor`, `ORG`, `DC.B`/`DC.W`, macros.
- [ACME manual](https://sourceforge.net/projects/acme-crossass/) — `!cpu`, `!to`, `!byte`, `!word`, `!macro`.

## Related skills in this repo

- [NES 6502 optimizations](../../nes-6502-assembly/SKILL.md) — NES-specific size/speed tricks.
- [NES memory map](../../nes-memory-map/SKILL.md) — CPU/PPU/APU address map.
- [NES PPU rendering](../../nes-ppu-rendering/SKILL.md) — vblank, OAM, nametables.
- [NES APU audio](../../nes-apu-audio/SKILL.md) — channels, envelopes, music engines.
- [NES cart mappers](../../nes-cart-mappers/SKILL.md) — banking and mapper hardware.
- [6502 learning resources](../../../docs/6502.md) — the curated reading list this skill grew from.

## Licensing notes

The skill text is original. The opcode data is factual (instruction encodings and cycles are not copyrightable); the table was generated from Masswerk and checked against py65. Easy 6502 is CC BY 4.0; cc65 is Zlib; py65 is BSD-3; perfect6502 is MIT; Klaus tests are GPL-3.0; 65x02 is MIT; Nova the Squirrel is GPL-3.0; jefftranter/6502 is Apache-2.0. Follow the original licenses if you reuse their code.
