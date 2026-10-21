# 6502 programming patterns

Copy these shapes, then adapt the addresses. All snippets are NMOS 6502 unless noted.

## 8-bit arithmetic

```asm
; sum = a + b
CLC
LDA a
ADC b
STA sum

; diff = a - b
SEC
LDA a
SBC b
STA diff
```

`ADC` adds the carry flag. If you forget `CLC`, the result is off by one. `SBC` subtracts the **inverse** of carry: `SEC` means no borrow.

## 16-bit arithmetic

```asm
; sum = a + b
CLC
LDA a_lo
ADC b_lo
STA sum_lo
LDA a_hi
ADC b_hi
STA sum_hi

; diff = a - b
SEC
LDA a_lo
SBC b_lo
STA diff_lo
LDA a_hi
SBC b_hi
STA diff_hi
```

Do not put `CLC`/`SEC` between the low and high bytes; the carry from the low byte is the input to the high byte.

## 16-bit compare, unsigned

```asm
LDA a_hi
CMP b_hi
BNE .done
LDA a_lo
CMP b_lo
.done:
; C=1 => a >= b
; Z=1 => a == b (only meaningful when the high bytes matched)
```

## 16-bit compare, signed

```asm
LDA a_hi
CMP b_hi
BNE .diff
LDA a_lo
CMP b_lo
.diff:
BVC .no_overflow
BMI .greater_or_equal   ; V=1, N=1 => a >= b
JMP .less
.no_overflow:
BMI .less               ; V=0, N=1 => a < b
.greater_or_equal:
; a >= b
```

The `N xor V` rule: after `CMP`, `a < b` when `N` and `V` differ.

## Multiply 8×8 → 16

Shift-and-add. `multiplicand` and `multiplier` are bytes; `mc` is a 16-bit shifted copy; `product` is 16-bit.

```asm
LDA multiplicand
STA mc_lo
LDA #0
STA mc_hi
STA product_lo
STA product_hi

LDX #8
.loop:
LSR multiplier
BCC .skip
CLC
LDA product_lo
ADC mc_lo
STA product_lo
LDA product_hi
ADC mc_hi
STA product_hi
.skip:
ASL mc_lo
ROL mc_hi
DEX
BNE .loop
```

This is 8 iterations, roughly 150–250 cycles depending on the bits. For speed, use a 256-byte square table or a 256×256 page-table scheme.

## Divide / modulo by powers of two

```asm
; unsigned A / 2
LSR A

; signed A / 2 (arithmetic shift right)
CMP #$80
ROR A

; A mod 16
AND #$0F

; 16-bit / 2
LSR hi
ROR lo

; signed 16-bit / 2
LDA hi
CMP #$80
ROR hi
ROR lo
```

`LSR` is logical (fills 0); the `CMP #$80` + `ROR` sequence shifts the sign bit back in.

## Arrays and pointers

```asm
; byte array, fixed base
LDX index
LDA array,X

; word array (lo/hi parallel tables)
LDX index
LDA array_lo,X
STA ptr
LDA array_hi,X
STA ptr+1

; walk a pointer
LDY #0
.loop:
LDA (ptr),Y
BEQ .done
INY
BNE .loop
.done:
```

`(ptr),Y` is limited to 256 bytes per pointer. For larger buffers, advance `ptr` by 256 and reset `Y`, or use a 16-bit index added into the pointer.

## Copy and fill 256 bytes

```asm
; copy 256 bytes from (src),Y to (dst),Y
LDY #0
.copy:
LDA (src),Y
STA (dst),Y
INY
BNE .copy

; fill 256 bytes at (dst),Y with A
LDY #0
.fill:
STA (dst),Y
INY
BNE .fill
```

`INY` wraps after 256 iterations, so the `BNE` exits exactly once.

## String length and compare

```asm
; length of NUL-terminated string at (ptr),Y -> Y
LDY #0
.len:
LDA (ptr),Y
BEQ .len_done
INY
BNE .len
.len_done:

; compare two NUL-terminated strings
LDY #0
.cmp:
LDA (a),Y
CMP (b),Y
BNE .different
CMP #0
BEQ .equal
INY
BNE .cmp
.equal:
; equal
.different:
; A = char from a, flags from the comparison
```

## Jump table

```asm
; 16-bit table split into parallel byte tables
LDX index
LDA table_lo,X
STA ptr
LDA table_hi,X
STA ptr+1
JMP (ptr)

table_lo: .byte <routine0, <routine1, <routine2
table_hi: .byte >routine0, >routine1, >routine2
```

For a dense 0–N dispatch this is faster and smaller than a `CMP`/`BEQ` chain.

## RTS dispatch (the "RTS trick")

