# CPU RAM and MMC3 General Locations

**Source:** https://tecmobowl.org/topic/53074-nes-ram-and-mmc3-layout-and-registers/  
**Category:** GENERAL INFO  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/53074-nes-ram-and-mmc3-layout-and-registers/).

## Summary

Some general infro from CXROM regarding NES ram layout and registers I think you are confusing the cpu addressing space with the actual rom addresses. so here is a better explanation:

## Key facts

- Some general infro from CXROM regarding NES ram layout and registers
- I think you are confusing the cpu addressing space with the actual rom addresses. so here is a better explanation:
- PPU = Picture Processing Unit
- the NES has a 16-bit PC which holds the address of the next instruction to be executed. with a 16-bit PC you can only address $0000-$FFFF. here is a break-down of what is what in CPU address space.
- $0000-$07FF: RAM
- $0800-$1FFF: Mirror of RAM
- $2000-$2007: PPU registers
- $2008-$3FFF: Mirror of PPU registers
- $4000-$4017: APU registers/sprite DMA register/controller port registers
- $4018-$5FFF: for TSB, there is nothing here
- $6000-$7FFF: SRAM
- $8000-$9FFF: prg bank 1

## Topics

`CHR`, `sprite`

## Source

<https://tecmobowl.org/topic/53074-nes-ram-and-mmc3-layout-and-registers/>
