# Rebuild and verify

A disassembly is only finished when the same assembler, the same linker config and the same header/CHR inputs produce a byte-identical ROM.

## The chain

```
copy_bank_*.asm  --ca65-->  *.o  --ld65-->  PRG_ROM.bin
header.bin + PRG_ROM.bin + CHR_ROM.chr  --cat-->  rebuilt.nes
```

BZK writes `header.bin` and `CHR_ROM.chr` from the original ROM, so the rebuild starts from the same bytes. If you edit the header or CHR, you are no longer verifying the disassembly.

## ca65 / ld65

BZK output is ca65 syntax. It uses `.segment`, `.include`, `.org` and (after prep) plain instructions.

```bash
ca65 -U copy_bank_00.asm -o bank_00.o
ld65 -C ld65.cfg -o PRG_ROM.bin bank_00.o
```

`-U` means "no need to `.import` symbols"; BZK's build scripts use it because each bank file is self-contained except for the RAM include.

A minimal 32 KB NROM config:

```
MEMORY {
    PRG: start = $8000, size = $8000, fill = yes, fillval = $FF, file = %O;
}
SEGMENTS {
    BANK_00: load = PRG, type = ro, start = $8000;
    VECTORS: load = PRG, type = ro, start = $FFFA;
}
```

For a banked ROM, one memory area per CPU window, or one area with segments placed at `start = $8000/$A000/$C000/$E000`. The linker must emit the PRG bytes in the same order as the original file. Check the first bank's offset before trusting a multi-bank config.

## Header and CHR

```bash
cat header.bin PRG_ROM.bin CHR_ROM.chr > rebuilt.nes
```

- `header.bin` is 16 bytes for iNES, 16 for NES 2.0 (the header is still 16 bytes; the fields differ).
- `PRG_ROM.bin` must be exactly the PRG size.
- `CHR_ROM.chr` must be exactly the CHR size, or omitted for CHR-RAM games.
- If the original has no CHR file, do not append one.

A size check is the first verification:

```bash
wc -c game.nes rebuilt.nes
```

## Byte-identical verification

```bash
python3 scripts/rom_verify.py game.nes rebuilt.nes
```

```
original  40976 bytes  B5D3...
rebuilt   40976 bytes  B5D3...
MATCH: byte-identical
```

If it differs:

```
DIFF: 37 bytes in 4 ranges
first diff at 0x0002F1
  0x0002F1-0x0002F1  1 bytes
  0x000812-0x000813  2 bytes
```

Always triage the **first** diff. A later diff is often a consequence of an earlier length error.

## Diff triage

| Pattern | Likely cause | Fix |
|---|---|---|
| Rebuilt is 1 byte shorter per occurrence | Missing `a:` on absolute zero-page access | Restore `a:` |
| Rebuilt is 1 byte longer per occurrence | Forced absolute where the original was zero page, or a `.word` where `.byte` belongs | Remove the forced `a:`, or use `.byte` |
| Single-byte diff at an operand | Wrong endianness, wrong table byte, or a `.byte` vs `.word` mistake | Compare source line at that offset |
| Whole bank differs | Bank mapped to the wrong CPU window or wrong file offset | Fix `ASM_config_table` |
| Header bytes differ | Wrong header file/size or edited flags | Regenerate `header.bin` |
| CHR differs | Wrong CHR offset/size, or CHR was edited | Regenerate `CHR_ROM.chr` |
| Trailing `$00`/`$FF` run | Missing fill/padding at the end of a bank | Add `.res`/fill in the segment |
| `Range error` on branch | Target not labeled | Add label, use it as operand |
| Build matches, game crashes | Disassembly is faithful; bug is in the original or your patch | Debug behavior, not bytes |

## Why `a:` matters

```
LDA $0010    ; original: AD 10 00 (3 bytes)
LDA $10      ; ca65: A5 10 (2 bytes)
```

If the original uses the absolute form for a zero-page address, ca65's automatic zero-page choice shifts the next instruction up by one byte. BZK emits `LDA a: ram_0010`; keep the `a:`.

The same trap exists for `STA`, `ADC`, `SBC`, `AND`, `ORA`, `EOR`, `CMP`, `BIT`, `INC`, `DEC`, `ASL`, `LSR`, `ROL`, `ROR`, `JMP` and `JSR` when the address is below `$0100`.

## Branches

BZK prints the raw target, for example:

```
C - - - - - 0x000123 00:8123: D0 05     BNE $812A
```

ca65 cannot encode `BNE $812A` as relative. Add a label at `$812A`:

```
        BNE loc_812A
...
loc_812A:
```

If the target is in another bank, the branch is impossible; the original must be using a trampoline or the CDL is wrong.

## Verification levels

1. **Size** — same byte count.
2. **Hash** — same SHA-1/SHA-256.
3. **Per-bank diff** — if not identical, at least know which bank.
4. **Boot** — reset vector, PPU init, first screen.
5. **Behavior** — play the same inputs/savestate and compare screenshots or RAM.

A byte-identical rebuild is the strongest result. If you cannot reach it, a behaviorally equivalent rebuild is acceptable only if you understand every diff.

## CI loop

```bash
#!/bin/sh
set -eu
lua preparations.lua
for f in copy_bank_*.asm; do ca65 -U "$f"; done
ld65 -C ld65.cfg -o PRG_ROM.bin copy_bank_*.o
cat header.bin PRG_ROM.bin CHR_ROM.chr > rebuilt.nes
python3 scripts/rom_verify.py game.nes rebuilt.nes
```

Run this after every labeling batch. A one-byte drift is much easier to find immediately than after 500 labels.

## Related

- [BZK workflow](bzk-workflow.md)
- [Labels](labels.md)
- [CDL](cdl.md)
- [ca65 Users Guide](https://cc65.github.io/doc/ca65.html)
- [ld65 Users Guide](https://cc65.github.io/doc/ld65.html)
