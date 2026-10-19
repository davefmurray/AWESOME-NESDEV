---
name: tecmosuper-data
description: "Tecmo Super Bowl data: player names, attributes, team pointers, team data, schedules, standings, stats and battery saves, plus 28 vs 32-team ROM differences. Use when editing rosters, ratings, team names, schedules or season saves, or when a data edit shifts a pointer and corrupts the next table."
---

# Tecmo Super Bowl data

TSB data is a set of fixed-size tables and pointer tables, mostly in banks `00`, `01`, `0E`, `19`. The tables are easy to edit; the pointers are what break.

## Core tables

| Data | File offset | Notes |
|---|---|---|
| Player names | `0x06D0–0x2E2C` | strings + pointer region; crosses bank 0→1 |
| Player attributes | `0x3010–0x3CD0` | ratings, positions, numbers |
| Team names / mascots | pointer table at `0x1FC10` | text at `0x1FD00+` |
| Team default playbooks | `0x1D310` | bank `0E` |
| Play names / pointers | `0x1D410–0x1DA10` | bank `0E` |
| Schedule / standings | bank `19` + menu scripts | screen data in bank `0F` |
| Season state / stats | SRAM `$6000–$7FFF` | battery-backed |
| CHR / graphics | `0x40010+` | see graphics skill |

### TSB pointer convention

Team-name pointers are little-endian pairs followed by a base add:

```
bytes at 0x1FC10: F0 BC
swap:             BC F0
add 0x14010:      BC F0 + 14 010 = 1F D00
→ text at 0x1FD00
```

The length of each string is the gap to the next pointer. Inserting characters shifts every following string **and** every pointer after it. Prefer replacing in place, or relocate the whole block and update the table.

Different tables use different base values; verify with one known string before editing a new table.

## Rosters and ratings

- TSBTool is the safe route: it writes the tables and pointers for you.
- If editing by hand, keep the table stride and order; a one-byte insert shifts every subsequent player.
- Ratings are not all on the same scale: RP/RS/PC/PA/APB/AKB/BC/REC/INT have their own ranges.
- Sim uses a separate attribute table; see [sim](../tecmosuper-sim/SKILL.md).

## Team data and names

- Team name, mascot, city and abbreviation each have a pointer/length convention.
- The team-data screen uses the same strings; changing a name can overflow the screen if the new string is longer.
- 32-team ROMs add teams and relocate some name tables.

## Schedule, standings, playoffs

- Schedule graphics and the number of games are separate edits.
- Playoff bracket graphics and seeding logic are separate.
- Some 32-team ROMs fix the top seed to P1; that is a code/data change, not a graphics one.

## Stats and saves

- Season stats live in SRAM; clearing the `.sav` is required when testing table changes.
- Save states from a different ROM/revision can carry stale data.
- "Enable battery emulation" is an emulator setting, not a ROM edit.
- Adding a stats screen or tackles is code + PPU work, not just a table.

## Doc map

Start with [GENERAL INFO](../../docs/tsb/README.md#general-info) and [STATS & SAVE STATES](../../docs/tsb/README.md#stats-and-save-states).

| Topic | Card |
|---|---|
| Team pointers | [TSB Team Pointer Info](../../docs/tsb/general-info/60112-401794-tsb-team-pointer-info.md) |
| ROM locations | [TSB ROM Hex Location Index](../../docs/tsb/general-info/53101-tsb-rom-hex-location-index.md) · [Various ROM Hex Locations](../../docs/tsb/general-info/53112-various-rom-hex-locations.md) |
| RAM / MMC3 | [CPU RAM and MMC3 General Locations](../../docs/tsb/general-info/53074-cpu-ram-and-mmc3-general-locations.md) |
| Control flow | [Control Execution Code](../../docs/tsb/general-info/9701-control-execution-code.md) |
| Stats code | [TSB Stats Code](../../docs/tsb/stats-save-states/10280-tsb-stats-code.md) |
| Saves | [Nestopia Save State Info](../../docs/tsb/stats-save-states/12156-nestopia-save-state-info.md) · [Battery emulation](../../docs/tsb/stats-save-states/7851-enable-battery-emulation-for-an-incorrectly-configured-tecmo-super-bow.md) |
| 32-team fix | [Player-2 Condition Fix](../../docs/tsb/32-team-rom-fixes/10436-player-2-condition-fix.md) |


## Checks

- Did you insert/delete bytes in a string table? Then every following pointer must move.
- Is the pointer base correct for this table?
- Does the new string fit the screen and the original allocation?
- Are you editing the 28-team or 32-team base?
- Did you clear SRAM before testing?
- Does TSBTool report overlapping writes?

## Failure modes

| Symptom | Cause |
|---|---|
| Garbled names after one edit | String length changed, pointers not updated |
| Player ratings shift | Table stride/order changed |
| Team name appears on wrong team | Pointer table misaligned |
| Season crashes | Corrupt SRAM or schedule table |
| Stats wrong after sim | Sim attribute table, not the roster table |

## References

- [GENERAL INFO index](../../docs/tsb/README.md#general-info) · [STATS & SAVE STATES](../../docs/tsb/README.md#stats-and-save-states)
- [Team pointer thread](https://tecmobowl.org/topic/60112-team-location-namemascot-length-pointer/)
- [ROM map](../tecmosuper-rom-map/SKILL.md) · [Hacking workflow](../tecmosuper-hacking/SKILL.md)
