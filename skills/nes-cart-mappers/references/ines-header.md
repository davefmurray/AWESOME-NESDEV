# iNES / NES 2.0 header

## File layout

```
16-byte header | [512-byte trainer] | PRG ROM | CHR ROM | [PlayChoice data]
```

## Byte map

| Byte | iNES | NES 2.0 |
|---|---|---|
| 0–3 | `NES\x1A` | same |
| 4 | PRG / 16 KB | PRG low 8 bits (exponent form if `$0F`) |
| 5 | CHR / 8 KB (0 = RAM) | CHR low 8 bits |
| 6 | mirroring, battery, trainer, four-screen, mapper low | same |
| 7 | console type, mapper high | bits 3–2 = `10`, mapper high |
| 8 | PRG-RAM / 8 KB | mapper bits 8–11 (low nibble), submapper (high nibble) |
| 9 | TV system bit 0 | PRG MSB (low nibble), CHR MSB (high nibble) |
| 10 | unofficial | PRG-RAM (low), PRG-NVRAM (high), `64 << n` |
| 11 | unused | CHR-RAM (low), CHR-NVRAM (high), `64 << n` |
| 12 | unused | TV/timing (0 NTSC, 1 PAL, 2 dual, 3 Dendy) |
| 13–15 | padding | miscellaneous |

Mapper = `(byte7 & 0xF0) | (byte6 >> 4)`, plus `(byte8 & 0x0F) << 8` for NES 2.0.

## Flags 6

```
7-4 mapper low nibble
3   four-screen (mapper-dependent; not always 4-screen)
2   trainer present (512 bytes at $7000)
1   battery-backed PRG-RAM
0   mirroring: 0 horizontal, 1 vertical (ignored by MMC1/MMC3/AxROM)
```

## Flags 7

```
7-4 mapper high nibble
3-2 10 = NES 2.0
1   PlayChoice-10
0   Vs. System
```

## Header examples

NROM, 32 KB PRG, 8 KB CHR, horizontal:

```asm
.byte "NES",$1A
.byte 2,1
.byte $00,$00
.byte $00,$00,$00,$00,$00,$00,$00,$00
```

UNROM (mapper 2), 128 KB PRG, CHR-RAM, vertical, NES 2.0:

```asm
.byte "NES",$1A
.byte 8,0
.byte $20,$08
.byte $00
.byte $00
.byte $00
.byte $07        ; 8192 bytes CHR-RAM (64 << 7)
.byte $00
.byte $00,$00,$00
```

MMC1 (mapper 1), 128 KB PRG, 8 KB CHR, vertical, battery:

```asm
.byte "NES",$1A
.byte 8,1
.byte $12        ; mapper 1 low, battery, vertical
.byte $00
.byte $00,$00,$00,$00,$00,$00,$00,$00
```

## Validation

- PRG bytes = byte4 × 16384 (unless exponent form).
- CHR bytes = byte5 × 8192; 0 means CHR-RAM.
- File size should equal 16 + trainer + PRG + CHR; trailing bytes are common but suspicious.
- Mapper 0 with byte5 = 0 is a valid CHR-RAM NROM.
