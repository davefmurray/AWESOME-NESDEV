# Conditions Change Explanation

**Source:** https://tecmobowl.org/forums/topic/58030-conditions-distribution/?tab=comments#comment-424391  
**Category:** GAMEPLAY → Player Attributes During Gameplay  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/58030-conditions-distribution/?tab=comments#comment-424391).

> **Note:** The linked post is short or a question; the most technical reply is shown instead.

## Summary

Ya i made a simulation in excel and you can see guys stay in conditions for a long period of time. ``` L_17_A395: ; UPDATE CONDITION ROUTINE

## Key facts

- LDA #$80                                        ; Allow SRAM write
- LDA $70                                         ; save possesion byte in $42
- STA $42                                         ;
- LDA #$00                                        ; SET TEAM to player 1
- STA $70                                         ;
- LDA #$00                                        ; SET current player to first player
- STA $44                                         ;
- LDA $44                                         ; LOAD current player to check
- LDA #$01                                        ; LOAD Average condition in case they are
- AND #$18                                        ; 25% chance of condition change (because 2 out of 8 bits being checked)
- LDA $44                                         ; LOAD player
- STA $45                                         ; SAVE in $45= current condituib

## Topics

`sim`

## Source

<https://tecmobowl.org/forums/topic/58030-conditions-distribution/?tab=comments#comment-424391>
