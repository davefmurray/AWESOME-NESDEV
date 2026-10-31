#!/usr/bin/env python3
"""Merge and report FCEUX/Mesen CDL files.

CDL maps PRG bytes only: one byte per PRG byte, no 16-byte iNES header and no
CHR. FCEUX flags: bit0 code, bit1 data, bits2-3 + bit7 data-mapping,
bit4 indirect-jump target, bit5 indirect read, bit6 DPCM sample.

Examples:
    python3 cdl_report.py run1.cdl run2.cdl --merge --rom game.nes --out merged.cdl
    python3 cdl_report.py merged.cdl --prg-size 0x8000 --json
"""

from __future__ import annotations
import argparse, json, sys

def num(s: str) -> int:
    return int(s, 0)

def parse_ines(path: str) -> dict:
    b = open(path, "rb").read()
    if b[:4] != b"NES\x1a":
        raise SystemExit(f"{path}: not an iNES/NES 2.0 file")
    flags6, flags7 = b[6], b[7]
    nes2 = (flags7 & 0x0C) == 0x08
    prg_lo, chr_lo = b[4], b[5]
    if nes2:
        exp = (flags7 & 0x03) << 8 | b[9]
        prg_units = prg_lo | ((b[9] & 0x0F) << 8)
        chr_units = chr_lo | ((b[9] & 0xF0) << 4)
        prg = prg_units * 16384 if exp == 0 else prg_units * (1 << exp)
        chr = chr_units * 8192 if exp == 0 else chr_units * (1 << exp)
    else:
        prg = prg_lo * 16384
        chr = chr_lo * 8192
    mapper = (flags7 & 0xF0) | (flags6 >> 4)
    return {"prg": prg, "chr": chr, "mapper": mapper, "nes2": nes2, "header": 16}

def flag_map(b: int) -> str:
    bits = []
    if b & 0x01: bits.append("C")
    if b & 0x02: bits.append("D")
    if b & 0x02:
        if b & 0x80: bits.append("4")
        else: bits.append(str((b >> 2) & 3))
    if b & 0x10: bits.append("J")
    if b & 0x20: bits.append("I")
    if b & 0x40: bits.append("A")
    return "".join(bits) or "-"

def ranges(buf: bytes, prg: int, min_len: int):
    out = []
    start = None
    for i in range(prg + 1):
        empty = i < prg and buf[i] == 0
        if empty and start is None:
            start = i
        elif not empty and start is not None:
            if i - start >= min_len:
                out.append((start, i))
            start = None
    return out

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cdl", nargs="+")
    ap.add_argument("--rom")
    ap.add_argument("--prg-size", type=num)
    ap.add_argument("--merge", action="store_true")
    ap.add_argument("--out", help="write merged CDL")
    ap.add_argument("--bank-kb", type=int, default=8)
    ap.add_argument("--min-gap", type=int, default=16)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)

    info = parse_ines(a.rom) if a.rom else None
    prg = info["prg"] if info else a.prg_size
    if not prg:
        print("error: pass --rom or --prg-size", file=sys.stderr); return 2

    blobs = []
    for p in a.cdl:
        b = open(p, "rb").read()
        if len(b) != prg:
            print(f"error: {p} is {len(b)} bytes, PRG is {prg}; CDL excludes the 16-byte header and CHR", file=sys.stderr)
            return 2
        blobs.append(b)
    if len(blobs) > 1 and not a.merge:
        print("error: multiple CDLs need --merge", file=sys.stderr); return 2

    m = bytearray(blobs[0])
    for b in blobs[1:]:
        for i, v in enumerate(b): m[i] |= v

    counts = {"code": 0, "data": 0, "both": 0, "neither": 0, "jump": 0, "indirect": 0, "dpcm": 0}
    for b in m:
        c, d = bool(b & 1), bool(b & 2)
        counts["code"] += c; counts["data"] += d
        counts["both"] += c and d; counts["neither"] += not c and not d
        counts["jump"] += bool(b & 0x10); counts["indirect"] += bool(b & 0x20); counts["dpcm"] += bool(b & 0x40)

    bank = a.bank_kb * 1024
    banks = []
    for off in range(0, prg, bank):
        chunk = m[off:off + bank]
        c = sum(1 for b in chunk if b & 1)
        d = sum(1 for b in chunk if b & 2)
        banks.append({"prg_offset": off, "file_offset": 16 + off, "size": len(chunk),
                      "code": c, "data": d,
                      "code_pct": round(100 * c / len(chunk), 1) if chunk else 0,
                      "data_pct": round(100 * d / len(chunk), 1) if chunk else 0})

    gaps = [{"prg_offset": s, "file_offset": 16 + s, "length": e - s} for s, e in ranges(m, prg, a.min_gap)]
    summary = {"rom": a.rom, "prg_bytes": prg, "prg_kb": prg // 1024, "mapper": info["mapper"] if info else None,
               "logs": a.cdl, "merged": len(blobs) > 1, **counts,
               "code_pct": round(100 * counts["code"] / prg, 1),
               "data_pct": round(100 * counts["data"] / prg, 1),
               "banks": banks, "gaps": gaps}

    if a.out:
        open(a.out, "wb").write(m)
        summary["out"] = a.out

    if a.json:
        print(json.dumps(summary, indent=2)); return 0

    print(f"PRG        {prg} bytes ({prg//1024} KB)")
    print(f"logs       {len(blobs)}" + (" (merged)" if len(blobs) > 1 else ""))
    print(f"code       {counts['code']} ({summary['code_pct']}%)")
    print(f"data       {counts['data']} ({summary['data_pct']}%)")
    print(f"both       {counts['both']}   neither {counts['neither']}")
    print(f"J/I/A      {counts['jump']} / {counts['indirect']} / {counts['dpcm']}")
    print()
    print(f"{'bank':>4}  {'file off':>10}  {'code':>8}  {'data':>8}  {'code%':>6}")
    for i, b in enumerate(banks):
        print(f"{i:4d}  0x{b['file_offset']:08X}  {b['code']:8d}  {b['data']:8d}  {b['code_pct']:6.1f}")
    if gaps:
        print("\nuntouched ranges (>= %d bytes):" % a.min_gap)
        for g in gaps[:40]:
            print(f"  PRG 0x{g['prg_offset']:06X}  file 0x{g['file_offset']:06X}  {g['length']} bytes")
        if len(gaps) > 40: print(f"  ... {len(gaps)-40} more")
    print("\nnote: code% is coverage, not truth. Unvisited bytes can be data, unreachable code, or code copied to RAM.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
