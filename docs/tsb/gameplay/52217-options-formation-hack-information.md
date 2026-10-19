# Options Formation Hack Information

**Source:** https://tecmobowl.org/topic/52217-a-button-to-cancel-handoff-and-a-to-pitch-along-a-path/  
**Category:** GAMEPLAY → Player Movement, Positioning  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/52217-a-button-to-cancel-handoff-and-a-to-pitch-along-a-path/).

## Summary

D4D8FCD852D800C0D810B0FF32B8D830E8D83028FD0D40FCFFE0CEE850FFE8BEF314D804CCD8E8D8E4C8DDAE Is this the QB and RB/WR code? If so, why is there a D4 command (taking the snap at center) as against a D5 command?

## Key facts

- I got this from FCEUX @8ea5:
- What are the 32b8, 3cbe, 38b8 and 4ebe commands doing?
- What specifically tells the QB to pitch (or A-to-cancel) here? Is that the (ff) 32 b8 command? If so, was the code at b842 altered?
- There was also this @84d7: D5CAD8A4FD0100CBDC2401DE0001FF
- *Edited January 2, 201313 yr by quince3800**
- > For cancelling a handoff from the Xplozv rom @84d7 I got:
- > CA:  man/computer to pointer... a4 c8 (?)
- > (a4 c8 looks like a defensive command:  C8F450FFADAAD00018ECF30AD8F8D8F414D810F8F428D81018D80C2CFFADAA; before that @a4c5 is d0 d8 e8, which looks like defensive presnap code)
- > What differentiates this line of code from the (option) pitch given earlier?
- 1. You aren't handling the NES banking properly (in the offensive play code $A000-$BFFF = x8010-xA00F).  So, CA D8 A4 doesn't go to xA4C8 it goes to x84E8 (E2 06 | FE F1).
- the next two bytes in the FD are selecting which players to pitch away from in a bitwise fashion
- (Player) = bits from QB to RT or RE to SS (0 = not set to 1 = set)

## Source

<https://tecmobowl.org/topic/52217-a-button-to-cancel-handoff-and-a-to-pitch-along-a-path/>
