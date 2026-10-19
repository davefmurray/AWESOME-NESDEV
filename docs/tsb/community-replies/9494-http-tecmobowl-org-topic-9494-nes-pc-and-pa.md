# NES PC and PA

**Source:** https://tecmobowl.org/forums/topic/9494-nes-pc-and-pa/  
**Category:** Community replies  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/9494-nes-pc-and-pa/).

## Summary

So I finally mostly figured out how the number work. Refer yourself to the byte strings listed below by jstout. The first byte is the chance the pass is on target. It gets compared to a random byte from 00-FF. If its less than the random byte its on target otherwise there is a chance for an underthrow/overthrow

## Key facts

- ex 06 pc @2be14 f7 34 80 80
- The first byte is the chance the pass is on target. It gets compared to a random byte from 00-FF. If its less than the random byte its on target otherwise there is a chance for an underthrow/overthrow
- > SET(0x2be14,0xf7348080)
- > SET(0x2be18,0xee328080)
- > SET(0x2be1c,0xe5308078)
- > SET(0x2be20,0xdc2e8078)
- > SET(0x2be24,0xd32c7870)
- > SET(0x2be28,0xca2a7870)
- > SET(0x2be2c,0xc1287868)
- > SET(0x2be30,0xb8267868)
- > SET(0x2be34,0xaf247060)
- > SET(0x2be38,0xa6227060)

## Source

<https://tecmobowl.org/forums/topic/9494-nes-pc-and-pa/>
