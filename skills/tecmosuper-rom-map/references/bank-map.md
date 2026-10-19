# Bank map

0-based bank IDs from `bank_ids.asm`. File offsets include the 16-byte iNES header.

| Bank | File start | File end | CPU window | Contents |
|---|---|---|---|---|
| `$00` | `0x00010` | `0x0200F` | switchable | Player names, name pointers |
| `$01` | `0x02010` | `0x0400F` | switchable | Player attributes and data |
| `$02` | `0x04010` | `0x0600F` | switchable | Offensive formations, play pointers, 4x4 metatiles |
| `$03` | `0x06010` | `0x0800F` | switchable | Defensive play pointers, special play pointers |
| `$04` | `0x08010` | `0x0A00F` | switchable | Offensive play scripts |
| `$05` | `0x0A010` | `0x0C00F` | switchable | Defensive play scripts |
| `$06` | `0x0C010` | `0x0E00F` | switchable | Cutscene scripts (gameplay) |
| `$07` | `0x0E010` | `0x1000F` | switchable | Season/scoreboard/leaders scripts |
| `$08` | `0x10010` | `0x1200F` | switchable | Sprite scripts 1 |
| `$09` | `0x12010` | `0x1400F` | switchable | Sprite scripts 2 |
| `$0A` | `0x14010` | `0x1600F` | switchable | 4x4 metatile tiles 1 |
| `$0B` | `0x16010` | `0x1800F` | switchable | 4x4 metatile tiles 2 + sim logic 1 |
| `$0C` | `0x18010` | `0x1A00F` | switchable | Sim logic 2, stats update |
| `$0D` | `0x1A010` | `0x1C00F` | switchable | Palettes, thrown-player animation |
| `$0E` | `0x1C010` | `0x1E00F` | switchable | Faces, team playbooks, play names, COM boost |
| `$0F` | `0x1E010` | `0x2000F` | switchable | Menus, roster, schedule, team data, message bar |
| `$10` | `0x20010` | `0x2200F` | switchable | Main game loop 1 |
| `$11` | `0x22010` | `0x2400F` | switchable | Main game loop 2 |
| `$12` | `0x24010` | `0x2600F` | switchable | High-level gameplay 1 |
| `$13` | `0x26010` | `0x2800F` | switchable | High-level gameplay 2, playcall |
| `$14` | `0x28010` | `0x2A00F` | switchable | Player script commands/physics 1 |
| `$15` | `0x2A010` | `0x2C00F` | switchable | Player script commands/physics 2, field/collision/ball |
| `$16` | `0x2C010` | `0x2E00F` | switchable | Ball animation |
| `$17` | `0x2E010` | `0x3000F` | switchable | Draw-script engine |
| `$18` | `0x30010` | `0x3200F` | switchable | NFL leaders, Pro Bowl, player data |
| `$19` | `0x32010` | `0x3400F` | switchable | Schedule, team data, defensive starters, control |
| `$1A` | `0x34010` | `0x3600F` | switchable | Sound mode, cutscene colors, COM juice, init, crash |
| `$1B` | `0x36010` | `0x3800F` | switchable | Sound engine |
| `$1C` | `0x38010` | `0x3A00F` | switchable | Song/effects data 1 |
| `$1D` | `0x3A010` | `0x3C00F` | switchable | Song/effects data 2 |
| `$1E` | `0x3C010` | `0x3E00F` | $C000–$DFFF (fixed) | Fixed main functions ($C000) |
| `$1F` | `0x3E010` | `0x4000F` | $E000–$FFFF (fixed) | DMC samples, reset, vectors ($E000) |
