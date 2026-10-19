#!/usr/bin/env python3
"""Summarise and merge CDL (Code/Data Log) files.

FCEUX-style default: code = bit 0, data = bit 1. If your emulator uses a
different mapping, pass --code-bit / --data-bit. Verify one known code address
before trusting a merged map.

Examples:
    python3 tools/cdl_stats.py work/lws.cdl --rom roms/lws.nes
    python3 tools/cdl_stats.py work/boot.cdl work/play.cdl --merge --rom roms/lws.nes
    python3 tools/cdl_stats.py work/lws.cdl --prg-size 0x20000 --json
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from nes_header import parse as parse_header  # noqa: E402


def num(s: str) -> int:
    return int(s, 0)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cdl", nargs="+", help="one or more .cdl files")
    ap.add_argument("--rom", help="derive PRG size from this ROM header")
    ap.add_argument("--prg-size", type=num, help="PRG size in bytes, if no --rom")
    ap.add_argument("--merge", action="store_true", help="OR multiple logs together")
    ap.add_argument("--code-bit", type=int, default=0)
    ap.add_argument("--data-bit", type=int, default=1)
    ap.add_argument("--page-kb", type=int, default=16, help="page size for the table")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    if args.rom:
        info = parse_header(args.rom)
        prg = info["prg_bytes"]
        if prg is None:
            print("error: NES 2.0 exponent PRG size — pass --prg-size", file=sys.stderr)
            return 1
    elif args.prg_size:
        prg = args.prg_size
    else:
        print("error: pass --rom or --prg-size", file=sys.stderr)
        return 1

    blobs = []
    for path in args.cdl:
        data = open(path, "rb").read()
        if len(data) != prg:
            print(f"error: {path} is {len(data)} bytes, PRG is {prg} "
                  f"(CDL maps PRG bytes, not the 16-byte header)", file=sys.stderr)
            return 1
        blobs.append(data)
    if len(blobs) > 1 and not args.merge:
        print("error: multiple logs need --merge", file=sys.stderr)
        return 1

    merged = bytearray(blobs[0])
    for blob in blobs[1:]:
        for i, b in enumerate(blob):
            merged[i] |= b

    cb = 1 << args.code_bit
    db = 1 << args.data_bit
    code = data_ = both = neither = 0
    for b in merged:
        c, d = bool(b & cb), bool(b & db)
        code += c
        data_ += d
        both += c and d
        neither += not c and not d

    page = args.page_kb * 1024
    pages = []
    for start in range(0, prg, page):
        chunk = merged[start:start + page]
        c = sum(1 for b in chunk if b & cb)
        d = sum(1 for b in chunk if b & db)
        pages.append({
            "file_offset": 16 + start,
            "code": c,
            "data": d,
            "code_pct": round(100 * c / len(chunk), 1) if chunk else 0,
        })

    summary = {
        "prg_bytes": prg,
        "logs": args.cdl,
        "merged": len(blobs) > 1,
        "code_bytes": code,
        "data_bytes": data_,
        "both": both,
        "neither": neither,
        "code_pct": round(100 * code / prg, 1),
        "data_pct": round(100 * data_ / prg, 1),
        "pages": pages,
    }

    if args.json:
        print(json.dumps(summary, indent=2))
        return 0

    print(f"PRG         {prg} bytes ({prg // 1024} KB)")
    print(f"logs        {len(args.cdl)}" + (" (merged)" if len(blobs) > 1 else ""))
    print(f"code        {code} bytes ({summary['code_pct']}%)")
    print(f"data        {data_} bytes ({summary['data_pct']}%)")
    print(f"both        {both} bytes")
    print(f"untouched   {neither} bytes")
    print()
    print(f"{'file off':>10}  {'code':>8}  {'data':>8}  {'code%':>6}")
    for p in pages:
        print(f"0x{p['file_offset']:08X}  {p['code']:8d}  {p['data']:8d}  {p['code_pct']:6.1f}")
    print()
    print("note: code% is of the page; pages with 0% may simply be unvisited.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
