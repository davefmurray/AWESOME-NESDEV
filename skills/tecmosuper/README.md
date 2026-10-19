# Tecmo Super Bowl

Game-specific skills for **Tecmo Super Bowl (NES, 1991)**, kept out of the generic NES packs. TSB has its own bank map, event engine, pointer tables, 28/32-team variants, and a community toolchain.

| Skill | Use when |
|---|---|
| [tecmosuper-events](../tecmosuper-events/SKILL.md) | Triggering or editing cutscenes, menus, halftime, touchdown scenes; decoding event IDs |
| [tecmosuper-rom-map](../tecmosuper-rom-map/SKILL.md) | Converting CPU addresses to file offsets; locating banks and tables |
| [tecmosuper-graphics](../tecmosuper-graphics/SKILL.md) | Uniforms, helmets, portraits, logos, palettes, screens, CHR |
| [tecmosuper-gameplay](../tecmosuper-gameplay/SKILL.md) | Kicking, clock, downs, injuries, fumbles, conditions |
| [tecmosuper-playbooks](../tecmosuper-playbooks/SKILL.md) | Play scripts, playbook slots, play names, defensive reactions |
| [tecmosuper-sim](../tecmosuper-sim/SKILL.md) | COM juice, sim attributes, run/pass weights, coverage, season sim |
| [tecmosuper-data](../tecmosuper-data/SKILL.md) | Rosters, attributes, team pointers, schedule, stats, saves, 32-team |
| [tecmosuper-hacking](../tecmosuper-hacking/SKILL.md) | TSBTool `SET` commands, hex edits, rebuild, testing, patches |

## Documentation library

Every link in the [TSB Hacks documentation directory](https://tecmobowl.org/forums/topic/9725-tsb-hacks-documentation-directory-updated-01182023/) is indexed at [`../../docs/tsb/`](../../docs/tsb/README.md): **174 cards**, grouped into graphics, gameplay, CPU/sim, playbooks, stats/saves, events, music, general info and 32-team fixes. Each card has a summary, key offsets and the source link.

## Install

```bash
cp -r skills/tecmosuper-* ~/.claude/skills/
```

Eight flat skill directories; the `tecmosuper/` folder itself is just this index.

## The one thing to get right

There are **two** numbering systems:

1. **Sequence index** — `CUTSCENE_TO_DRAW`, indexes `CUTSCENE_ADDR`, picks a whole sequence (punt, sack, FG).
2. **Scene/event ID** — one draw script inside a bank (`$38` = rushing TD in bank 6).

The group (`X` in the 2008 list) is the **bank**. The event (`A`) is the **scene**. `$38` in bank 6 is not `$38` in bank 15.

## Source hierarchy

1. **bruddog's disassembly** (2025) — labels, bank IDs, exact code.
2. **The 2008 events thread** — community event names and IDs.
3. **The 2023 documentation directory** — practical offsets and SET commands, but base-ROM-specific.

When they disagree, trust the disassembly.

## Base ROM caveat

TSB shipped with 28 teams; most modern hacks use a 32-team ROM. Offsets, menus and some code differ. Every offset assumes the original 28-team USA ROM unless stated.

## Not covered yet

- 32-team relocation details and schedule expansion.
- Full season/playoff seeding code.
- Music/sound engine internals (the cards index them; no skill yet).
- Cutscene script bytecode authoring (events skill covers calling, not every opcode).

## Legal

No ROMs, no patched ROMs. The disassembly requires the original ROM to build; it does not include it. The doc cards link to TecmoBowl.org and quote only short excerpts.
