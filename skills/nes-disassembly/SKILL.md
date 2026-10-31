---
name: nes-disassembly
description: "CDL-guided NES disassembly and rebuild: capture Code/Data logs in FCEUX or Mesen, merge coverage, configure BZK 6502, produce compilable ca65 source, label code and data, and byte-verify the rebuilt ROM. Use when turning a cold NES ROM into annotated source, fixing a disassembly that shifts or will not assemble, or auditing code/data coverage."
---

# NES disassembly

A Code/Data Log (CDL) is a map of what the game actually executed and read. BZK turns that map into ca65 source. The loop is:

```
ROM + CDL → BZK → ca65 → rebuilt ROM → diff
                 ↑                         │
                 └── better CDL/labels ←───┘
```

This is a **coverage-driven** process, not a magic decompiler. The CDL tells you where the game has been; it does not tell you what the bytes mean.

## When to use this

- You have a cold NES ROM and want rebuildable, annotated source.
- An existing disassembly will not assemble, or the rebuilt ROM is shifted by a few bytes.
- You need to separate code from data tables, pointers and DPCM samples.
- You need to audit how much of a ROM a playthrough actually covered.

Do **not** use it to redistribute a commercial game's source. The output is for ROMs you own; keep it private unless the game is legally free.

## The hard rules

1. **CDL is coverage, not truth.** A byte with no flags may be data, unreachable code, or code copied to RAM. A byte with `C` may be a false positive from a jump into data.
2. **`a:` is not optional.** BZK emits `a:` when an absolute instruction targets `$00xx`. Without it, ca65 picks zero-page addressing, the instruction shrinks by one byte, and everything after it shifts.
3. **Branches need labels.** BZK prints relative operands as raw addresses; ca65 cannot assemble `BNE $8123` as a relative branch. Label the target and use the label.
4. **The bank table is a claim.** BZK maps a file range to a CPU window. The CDL data-mapping digit (`D 0`–`D 4`) tells you whether that claim matches where the data was actually read.
5. **Code copied to RAM is invisible.** If the game copies a routine to `$0300` and runs it there, the source bytes are only marked `D`, not `C`. Disassemble the RAM copy separately or annotate the source routine by hand.
6. **Header and CHR are not in the CDL.** The CDL covers PRG bytes only. BZK writes the 16-byte header and the CHR file separately.
7. **Byte-identical is the test.** A disassembly that assembles but produces a different ROM is not done.

## The loop

### 0. Inventory the ROM

```bash
python3 scripts/nes_header.py game.nes
```

Record mapper, PRG/CHR size, mirroring, battery and the SHA-1. You need the exact same ROM revision for the CDL, the disassembly and the rebuild.

### 1. Capture CDL

FCEUX: **Debug → Code/Data Logger → Start → Hard Reset**, then play. Save the `.cdl` when done. Do several sessions: menus, every level, death, game over, cutscenes, sound test, two-player, reset.

```bash
# merge and report
python3 scripts/cdl_report.py logs/*.cdl --merge --rom game.nes --out work/game.cdl
```

The CDL must be exactly `PRG size` bytes. If it is 16 bytes longer, the header was included; if it is shorter, it is CHR or a truncated log.

### 2. Generate a BZK config

```bash
python3 scripts/bzk_config.py game.nes --cdl game.cdl --out work/config.lua
```

This is a **starting point** for NROM/CNROM, UxROM, MMC1, MMC3 and AxROM. It maps static windows; it does not simulate runtime banking. Check the first output against the CDL `D` digit and adjust.

### 3. Run BZK

Put the ROM, CDL and any `.tbl` files in BZK's `input/` folder, edit `config.lua`, then run `LAUNCHME.bat` on Windows or `lua disassembler.lua` with Lua 5.3 elsewhere.

The output is ca65-flavored source with a prefix on every line:

```
C - - - - - 0x000010 00:8000: 78        SEI
```

That prefix is CDL flags, file offset, bank:CPU address and raw bytes. It is useful while annotating and must be stripped before assembly.

### 4. Label and clean

