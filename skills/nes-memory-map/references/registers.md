# Register bitfields

## PPU

### `$2000` PPUCTRL

```
7  NMI enable
6  PPU master/slave (rarely used)
5  sprite size: 0 = 8x8, 1 = 8x16
4  background pattern table: 0 = $0000, 1 = $1000
3  sprite pattern table (8x8 only)
2  VRAM address increment: 0 = +1, 1 = +32
1-0 base nametable: 0=$2000, 1=$2400, 2=$2800, 3=$2C00
```

### `$2001` PPUMASK

```
7-5 emphasis (R/G/B)
4   show sprites
3   show background
2   show sprites in left 8 px
1   show background in left 8 px
0   greyscale
```

### `$2002` PPUSTATUS

```
7 vblank (cleared by reading; also clears the $2005/$2006 latch)
6 sprite 0 hit
5 sprite overflow
4-0 open bus
```

### `$2003` / `$2004`

- `OAMADDR`: OAM byte address.
- `OAMDATA`: read/write at OAMADDR; writes outside vblank are unreliable while rendering.

### `$2005` PPUSCROLL

Two writes: X, then Y. Shares the `w` toggle with `$2006`.

### `$2006` PPUADDR

Two writes: high 6 bits, then low 8. Sets the PPU address for `$2007`.

### `$2007` PPUDATA

- Writes increment by 1 or 32 (`$2000` bit 2).
- Reads are buffered: the first read returns the old buffer; palette reads are immediate.

## CPU I/O

### `$4014` OAMDMA

Write a page number `N`; copies `$NN00–$NNFF` to OAM. 513 cycles (+1 on odd cycles).

### `$4015` APUSTATUS

Write: `---D NT21` enable DMC, noise, triangle, pulse 2, pulse 1.
Read: `IF-D NT21` IRQ flags, DMC active, length-counter statuses. Reading clears the frame IRQ flag.

### `$4016` / `$4017`

Write `$4016`: `xxxx xEES` — controller port latch (bit 0), expansion latch bits 1–2.
Read: `xxxD DDDD` — D0–D4 input lines, inverted; high signal reads 0.

### `$4017` write (APU)

`MI------` — mode (0 = 4-step, 1 = 5-step), IRQ inhibit, immediate clock when M=1.
