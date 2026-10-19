# Homebrew

Two paths: let romdev do the toolchain work, or assemble with cc65 yourself. Start with the first. Do the second when you want to understand what the agent is doing.

## Pick a toolchain

| Path | Language | Setup | Good for |
|---|---|---|---|
| **romdev** (cc65 WASM) | C or 6502 asm | `npx romdevtools` | Fast iteration, screenshots, agent loop |
| **cc65** (host) | C or 6502 asm | `brew install cc65` / apt / Windows installer | Full control, CI, editor integration |
| **asm6 / NESASM** | 6502 asm | single binary | Small asm-only projects, tutorials |
| **dotnes** | C# (.NET IL) | .NET SDK | C# developers, transpiler experiments |
| **NESmaker** | GUI/logic blocks | Windows app | Non-programmers making action games |

NES is rated **Hard** to build in romdev's platform table, and that is fair: the CPU is simple, the PPU is not. Budget most of your debugging time for PPU state, not 6502 logic.

---

## Path A — romdev (recommended)

### 1. Start the server

```bash
npx romdevtools
```

### 2. Fork an example

Ask the agent, or call the HTTP API directly:

```bash
curl -s -X POST http://127.0.0.1:7331/tool/examples \
  -H 'content-type: application/json' \
  -H 'x-romdev-session: mygame' \
  -d '{"op":"fork","example":"nes/platformer","name":"mygame","path":"'"$PWD"'/mygame"}'
```

The fork contains:

```
main.c                 your game
nes_runtime.c/.h       input, PPU helpers, sprites
chr-ram-runtime.crt0.s startup code
chr-ram-runtime.cfg    linker config
MENTAL_MODEL.md        how this runtime thinks about the NES
TROUBLESHOOTING.md     the failure modes you will hit
README.md              build and structure notes
```

### 3. Build, run, screenshot

```text
build({output:'run', platform:'nes', path:'./mygame', frames:240})
```

One call: compile with cc65, link, load fceumm, run 240 frames, return a PNG. Once the platform binaries are cached the round trip is well under a second.

### 4. Iterate

```text
Read main.c. Change the background palette to dark green, rebuild,
run 240 frames, and show me the screenshot.
```

### 5. Know the commands

| Need | Call |
|---|---|
| Build only a ROM | `build({output:'project', outputPath:'./mygame.nes'})` |
| Build + run + shot | `build({output:'run', frames:240})` |
| Test input | `build({output:'run', holdInputs:[{right:true}]})` |
| Rebuild after editing | same call; it recompiles changed files |
| Open a playable window | `playtest({op:'open'})` |
| Check rendering without eyes | `frame({op:'verify'})` |
| Read a variable | `memory({op:'read', address:..., length:...})` with symbols |
| Inspect sprites | `sprites({op:'...'})`, `palette`, `background` |

### 6. When it breaks

Read `TROUBLESHOOTING.md` in the fork first. Then [Troubleshooting](troubleshooting.md). The usual suspects are a black screen (boot timing, palette, CHR-RAM not uploaded), a crash (NMI firing before RAM init), or a frozen game (NMI handler doing too much).

---

## Path B — plain cc65

You need `ca65` (assembler), `ld65` (linker), `make`, and an emulator (Mesen or FCEUX).

### Layout

```
mygame/
  main.s
  nes.cfg
  Makefile
```

### Minimal linker config

```ld
MEMORY {
    ZP:   file="",  start=$0000, size=$0100, type=rw;
    RAM:  file="",  start=$0200, size=$0600, type=rw;
    HDR:  file=%O,  start=$0000, size=$0010, fill=yes, fillval=$00;
    PRG:  file=%O,  start=$8000, size=$8000, fill=yes, fillval=$FF;
    CHR:  file=%O,  start=$0000, size=$2000, fill=yes, fillval=$00;
}

SEGMENTS {
    ZEROPAGE: load=ZP,  type=zp;
    BSS:      load=RAM, type=bss;
    HEADER:   load=HDR, type=ro;
    CODE:     load=PRG, type=ro, start=$8000;
    RODATA:   load=PRG, type=ro;
    VECTORS:  load=PRG, type=ro, start=$FFFA;
    CHARS:    load=CHR, type=ro;
}
```

This is the layout from Jay McGavren's verified hello-world (see [Resources](resources.md)); it produces a 16-byte header, 32 KB PRG and 8 KB CHR.

