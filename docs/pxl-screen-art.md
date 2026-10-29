# Pixel art that fits an NES screen

| Component | What it does | Evidence |
|---|---|---|
| [claude-pxl](https://github.com/augusto-scarvalho/claude-pxl) | Editable pixel art, sprites, scenes and inspection commands | Ran pinned renderer on menus, title and scoreboard |
| [nes-pxl-screen-art](../skills/nes-pxl-screen-art/SKILL.md) | NES budgets, conversion, dynamic fields and guarded integration | Workflow extracted from executed ROM and emulator checks |
| Project converter | Turns PNGs into CHR, nametables, attributes and palettes | Required separately; pxl itself is not an NES compiler |

## claude-pxl + nes-pxl-screen-art

**Repo:** <https://github.com/augusto-scarvalho/claude-pxl> · **Version:**
0.1.0 at commit `3bc816cb15a14592e0dc062ee98013637d399457`
(verified October 29, 2026) · **License:** MIT upstream; CC0 for this repo's skill.

pxl lets you describe a drawing in JavaScript and inspect its rendered
pixels. The companion skill connects that loop to NES screen constraints:
fixed tile IDs, palette cells, live text and score writers, CHR ownership,
input handoffs and PPU timing. Use it for a new menu or a visual replacement
in an existing game. It does not choose free banks or generate a safe ROM
patch merely from an image.

### NES capabilities

- Source-controlled artwork with repeatable PNG generation.
- Separate converter checks for 16×16 attribute palettes and 8×8 patterns.
- Reserved numeric/font tiles, dynamic-field exclusions and tile budgets.
- Guarded additive builds with exact before-bytes and output alias checks.
- ROM-executed previews and emulator acceptance distinct from concept art.

The skill's [worked example](../skills/nes-pxl-screen-art/references/little-league.md)
links the actual converter, builder, tests and screen contracts. Its
scoreboard uses 254 of 256 tiles and preserves stock score formatting.

### Install

From this repository, copy the whole skill folder. Choose your harness:

```bash
# Codex
mkdir -p ~/.codex/skills
cp -R skills/nes-pxl-screen-art ~/.codex/skills/

# Claude Code
mkdir -p ~/.claude/skills
cp -R skills/nes-pxl-screen-art ~/.claude/skills/
```

Keep a pinned pxl checkout in your project, or install its separate upstream
skill following [Use it with an AI agent](https://github.com/augusto-scarvalho/claude-pxl#use-it-with-an-ai-agent).
Do not copy only upstream SKILL.md: its CLI, libraries and references are
part of the repository. The NES skill here contains instructions, not pxl.

```bash
git clone https://github.com/augusto-scarvalho/claude-pxl.git vendor/claude-pxl
git -C vendor/claude-pxl checkout --detach 3bc816cb15a14592e0dc062ee98013637d399457
node vendor/claude-pxl/bin/pxl.js --help
```

This revision runs with Node ≥22.18 without npm installation. Update the
pin deliberately and rerun asset regeneration after an upgrade.

### Try it

```text
Use nes-pxl-screen-art to restyle this NES scoreboard like our colorful
menu. Keep the actual scores, extra-inning pages, controls and music.
Inspect its dynamic writers and tile budget before choosing a layout.
Show the art at native resolution, then verify the built screen in-game.
```

A separate drawing-only request can use upstream pxl directly. An unrelated
6502 gameplay bug should not activate this screen-art skill.

### Gotchas

- `pxl check` is an art diagnostic, not a proof of NES palette compatibility.
- A four-color tile can still conflict with its neighbors' attribute palette.
- A mirrored background pattern generally needs a second tile; NES background
  attributes do not offer sprite-style flipping.
- Blank CHR bytes may be live font quadrants or indirectly selected assets.
- A faster draw can change held-button behavior and audio phase. Measure it.
- Renderer output paths are writes: preflight nested PNGs, previews and
  screenshots, including symlink/hardlink and missing-path collisions.
- A pleasing preview does not validate NMI timing, mapper transitions or audio.

### Verification

**Ran it:** macOS 14.1.2, Node 26.7.0, pinned pxl above, romdev 0.150.2.
The Little League screen builds regenerate deterministically. The final
scoreboard's CPU suite and six-/31-game emulator gates pass; played-board
checks compare nametables, attributes, palettes and scores. The skill's CLI
examples also ran on an original scratch scene. See the
[dated evidence](https://github.com/davefmurray/little-league/blob/93bf9d4/docs/scoreart32.md).

**Read the source/docs:** upstream agent workflow and CLI, project converters,
ROM builders and output guards. **Limits:** the workflow was measured on one
MMC1 game, not every NES engine. Physical hardware and a second emulator
remain unvalidated. The packaged skill is guidance, not an automatic patcher.

### Verdict

Use pxl plus this skill when you want editable art that survives NES
conversion and in-game integration. For a standalone illustration, use pxl
without the ROM workflow. For hand-painted CHR, a conventional tile editor
may be simpler.

[Skills library](../skills/README.md) · [Agent skills](agent-skills.md) · [Home](../README.md)
