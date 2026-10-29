# Converting pxl output to NES graphics

These rules describe the ordinary NES background format. Mapper-specific
attribute modes or mid-frame CHR changes need their own explicit contract.
Do not silently assume those features to fit an oversized drawing.

## Inputs and color model

Use a native 256×240 canvas for one full nametable, with a separate visible
safe area if the target emulator crops overscan. A 256×224 screenshot is not
a different nametable format. Keep geometry in one structure that generates
both writer addresses and converter exclusions.

A useful layout input declares four background palettes, their shared
backdrop, any sprite palettes, static text and dynamic rectangles. Store NES
color codes as the hardware values and use an explicit RGB preview lookup.
RGB appearance varies by emulator; do not infer hardware codes from a
lossy screenshot or silently quantize unrecognized colors.

For each aligned 16×16 background attribute cell, find a palette that can
represent every pixel: shared backdrop plus its three visible colors. Reject
violations with the cell coordinates and offending colors. Four colors in
each separate 8×8 tile is insufficient if neighboring tiles need incompatible
palettes within the same attribute cell. Pixel value zero is the backdrop;
the same RGB color appearing at another palette index is not interchangeable
when the game writes fixed glyph patterns.

Validate sprite palettes separately. Sprite pixel value zero is transparent,
and sprite palette selection comes from OAM, not background attributes.

## Tile encoding and IDs

Each 8×8 tile uses 16 bytes: eight low-bit rows followed by eight high-bit
rows. For pixel value `p` at `(x,y)`:

```text
low[y]  |= (p & 1)        << (7 - x)
high[y] |= ((p >> 1) & 1) << (7 - x)
```

One 4 KiB pattern table holds 256 tiles. That is the addressable table budget,
not necessarily the mapper's bank size. Confirm how the game maps both
pattern tables, including 8×16 sprite mode if used.

Allocate runtime IDs first. Preserve each ID's meaning even when its glyph
is redrawn. A blank quadrant of a digit may later be overwritten; it is not
a free ID. Name the intentional blank tile rather than choosing whichever
all-zero pattern a deduplicator encounters first.

Deduplicate by encoded two-bit pattern, then assign remaining IDs in a
stable traversal order. Different RGB palettes can reuse the same pattern.
Ordinary background tiles cannot be flipped with an attribute bit; mirrored
art needs another encoded pattern unless it happens to be symmetric.
Report reserved, art and free counts, plus the cell that overflows the bank.

## Nametable and attributes

A full nametable has 960 tile indices followed by 64 attribute bytes.
For tile coordinates `(tx,ty)`, the tile offset is `ty*32+tx`. Its attribute
byte is `960+(ty//4)*8+(tx//4)`, with the two-bit palette shifted by
`2*((tx//2)%2)+4*((ty//2)%2)`. The last attribute row also covers the
nonexistent tile rows 30/31; initialize those unused bits deterministically.

Dynamic text regions need room for every state, not just the sample shown:
long names, two-digit totals, page changes, empty values and special markers.
Keep background art clear under sprite labels where required. Require the
palette the existing writer expects throughout its possible footprint.
If a field shrinks, clear its old extent so stale digits cannot remain.

## Validation at the asset boundary

Reject wrong dimensions, unexpected transparency, unknown colors, invalid
palette codes, bad field types, overlaps with live fields, duplicate/reserved
ID conflicts and overflow before constructing a ROM. Preserve source hashes,
layout version and renderer pin in the asset metadata.

Decode the generated CHR, nametable and attributes back into pixels and
compare with the intended indexed image. Separately render dynamic examples
through the real writer; the converter must not be its own sole oracle.
Include a deliberately invalid attribute cell, a reserved-ID collision and
a tile overflow in converter regression tests.

Hardware references:
[pattern tables](https://www.nesdev.org/wiki/PPU_pattern_tables),
[attribute tables](https://www.nesdev.org/wiki/PPU_attribute_tables),
[OAM](https://www.nesdev.org/wiki/OAM).
