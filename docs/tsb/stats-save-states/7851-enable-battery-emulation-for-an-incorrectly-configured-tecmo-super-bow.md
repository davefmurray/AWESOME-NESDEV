# Enable Battery emulation for an incorrectly configured Tecmo Super Bowl rom

**Source:** https://tecmobowl.org/forums/topic/7851-season-doesnt-save/  
**Category:** STATS & SAVE STATES → Stats  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/7851-season-doesnt-save/).

## Summary

> just curious, don't really need this info because save state serves the same purpose, but does anyone know why sometimes your game will save by itself and other times it won't? NES games have different "mappers" (how the game is setup on circuit boards allowing different functions), different bank sizes, and not all have saving (like Mario Brothers). So to let the emulator understand what the game is allowed to do and where the information is it has a x10 size header at the beginning of the rom. One of the bytes in the rom tells the emulator whether or not the game has SRAM (saving ability). It is quite common to see a TSB rom with the SRAM disabled in the header causing the emulator not to save afterwards.

## Key facts

- TSB roms that don't save likely have a 40 instead of 42 meaning that the emulator is told to use mapper #4 and to use horizontal mirroring while SRAM is turned off.
- Just to put a bow on this topic, most Tecmo Roms should save your progress in the same manner as in real life: if you play a game then turn the emulator on/off or reset, that result will be remembered.
- SET(0x06, 0x42)

## Topics

`formation`, `sim`

## Source

<https://tecmobowl.org/forums/topic/7851-season-doesnt-save/>
