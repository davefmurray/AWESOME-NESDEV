# Music Channels: Hex Guide

**Source:** https://tecmobowl.org/forums/topic/9849-tsb-music-info/  
**Category:** MUSIC → TSB Music  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/9849-tsb-music-info/).

## Summary

Here is a simple test song for those having problems (the commas in the hex below are just to help those see some breakup of the parts and notes). I'll find my notes and answer some of the questions in this thread soon. POP GOES THE WEASEL: (Put at x3A155 and play sound 4 on the sound test screen)

## Key facts

- $A145: (SET SONG DATA POINTERS)
- 04 52A1, 05 90A1, 06 20A2, 07 20A2, FF
- $A152: (SET SQUARE 1 VARIABLES)
- $A158: (SQUARE 1 MUSIC)
- E9 77A1, 8E 20, 88 20, 8E 22, 88 22, 92 24, 92 20, E9 77A1, 92 29, 8E 22, 88 25, 92 24, 92 20, E8 58A1
- $A177: (COMMON MELODY)
- $A186: (FILLER)
- $A190: (SET SQUARE 2 VARIABLES)
- $A196: (SQUARE 2 MUSIC)
- $A1F8: (COMMON MELODY)
- $A1FF: (COMMON MELODY)
- $A206: (COMMON MELODY)

## Topics

`sim`, `sound`, `music`, `pointer`

## Source

<https://tecmobowl.org/forums/topic/9849-tsb-music-info/>
