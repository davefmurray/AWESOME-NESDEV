#!/usr/bin/env python3
"""Parse an iNES / NES 2.0 header without trusting the file extension.

Usage:
    python3 tools/nes_header.py roms/lws.nes
    python3 tools/nes_header.py roms/lws.nes --json > work/header.json

Exit codes: 0 ok, 1 not a ROM / unreadable.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import zlib

MAGIC = b"NES\x1a"

MAPPER_NAMES = {
    0: "NROM",
    1: "MMC1",
    2: "UxROM",
    3: "CNROM",
    4: "MMC3",
    5: "MMC5",
    7: "AxROM",
    9: "MMC2",
    10: "MMC4",
    66: "GxROM",
    69: "Sunsoft FME-7",
    71: "Camerica",
}

CONSOLE_NAMES = {0: "NES / Famicom", 1: "Vs. System", 2: "PlayChoice-10", 3: "Extended"}


def ram_size(nibble: int) -> int:
    """NES 2.0 RAM size: 0 = none, otherwise 64 << value bytes."""
    return 0 if nibble == 0 else 64 << nibble


def parse(path: str) -> dict:
    size = os.path.getsize(path)
    with open(path, "rb") as fh:
        raw = fh.read()

    if len(raw) < 16:
        raise ValueError(f"{path}: too short ({len(raw)} bytes)")
    if raw[:4] != MAGIC:
        raise ValueError(
            f"{path}: not iNES/NES 2.0 (magic {raw[:4]!r}, expected {MAGIC!r})"
        )

    h = raw[:16]
    flags6, flags7 = h[6], h[7]
    nes2 = (flags7 & 0x0C) == 0x08

    prg_units, chr_units = h[4], h[5]
    exponent_prg = nes2 and prg_units == 0x0F
    exponent_chr = nes2 and chr_units == 0x0F

    prg_size = None if exponent_prg else prg_units * 16384
    chr_size = None if exponent_chr else chr_units * 8192

    mapper = (flags7 & 0xF0) | (flags6 >> 4)
    submapper = None
    prg_ram = nvram = chr_ram = None
    tv = None

    if nes2:
        mapper |= (h[8] & 0x0F) << 8
        submapper = h[8] >> 4
        prg_ram = ram_size(h[10] & 0x0F)
        nvram = ram_size(h[10] >> 4)
        chr_ram = ram_size(h[11] & 0x0F)
        tv_bits = h[12] & 0x03
        tv = {0: "NTSC", 1: "PAL", 2: "dual", 3: "Dendy"}.get(tv_bits, "unknown")
    else:
        prg_ram = h[8] * 8192
        tv = "PAL" if (h[9] & 0x01) else "NTSC"

    battery = bool(flags6 & 0x02)
    trainer = bool(flags6 & 0x04)
    four_screen = bool(flags6 & 0x08)
    mirroring = "four-screen" if four_screen else ("vertical" if (flags6 & 0x01) else "horizontal")

    expected = 16 + (512 if trainer else 0) + (prg_size or 0) + (chr_size or 0)
    trailing = size - expected

    warnings = []
    if exponent_prg or exponent_chr:
        warnings.append("NES 2.0 exponent size form (0x0F) — size not decoded")
    if trailing:
        warnings.append(f"{trailing} trailing byte(s) after PRG+CHR")
    if mapper not in MAPPER_NAMES:
        warnings.append(f"mapper {mapper} not in the local name table")
    if chr_size == 0 and not (nes2 and chr_ram):
        warnings.append("CHR size 0 — treat as CHR-RAM unless the mapper says otherwise")

    return {
        "file": os.path.abspath(path),
        "file_size": size,
        "format": "NES 2.0" if nes2 else "iNES",
        "mapper": mapper,
        "mapper_name": MAPPER_NAMES.get(mapper, "unknown"),
        "submapper": submapper,
        "prg_bytes": prg_size,
        "prg_kb": None if prg_size is None else prg_size // 1024,
        "chr_bytes": chr_size,
        "chr_kb": None if chr_size is None else chr_size // 1024,
        "chr_ram_bytes": chr_ram,
        "chr_is_ram": chr_size == 0,
        "mirroring": mirroring,
        "battery": battery,
        "trainer": trainer,
        "console_type": CONSOLE_NAMES.get(flags7 & 0x03, "unknown"),
        "tv_system": tv,
        "prg_ram_bytes": prg_ram,
        "prg_nvram_bytes": nvram,
        "expected_size": expected,
        "trailing_bytes": trailing,
        "warnings": warnings,
        "hashes": {
            "crc32": f"{zlib.crc32(raw) & 0xFFFFFFFF:08x}",
            "md5": hashlib.md5(raw).hexdigest(),
            "sha1": hashlib.sha1(raw).hexdigest(),
            "sha256": hashlib.sha256(raw).hexdigest(),
        },
    }


def human(info: dict) -> str:
    def kb(n):
        return "?" if n is None else f"{n // 1024} KB ({n} bytes)"

    lines = [
        f"file        {info['file']}",
        f"size        {info['file_size']} bytes",
        f"format      {info['format']}",
        f"mapper      {info['mapper']} ({info['mapper_name']})"
        + (f" submapper {info['submapper']}" if info["submapper"] is not None else ""),
        f"PRG         {kb(info['prg_bytes'])}",
        f"CHR         {kb(info['chr_bytes'])}" + ("  [CHR-RAM]" if info["chr_is_ram"] else ""),
        f"mirroring   {info['mirroring']}",
        f"battery     {'yes' if info['battery'] else 'no'}",
        f"trainer     {'yes' if info['trainer'] else 'no'}",
        f"console     {info['console_type']}",
        f"TV system   {info['tv_system']}",
        f"PRG RAM     {info['prg_ram_bytes']} bytes",
        f"PRG NVRAM   {'n/a' if info['prg_nvram_bytes'] is None else str(info['prg_nvram_bytes']) + ' bytes'}",
        f"CRC32       {info['hashes']['crc32']}",
        f"SHA-256     {info['hashes']['sha256']}",
    ]
    if info["warnings"]:
        lines.append("warnings    " + "; ".join(info["warnings"]))
    return "\n".join(lines)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("rom")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args(argv)

    try:
        info = parse(args.rom)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(info, indent=2) if args.json else human(info))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
