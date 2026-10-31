# Sources

This skill was built from the BZK toolchain and its worked examples, plus the FCEUX/Mesen logging behavior and the ca65 toolchain.

## Primary

| Source | What it contributed |
|---|---|
| [BZK 6502 Disassembler](https://github.com/cyneprepou4uk/BZK-6502-Disassembler) | Config format, output syntax, CDL flag decoding, `a:` handling, Lua implementation |
| [BZK manual: introduction](https://cyneprepou4uk.github.io/iromhacker/nes/en/bzk6502/1/index.html) | Workflow and requirements |
| [BZK manual: CDL](https://cyneprepou4uk.github.io/iromhacker/nes/en/bzk6502/2/index.html) | FCEUX Code/Data Logger procedure |
| [BZK manual: config](https://cyneprepou4uk.github.io/iromhacker/nes/en/bzk6502/3/index.html) | Bank table, input/output layout |
| [BZK manual: output](https://cyneprepou4uk.github.io/iromhacker/nes/en/bzk6502/4/index.html) | Prefix format, CDL flags, `a:`, ca65 compatibility |
| [BZK manual: Notepad++](https://cyneprepou4uk.github.io/iromhacker/nes/en/bzk6502/5/index.html) | Labeling scripts and preparation flow |
| [NES-Games-Disassembly](https://github.com/cyneprepou4uk/NES-Games-Disassembly) | 40+ compilable examples, `assemble.sh`, `preparations.lua`, `ld65.cfg`, label conventions |
| [iromhacker](https://github.com/cyneprepou4uk/iromhacker) | Russian ROM-hacking curriculum: 6502, FCEUX debugger, hex editor, PPU viewer, RAM watch |

## Emulators and CDL

| Source | What it contributed |
|---|---|
| [FCEUX](https://fceux.com/) | Code/Data Logger; CDL is written by the debugger |
| [FCEUX source: `debug.cpp`](https://github.com/TASEmulators/fceux) | Flag semantics (`C`, `D`, data mapping, `J`, `I`, `A`) cross-checked against BZK's decoder |
| [Mesen](https://www.mesen.ca/) | Alternative CDL source and debugger |
| [Mesen source](https://github.com/SourMesen/Mesen2) | CDL implementation reference |

The bit meanings in [cdl.md](cdl.md) are the ones BZK decodes. FCEUX's `debug.cpp` is the source of truth for the logger; if a different emulator writes a different layout, verify before feeding BZK.

## Assembler and linker

| Source | What it contributed |
|---|---|
| [ca65 Users Guide](https://cc65.github.io/doc/ca65.html) | Segments, `.org`, `.include`, address-size prefixes, macros, scoping |
| [ld65 Users Guide](https://cc65.github.io/doc/ld65.html) | Memory areas, segments, `file = %O`, label/debug output |
| [cc65](https://github.com/cc65/cc65) | Toolchain used by BZK output and NES-Games-Disassembly |

## NES context

| Source | What it contributed |
|---|---|
| [NESdev wiki: CPU](https://www.nesdev.org/wiki/CPU) | 2A03/2A07, vectors, memory map |
| [NESdev wiki: iNES](https://www.nesdev.org/wiki/INES) | Header layout, PRG/CHR sizes, mapper field |
| [NESdev wiki: Mapper](https://www.nesdev.org/wiki/Mapper) | Bank windows and mapper behavior |
| [NESdev wiki: CPU memory map](https://www.nesdev.org/wiki/CPU_memory_map) | `$8000–$FFFF` PRG windows, `$6000` SRAM |
| [6502 assembly skill](../../6502-assembly/SKILL.md) | ISA, addressing modes, `a:`/ca65 details, cycle rules |
| [NES cart mappers skill](../../nes-cart-mappers/SKILL.md) | Mapper bank layouts |
| [Tecmo Super Bowl ROM map skill](../../tecmosuper-rom-map/SKILL.md) | A worked example of bank/file-offset translation |

## Community

- [RHDN: BZK topic](https://www.romhacking.net/forum/index.php?topic=31875.0)
- [RHDN: NES-Games-Disassembly topic](https://www.romhacking.net/forum/index.php?topic=32220.0)
- [cyneprepou4uk profile](https://github.com/cyneprepou4uk)

## Licensing and use

BZK is the author's tool; check its repository for the current license before redistributing it. NES-Games-Disassembly contains source derived from commercial ROMs: use it to study games you own, and do not redistribute the ROMs or the reconstructed source. The scripts in this skill are original and dependency-free.
