# Rendering tables

## Palette layout

| Address | Use |
|---|---|
| `$3F00` | Universal background color |
| `$3F01–$3F03` | Background palette 0 colors 1–3 |
| `$3F04–$3F07` | Background palette 1 |
| `$3F08–$3F0B` | Background palette 2 |
| `$3F0C–$3F0F` | Background palette 3 |
| `$3F10` | Mirrors `$3F00` |
| `$3F11–$3F13` | Sprite palette 0 colors 1–3 |
| `$3F14`, `$3F18`, `$3F1C` | Mirror `$3F04`, `$3F08`, `$3F0C` |
| `$3F15–$3F1F` | Sprite palettes 1–3 |

A sprite pixel with color index 0 is transparent and shows the background.

## Attribute byte

One byte covers a 32×32 px area (4×4 tiles). Each 16×16 quadrant gets 2 bits:

```
bits 1-0  top-left
bits 3-2  top-right
bits 5-4  bottom-left
bits 7-6  bottom-right
```

Address and shift:

```
addr  = nametable_base + $3C0 + (coarse_y / 4) * 8 + (coarse_x / 4)
shift = ((coarse_y % 4) / 2) * 4 + ((coarse_x % 4) / 2) * 2
```

## Tile data

- 8×8 tile = 16 bytes: plane 0 rows 0–7, then plane 1 rows 0–7.
- Pixel value = `(plane1_bit << 1) | plane0_bit`, selecting palette color 0–3.
- Pattern table 0 at PPU `$0000`, table 1 at `$1000`.

## Sprite attributes

```
7 flip V
6 flip H
5 priority (0 in front, 1 behind background)
4-2 unimplemented (read as 0)
1-0 palette 0-3
```

## Sprite 0 hit summary

| Condition | Hit? |
|---|---|
| BG and sprites both enabled | required |
| Opaque BG and opaque sprite-0 pixel overlap | yes |
| Either pixel is CHR index 0 | no |
| x = 0–7 with left clipping | no |
| x = 255 | no |
| Priority says sprite is behind | still yes |
| Already hit this frame | no |

## Vblank budget

NTSC: 20 scanlines × 341 dots ÷ 3 dots per CPU cycle ≈ 2,273 CPU cycles. OAM DMA alone is 513. Keep NMI work small.
