# TSB Stats Code

**Source:** https://tecmobowl.org/topic/10280-stats-code-nes/  
**Category:** STATS & SAVE STATES → Stats  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/10280-stats-code-nes/).

## Summary

so i started diggin around for the stat code and found some of it. i'm not sure what each bit does but it looks pretty straigtforward. this code modfies the temp stats that are in-game, not the season stats. this portion jumps somewhere based on the player and stat being updated

## Key facts

- $B582:8A        TXA
- $B583:0A        ASL
- $B584:A8        TAY
- $B585:B9 63 AC  LDA $AC63,Y
- $B588:85 3E     STA $3E
- $B58A:B9 64 AC  LDA $AC64,Y
- $B58D:85 3F     STA $3F
- $B58F:A9 80     LDA #$80
- $B591:8D 01 A0  STA $A001
- $B594:6C 3E 00  JMP ($003E)
- $B597:A0 00     LDY #$00
- $B599:4C 46 B6  JMP $B646

## Source

<https://tecmobowl.org/topic/10280-stats-code-nes/>
