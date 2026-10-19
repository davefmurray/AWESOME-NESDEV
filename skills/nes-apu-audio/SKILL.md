---
name: nes-apu-audio
description: "NES APU programming: pulse, triangle, noise and DMC channels, $4000-$4017 registers, frame counter, envelopes, length counters, sweep, frequency math, and the DPCM/DMA hazards. Use when writing a sound driver, playing a note, debugging silent or detuned audio, or porting a FamiTracker/FamiStudio song."
---

# NES APU audio

Five channels: two pulses, triangle, noise, DMC. No hardware volume envelope beyond the 4-bit envelope unit; music drivers do the rest in software. The APU runs on its own frame counter, not the PPU's vblank.

## Channel map

| Registers | Channel | Units |
|---|---|---|
| `$4000–$4003` | Pulse 1 | timer, length, envelope, sweep |
| `$4004–$4007` | Pulse 2 | same |
| `$4008–$400B` | Triangle | timer, length, linear counter |
| `$400C–$400F` | Noise | timer (LFSR), length, envelope |
| `$4010–$4013` | DMC | sample reader, buffer, output |
| `$4015` | All | enable + status |
| `$4017` | All | frame counter mode + IRQ inhibit |

## Pulse

```
$4000  DDLC VVVV   duty, length-halt/loop, constant volume, volume/envelope
$4001  EPPP NSSS   sweep enable, period, negate, shift
$4002  TTTT TTTT   timer low
$4003  LLLL LTTT   length load, timer high; restarts envelope + phase
```

- Duty: 0 = 12.5%, 1 = 25%, 2 = 50%, 3 = 75%.
- Frequency: `f = fCPU / (16 * (t + 1))`, `t` is the 11-bit timer. `t < 8` silences.
- Writing `$4003`/`$4007` resets phase; for vibrato, write only the low byte.
- Sweep can silence the channel when the target period overflows; check its mute rules before using it.

NTSC `fCPU = 1.7897725 MHz`; PAL `1.662607 MHz`.

## Triangle

```
$4008  CRRR RRRR   length-halt/linear control, linear reload
$4009  ---- ----
$400A  TTTT TTTT   timer low
$400B  LLLL LTTT   length load, timer high; sets linear reload flag
```

- One octave below a pulse with the same timer: `f = fCPU / (32 * (t + 1))`.
- No volume control. A linear counter (7-bit) and the length counter both silence it; whichever is shorter wins.
- Writing `$400B` sets the reload flag; the linear counter reloads on the next quarter-frame tick.
- Silencing halts the wave at its last value, not at zero.

## Noise

```
$400C  --LC VVVV   loop/halt, constant volume, volume/envelope
$400D  ---- ----
$400E  M--- PPPP   mode (periodic), period index
$400F  LLLL L---   length load
```

Noise periods (NTSC): 4, 8, 16, 32, 64, 96, 128, 160, 202, 254, 380, 508, 762, 1016, 2034, 4068 CPU cycles. Mode 1 shortens the LFSR period for a metallic tone.

## DMC

```
$4010  IL-- RRRR   IRQ enable, loop, rate index
$4011  -DDD DDDD   direct 7-bit DAC load
$4012  AAAA AAAA   sample address = $C000 + A*64
$4013  LLLL LLLL   length = L*16 + 1 bytes
```

- Samples live in `$C000–$FFFF` (and wrap through `$8000`). Vectors and banking can get in the way.
- `$4011` can play raw PCM if you update it fast enough; this costs most of the CPU.
- DMC DMA steals CPU cycles and can corrupt controller reads and `$2007` reads. See `nes-input-devices`.

## Frame counter

```
$4017  MI------   M: 0 = 4-step, 1 = 5-step; I: IRQ inhibit
```

- 4-step mode: envelope/linear at ~240 Hz, length/sweep at ~120 Hz, IRQ at ~60 Hz if not inhibited.
- 5-step mode: no IRQ, different timing; writing with M=1 immediately clocks both quarter and half frames.
- The frame counter is independent of vblank. Writing `$4017` resets it.
- Most games write `$4017 = $40` (4-step, IRQ inhibited) at init and drive music from NMI.

## Envelope and length

- Envelope: constant volume or a decaying 15→0 saw, looped by the halt bit.
- `$4000/$4004/$400C` bit 5 = halt/loop; bit 4 = constant volume; bits 3–0 = volume or divider reload.
- Length counter: 5-bit index into a 32-entry table (10, 254, 20, 2, 40, 4, 80, 6, 160, 8, 60, 10, 14, 12, 26, 14, 12, 16, 24, 18, 48, 20, 96, 22, 192, 24, 72, 26, 16, 28, 32, 30 ticks at ~120 Hz).
- Setting the halt bit freezes the length counter; the channel still needs a non-zero length to sound.

## Init (silence everything)

```asm
  lda #$00
  sta $4015        ; disable all channels
  sta $4000
  sta $4001
  sta $4002
  sta $4003
  sta $4004
  sta $4005
  sta $4006
  sta $4007
  sta $4008
  sta $400A
  sta $400B
  sta $400C
  sta $400E
  sta $400F
  lda #$40
  sta $4017        ; 4-step, IRQ inhibited
  lda #$0F
  sta $4015        ; enable pulse 1/2, triangle, noise
```

## Mixer

The APU mixes nonlinearly:

```
pulse = 95.88 / (8128 / (p1 + p2) + 100)
tnd   = 159.79 / (1 / (t/8227 + n/12241 + d/22638) + 100)
out   = pulse + tnd
```

Approximate levels are fine for games; use the formula when matching a reference recording.

## Checks

- Is `$4015` enabling the channel? A silent channel with correct registers is usually disabled.
- Is the length counter non-zero and not halted at zero?
- Is the timer value in range (`t >= 8` for pulse)?
- Did you write `$4003`/`$4007` every note, resetting phase and envelope?
- Is the frame counter IRQ accidentally enabled (`$4017` bit 6 clear)?
- Is DMC DMA stealing cycles or corrupting `$4016` reads?
- NTSC vs PAL: frequency and frame-counter rates differ.

## Failure modes

| Symptom | Cause |
|---|---|
| Silence | `$4015` channel bit off, length zero, timer < 8, sweep muted |
| Clicks on vibrato | Writing the high timer byte resets phase |
| Detuned | Wrong `fCPU`, wrong timer formula, PAL values |
| Noise sounds wrong | Period table differs NTSC/PAL; mode bit |
| DMC crackle | Sample crossing a bank boundary, wrong length, IRQ enabled |
| Controller ghosts during music | DPCM DMA double-clocking `$4016` |

## References

- [APU](https://www.nesdev.org/wiki/APU) · [APU Pulse](https://www.nesdev.org/wiki/APU_Pulse) · [APU Triangle](https://www.nesdev.org/wiki/APU_Triangle)
- [APU Noise](https://www.nesdev.org/wiki/APU_Noise) · [APU DMC](https://www.nesdev.org/wiki/APU_DMC)
- [APU Frame Counter](https://www.nesdev.org/wiki/APU_Frame_Counter) · [APU Envelope](https://www.nesdev.org/wiki/APU_Envelope)
- `references/registers.md` · `references/tables.md`
