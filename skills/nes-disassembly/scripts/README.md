# Scripts

Dependency-free Python 3 helpers for the CDL → BZK → ca65 loop. Run from this directory or use an absolute path.

| Script | Use |
|---|---|
| `nes_header.py` | Print mapper, PRG/CHR sizes, mirroring, SHA-1/SHA-256 |
| `cdl_report.py` | Merge CDLs, report coverage/flags, list untouched ranges |
| `bzk_config.py` | Generate a starting BZK `config.lua` from a ROM |
| `rom_verify.py` | Compare original and rebuilt ROMs |

## Examples

```bash
# inventory
python3 scripts/nes_header.py game.nes

# merge and report
python3 scripts/cdl_report.py logs/*.cdl --merge --rom game.nes --out work/game.cdl

# starting BZK config (NROM/UxROM/MMC1/MMC3/AxROM)
python3 scripts/bzk_config.py game.nes --cdl game.cdl --out work/config.lua

# verify
python3 scripts/rom_verify.py game.nes rebuilt.nes
```

`cdl_report.py` uses the FCEUX/BZK flag layout: bit0 code, bit1 data, bits2–3 + bit7 data mapping, bit4 indirect-jump target, bit5 indirect read, bit6 DPCM sample.

`bzk_config.py` proposes static bank windows. It does not simulate runtime banking. Verify against the CDL `D` digit and duplicate windows by hand where needed.
