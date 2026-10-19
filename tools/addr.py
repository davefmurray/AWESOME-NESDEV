#!/usr/bin/env python3
"""Convert between iNES file offsets and 6502 CPU addresses.

Flat NROM is safe. Banked carts are not: only the fixed window is unambiguous,
and a switchable address is meaningless without the live bank number. This tool
refuses to guess for non-zero mappers unless you pass the bank explicitly.

Examples:
    python3 tools/addr.py --offset 0x10 --mapper 0 --prg-kb 32
    python3 tools/addr.py --cpu 0x8000 --mapper 0 --prg-kb 32
    python3 tools/addr.py --offset 0x4010 --mapper 4 \
        --bank-size 8192 --bank-index 2 --bank-base 0x8000
"""

from __future__ import annotations

import argparse
import sys


def num(s: str) -> int:
    return int(s, 0)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--offset", type=num, help="file offset in the .nes")
    src.add_argument("--cpu", type=num, help="6502 address, e.g. 0x8123")
    ap.add_argument("--mapper", type=int, default=0)
    ap.add_argument("--prg-kb", type=int, choices=(16, 32), default=32,
                    help="NROM only: 32 KB at $8000 or 16 KB at $C000")
    ap.add_argument("--bank-size", type=num, help="banked: bank size in bytes")
    ap.add_argument("--bank-index", type=int, help="banked: which bank is switched in")
    ap.add_argument("--bank-base", type=num, help="banked: CPU window base, e.g. 0x8000")
    args = ap.parse_args(argv)

    if args.mapper == 0:
        base = 0x8000 if args.prg_kb == 32 else 0xC000
        span = args.prg_kb * 1024
        if args.offset is not None:
            rel = args.offset - 16
            if not (0 <= rel < span):
                print(f"error: offset 0x{args.offset:X} outside NROM PRG "
                      f"(0x10..0x{16 + span - 1:X})", file=sys.stderr)
                return 1
            cpu = base + rel
            print(f"file 0x{args.offset:06X}  ->  CPU ${cpu:04X}   "
                  f"(NROM {args.prg_kb} KB, bank 0)")
        else:
            rel = args.cpu - base
            if not (0 <= rel < span):
                print(f"error: ${args.cpu:04X} outside ${base:04X}..${base + span - 1:04X}",
                      file=sys.stderr)
                return 1
            print(f"CPU ${args.cpu:04X}  ->  file 0x{rel + 16:06X}   "
                  f"(NROM {args.prg_kb} KB, bank 0)")
        return 0

    missing = [n for n, v in (("--bank-size", args.bank_size),
                              ("--bank-index", args.bank_index),
                              ("--bank-base", args.bank_base)) if v is None]
    if missing:
        print(f"error: mapper {args.mapper} is banked; pass {', '.join(missing)}.\n"
              "       The address is only valid while that bank is switched in.",
              file=sys.stderr)
        return 1

    start = 16 + args.bank_index * args.bank_size
    if args.offset is not None:
        rel = args.offset - start
        if not (0 <= rel < args.bank_size):
            print(f"error: offset 0x{args.offset:X} is not in bank {args.bank_index} "
                  f"(file 0x{start:X}..0x{start + args.bank_size - 1:X})", file=sys.stderr)
            return 1
        print(f"file 0x{args.offset:06X}  ->  CPU ${args.bank_base + rel:04X}   "
              f"(mapper {args.mapper}, bank {args.bank_index})")
    else:
        rel = args.cpu - args.bank_base
        if not (0 <= rel < args.bank_size):
            print(f"error: ${args.cpu:04X} outside window "
                  f"${args.bank_base:04X}..${args.bank_base + args.bank_size - 1:04X}",
                  file=sys.stderr)
            return 1
        print(f"CPU ${args.cpu:04X}  ->  file 0x{start + rel:06X}   "
              f"(mapper {args.mapper}, bank {args.bank_index})")
    print("warning: banked mapping — record the bank number with the address.",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
