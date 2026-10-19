# Offensive Playbook Design Guide

**Source:** https://tecmobowl.org/forums/topic/10528-nes-play-design-info/  
**Category:** PLAYBOOK → Play Code, Pointers, Data Tables  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/10528-nes-play-design-info/).

## Summary

Offensive Plays: x1D410 to x1DA0F (15 bytes for name, formation #, 8 bytes of play #s) Example: T FAKE SWEEP R 04 10 10 50 10 10 50 10 10, 04 = formation # and 10 and 50 are the play #s

## Key facts

- Offensive Formation Pointers: x4010 to x41F3 (Each formation is 11 pointers)
- Offensive Play Pointers: x4410 to x4BF7 (Each play is 11 pointers)
- Offensive Extra Pointers: x4E10 to x4F8F (Each extra is 12 pointers)
- Defensive Play Pointers: x6010 to x75F9 (Each play is 11 pointers)
- Defensive Extra Pointers: x7610 to x778F (Each extra is 12 pointers)
- Offensive Command Section: x8010 to x9F86 ($A000 to $BFFF)
- Defensive Command Section: xA010 to xBFCE ($A000 to $BFFF)
- x20 to x2F = Random (Pointer)
- x91 to x94 = Pass (Chance/Receivers, Pointer)
- xB0 to xB1 = Set Position From Kickoff (Location)
- xC3 = Vs Defense (Defense, Pointer) \*\*\*[Only TSB II and III]
- xC6 = Receiver Order (Amount, Receivers, Pointer) \*\*\*[Only TSB II and III]

## Topics

`face`, `formation`, `kick`, `punt`, `field goal`, `pointer`

## Source

<https://tecmobowl.org/forums/topic/10528-nes-play-design-info/>
