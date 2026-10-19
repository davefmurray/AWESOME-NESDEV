# Address space

## CPU

```
$0000–$07FF  2 KB RAM
$0800–$1FFF  mirrors of $0000–$07FF (every $0800)
$2000–$2007  PPU registers
$2008–$3FFF  mirrors of $2000–$2007 (every 8)
$4000–$4017  APU + I/O
$4018–$401F  disabled (CPU test mode)
$4020–$5FFF  cartridge expansion
$6000–$7FFF  cartridge WRAM / PRG-RAM
$8000–$FFFF  PRG ROM + mapper registers
```

- `$0000–$00FF` zero page, `$0100–$01FF` stack.
- `$FFFA/B` NMI, `$FFFC/D` RESET, `$FFFE/F` IRQ/BRK.
- Unmapped reads are open bus.
- The cartridge sees all CPU bus activity except `$4015` reads.

## PPU

```
$0000–$0FFF  pattern table 0
$1000–$1FFF  pattern table 1
$2000–$23FF  nametable 0 (960 tile bytes + 64 attribute bytes)
$2400–$27FF  nametable 1
$2800–$2BFF  nametable 2
$2C00–$2FFF  nametable 3
$3000–$3EFF  mirrors of $2000–$2EFF (not rendered)
$3F00–$3F1F  palette RAM
$3F20–$3FFF  mirrors of $3F00–$3F1F
```

- Only 2 KB of internal nametable RAM. Mirroring maps the four logical nametables onto it; four-screen carts add RAM.
- Palette mirrors: `$3F10/$3F14/$3F18/$3F1C` read the same bytes as `$3F00/$3F04/$3F08/$3F0C`.
- OAM is separate: 64 entries × 4 bytes, accessed via `$2003`/`$2004` or `$4014`.

## Address formulas

```
nametable byte  = $2000 + nt*$400 + y*32 + x        (x 0–31, y 0–29)
attribute byte  = $2000 + nt*$400 + $3C0 + (y/4)*8 + (x/4)
attribute shift = ((y%4)/2)*4 + ((x%4)/2)*2
pattern tile    = table*$1000 + tile*16
```

`nt` is the logical nametable 0–3 after mirroring, not necessarily the physical one.

## OAM entry

| Byte | Meaning |
|---|---|
| 0 | Y (top minus 1); `$EF–$FF` hides |
| 1 | Tile index (8×8: pattern table from PPUCTRL; 8×16: bit 0 selects table) |
| 2 | `palette` bits 1–0, priority bit 5, flip H bit 6, flip V bit 7 |
| 3 | X (left edge) |
