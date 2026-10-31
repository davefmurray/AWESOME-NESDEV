# BZK 6502 workflow

[BZK 6502](https://github.com/cyneprepou4uk/BZK-6502-Disassembler) is a Lua disassembler that reads a FCEUX-style CDL and writes ca65 source. It is the engine behind [NES-Games-Disassembly](https://github.com/cyneprepou4uk/NES-Games-Disassembly).

Manual: <https://cyneprepou4uk.github.io/iromhacker/nes/en/bzk6502/1/index.html>

## What it does

- Reads the ROM, CDL, header and CHR.
- For each configured bank, walks the file range.
- If the CDL says `C`, decodes an instruction; otherwise prints a `.byte`.
- Emits a prefix with the CDL flags, file offset, bank:CPU address and raw bytes.
- Writes ca65-compatible `.segment`, `.include`, `.org` and instructions.
- Writes a RAM label include and an optional debug file.

It does **not** simulate runtime banking, find function boundaries, or label branches. Those are your job.

## Files

```
BZK 6502/
  LAUNCHME.bat
  disassembler.lua
  functions.lua
  opcodes.lua
  config.lua
  input/
    game.nes
    game.cdl
    game.tbl
  output/
```

`LAUNCHME.bat` runs `lua53.exe disassembler.lua`. The bundled Lua is Windows; on macOS/Linux install Lua 5.3 and run `lua disassembler.lua`.

## Config anatomy

```lua
INPUT_folder  = "C:/BZK 6502/input/"
OUTPUT_folder = "C:/BZK 6502/output/"

ROM_file = "game.nes"
CDL_file = "game.cdl"

HEADER_file = { "header.bin",   0x000000, 0x10 }
CHR_file    = { "CHR_ROM.chr",  0x008010, 0x8000 }
RAM_file    = "bank_ram.inc"

DEBUG_file = { "debug.txt", true }
FORCE_byte_comments = true

ASM_config_table =
    {--       1            2        3       4        5
        "bank_00.asm", 0x000010, 0x8000, 0x2000, "game.tbl",
        "bank_01.asm", 0x002010, 0xA000, 0x2000, "game.tbl",
        "bank_02.asm", 0x004010, 0xC000, 0x2000, "game.tbl",
        "bank_03.asm", 0x006010, 0xE000, 0x2000, false,
    }
```

| Field | Meaning |
|---|---|
| `INPUT_folder`, `OUTPUT_folder` | Absolute paths. Lua does not resolve relative paths reliably. |
| `ROM_file` | The `.nes` file in `input/`. |
| `CDL_file` | The `.cdl` in `input/`; must be PRG-sized. |
| `HEADER_file` | Output name, ROM file offset, size. `0x10` for iNES. |
| `CHR_file` | Output name, ROM file offset, size. Offset is `0x10 + PRG size`. |
| `RAM_file` | `.inc` with `ram_xxxx` labels, included in every bank. |
| `DEBUG_file` | Optional per-bank debug text. |
| `FORCE_byte_comments` | Add `;` comments to bytes with table matches. |
| `ASM_config_table` | 5 fields per bank: file name, file offset, CPU base, size, table file or `false`. |

Each entry maps **one file range to one CPU window**. If the same physical bank appears at two windows, add two entries (use a different ASM file name to keep labels separate).

## Bank table

| Mapper | Entry pattern |
|---|---|
| NROM/CNROM, 32K | `0x000010, 0x8000, 0x8000` |
| NROM/CNROM, 16K | `0x000010, 0xC000, 0x4000` (mirrored at `$8000`) |
| UxROM/MMC1, 16K | banks 0..n-2 at `0x8000`; last at `0xC000` |
| MMC3, 8K | banks 0..n-3 at `0x8000`; n-2 at `0xC000`; n-1 at `0xE000` |
| AxROM, 32K | `0x000010, 0x8000, 0x8000` |

For MMC3, `$8000` and `$A000` are both switchable. The generator maps non-fixed banks to `$8000`; duplicate relevant banks at `$A000` if the code runs there. The CDL's `D` digit tells you which window the data came from.

## `a:` and the zero-page trap

6502 has both zero-page and absolute forms of many instructions. ca65 automatically chooses zero page when the address is `< $100`. If the original used the 3-byte absolute form for a zero-page RAM address, ca65's 2-byte form shifts every following byte.

BZK marks that case:

```
C - - - - - 0x001234 01:8123: AD 10 00   LDA a: ram_0010
```

`a:` forces absolute addressing. **Never strip it.** The same idea exists in other assemblers as `a:`/`z:` prefixes, but BZK output is ca65 syntax.

## Output line

```
C - - - - - 0x000010 00:8000: 78        SEI
```

| Part | Meaning |
|---|---|
| `C - - - - -` | CDL flags: C/D/mapping/J/I/A |
| `0x000010` | ROM file offset (header included) |
| `00:8000` | bank number:CPU address |
| `78` | raw opcode/bytes |
| `SEI` | decoded instruction or `.byte` |

`C` lines are instructions; `-` lines are bytes. The prefix is for humans and for the Notepad++ scripts; it must be removed before ca65.

## Table files

`.tbl` files map byte values to text for strings and data. BZK uses them for comments and for data lines. A table is optional per bank; pass `false` if the bank is pure code.

Keep one table per game (or per text encoding). The BZK example `game.tbl` is a starting point.

## Labels and Notepad++

BZK writes labels for RAM (`ram_xxxx`) and vectors, but **branches are not labeled**. The published disassemblies use Notepad++ Lua scripts to:

- Label all branches (`bra_`).
- Label tables in a range (`tbl_`).
- Label `JMP`/`JSR` targets (`loc_`).
- Convert `.byte` back to instructions.
- Convert byte pairs to `.word`/`.dbyt`.
- Strip the BZK prefix into `copy_*.asm` files.

The scripts live in BZK's `_notepad/startup.lua`; `preparations.lua` in NES-Games-Disassembly is the batch version. On macOS/Linux, replicate the useful parts with Python/sed; you do not need Notepad++.

## Running on macOS/Linux

1. Install Lua 5.3 (`brew install lua` or your package manager).
2. Copy BZK's Lua files to a working directory.
3. Edit `config.lua` to POSIX paths.
4. Run `lua disassembler.lua`.

The Lua scripts are portable. The bundled `lua53.exe`, `LAUNCHME.bat` and Notepad++ integration are Windows conveniences.

## Limitations

- **Static banking.** BZK does not know which bank is mapped at runtime; you tell it.
- **No function detection.** It decodes linearly until the bank ends.
- **No branch labels.** Relative operands need labels.
- **No CHR disassembly.** CHR is dumped as a binary file.
- **Code copied to RAM** is only `D` in the CDL; BZK prints bytes.
- **False `C` flags** from jumps into data become instructions; fix them by hand.
- **Output is a first pass.** The published NES-Games-Disassembly sources contain thousands of manual labels and comments.

## Related

- [CDL capture](cdl.md)
- [Rebuild and verify](rebuild-verify.md)
- [Labels](labels.md)
- [BZK repo](https://github.com/cyneprepou4uk/BZK-6502-Disassembler)
- [NES-Games-Disassembly](https://github.com/cyneprepou4uk/NES-Games-Disassembly)
