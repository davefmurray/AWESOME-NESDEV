# Cutscene & Event Editing Introduction

**Source:** https://tecmobowl.org/forums/topic/9946-events/  
**Category:** GRAPHICS → Background & Design Palettes, Cut Scene Colors  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked forum post. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/9946-events/).

## Summary

``` $C390:85 C2 STA $00C2 = #$53 ; <-ENTER HERE $C392:86 C3 STX $00C3 = #$BB $C394:A9 17 LDA #$17 $C396:85 10 STA $0010 = #$0F $C398:A0 02 LDY #$02 $C39A:A9 80 LDA #$80 $C39C:A2 0C LDX #$0C $C39E:20 45 CC JSR $CC45 $C3A1:60 RTS ``` ``` $C3AF:85 C2 STA $00C2 = #$53 ; <-ENTER HERE $C3B1:86 C3 STX $00C3 = #$BB ; $C3B3:A5 2E LDA $002E = #$10 ; $C3B5:48 PHA ; $C3B6:A2 17 LDX #$17 ; $C3B8:20 DD D8 JSR $D8DD ; bank swap? $C3BB:A5 C2 LDA $00C2 = #$53 ; $C3BD:A6 C3 LDX $00C3 = #$BB ; $C3BF:20 00 80 JSR $8000 ; $C3C2:68 PLA ; $C3C3:AA TAX ; $C3C4:4C DD D8 JMP $D8DD ; ```

## Key facts

- JSR $C390
- JSR $C3A2 (this will JSR to $C390)
- JSR $C3AF
- $C390:85 C2     STA $00C2 = #$53	; <-ENTER HERE
- $C392:86 C3     STX $00C3 = #$BB
- $C394:A9 17     LDA #$17
- $C396:85 10     STA $0010 = #$0F
- $C398:A0 02     LDY #$02
- $C39A:A9 80     LDA #$80
- $C39C:A2 0C     LDX #$0C
- $C39E:20 45 CC  JSR $CC45
- $C3A1:60        RTS

## Topics

`face`, `cutscene`, `event`, `roster`, `schedule`, `playoff`, `kick`, `punt`

## Source

<https://tecmobowl.org/forums/topic/9946-events/>
```
