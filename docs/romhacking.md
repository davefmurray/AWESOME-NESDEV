# ROM hacking

The loop is always the same: **observe → locate → change → verify**. The tools change; the loop does not.

> Use dumps you own. Do not distribute ROMs or patched ROMs of commercial games. This page describes technique, not sources.

## Mental model

An iNES file is:

```
16-byte header | [512-byte trainer] | PRG ROM | CHR ROM
```

- **PRG** is 6502 code and data, mapped into `$8000–$FFFF` (or banked).
- **CHR** is tile graphics, mapped into the PPU's `$0000–$1FFF`.
- The **mapper** decides how banks switch and how mirroring works.
- The **vectors** at `$FFFA–$FFFF` point at NMI, RESET and IRQ handlers.

Everything you can hack is in PRG (logic, text, level data, palettes if RAM-based) or CHR (tiles). Some games decompress graphics to CHR-RAM at runtime, which changes the approach.

## Phase 0 — triage

```bash
xxd -l 16 game.nes
# 4e45 531a 1008 ...  -> "NES\x1a", 16 PRG banks, 8 CHR banks
```

| Field | Meaning |
|---|---|
| Bytes 0–3 | `NES` + `$1A` |
| Byte 4 | PRG size in 16 KB units |
| Byte 5 | CHR size in 8 KB units (0 = CHR-RAM) |
| Byte 6 bits 3–0 | mapper low nibble, mirroring, battery, trainer |
| Byte 7 bits 7–4 | mapper high nibble; bits 3–2 = NES 2.0 marker |

