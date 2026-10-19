# Brand kit

## Files

| File | Size | Use |
|---|---|---|
| `awesome-nesdev-banner.png` | 1200×360 | README banner, dark mode |
| `awesome-nesdev-banner-light.png` | 1200×360 | README banner, light mode |
| `social-icon.png` | 1024×1024 | Square icon / avatar |
| `social-preview.png` | 1280×640 | GitHub social preview |
| `divider.png` | 1200×80 | Section divider |
| `sprites.png` | 306×158 | Transparent 8-icon sprite sheet |
| `logo-ascii.txt` | — | Terminal wordmark |

## Palette

| Name | Hex |
|---|---|
| NES red | `#E43B44` |
| Signal white | `#F5F3EE` |
| Gold | `#FFCC4D` |
| CRT cyan | `#57D9E8` |
| Deep navy | `#0A0E18` |
| Grid | `#111827` |
| Muted | `#8B93A7` |

## Type

[Press Start 2P](https://fonts.google.com/specimen/Press+Start+2P) by CodeMan38, SIL Open Font License 1.1. Rendered to PNG; the font file is not committed.

## Usage

- Keep the banner at `width="800"` in the README so it fits GitHub's column.
- Use the `<picture>` element with `prefers-color-scheme` to switch banners.
- Don't recolor the wordmark; the red offset shadow is part of the mark.

## GitHub social preview

Repository → **Settings** → **Social preview** → **Edit** → upload `assets/social-preview.png` (1280×640). GitHub does not expose this through the REST API, so it is a one-time manual step.
