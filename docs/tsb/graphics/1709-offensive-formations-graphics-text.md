# Offensive Formations: Graphics, Text

**Source:** https://tecmobowl.org/forums/topic/1709-changing-formations/  
**Category:** GRAPHICS → Formations, Names  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/1709-changing-formations/).

## Summary

> Here is the adjustment for the player position on the data screen that I didn't have before. > > It is located at x30FF8 to x3101F and is a similiar deal to the formation change. > > The ASM code: > > $8FE8:A5 6E LDA $6E > > $8FEA:C9 07 CMP #$07 > > $8FEC:F0 16 BEQ $9004 > > $8FEE:C9 14 CMP #$14 > > $8FF0:F0 12 BEQ $9004 > > $8FF2:C9 1B CMP #$1B > > $8FF4:F0 0E BEQ $9004 > > $8FF6:C9 0E CMP #$0E > > $8FF8:F0 10 BEQ $900A > > $8FFA:C9 11 CMP #$11 > > $8FFC:F0 0C BEQ $900A > > $8FFE:BD 39 90 LDA $9039,X > > $9001:4C 18 90 JMP $9018 > > $9004:BD 43 90 LDA $9043,X > > $9007:4C 18 90 JMP $9018 > > $900A:BD 4D 90 LDA $904D,X > > $900D:4C 18 90 JMP $9018 > > Ok, it loads the team # from 6E. Just like with the formation change, C9 07 F0 16 compares the # to 07 (Houston) if true move down 16…

## Key facts

- Does anyone know what the locations for this are for the 32-team rom?
- > $8FE8:A5 6E LDA $6E
- > $8FEA:C9 07 CMP #$07
- > $8FEC:F0 16 BEQ $9004
- > $8FEE:C9 14 CMP #$14
- > $8FF0:F0 12 BEQ $9004
- > $8FF2:C9 1B CMP #$1B
- > $8FF4:F0 0E BEQ $9004
- > $8FF6:C9 0E CMP #$0E
- > $8FF8:F0 10 BEQ $900A
- > $8FFA:C9 11 CMP #$11
- > $8FFC:F0 0C BEQ $900A

## Topics

`formation`, `sim`, `32-team`

## Source

<https://tecmobowl.org/forums/topic/1709-changing-formations/>