```asm
; jump to routine, no JMP (ptr) needed
LDA #>routine
PHA
LDA #<routine-1
PHA
RTS
```

`RTS` pulls the address and increments it, so push `target-1`. This is useful when the target is computed or when you want a compact trampoline.

## Save and restore registers

```asm
PHA
TXA
PHA
TYA
PHA

; ... body ...

PLA
TAY
PLA
TAX
PLA
RTS
```

Push order A, X, Y; pop order Y, X, A. The stack is LIFO.

## Stack frame / local variables

The 6502 has no frame pointer. Two common conventions:

1. **Zero-page frame**: reserve `$10–$1F` for arguments/locals; caller and callee agree on the layout. Fast, not reentrant.
2. **Stack frame**: push locals, address them with `TSX` and `LDA $0101,X` (the return address is at `$0101,X` after `JSR`). Slower, reentrant.

```asm
; stack-frame style: one local byte; A is scratch
LDA #0
PHA          ; allocate the local
TSX          ; X = current SP
; local       at $0101,X
; return low  at $0102,X
; return high at $0103,X

; ... body ...

PLA          ; deallocate the local
RTS
```

If you must preserve the caller's `A`, push it **before** allocating the local and pop it after:

```asm
PHA          ; save caller A
LDA #0
PHA          ; local
TSX
; local       at $0101,X
; saved A     at $0102,X
; return low  at $0103,X
; return high at $0104,X
; ...
PLA          ; drop local
PLA          ; restore caller A
RTS
```

Stack-frame code is easy to get wrong; prefer zero-page frames until you need recursion.

## Macros

ca65:

```asm
.macro inc16 addr
    inc addr
    bne :+
    inc addr+1
:
.endmacro

inc16 counter
```

asm6:

```asm
.macro inc16 addr
    inc addr
    bne :+
    inc addr+1
:
.endmacro
```

asm6 uses named macros with `MACRO`/`ENDM` and anonymous `+`/`-` labels:

```asm
MACRO inc16 addr
    INC addr
    BNE +
    INC addr+1
+
ENDM
```

Macros are textual. They do not create a scope unless the assembler supports one.

## Unrolled loops

```asm
; 4 bytes, no loop overhead
LDA #0
STA dst+0
STA dst+1
STA dst+2
STA dst+3
```

Unrolling trades ROM for cycles. On NES, ROM is usually cheaper than vblank time.

## Bit tricks

```asm
ORA #%00000100    ; set bit 2
AND #%11111011    ; clear bit 2
EOR #%00000100    ; toggle bit 2
BIT value         ; N = bit 7, V = bit 6, Z = (A & value)==0
```

```asm
; 16-bit shift left
ASL lo
ROL hi

; 16-bit shift right
LSR hi
ROR lo
```

## Self-modifying code

```asm
LDA #$EA          ; NOP
STA patch+1
patch:
LDA #$00
```

This works on the 6502 because there is no instruction cache, but only in **RAM**. NES PRG ROM is read-only; self-modifying code must live in RAM and be copied there first. On banked systems, make sure the code bank is still mapped when it runs.

## Reset and interrupt skeleton

```asm
RESET:
    SEI          ; no IRQ during init
    CLD          ; binary mode (harmless on 2A03)
    LDX #$FF
    TXS          ; stack = $01FF
    ; ... init RAM, PPU, APU, mapper ...
    CLI
main:
    JMP main

NMI:
    PHA
    TXA
    PHA
    TYA
    PHA
    ; ... vblank work ...
    PLA
    TAY
    PLA
    TAX
    PLA
    RTI

IRQ:
    PHA
    TXA
    PHA
    TYA
    PHA
    ; ... acknowledge the IRQ source ...
    PLA
    TAY
    PLA
    TAX
    PLA
    RTI
```

`RTI` restores the flags and returns; `RTS` does not restore `P`. NMI can interrupt an IRQ handler, so either keep NMI short or use a flag to defer work.

`BRK` is a software interrupt: it pushes `PC+2` and sets `B` in the pushed status. A handler that returns must skip the signature byte, or use `BRK` only as a trap.

## 16-bit pointer setup

```asm
; ptr -> buffer
LDA #<buffer
STA ptr
LDA #>buffer
STA ptr+1
```

There is no `LDA #buffer` 16-bit load. The `<`/`>` operators are assembler features, not CPU instructions.

## Fixed-point

8.8 fixed point is common when you need fractions without floats:

```asm
; add two 8.8 values
CLC
LDA a_lo
ADC b_lo
STA sum_lo
LDA a_hi
ADC b_hi
STA sum_hi

; multiply by 2
ASL lo
ROL hi
```

For 8.8 × 8.8, use a 16×16→32 shift-add or a table; the 6502 has no fractional type.
