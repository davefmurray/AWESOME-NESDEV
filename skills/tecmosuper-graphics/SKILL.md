---
name: tecmosuper-graphics
description: "Tecmo Super Bowl NES graphics: uniforms, large and mini helmets, player portraits, team logos, palettes, field/endzone art, menus and 4x4 metatile screens. Use when changing team colors, helmets, faces, logos, title/intro art, or when a TSB graphics edit corrupts another team or screen."
---

# Tecmo Super Bowl graphics

TSB graphics are ordinary NES graphics with two extra layers: **shared tiles** and **pointer tables**. A helmet edit is usually three separate things — the tile data, the palette, and the pointer that says which tiles/palette a team uses.

## Where graphics live

| Layer | Location | Notes |
|---|---|---|
| CHR (tiles) | `0x40010–0x6000F` | 128 KB, 16 × 8 KB CHR banks; 16 bytes per tile |
| Palettes | bank `0D` (`0x1A010+`) | NES `$3F00`-style color indices |
| 4×4 metatiles | `0x5010–0x6000` | background block definitions |
| Screen scripts | banks `06`, `07`, `0F` | draw-script events; see [events](../tecmosuper-events/SKILL.md) |
| Large helmet pointers | around `0x10072–0x100A4` | per-team pointer table |
| Mini helmet data/pointers | see cards | last byte mixes palette set + overlay |
| Team name pointers | `0x1FC10+` | example of TSB's pointer style |

TSB pointer convention (from the team-name thread): read the two bytes, swap them, add `0x14010` to get the file offset. The same little-endian-plus-base pattern appears in several tables; verify the base per table.

## Workflow

1. **Screenshot the screen** in Mesen. Use the PPU viewer to see the tile numbers, palette and nametable.
2. **Classify the edit:**
   - tile shape → CHR
   - color → palette
   - arrangement → metatile / screen script
   - which team/player → pointer table
3. **Find the doc card** for that asset in [the graphics library](../../docs/tsb/README.md#graphics). The card gives the table and offsets.
4. **Edit a copy.** Change one team/asset first.
5. **Check the sharing.** Many tiles and palettes are shared between teams, screens or home/away uniforms. A change that looks right for Buffalo can recolor Miami.
6. **Test every consumer:** all 28/32 teams, home/away, the relevant menu/intro screen.

## Helmets and portraits

- **Large helmets** have a per-team pointer table and a separate palette/overlay selection.
- **Mini helmets**: the last byte of the entry controls the palette set and the small logo overlay (e.g. Chicago's C, Falcons' logo). Values are documented in the mini-helmet cards.
- **Portraits/faces** are tile data plus a face script; the face script points at the tile layout. Edit the face card's pointers, not just the tiles.
- 32-team ROMs relocate some mini-helmet data (NFC West card).

## Palettes

- NES palette values are 6-bit indices (`$00–$3F`), not RGB.
- `$3F00` is the universal background; sprite palette 0 color 0 is transparent.
- TSB stores background and sprite palettes separately; the "Color Location Megathread" is the index.
- Changing a palette can affect cutscenes, menus and scoreboards that reuse it.

## Screens and metatiles

- Backgrounds are drawn from 4×4 metatiles; a metatile is four tile IDs plus attributes.
- The start-screen card shows a minimal draw using the metatile format.
- Menu/scoreboard/intro screens are draw scripts in banks `06`, `07`, `0F`; the event engine executes them.
- A screen edit can be: metatile data, screen script, or both.

## Tools

| Tool | Use |
|---|---|
| Mesen | PPU/VRAM viewer, palette viewer, screenshots, tile numbers |
| YY-CHR | CHR tile editing |
| TSBIDesign.exe | community design utility (in the disassembly `TOOLS/`) |
| HxD / 010 Editor | pointer/table edits |
| [Disassembly](https://github.com/bruddog/Tecmo_Super_Bowl_NES_Disassembly) | named graphics banks and pointers |

## Doc map

Start with the [graphics category index](../../docs/tsb/README.md#graphics).

| Topic | Card |
|---|---|
| Primary/secondary uniforms | [Uniforms: Primary and Secondary](../../docs/tsb/graphics/7703-uniforms-primary-and-secondary.md) |
| Alternate on-field colors | [Uniforms: Alternate On-Field Colors](../../docs/tsb/graphics/10697-uniforms-alternate-on-field-colors.md) |
| Large helmets | [Large Helmet: Guide](../../docs/tsb/graphics/2756-large-helmet-guide.md) |
| Mini helmets | [Mini-Helmet: Guide](../../docs/tsb/graphics/4048-mini-helmet-guide.md) · [Tiles/Colors](../../docs/tsb/graphics/2638-mini-helmet-tiles-colors-1.md) |
| Portraits/faces | [Player Portrait: Introduction](../../docs/tsb/graphics/9968-player-portrait-introduction.md) |
| Logos | [Mid-Field Logo](../../docs/tsb/graphics/10301-mid-field-logo-document-images.md) · [Pro Bowl Logos](../../docs/tsb/graphics/67376-pro-bowl-logos.md) |
| Palettes | [Color Location Megathread](../../docs/tsb/graphics/11748-color-location-megathread.md) · [Super Bowl Palettes](../../docs/tsb/graphics/13429-super-bowl-palettes-information.md) |
| Field/endzone | [Map of Field](../../docs/tsb/graphics/13441-map-of-field-of-play-hex-locations.md) · [End Zone Tutorial](../../docs/tsb/graphics/13438-end-zone-tutorial.md) |
| Screens/menus | [Various Screens](../../docs/tsb/graphics/3675-various-screens-colors-design-details.md) · [4×4 blocks](../../docs/tsb/graphics/67291-example-of-drawing-a-screen-using-4x4-blocks-start-screen.md) |
| Sprite flicker | [Turn off sprite flickering](../../docs/tsb/graphics/68629-turn-off-sprite-flickering-needed-for-the-hardware-sprite-limit.md) |

## Checks

- Did you change the tile, the palette **and** the pointer if the asset moved?
- Is the tile shared with another team or screen?
- Does the change survive home/away and the menu version of the uniform?
- Is the CHR bank correct (1 KB bank boundaries)?
- For a 32-team ROM, did the asset move?
- Does the screen still draw after a cutscene (draw-task/bank restore)?

## Failure modes

| Symptom | Cause |
|---|---|
| Wrong colors on one team | Wrong palette pointer, or shared palette |
| Helmet shape right, logo wrong | Mini-helmet overlay byte |
| Another team changed too | Shared CHR tiles or palette |
| Screen garbled | Metatile/script edit without updating the draw script |
| Crash after menu | Bank not restored (use the bank-swap event path) |

## References

- [Graphics category index](../../docs/tsb/README.md#graphics) — all 45 cards
- [ROM map](../tecmosuper-rom-map/SKILL.md) · [Events](../tecmosuper-events/SKILL.md)
