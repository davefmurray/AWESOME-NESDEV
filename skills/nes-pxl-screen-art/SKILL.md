---
name: nes-pxl-screen-art
description: Create or restyle NES title screens, menus, scoreboards and other tile-based screens with pxl, then convert and integrate the art without breaking dynamic fields or game behavior. Use for pxl-to-CHR workflows and NES screen-art replacements, not general image generation or unrelated gameplay edits.
---

# NES screen art with pxl

Turn editable pixel-art source into a screen the NES actually renders. Use
pxl for drawing and inspection; use a separate, target-aware converter for
CHR, nametables, attributes and palettes. A successful pxl render does not
establish that the screen fits the cartridge or PPU.

## Establish the screen contract

Inspect the project's existing art pipeline and capture the current screen
before choosing storage or drawing over it. For an existing game, identify:

- Scene entry, redraws and exits; input, sound and NMI behavior on each path.
- Background/sprite CHR mapping, palette ownership and nametable layout.
- Fields the game writes later: numbers, labels, cursors, markers and sprites.
- Tile IDs with runtime meaning, plus every other reader of shared assets.
- Available ROM/RAM ranges, mapper assumptions and the evidence for reuse.

Record bank and CPU address together. Blank bytes or an unused-looking tile
are candidates for space, not proof of ownership. Check title, attract,
submenus, return paths and gameplay when a CHR bank is shared or uncertain.
For homebrew, define these contracts in the engine instead of reverse
engineering them.

## Draw within the budget

Read the installed pxl `SKILL.md` and only the relevant guide sections.
[Upstream agent setup](https://github.com/augusto-scarvalho/claude-pxl#use-it-with-an-ai-agent)
explains its drawing loop. Pin the renderer commit and runtime version used
by the project; the tested setup is in [the worked example](references/little-league.md).

Begin with a native-resolution layout: important text and live fields first,
then architecture, people and decoration. Match the user's selected style,
not a default palette. Offer distinct compositions when direction is open;
once the user selects one, continue within that choice.

Keep repeated props and people as named pxl parts. Use 8-pixel alignment and
repeated textures where they save tiles without making the scene lifeless.
Reserve runtime glyphs before spending the remaining tile budget. Inspect
both 1x readability and a nearest-neighbor enlargement. Long names, wide
scores and the smallest captions deserve actual rendered examples.

Use `shot` to inspect an asset, `describe` to inspect scene structure, and
`check` for pxl diagnostics. Address relevant warnings, then build to scratch
storage. Changes belong in the editable source; generated PNGs are outputs.

## Convert and integrate

Read [NES conversion](references/nes-conversion.md) when implementing or
changing the converter. It covers attribute cells, tile deduplication,
reserved IDs and round-trip validation.

Prefer retaining the game's dynamic writers and changing their background,
glyph art and declared geometry. Move related row tables, sprites and cursor
positions together. Replace a writer only when the requested design needs
it, with tests for its formatting and state transitions.

For ROM replacements, read [integration and verification](references/integration.md)
before patching. Build a new stage from a pinned input with exact byte guards
and a changed-region manifest. Keep renderer, converter and ROM builder
separate so art can be iterated without rewriting gameplay code.

## Show and verify the result

Render from the built ROM's CHR, tilemap, attributes and palette, including
representative dynamic values. Mark converter previews as previews. In the
emulator, exercise real entry, navigation, redraw and exit paths; compare
PPU state, score/name state and audio timing where relevant. A CPU model can
prove a routine's behavior without proving visible transition frames.

Report the artifact/hash, editable source, tile usage, tests and meaningful
limits. Distinguish played scenarios from planted fixtures and emulator
coverage from hardware coverage. Publish only within the user's requested
scope; this skill does not grant permission to distribute assets or ROMs.
