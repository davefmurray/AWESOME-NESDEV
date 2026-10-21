# Skills library

Sixteen installable agent skills: eight 6502/NES skills (including a comprehensive, platform-agnostic 6502 language skill), plus an eight-skill [Tecmo Super Bowl](tecmosuper/README.md) category. Each is a folder with a `SKILL.md` and `references/` — copy the whole folder into your harness's skills directory.

```bash
cp -r skills/6502-assembly skills/nes*/ skills/tecmosuper-*/ ~/.claude/skills/
```

| Skill | Use when |
|---|---|
| [nesdev-wiki-guide](nesdev-wiki-guide/SKILL.md) | You need the right NESdev page or a primary source |
| [nes-memory-map](nes-memory-map/SKILL.md) | Placing variables, reading dumps, computing addresses, PPU warmup |
| [nes-ppu-rendering](nes-ppu-rendering/SKILL.md) | Rendering, palettes, sprites, scrolling, NMI, black screens |
| [nes-cart-mappers](nes-cart-mappers/SKILL.md) | Headers, mapper choice, banking, mirroring, battery saves |
| [nes-apu-audio](nes-apu-audio/SKILL.md) | Sound channels, frames, envelopes, frequency math, DPCM |
| [nes-input-devices](nes-input-devices/SKILL.md) | Controllers, DPCM glitch, Zapper, Four Score |
| [6502-assembly](6502-assembly/SKILL.md) | Full ISA, addressing, 8/16-bit patterns, toolchains, testing |
| [nes-6502-assembly](nes-6502-assembly/SKILL.md) | NES-specific 6502 code, cycles, jump tables, optimizations |

### Tecmo Super Bowl

Game-specific skills for TSB, kept separate from the generic NES hardware packs. See the [category page](tecmosuper/README.md).

| Skill | Use when |
|---|---|
| [tecmosuper-events](tecmosuper-events/SKILL.md) | Cutscenes, menus, event IDs, the `$C390`/`$C3A2`/`$C3AF` engine |
| [tecmosuper-rom-map](tecmosuper-rom-map/SKILL.md) | Bank map, file offsets, CPU↔file translation, data locations |
| [tecmosuper-hacking](tecmosuper-hacking/SKILL.md) | TSBTool SET commands, hex edits, rebuild, 28/32-team, patches |
| [tecmosuper-graphics](tecmosuper-graphics/SKILL.md) | Uniforms, helmets, portraits, logos, palettes, screens |
| [tecmosuper-gameplay](tecmosuper-gameplay/SKILL.md) | Kicking, clock, downs, injuries, fumbles, conditions |
| [tecmosuper-playbooks](tecmosuper-playbooks/SKILL.md) | Play scripts, slots, names, defensive reactions |
| [tecmosuper-sim](tecmosuper-sim/SKILL.md) | COM juice, sim weights, coverage, season sim |
| [tecmosuper-data](tecmosuper-data/SKILL.md) | Rosters, attributes, team pointers, schedule, saves |

## Design

- `SKILL.md` is the procedure and the quick reference. `references/` holds the tables you only need when the task goes deep.
- Descriptions are written to trigger on user language ("black screen", "bank switch crash"), not only jargon.
- Every skill states failure modes and a checklist, because that is what saves the debugging session.
- No ROMs, no copyrighted assets, no copied wiki text. The content is a distillation with links to the primary sources.

## Provenance and license

The facts come from the NESdev Wiki, fetched in October 2026; the 62-page index is in [`nesdev-wiki-guide/references/page-index.md`](nesdev-wiki-guide/references/page-index.md). The wiki retains its own terms — link back to it rather than mirroring large sections.

Original text in this directory is released under the repository's CC0 license, like the rest of the wiki.

## Installing

| Harness | Path |
|---|---|
| Claude Code | `~/.claude/skills/<name>/SKILL.md` |
| Codex | `~/.codex/skills/` |
| Copilot / VS Code | `.github/skills/` |
| Generic agents | `.agents/skills/` |

Copy directories, not just the Markdown: `references/` is part of the skill.

## Not covered yet

The first release targets the core hardware. Missing, and worth a follow-up skill each:

- Expansion audio (VRC6, VRC7, N163, FDS, MMC5) and NSF playback
- FDS disk format, BIOS, and the Famicom Disk System
- Vs. System and PlayChoice-10 differences
- Compression formats and text engines
- Advanced raster techniques beyond sprite 0 / MMC3 IRQ
- The long tail of mappers beyond NROM/UxROM/CNROM/MMC1/MMC3/AxROM

## Testing a skill

Ask a question that should trigger it and one that should not:

```text
# should trigger nes-ppu-rendering
My NES ROM builds but the screen is black.

# should trigger nes-cart-mappers
This ROM says mapper 4 but crashes when it switches banks.

# should not trigger
How do I install cc65 on Ubuntu?
```

If the third triggers, the description is too broad.
