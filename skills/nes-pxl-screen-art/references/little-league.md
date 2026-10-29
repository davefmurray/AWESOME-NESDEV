# Worked example: the Little League screen pipeline

This is a measured example, not a map for another cartridge. Source and
commands are frozen at [Little League commit 93bf9d4](https://github.com/davefmurray/little-league/tree/93bf9d4).
No game assets or ROM bytes are included in this skill.

## Tools and reproducibility

Verified October 29, 2026 on macOS 14.1.2, Node 26.7.0 and romdev 0.150.2.
The pxl checkout is
`3bc816cb15a14592e0dc062ee98013637d399457` of
[augusto-scarvalho/claude-pxl](https://github.com/augusto-scarvalho/claude-pxl),
package version 0.1.0, MIT. The package version alone does not identify the
renderer: pin the commit. This revision requires Node 22.18 or newer.

Read upstream `SKILL.md` for drawing commands and use `help` for individual
operations. A pinned checkout can run without an npm build/install step:

```bash
git clone https://github.com/augusto-scarvalho/claude-pxl.git vendor/claude-pxl
git -C vendor/claude-pxl checkout --detach 3bc816cb15a14592e0dc062ee98013637d399457
node vendor/claude-pxl/bin/pxl.js --help
node vendor/claude-pxl/bin/pxl.js check art/screen.px.js
node vendor/claude-pxl/bin/pxl.js shot art/screen.px.js screen --out build/look
node vendor/claude-pxl/bin/pxl.js describe art/screen.px.js screen --brief
node vendor/claude-pxl/bin/pxl.js build art/screen.px.js --out build/render --no-preview
```

`art/screen.px.js` and scene `screen` are example names, not shipped files.
The command forms were smoke-tested with an original 256×240 scene; `check`
reported no warnings. The complete scoreboard pipeline below has separate
ROM-execution and emulator evidence.

## Source → asset → ROM

The project's layout is:

```text
art/scoreart32/score32.px.js      editable drawing
art/scoreart32/layout.json       palettes, text and geometry inputs
art/scoreart32/PXL.json          renderer commit and command
art/scoreart32/out/              reproducible PNGs
data/scoreart32/scoreassets.json validated CHR/map/palette bytes and source hashes
tools/scoreart32_convert.py     render, validate, encode, compare
tools/build_scoreart32.py       guarded ROM stage
tools/test_scoreart32.py        execute actual game writers and exits
```

Paths are relative to the repository root. Existing bootstrap ROM artifacts
are required; these commands are not a from-scratch ROM recipe.
From its root, with its Python environment and pinned pxl checkout:

```bash
.venv/bin/python tools/scoreart32_convert.py --rom build/modeart32.nes --check --pxl build/vendor/claude-pxl
.venv/bin/python tools/build_scoreart32.py build/modeart32.nes -o build/scoreart32.nes
.venv/bin/python tools/test_scoreart32.py build/modeart32.nes --candidate build/scoreart32.nes --pxl build/vendor/claude-pxl
```

The scoreboard retains 78 runtime glyph IDs and uses 176 further art tiles,
leaving two free in its 4 KiB CHR table. Pattern IDs still mean the same
numbers and markers to the stock writer. People and architecture fit by
reusing tile-aligned parts. The line-score rows move one tile up; statistics
move three. Shared team-name sprites remain on the original CHR bank.

## What testing changed

A raw background copy drew faster than the original decoder. That altered
held-button and music behavior. The final adapter preserves two vblank waits
and a measured 41,436-cycle interval before the stock writer. Its delay is
specific to this code placement; it is not a general NES screen recipe.

The final CPU suite covers 409 boards, all byte-valued counters, extra-inning
pages, 13 exits, 15 timing/song variants and 40 injected NMI positions.
A controller-played WATCH game checks boards against score RAM, full
nametables, palettes and OAM. Additional extra-inning fixtures are planted
and labeled as such. The integrated six-game baseline and 31-game tournament
pass; SPEED tournament mode forces CPU ownership.

The probe review found screenshot destinations could alias protected input
files. Output protection now runs before emulator dispatch. Converter tests
also cover hardlinks, symlinks and initially missing PNG destinations that
collide with JSON/preview paths.

Read [the scoreboard contract and evidence](https://github.com/davefmurray/little-league/blob/93bf9d4/docs/scoreart32.md)
for exact bank ownership, logs and limitations. The CPU model approximates
the PPU; emulator success does not establish physical-hardware correctness.

## Other screens use different contracts

The [selector/bracket](https://github.com/davefmurray/little-league/blob/93bf9d4/docs/menuart32.md)
uses CHR19 and a measured frame-clocked music loop. The
[mode menu](https://github.com/davefmurray/little-league/blob/93bf9d4/docs/modeart32.md)
retains stock input and NMI audio while replacing the draw. The
[title](https://github.com/davefmurray/little-league/blob/93bf9d4/docs/title32.md)
retains its attract sequence. Reuse the source/converter/builder/test
structure, not their banks, scratch bytes, music guards or delay constants.
