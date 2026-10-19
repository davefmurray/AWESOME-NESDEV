# Cutscenes Events in Hex

**Source:** https://tecmobowl.org/forums/topic/9946-events/  
**Category:** EVENTS → In-Game  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/9946-events/).

## Summary

the game has 2 different ways of issuing events. an event can be a cutscene, a dropdown menu, ...whatever. now the arguments are in the A and X registers. X is the group number, and A is the event number. then you have a:

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
