# Labels and code/data separation

BZK gives you a linear decode. Labels turn it into source you can edit.

## The prefix is metadata

```
C D 1 J - - 0x001234 01:8123: AD 10 00   LDA a: ram_0010
```

- `C` = executed code.
- `D` = read as data.
- `1` = last data window `$A000`.
- `J` = indirect-jump target.
- `I` = read through a pointer.
- `A` = DPCM sample.
- `0x001234` = file offset.
- `01:8123` = bank:CPU address.

Keep the prefix while you work. Strip it only for the build copy.

## Label classes

| Prefix | Use |
|---|---|
| `vec_` | reset/NMI/IRQ vector entry |
| `loc_` | `JMP`/`JSR` target |
| `bra_` | branch target |
| `tbl_` | data table |
| `ptr_` | pointer table / indirect pointer |
| `ram_` | RAM variable |
| `sub_` | subroutine entry (optional) |
| `data_` | raw data block (optional) |

The exact names do not matter; consistency does. BZK's published disassemblies use `vec_`, `loc_`, `bra_`, `tbl_`, `ram_`.

## Branch labels

A branch operand is a signed offset from the byte after the instruction. To label:

1. Compute the target: `PC + 2 + signed8` (or read the address from the debugger).
2. Define a label at the target address.
3. Replace the operand with the label.

```asm
        BNE bra_812A
...
bra_812A:
```

If the target is in another bank, the branch cannot reach it; the original code must be using a trampoline, or the bank mapping is wrong.

## JMP and JSR labels

`JMP`/`JSR` take a 16-bit absolute address. Define `loc_xxxx` at the target and replace the operand.

```asm
        JSR loc_9000
...
loc_9000:
        RTS
```

If the target is outside the bank, the address is in another CPU window. Mark it as an external symbol or keep the raw address with a comment; ca65 will not resolve a label that is not in the same segment unless you `import` it.

## Jump tables

Indirect jumps use a table of 16-bit addresses:

```asm
        LDX index
        LDA tbl_9000_lo,X
        STA ptr
        LDA tbl_9000_hi,X
        STA ptr+1
        JMP (ptr)
```

The `J` flag marks the **targets**, not the table bytes. The `I` flag marks bytes read through `(zp),Y`/`(zp,X)`, which often includes the table bytes.

Label the table (`tbl_`), each target (`loc_`), and the pointer variable (`ptr_`). If the table is split into low/high parallel arrays, label both.

## Data tables

Data can be:

- `.byte` bytes
- `.word` 16-bit values
- `.dbyt` big-endian words (ca65)
- strings via `.byte "text"` or `.asciiz`
- raw binary via `.incbin`

Use the CDL `D` flag and the table file comments to decide. If the bytes look like code but `C` is not set, they are data until proven otherwise.

## DPCM samples

`A` bytes are audio samples, not code. Extract the range to a `.bin`:

```bash
# NROM 32K example: CPU $C000 -> file 0x10 + ($C000 - $8000) = 0x4010
dd if=game.nes of=samples.bin bs=1 skip=$((0x4010)) count=$((0x1000))
```

For a banked ROM, compute the bank's file offset with `tools/addr.py` or the BZK config; do not use the linear formula.

Then:

```asm
samples:
    .incbin "samples.bin"
```

Find the sample start/length from the `$4012`/`$4013` writes; the CDL does not encode length.

## False `C` flags

A `JMP` into a data table can mark bytes as code. Signs:

- The decode runs into obvious data (text, pointer tables, graphics).
- The instruction stream makes no sense after a few bytes.
- The same bytes are also read as data (`D`).
- Execution never returns to the range.

Fix: convert the range to `.byte`/`.word` and add a comment explaining the jump target. Do not “fix” the CDL; the log is evidence of what happened.

## Function boundaries

Heuristics:

- `RTS`/`RTI` ends a subroutine.
- `JMP` ends a basic block.
- A label targeted by `JSR` starts a subroutine.
- A `PHA`/`TXA`/`PHA` prologue is a save-registers function.
- A jump table target starts a handler.

Do not over-fit: 6502 code shares tails and falls through. A `JMP` to another routine is a tail call, not an error.

## ca65 scoping

- `name:` is a global label.
- `@name` is a cheap local label, scoped to the previous global label.
- `:` is an unnamed label; reference with `:+`/`:-`.
- `.proc name` / `.endproc` creates a scope; `.import`/`.export` for cross-module symbols.

Use `.proc` for subroutines with many locals; use `@` for short loops.

## Cross-bank references

- A label in another bank cannot be a plain 16-bit reference unless that bank is mapped at the same CPU address.
- Use a comment or an `import`ed symbol for the bank and address.
- For a fixed bank (`$C000`/`$E000` on MMC3), labels are stable across banks; for switchable banks, they are not.
- Keep a per-bank symbol map (`bank_00.sym`, etc.) so you do not collide names.

## Comments

- Keep the original BZK prefix in a comment if it helps: `; C 0x001234 01:8123`.
- Record the evidence: “CDL C+D, J target”, “read by LDA ($20),Y”, “DPCM sample”.
- Mark uncertain code: `; TODO verify`.
- Note the ROM revision and SHA-1 at the top of the first bank.

## Automation

The BZK Notepad++ scripts do the mechanical parts:

- **Label all branches** — scans `BNE/BCC/...` and creates `bra_` labels.
- **Label tables [range]** — creates `tbl_` labels for data ranges.
- **Label JMP/JSR [range]** — creates `loc_` labels.
- **.byte -> instruction** — converts a byte run back to code.
- **.byte x2 -> .word** — combines byte pairs.

On macOS/Linux, write the equivalent in Python:

1. Parse each line's CPU address and mnemonic.
2. For branches, compute the target and record it.
3. Emit labels at targets.
4. Replace operands with labels.
5. Re-run ca65 and diff.

Do this in small batches. A mass relabel that breaks the build is harder to debug than ten labeled branches.

## Related

- [BZK workflow](bzk-workflow.md)
- [Rebuild and verify](rebuild-verify.md)
- [CDL](cdl.md)
- [6502 addressing modes](../../6502-assembly/references/addressing-modes.md)
