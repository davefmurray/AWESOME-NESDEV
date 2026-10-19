# Defense: 3-4 or 4-3 Team Formations

**Source:** https://tecmobowl.org/forums/topic/11034-tsb-with-both-34-and-43-defenses/  
**Category:** GAMEPLAY → Player Movement, Positioning  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/11034-tsb-with-both-34-and-43-defenses/).

## Summary

> Could you post the code for just the defensive starters image hack? Here is the code for the defensive starters screen

## Key facts

- 4C 60 9F    JMP $9F60
- x33F70: ($9F60)
- A6 6E       LDX $006E ; GET TEAM NUMBER
- BD AE 9F    LDA $9FAE,X ; GET TEAM DEFENSE
- A9 1D       LDA #$1D ; POINTER LOCATION
- A2 2F       LDX #$2F ; BANK NUMBER
- 4C 06 84    JMP $8406
- A9 1D     : LDA #$1D ; POINTER LOCATION
- A2 0F       LDX #$0F ; BANK NUMBER
- 4C 20 9F    JMP $9F20
- x33F30: ($9F20)
- A0 00       LDY #$00

## Topics

`formation`, `pointer`, `text`, `pro bowl`

## Source

<https://tecmobowl.org/forums/topic/11034-tsb-with-both-34-and-43-defenses/>
