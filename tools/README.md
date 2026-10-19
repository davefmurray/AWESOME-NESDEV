# tools

Small, dependency-free helpers used by the [cold-ROM playbook](../docs/cold-rom-playbook.md). Python 3 standard library only.

| Tool | Use |
|---|---|
| `nes_header.py` | Parse iNES/NES 2.0: mapper, PRG/CHR, mirroring, battery, TV, hashes |
| `addr.py` | File offset ↔ CPU address, refusing to guess on banked carts |
| `cdl_stats.py` | Summarise or merge CDL logs; per-page code coverage |

```bash
python3 tools/nes_header.py roms/lws.nes
python3 tools/addr.py --offset 0x10 --mapper 0 --prg-kb 32
python3 tools/cdl_stats.py work/boot.cdl work/play.cdl --merge --rom roms/lws.nes
```

Tested against synthetic NROM and MMC3 NES 2.0 headers. They answer questions you should not be guessing at; they do not replace a debugger.
