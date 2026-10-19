# Resources

Non-agent tools and references. Everything here was reachable in October 2026; community sites rot, so prefer repositories and archives when a link dies.

## Learn

| Resource | Why |
|---|---|
| [NESdev wiki](https://www.nesdev.org/wiki/) | The reference. Hardware, mappers, formats, tools, tests |
| [Nerdy Nights](https://nerdy-nights.nes.science/) | The classic step-by-step NES assembly course, now a PDF/online book |
| [nesdoug](https://nesdoug.com/) | C-based NES tutorials; pairs well with cc65 |
| [NESdev forums](https://forums.nesdev.org/) | Where the people who wrote the wiki answer questions |
| [NESdev wiki: Tools](https://www.nesdev.org/wiki/Tools) | Canonical list of assemblers, editors, emulators, utilities |
| [NESdev wiki: Emulator tests](https://www.nesdev.org/wiki/Emulator_tests) | Test ROMs for PPU/APU/CPU behaviour |

## Emulators

| Emulator | Platform | Why use it |
|---|---|---|
| [Mesen](https://www.mesen.ca/) | Windows/Linux/macOS | Best-in-class debugger, accuracy, rewinding; the MCP fork is built on it |
| [FCEUX](https://fceux.com/) | Windows/Linux/macOS | Lua scripting, CDL coverage, cheat search; the NES hacking workhorse |
| [BizHawk](https://github.com/TASEmulators/BizHawk) | Windows (Wine elsewhere) | TAS tools, Lua, many cores; the base for mcp-bizhawk |
| [Nestopia UE](http://0ldsk00l.ca/nestopia/) | Multi | Accuracy-focused, simple |
| [puNES](https://github.com/punesemu/puNES) | Multi | Accurate, good for hardware-edge testing |

Agent note: only Mesen (fork) and BizHawk have MCP servers. FCEUX is driven by Lua scripts from the `fceux-lua` skill.

## Assemblers and toolchains

| Tool | Language | Link |
|---|---|---|
| cc65 / ca65 / ld65 | C and 6502 asm | <https://cc65.github.io/> · [ca65 manual](https://cc65.github.io/doc/ca65.html) · [ld65 manual](https://cc65.github.io/doc/ld65.html) |
| asm6f | 6502 asm | <https://github.com/freem/asm6f> |
| NESASM | 6502 asm | See [NESdev Tools](https://www.nesdev.org/wiki/Tools) |
| dotnes | C# (.NET IL) | <https://github.com/jonathanpeppers/dotnes> |
| neslib | C library for cc65 | <https://github.com/clbr/neslib> |
| NESmaker | GUI / logic blocks | <https://www.thenew8bitheroes.com/> |

ROM-only projects can skip all of these and use romdev's bundled cc65.

## Graphics

| Tool | Use |
|---|---|
| [YY-CHR](https://www.romhackplaza.org/index.php/utilities/yy-chr-utility) | Tile/CHR editor; the classic for NES ripping and editing |
| [NES Screen Tool](https://github.com/BrokeStudio/NES-Screen-Tool) | Nametable, attribute and sprite layout |
| [Aseprite](https://www.aseprite.org/) | Source pixel art; romdev imports Aseprite/LibreSprite |
| [NESdev: pattern tables](https://www.nesdev.org/wiki/PPU_pattern_tables) | Tile format, 2-bitplanes |
| [NESdev: nametables](https://www.nesdev.org/wiki/PPU_nametables) | 32×30 layout and mirroring |
| [NESdev: palettes](https://www.nesdev.org/wiki/PPU_palettes) | The 64-color master palette |

## Audio

| Tool | Use |
|---|---|
| [FamiStudio](https://www.famistudio.org/) | Modern NES tracker; exports data for homebrew players |
| [0CC-FamiTracker](https://github.com/HertzDevil/0CC-FamiTracker) | Extended FamiTracker fork; text export widely supported |
| FamiTone2 | Lightweight homebrew sound driver; bundled in romdev's NES examples |
| [NESdev: APU](https://www.nesdev.org/wiki/APU) | Channels, envelopes, frame counter, DMC |

## Reverse engineering and patching

| Tool | Use |
|---|---|
| [retrodisasm](https://github.com/retroenv/retrodisasm) | Tracing disassembler, CDL-guided, reassemblable output |
| [Ghidra](https://ghidra-sre.org/) | Static analysis and decompiler; 6502 language built in |
| [Rizin](https://rizin.re/) | Scriptable binary analysis; 6502 support |
| [Flips](https://github.com/Alcaro/Flips) | IPS/BPS patch creation and application |
| [HxD](https://mh-nexus.de/en/hxd/) | Windows hex editor |
| [010 Editor](https://www.sweetscape.com/010editor/) | Templates for binary formats; commercial |
| [NESdev: iNES](https://www.nesdev.org/wiki/INES) | Header format |
| [NESdev: Mapper](https://www.nesdev.org/wiki/Mapper) | Mapper list and behavior |

## Hardware

| Item | Notes |
|---|---|
| [EverDrive-N8](https://krikzz.com/our-products/cartridges/everdrive-n8.html) | Flash cart; runs homebrew and most mappers |
| PowerPak | Older flash cart; check availability before buying |
| Famicom + adapter | Needed for Famicom-only mappers and expansion audio |
| CRT / RGB mod | Useful for timing-sensitive effects and light-gun games |

## Community

- [r/NESdev](https://www.reddit.com/r/NESdev/) — smaller, practical
- [itch.io NES tag](https://itch.io/games/tag-nes) — play what people are making
- [NESdev forums](https://forums.nesdev.org/) — the deep end

## Agent-era additions

These are the pages that did not exist a year ago:

- [MCP servers](mcp-servers.md) — romdev, Mesen MCP, mcp-bizhawk, Nes.Mcp, GhidraMCP, Gearlynx
- [Agent skills](agent-skills.md) — nes-skills, re-skill, dotnes skills, retro-build, 6502 reference
- [The agent stack](agent-stack.md) — configs and session hygiene
- [Homebrew](homebrew.md) and [ROM hacking](romhacking.md) — workflows that use them

## Link policy

- Prefer the upstream repository over a blog repost.
- If a tool is Windows-only or abandoned, say so rather than hiding it.
- When a community site is down, link the NESdev wiki page or an archive instead of a dead homepage.
---

Part of [AWESOME NESDEV](../README.md) · [Start here](start-here.md) · [MCP servers](mcp-servers.md) · [Skills](agent-skills.md) · [Homebrew](homebrew.md) · [ROM hacking](romhacking.md)
