# 6502 toolchains and assembler syntax

There is no single 6502 syntax. The instruction mnemonics are the same; directives, labels, macros and linking are not.

## Pick one

| Assembler | Model | Best for |
|---|---|---|
| **ca65** (cc65) | objects + linker config, segments, strong macros | NES homebrew, multi-bank projects, C interop |
| **asm6f** | single source, simple directives, NES headers | Small NES ROMs, learning, fast iteration |
| **dasm** | single source, macros, Atari heritage | Atari 2600/8-bit, small 6502 projects |
| **ACME** | single source, `!` directives | Cross-platform 6502/6510/65816 |
| **64tass** | single source, C64 focus | C64, 65816 |

If you are following a tutorial, use the assembler the tutorial uses. Converting syntax while learning is unnecessary pain.

## ca65 / ld65

```bash
ca65 -t nes -g src/main.s -o build/main.o
ld65 -C nes.cfg -Ln build/labels.txt --dbgfile build/game.dbg \
     build/main.o -o build/game.nes
```

`-t nes` selects the NES CPU/header conventions. `-g` emits debug info; `-Ln` writes a label file; `--dbgfile` writes a debug file for emulators.

### Segments

ca65 does not use `.org` for the final layout. You assemble into segments, then ld65 places them:

```asm
.segment "ZEROPAGE"
ptr:    .res 2
counter:.res 1

.segment "CODE"
reset:
    lda #0
    sta counter
    jmp *

.segment "VECTORS"
.word reset, reset, reset
```

A minimal NROM config:

```
MEMORY {
    ZP:  start = $0000, size = $0100, type = rw;
    RAM: start = $0200, size = $0600, type = rw;
    ROM: start = $8000, size = $8000, type = ro, file = %O, fill = yes, fillval = $FF;
}
SEGMENTS {
    ZEROPAGE: load = ZP,  type = zp;
    CODE:     load = ROM, type = ro;
    RODATA:   load = ROM, type = ro;
    VECTORS:  load = ROM, type = ro, start = $FFFA;
}
```

### ca65 syntax that matters

| Feature | Syntax |
|---|---|
| Byte / word / reserve | `.byte`, `.word`, `.res` |
| Include | `.include "file.inc"` |
| Macro | `.macro name arg` … `.endmacro` |
| Procedure | `.proc name` … `.endproc` |
| Export/import | `.export name`, `.import name` |
| Cheap local label | `@loop` |
| Unnamed label | `:` (referenced with `:+`, `:-`) |
| Global label | `name:` |
| Absolute/zero-page force | `a:$1234`, `z:$12` |
| Character | `'A'` |
| Low/high byte | `<label`, `>label` |

ca65 is case-sensitive by default? Mnemonics are case-insensitive; symbols are case-sensitive.

## asm6f

```bash
asm6f src/main.asm build/game.nes build/game.lst
```

asm6f is a fork of ASM6 with NES-specific additions: iNES header directives, Mesen/FCEUX symbol files, CDL output, and some undocumented opcodes.

```asm
; NROM-256, 32K PRG, 8K CHR
INESPRG 2
INESCHR 1
INESMAP 0
INESMIR 0

ORG $8000
reset:
    lda #0
    sta $10
    jmp *

ORG $FFFA
DW reset, reset, reset
```

| Feature | Syntax |
|---|---|
| Origin | `ORG $8000` |
| Byte / word | `DB`, `DW` |
| Reserve | `DSB n` / `DSW n` |
| Include | `INCLUDE "file.asm"` |
| Binary include | `INCBIN "file.bin"` |
| Macro | `MACRO name args` … `ENDM` |
| Local label | `@loop` |
| Anonymous branch | `+`, `-` |
| Low/high byte | `<label`, `>label` |
| iNES header | `INESPRG`, `INESCHR`, `INESMAP`, `INESMIR` |
| NES 2.0 | `NES2CHRRAM`, `NES2PRGRAM`, `NES2CHRBRAM` |

`asm6f -l` writes a listing, `-m` writes a Mesen `.mlb` label file, `-n` writes FCEUX `.nl`.

## dasm

```asm
    processor 6502
    ORG $8000
reset:
    lda #0
    jmp *
    ORG $FFFA
    .word reset
    .word reset
    .word reset
```

| Feature | Syntax |
|---|---|
| Origin | `ORG` |
| Byte / word | `DC.B`, `DC.W` (also `.byte`, `.word`) |
| Include | `INCLUDE "file.asm"` |
| Macro | `MACRO` … `ENDM` |
| Local label | `.loop` |
| Low/high byte | `<label`, `>label` |

## ACME

```asm
!cpu 6502
!to "game.nes", plain
* = $8000
reset:
    lda #0
    jmp *
* = $FFFA
!word reset, reset, reset
```

ACME uses `!` directives (`!byte`, `!word`, `!fill`, `!source`, `!macro`). It is a good cross-assembler for 6502/6510/65816, but the syntax is its own dialect.

## 64tass

C64-focused, 65816-capable. Directives start with `.` (` .byte`, `.word`, `.cpu`), origin with `*=`.

## Symbol and debug files

| Tool | Command | Output |
|---|---|---|
| ca65/ld65 | `ca65 -g`, `ld65 -Ln labels.txt --dbgfile game.dbg` | labels + debug |
| asm6f | `-l`, `-m`, `-n` | listing, Mesen `.mlb`, FCEUX `.nl` |
| dasm | `-l`, `-s` | listing, symbols |
| 8bitworkshop CLI | `--symbols` | symbols for its debugger |

Load the symbol file in Mesen/FCEUX/8bitworkshop before stepping. Without it you are reading hexadecimal addresses.

## 8bitworkshop CLI

From an 8bitworkshop checkout:

```bash
npm run cli -- build --platform nes src/main.s -o build/game.nes --symbols
npm run cli -- run --platform nes --frames 240 --png shot.png build/game.nes
npm run cli -- run --platform nes game.nes -e "break _main; step 10; mem $0200 16"
```

The CLI uses the same assemblers/emulators as the browser IDE. It is useful for CI and for agents that cannot click a UI.

## A small Makefile

```make
ASM  = ca65
LD   = ld65
SRC  = src/main.s
OBJ  = build/main.o
ROM  = build/game.nes

all: $(ROM)

$(OBJ): $(SRC)
	@mkdir -p build
	$(ASM) -t nes -g $(SRC) -o $(OBJ)

$(ROM): $(OBJ) nes.cfg
	$(LD) -C nes.cfg -Ln build/labels.txt --dbgfile build/game.dbg $(OBJ) -o $(ROM)

clean:
	rm -rf build
```

## Syntax conversion checklist

When moving code between assemblers:

1. Directives (`ORG`/`.org`, `DB`/`.byte`, `DW`/`.word`).
2. Comment character (`;` almost everywhere).
3. Local label syntax (`@`, `.`, `:`).
4. Macro syntax and argument references.
5. Include and binary-include syntax.
6. Header/segment setup (ca65 needs a linker config; asm6 uses `INES*`).
7. Address-size prefixes (`a:`, `z:`).

The instruction stream is the same; only the packaging changes.