Confirm with a tool rather than by hand. `nes-format` from [nes-skills](agent-skills.md#yuki001nes-skills) has the full bitfield and mapper tables; romdev's `catalog`/`platform` docs identify the loaded ROM; `file game.nes` often says "iNES ROM".

Also record: CRC32, PRG/CHR hashes, whether CHR is RAM, and the mapper number. Put it in `REVERSE.md` if you are using [re-skill](agent-skills.md#re-skill).

## Phase 1 — dynamic analysis

This is where most hacks are found. Static reading of 6502 is slow; watching a value change is fast.

### Set up

- Load the ROM in a debugger MCP (Mesen on Windows, BizHawk elsewhere) or romdev.
- Pause immediately. Take a save state at a known point (title screen, first level).
- Enable CDL/coverage capture if the emulator supports it (FCEUX Lua and Mesen do).

### Find the variable

1. Note the visible value (lives = 3, health bar full, timer = 300).
2. Search RAM for that value (`memory({op:'search'})` in romdev, `bizhawk_read_range` + filter, or the emulator's cheat search).
3. Change it in-game (die once, take damage).
4. Search for the new value among the previous candidates.
5. Repeat until one or two addresses remain.

This is the classic "value search" and it works for lives, health, ammo, timer, score, position, and inventory counts.

### Find the code

Set a **write breakpoint** on the address. The breakpoint fires on the instruction that changes it. Now you have a PC.

- In romdev: `breakpoint({on:'write', address:...})`, then `cpu`/`disasm`.
- In Mesen: `add_write_hook`, then `drain_notifications`.
- In BizHawk: the Lua console or a watchpoint; MCP write hooks are not exposed, so use the emulator UI for this step.

Read backwards from the PC to understand the branch: is it `DEC $xx`, a `CMP`/`BEQ`, or a table lookup? The patch is usually one of:

- NOP the decrement.
- Change the branch to always/never take.
- Change the immediate value.
- Redirect a `JSR` to free space.

### Capture coverage

Run the game through the area you care about with CDL on. You now have a bitmap of which PRG bytes executed and which were read as data. This is the single most useful input to a disassembler, because it prevents code/data confusion in a 6502 ROM full of inline data.

## Phase 2 — static analysis

### retrodisasm (fastest path to reassemblable asm)

```bash
retrodisasm -s nes -a ca65 -o game.asm game.nes -cdl game.cdl -verify
```

- `-a` choices: `ca65` (default), `asm6`, `nesasm`, `retroasm`.
- `-cdl` uses the coverage file to split code and data.
- `-verify` reassembles the output and compares to the input; if it does not match, do not trust the listing.

Reassembly:

```bash
ca65 game.asm -o game.o && ld65 game.o -t nes -o rebuilt.nes
```

For asm6: `asm6f game.asm rebuilt.nes` (needs asm6f v1.6+). `retroasm` does not support `-verify`.

### romdev disassembly project

```text
disasm({target:'project', path:'./game.nes', outputPath:'./disasm'})
```

Produces a byte-exact rebuildable project: region `.asm` files plus a build. Edit a region, then:

```text
build({output:'reassemble', platform:'nes', path:'./disasm'})
```

Compare the rebuilt ROM to the original outside your patch. If bytes differ elsewhere, the project is not byte-exact and your diff is lying to you.

### Ghidra

Use GhidraMCP when you need decompiler structure, xrefs and renamed functions across a large ROM. Import the PRG at `$8000`, set the 6502 language, add vectors, and analyze from RESET. For banked carts, create one memory block per bank. Details: [MCP servers → GhidraMCP](mcp-servers.md#ghidramcp).

Expect rough C. 6502 decompilation is best treated as a map, not source.

## Phase 3 — data

| Target | Approach |
|---|---|
| Text | Find the font/tile map, build a `.tbl`, search for known strings, then follow pointer tables |
| Level data | Watch the RAM buffer the level decompresses into, then find the ROM source |
| Palettes | If written from RAM, breakpoint on `$3F00` writes; if immediate, search for the byte sequence |
| Sprites/CHR | Extract tiles from CHR-ROM directly; for CHR-RAM, dump VRAM at the right frame |
| Music | APU writes (`$4000–$4017`) are the trace point; trackers vary wildly |
| Compression | Identify the decompressor from its loop, then re-inject with a tool that understands it |

romdev has `romPatch` operations for pointer finding and compressed-asset re-injection; check `GET /tool/romPatch/schema` for the exact ops in your version. Do not hand-roll a compressor until you know the format.

## Phase 4 — patch

Three ways, in increasing order of robustness:

1. **Byte patch** — change a few bytes in place. Fine for a branch or immediate. Record the file offset and the original bytes.
2. **IPS/BPS** — ship a diff, not a ROM. IPS is limited to 16 MB and has no checksum; BPS adds a checksum and is preferred. [Flips](https://github.com/Alcaro/Flips) handles both; `xdelta` handles VCDIFF.
3. **Reassemble from source** — edit the disassembly project and rebuild. Best for anything larger than a few bytes, because you can read the diff.

For ROM expansion or moving code, you need free space: `$FF` padding, unused banks, or a mapper with room. Update the vectors and any bank-switch calls that assumed the old layout.

## Phase 5 — verify

- Re-run the exact path you changed, from a save state, and check the value.
- Check a path you did **not** change (regression).
- For a patch: apply it to a clean ROM, compare the result to your working copy.
- For a rebuild: byte-compare outside the patched region.
- If the game has a checksum, fix it or the patch will be rejected.

## Worked example — infinite lives (generic)

The addresses are placeholders; the method is the point.

```text
1. Boot, start a game, note lives = 3.
2. Search RAM for 3. Die. Note lives = 2.
3. Search the previous results for 2. One address remains: $07A2.
4. Set a write breakpoint on $07A2.
5. Die again. Breakpoint hits at $C123: DEC $07A2.
6. Disassemble around $C123. Confirm the routine is the death handler.
7. Patch: replace the three bytes of DEC $07A2 with NOP NOP NOP.
8. Rebuild, apply, test: die twice, lives stay at 2.
9. Regression: finish a level, confirm the life counter still updates on 1UP.
```

If the game stores lives as "lives - 1" or as a BCD value, the search values shift. If the value is copied to a display buffer each frame, you will find two addresses: the real variable and the mirror. Breakpoint on writes to distinguish them: the mirror is written by the display routine, the real one by the game logic.

## Tool matrix

| Job | Tool | Where |
|---|---|---|
| Header/mapper triage | `nes-format` skill, `xxd`, romdev `catalog` | [Skills](agent-skills.md) |
| RAM search / breakpoints | romdev, Mesen MCP, BizHawk | [MCP servers](mcp-servers.md) |
| Coverage / CDL | FCEUX Lua, Mesen | [Skills](agent-skills.md), [MCP servers](mcp-servers.md) |
| Disassembly (reassemblable) | retrodisasm, romdev `disasm` | this page |
| Decompiler | GhidraMCP | [MCP servers](mcp-servers.md) |
| Tile extraction | FCEUX Lua PPU dumps, YY-CHR, romdev `sprites` | [Resources](resources.md) |
| Patching | Flips, xdelta, romdev `romPatch` | this page |
| Process / task ledger | re-skill | [Skills](agent-skills.md#re-skill) |

## Pitfalls

- **Mistaking data for code.** Without CDL, a disassembler will happily decode jump tables as instructions. Capture coverage first.
- **Patching a mirror.** The visible value is often a copy. Breakpoint on writes to find the owner.
- **Forgetting the header.** File offsets and CPU addresses differ by 16 bytes plus the mapper's banking. `cpu = 0x8000 + (offset - 16)` only for a flat 32 KB NROM.
- **Checksums.** Some games verify PRG; a patch that ignores this boots to a reset loop.
- **Timing.** A patch that adds cycles to an NMI handler can break raster effects. If the game uses sprite-0 or MMC3 IRQ splits, count cycles.
- **Expansion.** Moving code without updating every absolute reference is the classic way to spend a weekend.
---

Part of [AWESOME NESDEV](../README.md) · [Start here](start-here.md) · [MCP servers](mcp-servers.md) · [Skills](agent-skills.md) · [Homebrew](homebrew.md) · [ROM hacking](romhacking.md)
