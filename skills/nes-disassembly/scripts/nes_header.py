#!/usr/bin/env python3
"""Print iNES/NES 2.0 header facts and hashes.

    python3 nes_header.py game.nes
    python3 nes_header.py game.nes --json
"""

from __future__ import annotations
import argparse, hashlib, json, sys

def num(s: str) -> int:
    return int(s, 0)

def parse(path: str) -> dict:
    b = open(path, "rb").read()
    if b[:4] != b"NES\x1a":
        raise SystemExit(f"{path}: not an iNES/NES 2.0 file")
    f6, f7 = b[6], b[7]
    nes2 = (f7 & 0x0C) == 0x08
    prg_lo, chr_lo = b[4], b[5]
    if nes2:
        exp = (f7 & 0x03) << 8 | b[9]
        pu = prg_lo | ((b[9] & 0x0F) << 8)
        cu = chr_lo | ((b[9] & 0xF0) << 4)
        prg = pu * 16384 if exp == 0 else pu * (1 << exp)
        chr = cu * 8192 if exp == 0 else cu * (1 << exp)
    else:
        prg, chr = prg_lo * 16384, chr_lo * 8192
    mapper = (f7 & 0xF0) | (f6 >> 4)
    if nes2:
        mapper |= (b[8] & 0x0F) << 8
    return {
        "file": path, "size": len(b), "format": "NES 2.0" if nes2 else "iNES",
        "mapper": mapper, "prg_bytes": prg, "chr_bytes": chr,
        "prg_kb": prg // 1024, "chr_kb": chr // 1024,
        "mirroring": {0: "horizontal", 1: "vertical", 2: "four-screen", 3: "mapper-controlled"}.get(f6 & 1, "?"),
        "battery": bool(f6 & 2), "trainer": bool(f6 & 4),
        "sha1": hashlib.sha1(b).hexdigest().upper(),
        "sha256": hashlib.sha256(b).hexdigest().upper(),
    }

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("rom")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    d = parse(a.rom)
    if a.json:
        print(json.dumps(d, indent=2)); return 0
    print(f"file       {d['file']}")
    print(f"format     {d['format']}")
    print(f"mapper     {d['mapper']}")
    print(f"PRG        {d['prg_bytes']} bytes ({d['prg_kb']} KB)")
    print(f"CHR        {d['chr_bytes']} bytes ({d['chr_kb']} KB)")
    print(f"mirroring  {d['mirroring']}")
    print(f"battery    {d['battery']}")
    print(f"trainer    {d['trainer']}")
    print(f"SHA-1      {d['sha1']}")
    print(f"SHA-256    {d['sha256']}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
