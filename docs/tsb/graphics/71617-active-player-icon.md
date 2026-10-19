# Active Player Icon

**Source:** https://tecmobowl.org/forums/topic/71617-editing-player-icons/  
**Category:** GRAPHICS → **NEW** (2.13.2021)(Completed)  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/71617-editing-player-icons/).

## Summary

The icons aren't separated by offense and defense. I haven't gotten to test this out yet beyond a few plays so I'll do that when I have the chance but this seemed to be working. ``` A5 70 LDA $70 ; Play Value 29 40 AND #$40 C9 40 CMP #$40 D0 0A BNE :+ ; Player 2 has Ball A9 FE LDA #$FE ; Set Player 1 Icon off screen 8D 00 02 STA $0200 A9 A3 LDA #$A3 ; Tile # of Football A0 43 LDY #$43 ; Color Palette 3 and Flip Tile 60 RTS ; Player 1 has Ball A9 FE : LDA #$FE ; Set Player 2 Icon off screen 8D 04 02 STA $0204 A9 A3 LDA #$A3 ; Tile # of Football A0 01 LDY #$01 ; Color Palette 1 60 RTS ```

## Key facts

- 20 70 BF  JSR $BF70
- A5 70     LDA $70 ; Play Value
- 29 40     AND #$40
- C9 40     CMP #$40
- A9 FE     LDA #$FE ; Set Player 1 Icon off screen
- 8D 00 02  STA $0200
- A9 A3     LDA #$A3 ; Tile # of Football
- A0 43     LDY #$43 ; Color Palette 3 and Flip Tile
- A9 FE   : LDA #$FE ; Set Player 2 Icon off screen
- 8D 04 02  STA $0204
- A0 01     LDY #$01 ; Color Palette 1

## Topics

`palette`, `tile`

## Source

<https://tecmobowl.org/forums/topic/71617-editing-player-icons/>
