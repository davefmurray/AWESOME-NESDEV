# Turn off sprite flickering needed for the hardware sprite limit

**Source:** https://tecmobowl.org/forum/topic/68629-no-sprite-flicker-rom-and-15-sprite-per-scanline-rom-for-avs  
**Category:** GRAPHICS → Background & Design Palettes, Cut Scene Colors  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forum/topic/68629-no-sprite-flicker-rom-and-15-sprite-per-scanline-rom-for-avs).

## Summary

These are only meant to be used in hardware or emulators that can take advantage of the no sprite flickering. This rom completely removes sprite flickering with the following patch

## Key facts

- This rom completely removes sprite flickering with the following patch
- *SET(0x2d04C, 0xA901209ACC4C3C90)**
- [TSB\_no\_sprite\_flicker.nes](https://tecmobowl.org/applications/core/interface/file/attachment.php?id=25720)
- This patch changes the check from 8 sprites per scanline to 15. You could also use this in nestopia as with the above using the no sprite limit option to see how much of an improvement it makes (A LOT).
- SET(0x2D14E,0x10)
- SET(0x2D174,0x10)
- SET(0x2D19A,0x10)
- SET(0x2D1C0,0x10)
- [TSB\_sprite\_limit\_15.nes](https://tecmobowl.org/applications/core/interface/file/attachment.php?id=27565&key=bec03e9d3043fb8f0967a88058f31e73)
- > This rom completely removes sprite flickering with the following patch
- > **SET(0x2d04C, 0xA901209ACC4C3C90)**
- > [TSB\_no\_sprite\_flicker.nes](https://tecmobowl.org/applications/core/interface/file/attachment.php?id=15337)

## Topics

`face`, `sprite`

## Source

<https://tecmobowl.org/forum/topic/68629-no-sprite-flicker-rom-and-15-sprite-per-scanline-rom-for-avs>