### Minimal source

```asm
.segment "HEADER"
    .byte "NES", $1A
    .byte 2                 ; 32 KB PRG
    .byte 1                 ; 8 KB CHR
    .byte $00               ; mapper 0, horizontal mirroring
    .byte $00,$00,$00,$00,$00,$00,$00,$00

.segment "CODE"
reset:
    sei
    cld
    ldx #$40
    stx $4017               ; disable APU frame IRQ
    ldx #$FF
    txs
    inx                     ; X = 0
    stx $2000               ; NMI off
    stx $2001               ; rendering off
    stx $4010               ; DMC IRQ off

wait1:
    bit $2002
    bpl wait1               ; first vblank

    lda #$00
    tax
clear_ram:
    sta $0000,x
    sta $0100,x
    sta $0200,x
    sta $0300,x
    sta $0400,x
    sta $0500,x
    sta $0600,x
    sta $0700,x
    inx
    bne clear_ram

wait2:
    bit $2002
    bpl wait2               ; second vblank: PPU ready

    ; palette entry 0 = $21 (light blue)
    lda $2002
    lda #$3F
    sta $2006
    lda #$00
    sta $2006
    lda #$21
    sta $2007

    ; scroll to 0,0
    lda #$00
    sta $2005
    sta $2005

    lda #%00001010          ; show background
    sta $2001
    lda #%10000000          ; NMI on
    sta $2000

forever:
    jmp forever

nmi:
    rti
irq:
    rti

.segment "VECTORS"
    .word nmi, reset, irq

.segment "CHARS"
    .res 8192, $00
```

