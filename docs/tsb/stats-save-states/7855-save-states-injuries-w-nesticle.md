# Save States & Injuries w/ Nesticle

**Source:** https://tecmobowl.org/forums/topic/7855-nesticle-save-state-format/  
**Category:** STATS & SAVE STATES → Tackles & Injuries  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/7855-nesticle-save-state-format/).

## Summary

The Nesticle Save State Format Documentation from Goroh lists: ``` x0000 (x2000) Extend RAM Dump x2000 (x0800) Static RAM Dump x2800 (x0002) Current reg PC x2802 (x0001) Current reg A x2803 (x0001) Current reg S SO-BDIZC |||||||+ Carry flag ||||||+- Zero flag |||||+-- Interrupt flag ||||+--- Decimal mode flag |||+---- BRK flag ||+----- 0 |+------ Overflow flag +------- Sign flag x2804 (x0001) Current reg X x2805 (x0001) Current reg Y x2806 (x0001) Current reg SP x2807 (x0100) Sprite Setting (unknown fill #$00) x2907 (x4000) PPU-RAM Dump x0000 Pattern Table Dump (if chr-bank size=0, else fill #$00) x2000 NameTable & Attribute Dump x5907 (x00c9) Other Setting x0077 Current H,V setting 0:H 1:V ```

## Key facts

- The Nesticle Save State Format Documentation from Goroh lists:
- x2807 (x0100) Sprite Setting (unknown fill #$00)
- x2907 (x4000) PPU-RAM Dump
- x0000  Pattern Table Dump (if chr-bank size=0, else fill #$00)
- The Nesticle info for injuries and conditions in the save state (STA) comes from the RAM section of the game (x6000 to x7FFF during play).

## Topics

`CHR`, `attribute`, `sprite`

## Source

<https://tecmobowl.org/forums/topic/7855-nesticle-save-state-format/>
