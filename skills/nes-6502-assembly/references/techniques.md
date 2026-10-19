# 6502 techniques

## 16-bit increment

```asm
  inc ptr
  bne done
  inc ptr+1
done:
```

## 16-bit add

```asm
  clc
  lda a_lo
  adc b_lo
  sta sum_lo
  lda a_hi
  adc b_hi
  sta sum_hi
```

## Multiply by a constant

- ×2: `ASL A`
- ×3: `ASL A` then `CLC / ADC original`
- ×4, ×8: repeated `ASL`
- General 8×8: shift-and-add loop, 8 iterations

The wiki's [6502 assembly optimisations](https://www.nesdev.org/wiki/6502_assembly_optimisations) page has multiplication and division routines.

## Delay loops

```asm
delay:
  ldx #count
@loop:
  dex
  bne @loop
  rts
```

Cycle count = `count * 5 - 1` (approx), plus call overhead. For exact delays, unroll `NOP`s or use a cycle table.

## Jump table without the page bug

```asm
  ldx index
  lda lo_table,x
  sta ptr
  lda hi_table,x
  sta ptr+1
  jmp (ptr)
```

Keep `ptr` off `$xxFF`, or use the RTS trick.

## RTS trick

```asm
  ldx index
  lda hi_table,x
  pha
  lda lo_table,x
  pha
  rts
```

Tables hold `target - 1`. Costs 6 cycles for RTS plus the pushes, no indirect jump.

## Tail call

```asm
; before
  jsr routine
  rts

; after
  jmp routine
```

Saves 9 cycles and 1 byte per call site.

## Zero page

`LDA $10` is 2 bytes/3 cycles; `LDA $0010` is 3 bytes/4 cycles. Put pointers, counters and hot flags in `$00–$FF`.

## Constant-time code

Branches cost different cycles depending on path. For raster code, replace branches with lookup tables or `AND` masks when the timing must be exact.
