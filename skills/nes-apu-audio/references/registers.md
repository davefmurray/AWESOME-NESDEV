# APU register reference

## Pulse 1 / 2

| Addr | Bits | Meaning |
|---|---|---|
| `$4000`/`$4004` | `DDLC VVVV` | duty 0–3; length halt/loop; constant volume; volume/envelope divider |
| `$4001`/`$4005` | `EPPP NSSS` | sweep enable; period; negate; shift |
| `$4002`/`$4006` | `TTTT TTTT` | timer low 8 bits |
| `$4003`/`$4007` | `LLLL LTTT` | length index; timer high 3 bits; restarts envelope and phase |

Duty: 0 = 12.5%, 1 = 25%, 2 = 50%, 3 = 75%.
`f = fCPU / (16 * (t + 1))`; muted when `t < 8` or length is 0.

## Triangle

| Addr | Bits | Meaning |
|---|---|---|
| `$4008` | `CRRR RRRR` | length halt / linear control; linear reload |
| `$400A` | `TTTT TTTT` | timer low |
| `$400B` | `LLLL LTTT` | length index; timer high; sets linear reload flag |

`f = fCPU / (32 * (t + 1))`. No volume. The linear counter is 7-bit and reloads on the next quarter-frame tick.

## Noise

| Addr | Bits | Meaning |
|---|---|---|
| `$400C` | `--LC VVVV` | loop/halt; constant volume; volume/envelope |
| `$400E` | `M--- PPPP` | periodic mode; period index |
| `$400F` | `LLLL L---` | length index |

## DMC

| Addr | Bits | Meaning |
|---|---|---|
| `$4010` | `IL-- RRRR` | IRQ enable; loop; rate index |
| `$4011` | `-DDD DDDD` | 7-bit DAC value |
| `$4012` | `AAAA AAAA` | sample address = `$C000 + A*64` |
| `$4013` | `LLLL LLLL` | length = `L*16 + 1` bytes |

## Status / control

`$4015` write: `---D NT21` — DMC, noise, triangle, pulse 2, pulse 1.
`$4015` read: `IF-D NT21` — DMC IRQ, frame IRQ, DMC active, length statuses.
Reading `$4015` clears the frame IRQ flag (not the DMC flag).

`$4017` write: `MI------` — 0 = 4-step, 1 = 5-step; IRQ inhibit; M=1 immediately clocks quarter and half frames.

## Frame counter

4-step (M=0): quarter at ~240 Hz, half at ~120 Hz, IRQ at ~60 Hz if I=0.
5-step (M=1): quarter at ~192 Hz, half at ~96 Hz, no IRQ.

The sequencer is independent of the PPU. Writing `$4017` resets it.
