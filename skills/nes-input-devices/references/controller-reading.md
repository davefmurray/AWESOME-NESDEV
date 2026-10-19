# Controller reading details

## Signal path

- 4021 parallel-in/serial-out shift register in the controller.
- `$4016` bit 0 high = latch (parallel load); low = serial shift.
- Each read of `$4016`/`$4017` pulses CLK; the console inverts the data line.
- After 8 clocks, official controllers shift in 0s, which read back as 1s.

## Report order

| Bit | Button |
|---|---|
| 0 | A |
| 1 | B |
| 2 | Select |
| 3 | Start |
| 4 | Up |
| 5 | Down |
| 6 | Left |
| 7 | Right |

## Bit order in code

If you shift with `ROR`, the first bit read ends in bit 0. If you shift with `ROL`, it ends in bit 7. Pick one and keep the button masks consistent — mixing them produces "left/right swapped" bugs.

## DPCM double clock

DMC DMA can steal the cycle of a `$4016` read, adding an extra clock. The report loses one bit; the trailing 1 shifts into the Right position, producing a phantom Right press.

Options:

1. Read twice, compare, discard disagreements.
2. OAM DMA immediately before reading, keep reads evenly spaced.
3. Disable DPCM during input.

## OAM-sync sketch

```asm
  lda #0
  sta $4014        ; OAM DMA, 513 cycles
  ; read both pads with fixed-cycle instructions
```

The APU alternates get/put cycles; DMA aligns the CPU so the following reads miss the glitch. This is hardware behavior that many emulators approximate poorly.

## Zapper

- D3: 0 = light detected.
- D4: 0 = released or fully pulled; 1 = half-pulled.
- Read during vblank with the screen black to confirm a gun is present.
- Flash one white target at a time and poll D3 for a full frame.

## Four Score

Uses a signature sequence and returns 24 bits per port (four controllers). It is not the standard 8-bit protocol; implement the adapter's handshake, and remember it only passes D0.
