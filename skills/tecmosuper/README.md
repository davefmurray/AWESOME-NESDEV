# Tecmo Super Bowl

Game-specific skills for **Tecmo Super Bowl (NES, 1991)**. TSB is not a generic NES ROM: it has its own bank map, event engine, pointer tables, 28/32-team variants, and a community toolchain. These skills keep that knowledge out of the generic NES packs.

| Skill | Use when |
|---|---|
| [tecmosuper-events](../tecmosuper-events/SKILL.md) | Triggering or editing cutscenes, menus, halftime, touchdown scenes; decoding event IDs |
| [tecmosuper-rom-map](../tecmosuper-rom-map/SKILL.md) | Converting CPU addresses to file offsets; locating team data, playbooks, cutscenes, sound |
| [tecmosuper-hacking](../tecmosuper-hacking/SKILL.md) | TSBTool `SET` commands, hex edits, rebuilding from the disassembly, testing, patching |

## Install

These are flat skill directories so any harness can load them:

```bash
cp -r skills/tecmosuper-events ~/.claude/skills/
cp -r skills/tecmosuper-rom-map ~/.claude/skills/
cp -r skills/tecmosuper-hacking ~/.claude/skills/
```

## The one thing to get right

There are **two** numbering systems:

1. **Sequence index** — `CUTSCENE_TO_DRAW`, indexes `CUTSCENE_ADDR`, picks a whole sequence (punt, sack, FG).
2. **Scene/event ID** — one draw script inside a bank (`$38` = rushing TD in bank 6).

The group (`X` in the 2008 list) is the **bank**. The event (`A`) is the **scene**. `$38` in bank 6 is not `$38` in bank 15.

## Source hierarchy

1. **bruddog's disassembly** (2025) — labels, bank IDs, exact code. Newer than everything else.
2. **The 2008 events thread** — the community's event names and IDs; still the reference for "what is event $4A".
3. **Community docs / TSBTool lists** — practical offsets and SET commands, but base-ROM-specific.

When they disagree, trust the disassembly and note the discrepancy.

## Base ROM caveat

TSB shipped with 28 teams; most modern hacks use a 32-team ROM. Offsets, menus and some code differ. Every offset in these skills assumes the original 28-team USA ROM unless stated. Test on the exact base you ship.

## Not covered yet

- Full playbook design (formation/play data structures) — the disassembly and `TECMO PLAYBOOK HACKERS GUIDEBOOK` cover it.
- Graphics pipeline beyond CHR/palette basics.
- Schedule/playoff expansion.
- Sim engine stat formulas.
- 32-team relocation details.

Each is a candidate for its own skill; the category is meant to grow.

## Legal

No ROMs, no patched ROMs. The disassembly is source code that requires the original ROM to build; it does not include it.
