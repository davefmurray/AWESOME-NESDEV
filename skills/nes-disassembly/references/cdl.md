# Code/Data Logs (CDL)

A CDL is a byte-per-PRG-byte map of what the emulator saw. It is the single most important input to a rebuildable disassembly.

## Shape

- **One byte per PRG byte**, in the same order as the PRG ROM.
- **No 16-byte iNES header.**
- **No CHR.** CHR is tile data, not CPU code.
- A 32 KB PRG ROM produces a 32 KB CDL, not 32 KB + 16.

If the file is 16 bytes longer than PRG, someone included the header. If it is shorter, it is truncated or belongs to another revision.

## Flags (FCEUX and BZK)

| Bit | Mask | Flag | Meaning |
|---|---|---|---|
| 0 | `0x01` | `C` | byte was executed as an instruction |
| 1 | `0x02` | `D` | byte was read as data; also set on absolute `JMP` targets |
| 2–3 | `0x0C` | mapping | last data window: 0=`$8000`, 1=`$A000`, 2=`$C000`, 3=`$E000` |
| 4 | `0x10` | `J` | target of an indirect `JMP ($xxxx)` |
| 5 | `0x20` | `I` | read through `($zp,X)` or `($zp),Y` |
| 6 | `0x40` | `A` | DPCM sample byte |
| 7 | `0x80` | mapping 4 | data read from `$6000–$7FFF` when combined with bits 2–3 |

A byte can carry several flags. `C D 1 J - -` is code that was also read as data and is an indirect-jump target; the `1` says the last data access came through the `$A000` window.

`D` being set on a `JMP` target is a FCEUX logger convention, not a read. That is why `C D` often marks a legitimate code entry.

## Capture with FCEUX

1. Open the ROM.
2. **Debug → Code/Data Logger**.
3. Press **Start**.
4. **NES → Power** (hard reset) so the logger sees the reset path.
5. Play. Exercise menus, every level, death, game over, continues, cutscenes, sound test, two-player, reset.
6. Press **Save** and keep the `.cdl`.

FCEUX writes the log while the logger is active. If you start the logger after loading a savestate, you miss everything that ran before that point. Hard reset after starting the logger.

### Coverage strategy

- **Multiple runs, then OR them.** A CDL is a set of bits; merging is bitwise OR, never addition or averaging.
- Exercise paths that normal play skips: continue screens, game over, level select, debug menus, sound test, all characters/teams, both players, pause, reset during play.
- Use FCEUX movies (`.fm2`) for repeatable runs. The BZK example disassemblies include `.fm2` recordings and `.cdl` files under `_misc`.
- Long idle time does not help. The logger records execution, not wall-clock time.
- If a bank is still mostly untouched, play the content that uses it; do not assume the bank is empty.

## Capture with Mesen

Mesen's debugger has a Code/Data Logger and can export a CDL. The C/D concept is the same, but verify the file size and the first flags against a known code address before feeding it to BZK. If the layout differs, capture with FCEUX instead; BZK's flag decoder is written for FCEUX.

## Merge and report

```bash
python3 scripts/cdl_report.py logs/*.cdl --merge --rom game.nes --out work/game.cdl
```

Output:

```
PRG        32768 bytes (32 KB)
logs       4 (merged)
code       18342 (56.0%)
data       9210 (28.1%)
both       1204   neither 13786
J/I/A      388 / 612 / 0
```

- `code%` is coverage, not correctness.
- `neither` is unvisited bytes: data, unreachable code, code copied to RAM, or padding.
- `J/I/A` counts tell you whether the log contains jump tables, pointer reads and DPCM samples.

Per-bank report (`--bank-kb 8`) is the fastest way to find a bank that the playthrough never touched.

## Validate the bank map with `D`

The mapping digit is a free correctness check for your BZK config:

- If you mapped a bank at `$8000` but see `D 1` all over it, the data was actually read through `$A000`. The config is wrong.
- `D 4` means `$6000–$7FFF`, often SRAM or a mapper's low window.
- The digit is only present when `D` is set; ignore it for pure code bytes.

Fix the config, not the CDL.

## Code copied to RAM

Some games copy a routine from PRG to RAM (`$0300`, `$0400`, or SRAM) and execute the copy. The logger sees the source bytes only as `D`, because the CPU fetched the copy, not the ROM. The source routine will be printed as `.byte`.

Options:

1. Find the copy routine (source pointer, destination, length) and disassemble the RAM destination separately with a RAM-aware disassembler.
2. Annotate the source range by hand and add a comment pointing at the RAM address.
3. Use an emulator trace on the RAM address to recover the executed instructions.

Do not blindly mark the range `C`; the bytes may be a mix of code and data.

## DPCM samples

`A` (bit 6) marks bytes read by the DMC channel. They live in `$C000–$FFFF` and the last sample byte address ends in `0`.

- Extract the range to a `.bin` and use `.incbin "samples.bin"`.
- Do not let BZK disassemble them as instructions.
- The sample length is encoded in the APU register write, not in the CDL; find the `$4012`/`$4013` writes to get the start/length.

## Common mistakes

| Mistake | Result |
|---|---|
| CDL from a different ROM revision | Flags point at the wrong bytes; coverage is meaningless |
| Header included | Size is PRG+16; BZK reads shifted data |
| CHR appended | Size is PRG+CHR; same problem |
| Only one short run | Large parts of the ROM look like data |
| Savestate before logger start | Reset/init code is missing |
| Merging with AND/average | Destroys coverage; always OR |
| Trusting `C` blindly | Jump-into-data false positives become instructions |
| Ignoring `D` mapping | Bank config is wrong and never detected |

## Related

- [BZK workflow](bzk-workflow.md)
- [Rebuild and verify](rebuild-verify.md)
- [Labels and code/data separation](labels.md)
- FCEUX: <https://fceux.com/>
- Mesen: <https://www.mesen.ca/>
