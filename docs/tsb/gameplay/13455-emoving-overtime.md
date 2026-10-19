# emoving Overtime

**Source:** https://tecmobowl.org/forums/topic/13455-editing-overtime  
**Category:** GAMEPLAY → Gameplay Clock, Playbook Clock, Quarter scores  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/13455-editing-overtime).

## Summary

From Jstout via: [http://tecmobowl.org...style-overtime/](https://tecmobowl.org/forum/topic/10427-possession-style-overtime/) > x253BF: > > ; Score is above 99 so adjust (TECMO POOR CODING) > > BCC $93DE ; 2D and sent to the first RTS found > > JMP SCORE\_FIX\_START > > SCORE\_FIX\_START: > > TAX > > LDA #$07 > > STA $8000 > > LDA #$01 > > STA $8001 > > JSR SCORE\_FIX > > LDA #$07 > > STA $8000 > > LDA $002F > > STA $8001 > > ; New Fixed Value > > TXA > > SBC #$10 > > RTS > > SCORE\_FIX: > > LDA $76 > > CMP #$04 > > BNE :++ > > ; Fix during Overtime > > LDA SCORE1 > > CMP #$0A > > BCC :+ > > LDA SCORE2 > > CMP #$0A > > BCC :+ > > LDA SCORE1 > > SBC #$10 > > STA SCORE1 > > LDA SCORE2 > > SBC #$10 > > STA SCORE2 > > : LDA FSCORE1 > > SBC #$10 > > STA FSCORE1 > > LDA FSCORE2 > > SBC #$10…

## Key facts

- From Jstout via: [http://tecmobowl.org...style-overtime/](https://tecmobowl.org/forum/topic/10427-possession-style-overtime/)
- > BCC $93DE ; 2D and sent to the first RTS found
- > LDA #$07
- > STA $8000
- > LDA #$01
- > STA $8001
- > LDA $002F
- > SBC #$10
- > LDA $76
- > CMP #$04
- > CMP #$0A
- 99 point fix hex (change rom hex @ x253BF)

## Topics

`face`

## Source

<https://tecmobowl.org/forums/topic/13455-editing-overtime>
