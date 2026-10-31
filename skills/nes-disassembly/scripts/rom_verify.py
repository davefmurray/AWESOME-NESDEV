#!/usr/bin/env python3
"""Compare an original ROM with a rebuilt ROM.

    python3 rom_verify.py original.nes rebuilt.nes
    python3 rom_verify.py original.nes rebuilt.nes --bank-kb 8 --json
"""

from __future__ import annotations
import argparse, hashlib, json, sys

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("original")
    ap.add_argument("rebuilt")
    ap.add_argument("--bank-kb", type=int, default=8)
    ap.add_argument("--max-ranges", type=int, default=20)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    x = open(a.original, "rb").read(); y = open(a.rebuilt, "rb").read()
    same_size = len(x) == len(y)
    diffs = [i for i, (p, q) in enumerate(zip(x, y)) if p != q]
    if len(x) != len(y):
        diffs += list(range(min(len(x), len(y)), max(len(x), len(y))))
    ranges = []
    if diffs:
        start = prev = diffs[0]
        for i in diffs[1:]:
            if i == prev + 1: prev = i; continue
            ranges.append((start, prev + 1)); start = prev = i
        ranges.append((start, prev + 1))
    out = {
        "original": a.original, "rebuilt": a.rebuilt,
        "original_size": len(x), "rebuilt_size": len(y), "same_size": same_size,
        "original_sha1": hashlib.sha1(x).hexdigest().upper(),
        "rebuilt_sha1": hashlib.sha1(y).hexdigest().upper(),
        "same_sha1": hashlib.sha1(x).digest() == hashlib.sha1(y).digest(),
        "diff_bytes": len(diffs), "diff_ranges": len(ranges),
        "first_diff": diffs[0] if diffs else None,
        "ranges": [{"offset": s, "length": e - s} for s, e in ranges[:a.max_ranges]],
    }
    if a.json:
        print(json.dumps(out, indent=2)); return 0 if not diffs and same_size else 1
    print(f"original  {len(x)} bytes  {out['original_sha1']}")
    print(f"rebuilt   {len(y)} bytes  {out['rebuilt_sha1']}")
    if out["same_sha1"] and same_size:
        print("MATCH: byte-identical")
        return 0
    print(f"DIFF: {len(diffs)} bytes in {len(ranges)} ranges")
    if diffs: print(f"first diff at 0x{diffs[0]:06X}")
    for r in ranges[:a.max_ranges]:
        print(f"  0x{r[0]:06X}-0x{r[1]-1:06X}  {r[1]-r[0]} bytes")
    if len(ranges) > a.max_ranges: print(f"  ... {len(ranges)-a.max_ranges} more")
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
