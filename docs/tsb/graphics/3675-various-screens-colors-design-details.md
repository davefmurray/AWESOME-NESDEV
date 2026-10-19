# Various Screens: Colors / Design Details

**Source:** https://tecmobowl.org/forums/topic/3675-a-guide-for-changing-nes-tsb-background-palettes/  
**Category:** GRAPHICS → Background & Design Palettes, Cut Scene Colors  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/3675-a-guide-for-changing-nes-tsb-background-palettes/).

## Summary

Okay, this is long overdue i feel, but i'll give the locations of some major background palettes to everyone, and a brief guide on to which values to change. I hope everyone can understand this. Are you sick of the same old ugly Light Blue Tecmo backgrounds on the main menu? Or the dumb Pink they use all over the place? Well this guide is here to help.

## Key facts

- Okay, this is long overdue i feel, but i'll give the locations of some major background palettes to everyone, and a brief guide on to which values to change. I hope everyone can understand this.
- *BE CAREFUL CHANGING ANY WHITE PALETTE TILES, DOING SO MAY CHANGE THE TEXT COLOR, AND LOCK THE GAME UP, SO USE CAUTION WHEN CHANGING WHITE COLORS.**
- *ANY CHANGES MADE USING THESE METHODS ARE PERMANANT, NO EXTRA PALETTE FILES ARE NEEDED WHEN USING THESE METHODS!**
- Okay first we'll change the Main Menu Screens, here are the offsets for those....
- 0x1A140 - 0x1A14F
- 0x1A850 - 0x1A85F
- For the Pink Tecmo Letters and Year Numbers on the Main Menu Screens, just change the value at offset x1A147 and there you go.
- For the NFL logo, there is multiple positions for the Blue in the NFL logo, the Red is located at offset x1A856, and the blue is located at the following offsets....
- These screens are all linked to one palette, mainly because they all display the tecmo mini-helmets, so it just takes up les room to have only one set pallete for all backgrounds and mini-helmets.
- Here are the offsets for these screens....
- 0x1A150 - 0x1A15F
- 0x1A840 - 0x1A84F

## Topics

`palette`, `helmet`, `logo`, `tile`, `playbook`, `roster`, `attribute`, `schedule`

## Source

<https://tecmobowl.org/forums/topic/3675-a-guide-for-changing-nes-tsb-background-palettes/>
