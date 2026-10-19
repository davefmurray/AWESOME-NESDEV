---
name: tecmosuper-hacking
description: "Tecmo Super Bowl ROM hacking workflow: TSBTool SET commands, hex edits, the disassembly rebuild, 28 vs 32-team ROMs, testing in Mesen/FCEUX, and shipping IPS/BPS patches. Use when editing TSB rosters, attributes, playbooks, graphics, cutscenes, gameplay or schedules."
---

# Tecmo Super Bowl hacking

Three routes, in increasing order of control:

| Route | Use for | Tools |
|---|---|---|
| **TSBTool text file** | Rosters, team data, and `SET` byte patches | TSBTool Supreme |
| **Hex edit** | One table, one palette, one instruction | HxD / 010 Editor + this map |
| **Rebuild from disassembly** | Code changes, new routines, large moves | asm6f + bruddog disassembly + original ROM |

Most community hacks are route 1 plus a handful of route 2 edits. Route 3 is for gameplay code and anything that needs labels.

## SET commands

TSBTool accepts lines like:

```text
SET(0x28293,0xEAEAEAEA)
SET(0x24F7D,0xEAEAEAEAEA)
SET(0x1897f,0x20)
```

- First argument: **file offset** in the ROM, header included.
- Second argument: hex bytes to write, in order.
- `#` starts a comment.

That is the entire patching model. It is powerful and easy to misuse:

- **Offsets are file offsets, not CPU addresses.**
- A `SET` from a 28-team hack can corrupt a 32-team ROM, and vice versa.
- Two `SET`s can overlap; TSBTool's "check SET commands setting values in the same location" option exists for a reason.
- A `SET` can land in the middle of a pointer table or a string; back up first.

