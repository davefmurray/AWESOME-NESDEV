# Condition Change Every Play

**Source:** https://tecmobowl.org/forums/topic/10222-player-conditions-change-more/  
**Category:** GAMEPLAY → Player Attributes During Gameplay  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/10222-player-conditions-change-more/).

## Summary

> On 10/7/2008 at 3:44 PM, jstout said: > > Buck, I was able to squeeze this into cxrom's 32 team rom in the general area you wanted. Let me know if this don't fit on your copy. > > You can place code anywhere in the game (multiple FFs are almost always unused areas) as long as you can write code there without writing over something else and you are able to get the area loaded when it is needed ($8000-$9000 and $A000-$B000 are swappable and $C000-$FFFF is fixed). > > ``` > x25AE9: > 4C F3 9F JMP $9FF3 > EA NOP > EA NOP > EA NOP > EA NOP > > x25FFB: > ; RETURN TO NORMAL CODE: > A5 70 LDA $0070 > 10 0E BPL :+ > 4C 3E 9C JMP $9C3E > ; UNUSED FILLER BYTE > FF > ; CHANGE $8000 BANK TO NEW CODE > A9 06 LDA #$06 > 8D 00 80 STA $8000 > A9 18 LDA #$18 > 8D 01 80 STA $8001 > ; SQUEEZING IN PART…

## Key facts

- > On 10/7/2008 at 3:44 PM, jstout said:
- > Buck, I was able to squeeze this into cxrom's 32 team rom in the general area you wanted. Let me know if this don't fit on your copy.
- > 4C F3 9F   JMP $9FF3
- > A5 70      LDA $0070
- > 4C 3E 9C   JMP $9C3E
- > ; CHANGE $8000 BANK TO NEW CODE
- > A9 06      LDA #$06
- > 8D 00 80   STA $8000
- > A9 18      LDA #$18
- > 8D 01 80   STA $8001
- > 4C E0 9A : JMP $9AE0
- > 4C CA 9F   JMP $9FCA

## Source

<https://tecmobowl.org/forums/topic/10222-player-conditions-change-more/>