> This is deliberately minimal: a solid background, no text, no sprites. It is here to show the shape of a ROM, not as a tested artifact of this repo. The full hello-world that prints text is in the [verified walkthrough](https://jay.mcgavren.com/2026/05/25/claude-code-for-nes-development.html).

### Makefile

```make
TARGET = mygame

all: $(TARGET).nes

$(TARGET).nes: main.s nes.cfg
	ca65 main.s -o $(TARGET).o
	ld65 -C nes.cfg $(TARGET).o -o $(TARGET).nes

clean:
	rm -f $(TARGET).o $(TARGET).nes

.PHONY: all clean
```

### Build and run

```bash
make
open -a Mesen mygame.nes      # macOS
mesen mygame.nes              # Linux/Windows
```

Check the header before you blame the emulator:

```bash
xxd -l 16 mygame.nes
# 00000000: 4e45 531a 0201 0000 0000 0000 0000 0000  NES.............
```

`02 01` = two 16 KB PRG banks, one 8 KB CHR bank. `00` at offset 6 = mapper 0, horizontal mirroring.

---

## What the CPU does at power-on

1. Reads the RESET vector at `$FFFC`, jumps there.
2. Your reset code disables NMI/rendering, sets the stack, clears RAM.
3. Waits for vblank (two waits after power-on is the safe convention).
4. Uploads palette, nametable and (if CHR-RAM) tiles through `$2006`/`$2007`.
5. Enables NMI and rendering.
6. Falls into the main loop; NMI fires ~60 times per second and does per-frame work.

If any of steps 2–5 is wrong, you get a black screen. There is no exception, no log, no stack trace. This is why the [PPU bring-up checklist](#ppu-bring-up-checklist) matters.

## PPU bring-up checklist

- [ ] Rendering and NMI are **off** while uploading PPU data.
- [ ] `$2002` read clears the write latch before using `$2006`/`$2005`.
- [ ] Two vblank waits after power-on (the PPU ignores early writes).
- [ ] Palette written to `$3F00`; entry 0 is not the same color as everything else.
- [ ] Nametable points at a tile that exists in CHR.
- [ ] If CHR-RAM: tiles uploaded before rendering is enabled.
- [ ] Scroll set with two writes to `$2005`.
- [ ] NMI enabled only after RAM and PPU state are ready.
- [ ] OAM DMA (`$4014`) done inside NMI, not in the middle of rendering.
- [ ] You ran at least 120 frames before concluding "black screen".

## Graphics

| Concept | What to know |
|---|---|
| Pattern tables | 2 × 256 tiles × 16 bytes; `$0000` and `$1000` in PPU space |
| Nametable | 32 × 30 tile indices + attribute table; `$2000`, `$2400`, `$2800`, `$2C00` |
| Palette | 32 bytes at `$3F00`: 16 background, 16 sprite; `$3F00` is the universal background |
| OAM | 64 sprites × 4 bytes (Y, tile, attributes, X); DMA from `$0200` via `$4014` |
| CHR-ROM vs CHR-RAM | ROM is cheaper to use; RAM allows dynamic tile updates and is common in homebrew |
| 8×16 sprites | `$2000` bit 5; tile index selects a pair |
| Sprite 0 hit | `$2002` bit 6; the classic split-screen trick |

Tools: [YY-CHR](https://www.romhackplaza.org/index.php/utilities/yy-chr-utility) for tile editing, [NES Screen Tool](https://github.com/BrokeStudio/NES-Screen-Tool) for nametables, Aseprite for source art (romdev can import Aseprite/LibreSprite).

## Sound

- **FamiTone2** is the usual homebrew driver and ships in romdev's NES examples.
- **FamiStudio** (<https://www.famistudio.org/>) is the modern tracker with NES instrument support and export options.
- **FamiTracker** / 0CC-FamiTracker are the classic trackers; their text export is widely supported.
- The APU has two pulse channels, triangle, noise and DMC. Volume envelopes are software; there is no hardware sample playback beyond DMC.

If you are using romdev, `encodeAudio` can convert note data to FamiTone2 format; the `music_demo` example shows the wiring.

## Mappers and size

NROM (mapper 0) is 32 KB PRG / 8 KB CHR and no banking. It is enough for a small game. Move to:

| Mapper | Name | Typical use |
|---|---|---|
| 0 | NROM | ≤32 KB PRG, no banking |
| 1 | MMC1 | flexible banking, battery saves, common in 80s carts |
| 2 | UxROM | 16 KB switchable PRG, CHR-RAM, cheap |
| 3 | CNROM | CHR banking only |
| 4 | MMC3 | 8 KB PRG + 1 KB CHR banking, scanline IRQ; the workhorse |
| 7 | AxROM | 32 KB switchable, single-screen mirroring |

Start with NROM, then MMC1 or MMC3. Every mapper adds init code, banking state and new failure modes.

## Debugging

- **romdev:** `breakpoint`, `watch`, `disasm`, `memory`, `cpu`. Use `build({output:'romWithDebug'})` and `symbols` to assert on named variables instead of magic addresses.
- **Mesen MCP:** hooks, symbols, call stack, tilemap/OAM renders. Pause before reading.
- **mcp-bizhawk:** memory domains, savestates, frame advance. ~1 frame latency.
- **Plain Mesen/FCEUX:** the built-in debuggers are excellent; the MCP layer is convenience, not a replacement.

Assert on memory, not pixels. A screenshot tells you *that* it is wrong; a memory read tells you *where*.

## Testing on hardware

- Flash carts: EverDrive-N8, PowerPak. Both run most NROM/MMC1/MMC3 homebrew.
- NTSC vs PAL: 60 Hz vs 50 Hz changes your frame budget and music pitch. Decide early.
- Real PPU behavior differs at power-on and with sprite overflow; if you target hardware, test on hardware.
- Famicom vs NES: cartridge pinout and expansion audio differ; a Famicom-only mapper (e.g. FME-7) needs an adapter or a Famicom.

## Learning resources

- [Nerdy Nights](https://nerdy-nights.nes.science/) — the classic step-by-step NES assembly course, now as a PDF/online book.
- [nesdoug](https://nesdoug.com/) — C-based NES tutorials that pair well with cc65.
- [NESdev wiki](https://www.nesdev.org/wiki/) — the reference. Start with [CPU memory map](https://www.nesdev.org/wiki/CPU_memory_map), [PPU registers](https://www.nesdev.org/wiki/PPU_registers), [iNES](https://www.nesdev.org/wiki/INES), [mappers](https://www.nesdev.org/wiki/Mapper).
- [NESdev forums](https://forums.nesdev.org/) — search before asking; most questions are answered.
- [Resources](resources.md) — tools, emulators, audio and art.
---

Part of [AWESOME NESDEV](../README.md) · [Start here](start-here.md) · [MCP servers](mcp-servers.md) · [Skills](agent-skills.md) · [Homebrew](homebrew.md) · [ROM hacking](romhacking.md)
