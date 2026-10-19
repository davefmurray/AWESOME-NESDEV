# Mapper recipes

## MMC1 serial write

```asm
; A = value, bit 7 set resets the shift register
mmc1_write:
  sta $8000
  lsr a
  sta $8000
  lsr a
  sta $8000
  lsr a
  sta $8000
  lsr a
  sta $8000
  rts
```

Send five times, LSB first. A reset write is `$80`; after reset, the next five writes configure.

## MMC1 bank switch

```asm
; A = 16 KB PRG bank
mmc1_bank:
  sta $E000
  lsr a
  sta $E000
  lsr a
  sta $E000
  lsr a
  sta $E000
  lsr a
  sta $E000
  rts
```

Keep this routine and the vectors in the fixed bank.

## MMC3 register write

```asm
; A = register (0-7), Y = value
mmc3_write:
  sta $8000
  sty $8001
  rts
```

Set the PRG/CHR mode bits deliberately: `$8000` bits 6 (PRG mode) and 7 (CHR A12 inversion) are part of the register select.

## MMC3 scanline IRQ

```asm
; once per frame
  lda #0
  sta $C001       ; reload
  sta $E001       ; enable
  lda #<scanlines
  sta $C000       ; latch
```

IRQ handler: acknowledge with `$E000`, then do the split. The exact latch value depends on where in the frame you arm it; tune against a visual split.

## UNROM bus-conflict-safe switch

```asm
bankswitch_y:
  tya
  sta banktable,y
  rts

.segment "RODATA"
banktable: .byte $00,$01,$02,$03,$04,$05,$06
```

The table must live in the fixed bank. `STA abs,Y` writes the bank number to a ROM address whose byte equals that number, satisfying the bus.

## AxROM

```asm
; A = 32 KB bank; bit 4 = one-screen mirroring
  sta $8000
```
