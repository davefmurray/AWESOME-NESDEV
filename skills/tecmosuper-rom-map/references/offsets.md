# Offset worksheet

## Header

| Byte | Expected for TSB |
|---|---|
| 0–3 | `4E 45 53 1A` |
| 4 | `0x10` — 16 × 16 KB = 256 KB PRG |
| 5 | `0x10` — 16 × 8 KB = 128 KB CHR |
| 6 | mapper low nibble 4, battery bit set, mirroring bit 0 |
| 7 | mapper high nibble 0 |

Verify with a hex editor; hacks and 32-team ROMs can differ.

## Formulas

```
PRG file = 0x10 + bank*0x2000 + offset_in_bank
CHR file = 0x40010 + bank*0x2000 + offset_in_bank

fixed bank 30: cpu = 0xC000 + (file - 0x3C010)
fixed bank 31: cpu = 0xE000 + (file - 0x3E010)
```

## Worked examples

| Want | Calculation | Result |
|---|---|---|
| `$C390` to file | `0x3C010 + ($C390 - $C000)` | `0x3C3A0` |
| `$E000` to file | `0x3E010 + 0` | `0x3E010` |
| RESET vector `$FFFC` | `0x3E010 + ($FFFC - $E000)` | `0x3FFFC` |
| bank 6 + `$8000` | `0x10 + 6*0x2000` | `0x30010` |
| CHR bank 0 | — | `0x40010` |

## Common traps

- Forgetting the 16-byte header: everything is off by `0x10`.
- Treating a CPU address in a switchable bank as a file offset.
- Using the disassembly's 1-based `BankNN` name as the 0-based bank ID.
- Assuming CHR starts at `0x40000`; it starts at `0x40010`.
- Mixing pointer tables that store file offsets with code that expects CPU addresses.
