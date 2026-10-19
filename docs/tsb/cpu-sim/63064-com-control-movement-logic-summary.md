# COM Control Movement Logic Summary

**Source:** https://tecmobowl.org/topic/63064-com-takes-control-movement-logic-summary/  
**Category:** CPU & SIM → Attributes, Play Ratio, SIM Stats  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/63064-com-takes-control-movement-logic-summary/).

## Summary

It works, I like it! Here's some set commands for the hex editing challenged: ``` #CPU angles to the sidelines if there's no defenders in front of them #https://tecmobowl.org/forums/topic/63064-com-takes-control-movement-logic-summary/#findComment-517413 SET(0x28F68, 0x78) SET(0x28F6D, 0x88) SET(0x28FCF, 0x08) SET(0x28FD4, 0xF8)

## Key facts

- SET(0x28F68, 0x78)
- SET(0x28F6D, 0x88)
- SET(0x28FCF, 0x08)
- SET(0x28FD4, 0xF8)
- SET(0x28F68, 0x80)
- SET(0x28F6D, 0x80)
- SET(0x28FCF, 0x00)
- SET(0x28FD4, 0x00)
- cool.  to be clear, this info is related to the **DF** in FCFFE0**DF**FEFC, for example?
- *Edited December 10, 201411 yr by buck**
- I tried to make the changes to a unmodified rom and the game crashed:[Tecmo Super Bowl (USA).nes](https://tecmobowl.org/applications/core/interface/file/attachment.php?id=30247&key=4100f704a7ab2d599c137f8addb2351e)

## Source

<https://tecmobowl.org/topic/63064-com-takes-control-movement-logic-summary/>
