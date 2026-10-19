# APU tables and math

## Length counter values

Index `$00–$1F`, ticks at ~120 Hz NTSC (~100 Hz PAL):

```
10, 254, 20, 2, 40, 4, 80, 6,
160, 8, 60, 10, 14, 12, 26, 14,
12, 16, 24, 18, 48, 20, 96, 22,
192, 24, 72, 26, 16, 28, 32, 30
```

## Noise periods

CPU cycles between LFSR clocks, NTSC:

```
4, 8, 16, 32, 64, 96, 128, 160,
202, 254, 380, 508, 762, 1016, 2034, 4068
```

PAL differs from index 2 onward (14, 30, 60, 88, 118, 148, 188, 236, 354, 472, 708, 944, 1890, 3778).

## DMC rates

CPU cycles per output bit, NTSC:

```
428, 380, 340, 320, 286, 254, 226, 214,
190, 160, 142, 128, 106, 84, 72, 54
```

## Note math

Pulse period for frequency `f`:

```
t = round(fCPU / (16 * f)) - 1
```

Examples at NTSC:

| Note | f (Hz) | t (dec) | t (hex) |
|---|---|---|---|
| A3 | 220.00 | 507 | $1FB |
| A4 | 440.00 | 253 | $0FD |
| A5 | 880.00 | 126 | $07E |
| C4 | 261.63 | 426 | $1AA |
| C5 | 523.25 | 212 | $0D4 |

Triangle uses half the frequency for the same `t`, i.e. one octave lower.

To avoid phase-reset clicks on vibrato, write only `$4002`/`$4006` (timer low); reserve `$4003`/`$4007` for note starts.

## Mixer

```
pulse = 95.88 / (8128 / (p1 + p2) + 100)
tnd   = 159.79 / (1 / (t/8227 + n/12241 + d/22638) + 100)
out   = pulse + tnd
```

`p1`, `p2`, `t`, `n`, `d` are the channel outputs (0–15, DMC 0–127). The mix is nonlinear; do not sum channels linearly if you are matching a recording.
