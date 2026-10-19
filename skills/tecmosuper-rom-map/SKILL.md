---
name: tecmosuper-rom-map
description: "Tecmo Super Bowl NES ROM layout: 16-byte header, 256 KB PRG, 128 KB CHR, MMC3 banks, fixed $C000/$E000 banks, file-offset formulas, and where team data, playbooks, cutscenes, menus and sound live. Use when translating a TSB CPU address to a file offset, editing a bank, or locating a data table."
---

# Tecmo Super Bowl ROM map

TSB is a 384 KB image: a 16-byte iNES header, **256 KB PRG** (32 × 8 KB MMC3 banks), and **128 KB CHR** (16 × 8 KB banks), with battery-backed SRAM. Mapper **4 (MMC3)**.

The disassembly numbers banks two ways: its file names (`Bank1`, `Bank31`) are 1-based, while the source constants and this skill use 0-based bank IDs `$00–$1F`. Always say which one you mean.

## File layout

```
0x000010 – 0x04000F   256 KB PRG, 32 banks × 8 KB
0x040010 – 0x06000F   128 KB CHR, 16 banks × 8 KB
```

## Offset formulas

```
PRG bank b (0–31):    file = 0x10 + b * 0x2000
CHR bank c (0–15):    file = 0x40010 + c * 0x2000

bank 30 ($1E): file 0x3C010, CPU $C000–$DFFF   (fixed main functions)
bank 31 ($1F): file 0x3E010, CPU $E000–$FFFF   (DMC samples, reset, vectors)
```

Examples:

| CPU address | Bank | File offset |
|---|---|---|
| `$C390` | 30 | `0x3C3A0` |
| `$E000` | 31 | `0x3E010` |
| `$FFFC` (RESET) | 31 | `0x3FFFC` |
| `$8000` in bank 6 | 6 | `0x30010` |

`$C390` check: `0x10 + 30*0x2000 + ($C390-$C000) = 0x10 + 0x3C000 + 0x390 = 0x3C3A0`.

For a switchable bank, the CPU address alone is ambiguous — you must know which bank is mapped. Only the two fixed banks above are safe.

## Bank map

| Bank | Contents |
|---|---|
| `00` | Player names, name pointers |
| `01` | Player attributes and data |
| `02` | Offensive formations, offensive play pointers, 4×4 metatile backgrounds |
| `03` | Defensive play pointers, special play pointers |
| `04` | Offensive play scripts (per-player commands) |
| `05` | Defensive play scripts |
| `06` | Cutscene draw scripts — gameplay (`CUTSCENE_DRAW_SCRIPT_BANK`) |
| `07` | Season / scoreboard / leaders screens |
| `08` | Sprite scripts 1 |
| `09` | Sprite scripts 2 |
| `0A` | 4×4 metatile tiles 1 |
| `0B` | 4×4 metatile tiles 2 + sim logic 1 |
| `0C` | Sim logic 2, stats update |
| `0D` | Palettes, thrown-player animation |
| `0E` | Player faces, team playbooks, play names, COM boost |
| `0F` | Menus, roster, schedule, team data, message bar (`MENU_DRAW_SCRIPT_BANK`) |
| `10` | Main game loop 1 |
| `11` | Main game loop 2 |
| `12` | High-level gameplay loop 1 |
| `13` | High-level gameplay loop 2, play-call screen |
| `14` | Player script commands / physics 1 |
| `15` | Player script commands / physics 2, uniforms, field, collision, banner, ball |
| `16` | Ball animation |
| `17` | Draw-script engine (bank 24 in file names) |
| `18` | NFL leaders, Pro Bowl positions, player-attribute screens |
| `19` | Schedule, team data, defensive starters, team control, season reset |
| `1A` | Sound mode, cutscene colors, COM juice, player init, crash handler |
| `1B` | Sound engine |
| `1C` | Song / effects data 1 |
| `1D` | Song / effects data 2 |
| `1E` | Fixed main functions at `$C000` |
| `1F` | DMC samples, reset stub, vectors at `$E000` |

