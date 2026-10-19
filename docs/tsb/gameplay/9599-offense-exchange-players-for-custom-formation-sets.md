# Offense: Exchange Players for Custom Formation Sets

**Source:** https://tecmobowl.org/forums/topic/9599-different-players-on-the-field-for-different-formations/  
**Category:** GAMEPLAY → Player Movement, Positioning  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/9599-different-players-on-the-field-for-different-formations/).

## Summary

Here is what the code looks like for Player 1 without any injury checks. Note: This could be worked into shorter code if it were to remain the same. x3D30: $BD20:A6 78 LDX $78 ; Player 1 Play Slot Called $BD22:BD 7E 66 LDA $667E,X ; Load Play # $BD25:AA TAX $BD26:BD D0 BC LDA $BCD0,X ; Load Table 0=2WR, 1=3WR, 2=4WR $BD29:C9 01 CMP #$01 $BD2B:F0 20 BEQ $BD4D ; Goto 3WR $BD2D:C9 02 CMP #$02 $BD2F:F0 38 BEQ $BD69 ; Goto 4WR ; 2WR Code: $BD31:A9 02 LDA #$02 ; RB1 $BD33:8D 13 66 STA $6613 $BD36:A9 03 LDA #$03 ; RB2 $BD38:8D 15 66 STA $6615 $BD3B:A9 06 LDA #$06 ; WR1 $BD3D:8D 17 66 STA $6617 $BD40:A9 07 LDA #$07 ; WR2 $BD42:8D 19 66 STA $6619 $BD45:A9 0A LDA #$0A ; TE1 $BD47:8D 1B 66 STA $661B $BD4A:4C 82 BD JMP $BD82 ; 3WR Code: $BD4D:A9 02 LDA #$02 ; RB1 $BD4F:8D 13 66 STA $6613 $BD52:A9…

## Key facts

- x255FF: 4C 20 BD EA EA ; Goto $BD20
- $BD20:A6 78     LDX $78 ; Player 1 Play Slot Called
- $BD22:BD 7E 66  LDA $667E,X ; Load Play #
- $BD25:AA        TAX
- $BD26:BD D0 BC  LDA $BCD0,X ; Load Table 0=2WR, 1=3WR, 2=4WR
- $BD29:C9 01     CMP #$01
- $BD2B:F0 20     BEQ $BD4D ; Goto 3WR
- $BD2D:C9 02     CMP #$02
- $BD2F:F0 38     BEQ $BD69 ; Goto 4WR
- $BD31:A9 02     LDA #$02 ; RB1
- $BD33:8D 13 66  STA $6613
- $BD36:A9 03     LDA #$03 ; RB2

## Topics

`formation`

## Source

<https://tecmobowl.org/forums/topic/9599-different-players-on-the-field-for-different-formations/>
