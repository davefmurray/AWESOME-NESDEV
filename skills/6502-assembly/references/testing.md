# Testing 6502 code

You would not ship a parser without tests. The same applies to an opcode, a fixed-point routine or a new addressing-mode calculation. The 6502 has excellent test material; use it.

## The test ladder

| Level | Tool | What it proves |
|---|---|---|
| Single routine | **py65** | Your algorithm and flags |
| Whole CPU | **Klaus functional tests** | Every official opcode and addressing mode |
| Per-cycle | **65x02** | Exact cycle-by-cycle state |
| Transistor reference | **perfect6502** | Behavior of the original NMOS netlist |
| Browser quick check | **6502js / 8bitworkshop** | The code runs at all |

## py65: unit tests for routines

```python
from py65.devices.mpu6502 import MPU

CODE = bytes([
    0x18,             # CLC
    0xA9, 0x34,       # LDA #$34
    0x69, 0x22,       # ADC #$22
    0x85, 0x10,       # STA $10
])

m = MPU()
m.memory[0x8000:0x8000 + len(CODE)] = CODE
m.pc = 0x8000
m.a = 0
m.x = 0
m.y = 0
m.p = MPU.UNUSED | MPU.BREAK   # known flag state
start = m.processorCycles

for _ in range(10):
    m.step()
    if m.pc == 0x8000 + len(CODE):
        break

assert m.memory[0x10] == 0x56
assert m.p & MPU.CARRY == 0
assert m.processorCycles - start == 2 + 2 + 2 + 3
```

`MPU` exposes `a`, `x`, `y`, `sp`, `p`, `pc`, `memory`, `processorCycles`. Flag constants are `NEGATIVE`, `OVERFLOW`, `UNUSED`, `BREAK`, `DECIMAL`, `INTERRUPT`, `ZERO`, `CARRY`.

### A reusable harness

```python
def run(code, *, a=0, x=0, y=0, carry=0, steps=100, org=0x8000):
    m = MPU()
    m.memory[org:org + len(code)] = code
    m.pc = org
    m.a, m.x, m.y = a, x, y
    m.p = MPU.UNUSED | MPU.BREAK
    if carry:
        m.p |= MPU.CARRY
    start = m.processorCycles
    for _ in range(steps):
        m.step()
        if m.pc == org + len(code):
            break
    return m, m.processorCycles - start
```

Assemble the routine with ca65/asm6, extract the bytes, and feed them to `run`. Keep the assembly source and the bytes in sync with a build step, not by hand.

### Testing flags

```python
# 0 - 1 = $FF, C=0, N=1, Z=0, V=0
code = bytes([0x38, 0xA9, 0x00, 0xE9, 0x01])  # SEC; LDA #0; SBC #1
m, _ = run(code)
assert m.a == 0xFF
assert m.p & MPU.CARRY == 0
assert m.p & MPU.NEGATIVE
```

### Testing page crossings and cycles

```python
# LDA $12FF,X
code = bytes([0xBD, 0xFF, 0x12])
m, cycles = run(code, x=0)
assert cycles == 4          # no page cross

m, cycles = run(code, x=1)
assert cycles == 5          # $1300, page crossed
```

This is the fastest way to catch a wrong cycle count in a raster or audio routine.

## Klaus functional tests

[`Klaus2m5/6502_65C02_functional_tests`](https://github.com/Klaus2m5/6502_65C02_functional_tests) contains:

- `6502_functional_test.a65` — all official NMOS opcodes and addressing modes.
- `65C02_extended_opcodes_test.a65c` — 65C02 additions, including undefined opcodes.
- `6502_interrupt_test.a65` — IRQ/NMI behavior.
- `6502_decimal_test.a65` — Bruce Clark's decimal-mode tests.

The test traps at a `success` label. Run it in your emulator, set a breakpoint at `success`, and fail if the PC lands anywhere else. The repository includes the original `as65` assembler; a ca65-compatible port exists in `amb5l`'s repository.

This is the test to run after writing a new CPU core or changing interrupt/flag behavior.

## 65x02: per-cycle JSON tests

[`SingleStepTests/65x02`](https://github.com/SingleStepTests/65x02) provides one JSON file per opcode. Each test is a single instruction with full state before and after:

Each file has an `initial` and `final` object with `pc`, `a`, `x`, `y`, `sp`, `p`, and a **sparse** `ram` list of `[address, value]` pairs, plus the expected `cycles`.

Run one instruction, compare every register and the listed RAM bytes, and compare the cycle count. Do not compare the whole 64 KB array unless the test specifies it; the JSON only lists memory that matters.

## perfect6502

[`mist64/perfect6502`](https://github.com/mist64/perfect6502) simulates the original NMOS 6502 transistor netlist. It is ~1/30 real speed, but it is the reference for ambiguous behavior: undocumented flags, decimal mode, interrupt timing, the `JMP ($xxFF)` bug.

Use it when two emulators disagree and the documentation is silent. Build with `make`, run `cbmbasic/cbmbasic`, or call its C API from a harness.

## 6502js and 8bitworkshop

- [Easy 6502](https://skilldrick.github.io/easy6502/) embeds `6502js`; paste a routine, assemble, step, inspect memory.
- [8bitworkshop](https://8bitworkshop.com/) has a debugger with breakpoints, memory browser and time-travel; its CLI can run a ROM for N frames and save a screenshot.

Neither is a substitute for py65/Klaus, but they are the fastest way to see a routine fail.

## What to test

For every nontrivial routine:

1. **Zero / max / min** inputs. `$00`, `$FF`, `$7F`, `$80`.
2. **Carry in and out** for `ADC`/`SBC`.
3. **Page crossing** for `abs,X`, `abs,Y`, `(zp),Y`.
4. **Zero-page wrap** for `zp,X`/`zp,Y`.
5. **Branch taken/not taken**, and at the range edge.
6. **Stack balance** on every return path.
7. **Interrupt reentrancy** if the routine is called from NMI/IRQ.
8. **Decimal disabled** on the target (2A03) vs enabled (NMOS 6502).

## Cycle testing

Count cycles from the opcode table plus penalties:

```
total = base_cycles
      + (page_crossed ? 1 : 0)     ; reads only
      + (branch_taken ? 1 : 0)
      + (branch_page_crossed ? 1 : 0)
```

`processorCycles` in py65 includes the extra cycles. If your emulator does not, fix the emulator before trusting the test.

## A minimal CI loop

```bash
# assemble
ca65 -t nes -g src/main.s -o build/main.o
ld65 -C nes.cfg build/main.o -o build/game.nes

# unit tests
python3 tests/test_math.py

# full CPU
# run Klaus test ROM in the emulator; fail unless PC == success

# screenshot / smoke test
npm run cli -- run --platform nes --frames 240 --png build/shot.png build/game.nes
```

The order matters: unit tests catch logic, Klaus catches CPU, the screenshot catches integration.