This is the `bank_ids.asm` enum, which is the most reliable bank map in the disassembly. The `rom_map.xlsx` sheet adds byte ranges inside each bank.

## Known data landmarks

| Data | File offset | Notes |
|---|---|---|
| iNES header | `0x00–0x0F` | 16 bytes; not part of PRG |
| Player names | `0x06D0–0x2E2C` | string/pointer region, crosses bank 0→1 |
| Player attributes | `0x3010–0x3CD0` | ratings, positions, numbers |
| Offensive formations | `0x4010–0x41F3` | positioning |
| Offensive play pointers | `0x4410–0x4BF6` | point into bank 4 scripts |
| 4×4 metatile backgrounds | `0x5010–0x6000` | background structures |
| Defensive play pointers | `0x6010–0x75FF` | point into bank 5 scripts |
| Special defensive pointers | `0x7600–0x800F` | fumble/onside/etc. |
| Offensive play commands | CPU `$8000–$9FFF` (file `0x8010–0x9FFF`) | bank 4 |
| Defensive play commands | CPU `$A000–$BFFF` (file `0xA010–0xBFFF`) | bank 5 |
| Team default playbooks | `0x1D310` | bank `0E` |
| Play names / pointers | `0x1D410–0x1DA10` | bank `0E` |
| Defensive reaction pointers | `0x1DC10` | bank `0E` |
| Cutscene scripts | `0x30010+` | bank 6 |
| Menu scripts | `0x1E010+` | bank `0F` |
| CHR | `0x40010–0x6000F` | 128 KB, 16 × 8 KB banks |

These are file offsets (header included). The 2013 community index lists the same regions with slightly different boundaries because it omits or includes the header in places; verify the first bytes before trusting a boundary.

## SRAM

- `$6000–$7FFF` is battery-backed PRG-RAM.
- Season state, team control, schedule and stats live there.
- On reset, the game validates/initializes SRAM; a corrupt save can look like a crash.
- MMC3 SRAM write-protect is toggled via `$A001`; the game has helpers (`MMC3_SRAM_WRITE_ENABLE` in the disassembly).

## CPU ↔ file translation

For the fixed banks:

```
file = 0x10 + bank*0x2000 + (cpu - base)
cpu  = base + (file - 0x10 - bank*0x2000)
```

`base` is `$C000` for bank 30, `$E000` for bank 31. For switchable banks, use the debugger's current mapping, not a formula.

## Checks

- Did you subtract/add the 16-byte header? A 0x10 error looks like "the data is shifted by one byte".
- Is the bank number 0-based (`$00–$1F`) or the disassembly's 1-based file name?
- Is the address in the fixed area (`$C000+`) or a switchable window?
- Does the CHR offset start at `0x40010`, not `0x40000`?
- Are you editing PRG when you meant CHR (or vice versa)?
- For a table with pointers, are the pointers file offsets or CPU addresses? TSB uses both in different places.

## Tools

- [Disassembly](https://github.com/bruddog/Tecmo_Super_Bowl_NES_Disassembly) — `constants_variables/bank_ids.asm`, `rom_map.xlsx`, per-bank `.asm`.
- [TSB ROM Hex Location Index](https://tecmobowl.org/topic/53101-tsb-rom-hex-location-index/) — community offset list.
- [Many Various ROM Locations](https://tecmobowl.org/topic/53112-many-various-rom-locations/).
- Mesen or FCEUX hex editor for live mapping; HxD/010 Editor for file edits.

## References

- `references/bank-map.md` — bank table plus per-bank file ranges.
- `references/offsets.md` — formula worksheet and common landmarks.
- [Disassembly README](https://github.com/bruddog/Tecmo_Super_Bowl_NES_Disassembly)
