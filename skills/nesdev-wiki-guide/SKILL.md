---
name: nesdev-wiki-guide
description: "Route NES/Famicom questions to the authoritative NESdev Wiki page and extract the answer. Use when researching NES hardware, PPU/APU behavior, mappers, ROM formats, timing, controllers, or when a claim about the NES needs a primary source."
---

# NESdev Wiki guide

The NESdev Wiki is the primary source for NES hardware behavior. Use this skill to find the right page before answering from memory — especially for register bits, timing, mapper behavior, and file formats, where a wrong detail propagates into code.

## When to use

- Any NES/Famicom hardware question.
- A ROM's header, mapper, or banking needs identification.
- PPU/APU behavior is unclear or contested.
- You need a primary source for a claim, or a test ROM.

## Canonical access

- Page: `https://www.nesdev.org/wiki/<Page_Name>`
- Raw wikitext (MediaWiki API):
  `https://www.nesdev.org/w/api.php?action=parse&page=<Page_Name>&prop=wikitext&format=json&formatversion=2`
- Search:
  `https://www.nesdev.org/w/api.php?action=query&list=search&srsearch=<terms>&format=json`

Use underscores or spaces; page titles are case-sensitive on the first letter only. `iNES` is stored as `INES`.

## Topic map

| Question | Page |
|---|---|
| CPU address space, mirrors, vectors | `CPU memory map` |
| PPU address space, palettes, OAM | `PPU memory map` |
| Register bitfields | `PPU registers`, `Registers` |
| Power-on/reset state | `PPU power up state`, `CPU power up state` |
| PPU rendering, sprites, scrolling | `PPU`, `PPU OAM`, `PPU scrolling`, `PPU palettes` |
| Nametable/attribute layout | `PPU nametables`, `PPU attribute tables` |
| Frame timing, NMI | `The frame and NMIs`, `Cycle reference chart` |
| Cartridge header | `INES`, `NES 2.0`, `Nintendo header` |
| Mapper behavior | `Mapper`, `MMC1`, `MMC3`, `UxROM`, `Programming MMC1`, `Programming MMC3` |
| APU channels and registers | `APU`, `APU Pulse`, `APU Triangle`, `APU Noise`, `APU DMC` |
| APU timing/envelopes | `APU Frame Counter`, `APU Envelope`, `APU Length Counter`, `APU Sweep` |
| Controllers | `Controller reading`, `Standard controller`, `Input devices` |
| 6502 | `Instruction reference`, `CPU unofficial opcodes`, `6502 cycle times` |
| Test ROMs | `Emulator tests`, `Category:Test ROMs` |
| Tools/emulators | `Tools`, `Emulators` |

Full page index with the pages this skill set was distilled from: `references/page-index.md`.

## Procedure

1. **Classify** the question: CPU, PPU, APU, cartridge, input, timing, or tooling.
2. **Open the most specific page**, not the overview. `PPU registers` beats `PPU`.
3. **Read the bitfield table**, not a summary. Register bit order is the usual source of bugs.
4. **Check errata** for hardware quirks: `Errata`, `CPU interrupts`, `Open bus behavior`.
5. **Cite the page** in your answer, with the section anchor when useful.
6. If the wiki is ambiguous or the behavior is revision-dependent, say so and prefer a test ROM.

## Rules

- Do not invent register bits or cycle counts. If the page does not say it, say "not documented here".
- The wiki uses both US and UK spellings (`optimisations`, `mirroring`); redirects exist, but the API needs the real title.
- Tables on the wiki are community-maintained. For a disputed behavior, check the talk page or forums.
- Distinguish NTSC / PAL / Dendy; many values differ.
- Distinguish stock hardware from famiclones and flash carts.

## Output shape

When answering, give:

1. The fact, in one or two sentences.
2. The register/address or formula.
3. The source page link.
4. The caveat that matters (revision, region, mapper).

## References

- `references/page-index.md` — grouped index of the 64 pages used to build these skills.
- [NESdev Wiki](https://www.nesdev.org/wiki/) · [Reference guide](https://www.nesdev.org/wiki/NES_reference_guide) · [Programming guide](https://www.nesdev.org/wiki/Programming_guide)
