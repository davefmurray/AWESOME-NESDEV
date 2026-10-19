# Cold-ROM playbook

For a ROM with no documentation, no symbols and no existing disassembly. The example is *Little World Series* (NES), identity unconfirmed; the method is generic.

The rule: **prove each step before building on it.** A wrong mapper guess poisons every address that follows.

## 0. Workspace

```
~/lws-hack/
  roms/      pristine dump, never edited
  work/      copies, CDL, disassembly, screenshots, states
  patches/   IPS/BPS + notes
  notes/     REVERSE.md, labels.csv, hashes
  tools/     nes_header.py, addr.py, cdl_stats.py
```

Hash the ROM before anything else:

```bash
shasum -a 256 roms/lws.nes | tee notes/rom.sha256
cp roms/lws.nes work/lws.working.nes
```

## 1. Identify

```bash
python3 tools/nes_header.py roms/lws.nes
```

Record in `notes/REVERSE.md`:

- format (iNES vs NES 2.0)
- mapper number and submapper
- PRG size, CHR size, CHR-ROM vs CHR-RAM
- mirroring, battery, trainer
- TV system
- CRC32 and SHA-256

Then boot it in two emulators. If it runs in one and not the other, suspect the header or a mapper edge case before suspecting the game.

**Identity is not a header field.** Confirm the title from the title screen and copyright text. "Little World Series" may be a bootleg, a localisation, or a different game entirely; the screenshot is the evidence.

## 2. Decide the hack

| Hack type | First move | Tooling |
|---|---|---|
| Roster / stats / schedule | Find the table. Compare bytes across known values | Hex editor, relative search, maybe no disassembly |
| Graphics | Dump CHR and palettes | FCEUX PPU viewer, YY-CHR, NES Screen Tool |
| Mechanics (AI, innings, score, difficulty) | RAM search → write breakpoint | Debugger MCP, FCEUX, romdev |

Do not start with a disassembler for a roster edit. Do not start with a hex editor for an AI change.

If the target is a level or block layout, capture a PPU nametable dump and use [NesBlockFinder](https://github.com/spiiin/NesBlockFinder) to turn it into ROM offsets before disassembling. See [ROM hacking](romhacking.md#finding-block-and-screen-data).

## 3. Find one visible value

Pick something you can change in one action: lives, score, inning, cursor position, pitcher stamina.

1. Search RAM for the value.
2. Change it in-game (give up a run, strike out, pause).
3. Search the previous results for the new value.
4. Repeat until one or two addresses remain.
5. Write-breakpoint the survivor. The PC that hits is the writer.
6. Log it:

```csv
address,name,comment
$07A2,lives,"bank 7 at the time, frame 412, write BP at $C123"
```

**Banked caveat:** on MMC1/MMC3/etc. only the last 8 KB is pinned at `$E000–$FFFF`. A `$8xxx` address without the live bank number is not reproducible. Put the bank in the comment until the project tracks it properly.

## 4. Capture CDL

CDL (Code/Data Log) records which PRG bytes executed and which were read as data. It is the difference between a disassembly and a guess.

Capture separate sessions:

- boot / title
- each menu
- gameplay (a full inning or level)
- pause
- game over / continue
- any mode you intend to patch

Then merge and summarize:

```bash
python3 tools/cdl_stats.py work/cdl/*.cdl --merge --rom roms/lws.nes
```

If a page shows 0% code, you did not exercise it. That is information, not failure.

**CDL caveat:** it only covers what ran. A routine that triggers on a rare error, a secret menu, or a second player will be invisible. Plan sessions around the code you need to read.

## 5. Disassemble with coverage

```bash
retrodisasm -s nes -a ca65 -o work/disasm/lws.asm roms/lws.nes \
  -cdl work/cdl/merged.cdl -verify
```

- `-verify` reassembles and compares. If it fails, fix the code/data split before editing anything.
- Keep the generated `.asm` in `work/`, not in `patches/`.
- Re-run after new CDL sessions; coverage improves the split.

Alternative: romdev's `disasm({target:'project'})` produces a byte-exact rebuildable project; edit a region and `build({output:'reassemble'})`.

## 6. Patch the smallest thing

- Prefer a branch flip or an immediate change over moving code.
- If you need free space, find `$FF` padding or an unused bank, and update every reference.
- Record the original bytes and the file offset.
- Build an IPS/BPS against the **pristine** hash; never distribute a patched ROM.

```bash
cp roms/lws.nes work/check.nes
flips --apply patches/lws-<what>-<date>.ips work/check.nes
shasum -a 256 work/check.nes
```

## 7. Verify

1. Replay the changed path from a save state.
2. Replay one unchanged path (regression).
3. Apply the patch to a clean ROM; compare with your working copy.
4. If the game checksums PRG, fix it or the patch will reset-loop.
5. If the change adds cycles to NMI, check raster effects.

## Mapper cheat sheet for address math

| Mapper | PRG windows | Safe assumption |
|---|---|---|
| 0 NROM | 32 KB at `$8000`, or 16 KB at `$C000` | flat; formula works |
| 1 MMC1 | 16 KB switchable + 16 KB fixed | only `$C000–$FFFF` fixed |
| 2 UxROM | 16 KB switchable at `$8000`, last fixed at `$C000` | `$C000` fixed |
| 3 CNROM | 32 KB fixed PRG | flat |
| 4 MMC3 | 8 KB banks, last two fixed | `$E000–$FFFF` fixed |

Use `tools/addr.py`; it refuses to guess for non-zero mappers unless you supply the bank.

## Checklist

- [ ] ROM hashed, pristine copy kept
- [ ] Header parsed: mapper, PRG, CHR, mirroring, battery
- [ ] Boots in two emulators
- [ ] Identity confirmed from the title screen
- [ ] Hack type chosen
- [ ] One value found and write-breakpointed
- [ ] Writer instruction identified, bank recorded
- [ ] CDL captured for every relevant mode
- [ ] CDL merged, coverage reviewed
- [ ] Disassembly verified byte-identical
- [ ] Patch built against pristine hash
- [ ] Changed path + regression path verified

---

Part of [AWESOME NESDEV](../README.md) · [Start here](start-here.md) · [MCP servers](mcp-servers.md) · [Skills](agent-skills.md) · [Homebrew](homebrew.md) · [ROM hacking](romhacking.md) · [Cold ROM](cold-rom-playbook.md)