- Strip the prefix (BZK's `preparations.lua` or the equivalent regex).
- Label branch targets, `JMP`/`JSR` targets and jump tables.
- Replace data runs with `.byte`/`.word`/`.incbin`.
- Name RAM addresses (`ram_`) and hardware registers.
- Split or merge banks so `.segment` names match the linker config.

See [labels.md](references/labels.md).

### 5. Build

```bash
ca65 -U copy_bank_00.asm -o bank_00.o
ld65 -C ld65.cfg -o PRG_ROM.bin bank_*.o
cat header.bin PRG_ROM.bin CHR_ROM.chr > rebuilt.nes
```

Or use the `assemble.sh` pattern from NES-Games-Disassembly: prep → ca65 → ld65 → header+PRG+CHR → size/checksum check.

### 6. Verify

```bash
python3 scripts/rom_verify.py game.nes rebuilt.nes
```

If it is not byte-identical, stop and triage the first diff. Do not "fix" it by editing the rebuilt ROM.

## CDL flags

| Flag | Bit | Meaning | Use |
|---|---|---|---|
| `C` | 0 | executed as code | disassemble as instruction |
| `D` | 1 | read as data (also set on `JMP` targets) | data or code entry |
| `0`–`3` | 2–3 | last data window: `$8000/$A000/$C000/$E000` | validate bank mapping |
| `4` | 2–3 + 7 | data read from `$6000–$7FFF` | SRAM/banked low area |
| `J` | 4 | indirect `JMP ($xxxx)` target | jump-table entry |
| `I` | 5 | read through `($zp,X)` or `($zp),Y` | pointer table bytes |
| `A` | 6 | DPCM sample byte | keep as `.incbin`, never code |

A line like `C D 1 - - -` means the byte was executed and read, and the last data access came from the `$A000` window. If your config maps that bank at `$8000`, the `D 1` is telling you the mapping is wrong.

## Bank windows

| Mapper | Typical PRG windows | BZK config |
|---|---|---|
| NROM (0), CNROM (3) | 16K at `$8000`/`$C000` or 32K at `$8000` | one 16K/32K entry |
| UxROM (2) | 16K switch at `$8000`, fixed last 16K at `$C000` | switchable banks + fixed bank |
| MMC1 (1) | 16K switch at `$8000`, `$C000` switchable or fixed | same, verify mode |
| MMC3 (4) | 8K at `$8000`/`$A000`, fixed last two at `$C000`/`$E000` | non-fixed + fixed entries |
| AxROM (7) | 32K at `$8000` | one 32K entry |

For MMC3, the generator maps non-fixed banks to `$8000`. If code also runs from `$A000`, add duplicate entries for that window. The same file bank can appear at more than one CPU address; that is normal.

## Failure modes

| Symptom | Likely cause |
|---|---|
| Rebuilt ROM one byte short per missing `a:` | Missing `a:` on an absolute zero-page access |
| `Range error` on a branch | Branch target not labeled |
| Code shifted after an address | ca65 chose zero page, or a `.byte` run became an instruction |
| Wrong bank/data | Config window does not match the CDL `D` digit |
| Missing routine | CDL did not log it; code copied to RAM; wrong ROM revision |
| Garbage instructions in a table | `C` false positive; mark the range `.byte` |
| DPCM bytes disassembled as code | `A` flag ignored; move samples to `.incbin` |
| Build matches but game crashes | Disassembly is faithful; the bug is in the original or in your patch |

## Toolbox

| Tool | Use |
|---|---|
| [`scripts/nes_header.py`](scripts/nes_header.py) | Mapper, PRG/CHR sizes, mirroring, SHA-1 |
| [`scripts/cdl_report.py`](scripts/cdl_report.py) | Merge CDLs, report coverage, flags and untouched ranges |
| [`scripts/bzk_config.py`](scripts/bzk_config.py) | Generate a starting BZK `config.lua` from the iNES header |
| [`scripts/rom_verify.py`](scripts/rom_verify.py) | Hash/size/diff report between original and rebuilt |
| [BZK 6502](https://github.com/cyneprepou4uk/BZK-6502-Disassembler) | CDL → ca65 disassembler |
| [NES-Games-Disassembly](https://github.com/cyneprepou4uk/NES-Games-Disassembly) | 40+ worked examples of the full loop |
| [FCEUX](https://fceux.com/) | Code/Data Logger |
| [Mesen](https://www.mesen.ca/) | CDL + debugger alternative |
| [cc65](https://cc65.github.io/) | ca65/ld65 |

## References

- [CDL capture and flags](references/cdl.md)
- [BZK workflow and config](references/bzk-workflow.md)
- [Rebuild and verify](references/rebuild-verify.md)
- [Labels and code/data separation](references/labels.md)
- [Sources](references/sources.md)

## Companion skills

- [6502 assembly](../6502-assembly/SKILL.md) — ISA, addressing, `a:`/ca65 details
- [NES cart mappers](../nes-cart-mappers/SKILL.md) — bank layout and mapper behavior
- [NES memory map](../nes-memory-map/SKILL.md) — RAM/PPU/APU addresses
- [Tecmo Super Bowl ROM map](../tecmosuper-rom-map/SKILL.md) — a worked banked-ROM map
