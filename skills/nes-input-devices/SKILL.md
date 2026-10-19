---
name: nes-input-devices
description: "Read NES/Famicom controllers through $4016/$4017, handle the DPCM double-clock glitch, support Famicom expansion controllers, the Zapper, and Four Score. Use when input is unresponsive, buttons ghost, a controller read routine is needed, or a light gun/multitap is involved."
---

# NES input devices

Controllers are 4021 shift registers. The CPU strobes them through `$4016` and reads one bit at a time from `$4016` (port 1) or `$4017` (port 2). The signal is inverted: a pressed button reads as 1 after the inversion in the console, but the raw line is active-low.

## Standard read

```
$4016 write:  xxxx xEES   S = controller latch, EE = expansion latch
$4016 read:   xxxD DDDD   D0 = port 1 data
$4017 read:   xxxD DDDD   D0 = port 2 data
```

Sequence:

1. Write 1 to `$4016` (latch buttons).
2. Write 0 to `$4016` (serial mode).
3. Read 8 bits from `$4016`/`$4017`, one per read.

Report order: **A, B, Select, Start, Up, Down, Left, Right**. 1 = pressed. After 8 reads, official controllers return 1s.

```asm
read_pad:
  lda #1
  sta $4016
  lda #0
  sta $4016
  ldx #8
@loop:
  lda $4016
  lsr a            ; bit 0 -> carry
  ror buttons      ; first bit ends in bit 0 (A), last in bit 7 (Right)
  dex
  bne @loop
  rts
```

Read both ports every frame unless you have a reason not to; some devices need the clocks.

## DPCM double-clock glitch

If DMC DMA starts a read in the same cycle as a `$4016`/`$4017` read, the shift register gets an extra clock and drops a bit. The classic symptom is a **spurious Right press**: the missing bit is replaced by the trailing 1.

Mitigations:

- **Read twice and compare.** Cheap, works for standard controllers, fails for devices that cannot be reread (mouse).
- **Synchronize with OAM DMA.** Trigger OAM DMA immediately before the read; the APU's get/put cycle alignment then avoids the glitch. Keep reads an even number of cycles apart. This is the modern technique; not every emulator models it.
- **Do not play DPCM while reading.** Simplest, costs a channel.
- Fix is in the 2A07 (PAL) CPU; NTSC is affected.

## Famicom differences

- Hardwired controllers: player 1 on `$4016` D0, player 2 on `$4017` D0.
- Player 2 has no Start/Select; those bits read 0.
- Microphone on `$4016` D2 (player 2). Reads as a bit, not audio; games detect changes.
- Expansion port controllers appear on D1; OR D1 and D0 to accept either.
- AV Famicom uses detachable NES-style controllers; no microphone.

## Zapper

| Bit | Meaning |
|---|---|
| D3 | Light sense: 0 = light detected, 1 = not |
| D4 | Trigger: 0 = released or fully pulled, 1 = half-pulled |

Sequence:

1. Wait for trigger.
2. During vblank, confirm no light is sensed (otherwise a standard controller is plugged in).
3. Draw a white box per target; check D3 over a full frame (sensor stays on ~19–26 scanlines).
4. Register a hit if the bit goes low while that target is displayed.

The sensor is tuned for CRT scan rates; LCD lag and 60 Hz panels break it. Some clones invert the trigger.

## Four Score / multitaps

The Four Score multiplexes four controllers onto `$4016`/`$4017` using a signature handshake. Do not assume the standard 8-bit report; follow the adapter's protocol. It only passes D0 from each controller.

## Controller detection

- No controller: D0 reads 0 (pull-up + inverter).
- Standard controller: first 8 bits are meaningful, then 1s.
- Expansion device: may use D1–D4 differently; identify by the signature its protocol returns.

## Checks

- Did you write 1 **then** 0 to `$4016` before reading?
- Are you reading exactly 8 bits per port per frame?
- Is the report order A,B,Select,Start,Up,Down,Left,Right?
- Are you reading during vblank while also doing heavy PPU work? Reads can wait; keep them short.
- Is DPCM playing? Compare two reads or use the OAM-DMA sync.
- On Famicom, are you OR-ing D1 for expansion controllers?
- For Zapper, is the display CRT or a low-lag setup?

## Failure modes

| Symptom | Cause |
|---|---|
| All buttons dead | Missing strobe, reading `$4016` only once, wrong port |
| Spurious Right | DPCM double clock |
| Player 2 Start never works | Famicom hardwired controller |
| Zapper always misses | LCD lag, black screen, wrong bit polarity |
| Four Score returns garbage | Standard protocol used instead of the adapter's |

## References

- [Controller reading](https://www.nesdev.org/wiki/Controller_reading) · [Standard controller](https://www.nesdev.org/wiki/Standard_controller)
- [Input devices](https://www.nesdev.org/wiki/Input_devices) · [Zapper](https://www.nesdev.org/wiki/Zapper)
- [Controller reading code](https://www.nesdev.org/wiki/Controller_reading_code)
- `references/controller-reading.md`