The community list is the reference: [Set commands list for NES TSB](https://tecmobowl.org/forums/topic/69338-set-commands-list-for-nes-tsb-updated-91725/). Every entry there is a file offset plus bytes, often with a forum link explaining the hack.

## What lives where

| Edit | Where | Route |
|---|---|---|
| Player names | bank `00`, around `0x06D0` | TSBTool |
| Attributes / ratings | bank `01`, around `0x3010` | TSBTool |
| Team data, playbooks | bank `0E`, around `0x1D310` | TSBTool |
| Offensive play scripts | bank `04` | disassembly / hex |
| Defensive play scripts | bank `05` | disassembly / hex |
| Cutscenes / events | banks `06`, `07`, `0F` | [events skill](../tecmosuper-events/SKILL.md) |
| Menus / standings / schedule screens | bank `0F` | events + hex |
| Graphics / tiles | CHR `0x40010+` | YY-CHR / TSBIDesign |
| Palettes | bank `0D` | hex |
| Gameplay / sim logic | banks `12`–`16`, `1A`–`1D` | disassembly / SET hacks |
| Schedule / playoffs | bank `19` + menu scripts | hex / docs |
| Sound / music | banks `1B`–`1D` | docs / hex |

Exact offsets are in [the ROM map](../tecmosuper-rom-map/SKILL.md) and the [rom_map.xlsx](https://github.com/bruddog/Tecmo_Super_Bowl_NES_Disassembly/blob/main/DOCS/rom_map.xlsx).

## Workflow

1. **Start from a known base.** Record the ROM's name, region, 28/32-team status, CRC32 and SHA-256. Keep it read-only in `roms/`.
2. **Copy to `work/`.** Never edit the pristine file.
3. **Pick the edit route.** Data → TSBTool/hex; code → disassembly; graphics → CHR.
4. **Change one thing.** Write down the offset and the original bytes.
5. **Test in an emulator.** Boot, exhibition, the specific screen/play, then a season save.
6. **Clear SRAM** when testing season/team-control changes; stale saves hide bugs.
7. **Diff against pristine.** Confirm only the intended bytes changed.
8. **Ship IPS/BPS**, never the patched ROM.

## 28-team vs 32-team

TSB shipped with 28 teams. The community 32-team ROM adds teams by relocating and expanding tables. Consequences:

- Offsets differ; a `SET` for one base can be wrong for the other.
- Menu/standings/playoff screens have different scene scripts.
- Some hacks explicitly say "28 team" or "32 team only".
- Always test the exact base you are shipping.

## Rebuilding from source

The [bruddog disassembly](https://github.com/bruddog/Tecmo_Super_Bowl_NES_Disassembly) rebuilds the original ROM byte-for-byte.

```bash
# requires the original ROM as TSB.nes in the repo root
asm6f_32.exe master_build.asm -L
```

- `asm6f_32.exe` is Windows; build/use asm6f on macOS/Linux.
- The build **reads bytes from `TSB.nes`** for graphics and samples, so the source alone is not a complete ROM.
- `-L` produces a listing; keep it, it is the symbol map.
- Edit the `.asm` bank files, rebuild, then diff against the original.

Labels you will use constantly:

| Label | Bank | Meaning |
|---|---|---|
| `CUTSCENE_DRAW_SCRIPT_BANK` | 6 | gameplay cutscenes |
| `LEADERS_SCOREBOARD_SCHED_DRAW_SCRIPT_BANK` | 7 | leaders/scoreboards |
| `MENU_DRAW_SCRIPT_BANK` | 15 | menus/data screens |
| `DRAW_SCENE_UNTIL_ENDED` | 30 | play a scene and wait |
| `END_OLD_SCENE_DRAW_NEW_SCENE` | 30 | queue a scene |
| `DRAW_SCENE_RETURN_PREV_8000_BANK` | 30 | bank-safe menu scene |
| `CUTSCENE_ADDR` | 18/19 | sequence pointer table (gameplay loop source) |
| `CUTSCENE_TO_DRAW` | RAM | sequence index |

## Graphics and palettes

- CHR starts at `0x40010` and runs 128 KB (16 × 8 KB banks). A 1 KB CHR bank is 0x400 bytes (four 0x100-byte quarters).
- Tiles are NES 2bpp planar, 16 bytes each.
- Palettes are in bank `0D`; the palette format is NES `$3F00`-style indices.
- Helmet/portrait/logo edits have their own pointers and palettes; use the docs directory, not guesswork.
- `TSBIDesign.exe` (in the disassembly `TOOLS/`) is a community design utility; read its docs before assuming which graphics it edits.

## Testing

| Test | Why |
|---|---|
| Boot + title | Header/bank sanity |
| Exhibition | Fast access to gameplay |
| The edited play/screen | The actual change |
| Season + save | SRAM, schedule, standings |
| Cutscene path | Event sequences and pointers |
| 2-player | Some hacks assume P1 |

Emulators: Mesen (best debugger), FCEUX (Lua/CDL, familiar). Clear `.sav` files between season tests.

## Distribution

- Build an IPS or BPS against the **pristine** ROM ([Flips](https://github.com/Alcaro/Flips)).
- Record the source ROM's SHA-256 and the patch's target base (28/32 team, region, revision).
- Do not distribute ROMs or pre-patched ROMs.
- Keep a changelog of offsets and SET commands; it is the only way to rebase a hack later.

## Pitfalls

- **Wrong base ROM.** Most "my patch broke the game" reports are a 28 vs 32-team mismatch.
- **Overlapping SETs.** Two hacks write the same byte; the last one wins silently.
- **Pointer tables.** Inserting text or scenes without updating pointers shifts data and corrupts the next table.
- **Bank boundaries.** A table that crosses an 8 KB bank is fine in the file, but code that indexes it with a bank switch is not.
- **SRAM.** Old saves mask new bugs; clear them.
- **Cutscenes are visual.** Editing a touchdown event does not change scoring.

## References

- [Disassembly](https://github.com/bruddog/Tecmo_Super_Bowl_NES_Disassembly) · [ROM map](https://github.com/bruddog/Tecmo_Super_Bowl_NES_Disassembly/blob/main/DOCS/rom_map.xlsx)
- [Set commands list](https://tecmobowl.org/forums/topic/69338-set-commands-list-for-nes-tsb-updated-91725/)
- [TSB Hacks documentation directory](https://tecmobowl.org/forums/topic/9725-tsb-hacks-documentation-directory-updated-01182023/)
- [TSBTool topic](https://tecmobowl.org/forums/topic/11106-tsb-editor-tsbtool-supreme-season-generator/)
- [Hex location index](https://tecmobowl.org/topic/53101-tsb-rom-hex-location-index/)
- `references/set-commands.md` · `references/tools.md`
