# Glossary

**6502** — The NES CPU. 8-bit, ~1.79 MHz NTSC, 16-bit address bus. Variant in the NES omits decimal mode.

**APU** — Audio Processing Unit, inside the CPU die. Two pulse channels, triangle, noise, DMC.

**Bank** — A chunk of ROM swapped into a CPU/PPU address window by the mapper. 16 KB PRG banks and 8 KB CHR banks are common; MMC3 uses 8 KB PRG and 1 KB CHR.

**BPS** — Binary Patch System. A delta patch format with a checksum; preferred over IPS for new patches.

**CDL** — Code/Data Log. Per-byte coverage recorded by an emulator: executed vs read as data. Used to separate code from data in a disassembler.

**CHR** — Character/graphics ROM. Tile data for the PPU: two 8×8 pattern tables of 256 tiles each.

**CHR-RAM** — Cartridge RAM used for tiles instead of CHR-ROM. Common in homebrew; you must upload tiles at runtime.

**CPU** — Here, the 6502. Not the PPU.

**DMA** — Direct Memory Access. On NES, `$4014` copies a 256-byte page to OAM in one go (~513 cycles).

**Disassembly** — Bytes → assembly mnemonics. Without symbols or coverage it is a guess.

**Emulator** — Software NES. Accuracy varies; test timing-sensitive code on more than one.

**Header** — The 16-byte prefix of an iNES/NES 2.0 file describing sizes, mapper, mirroring and TV system. Not part of the ROM the CPU sees.

**iNES** — The common `.nes` container format. Header + optional trainer + PRG + CHR.

**IPS** — International Patching System. Simple delta format, 16 MB limit, no checksum.

**IRQ** — Interrupt request. On NES, usually from the mapper (MMC3 scanline counter) or APU; `$FFFE` vector.

**Mapper** — Cartridge hardware that maps banks and sometimes adds IRQs, audio or RAM. Encoded in the header; a mismatch means a black screen or crash.

**MMC1** — Nintendo mapper 1. Switchable 16 KB PRG, 4/8 KB CHR, battery saves, shift-register writes.

**MMC3** — Nintendo mapper 4. 8 KB PRG / 1 KB CHR banking plus a scanline IRQ; the most common advanced mapper.

**Nametable** — 32×30 grid of tile indices plus attribute data; the PPU's background layout. Four logical nametables, mirrored depending on the cart.

**NES 2.0** — Extended header format. More mapper bits, explicit RAM sizes, submappers. Byte 7 bits 3–2 = `10`.

**NMI** — Non-maskable interrupt. Fires at vblank when enabled; the usual place for per-frame updates. Vector at `$FFFA`.

**NROM** — Mapper 0. No banking: 16/32 KB PRG, 8 KB CHR. The simplest cart.

**OAM** — Object Attribute Memory: 64 sprites × 4 bytes. Usually staged in CPU RAM at `$0200` and DMA'd.

**Palette** — 32 bytes at `$3F00`: 16 background, 16 sprite. Values are NES color indices, not RGB.

**Pattern table** — 256 tiles of 16 bytes each, at PPU `$0000` or `$1000`.

**PPU** — Picture Processing Unit. Tile-based; 256×240 visible, 262 scanlines NTSC, 5.37 MHz.

**PRG** — Program ROM: 6502 code and data, mapped into `$8000–$FFFF`.

**Reassembly** — Assembly → bytes, ideally byte-identical to the original outside your patch. The test of a good disassembly.

**ROM** — Read-only memory; here, the game image file.

**Scanline** — One horizontal line. 262 per frame NTSC (240 visible). Raster effects change PPU state mid-frame.

**Sprite 0 hit** — PPU status flag set when a non-transparent sprite 0 pixel overlaps a background pixel. Used for split-screen timing.

**SRAM / WRAM** — Cartridge RAM at `$6000–$7FFF`, often battery-backed for saves.

**Symbol file** — Address → name mapping (`.sym`, `.lbl`, `.noi`). Makes debugger output readable and lets agents assert on names.

**Tile** — 8×8 pixels, 2 bitplanes, 16 bytes. The unit of NES graphics.

**Tilemap** — A grid of tile indices; nametables are the background tilemap.

**Trainer** — Optional 512-byte blob at `$7000` in old iNES files. Rare; usually absent.

**VBlank** — Vertical blanking: the ~20 scanlines after the visible frame when the PPU is idle enough to accept VRAM writes. NMI fires at its start.

**VRAM** — PPU memory: pattern tables, nametables, palettes. Separate from CPU RAM; accessed through `$2006`/`$2007`.
---

Part of [AWESOME NESDEV](../README.md) · [Start here](start-here.md) · [MCP servers](mcp-servers.md) · [Skills](agent-skills.md) · [Homebrew](homebrew.md) · [ROM hacking](romhacking.md)
