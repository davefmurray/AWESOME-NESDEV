# Control Execution Code

**Source:** https://tecmobowl.org/topic/9701-tsb-nes-gameplay-code/  
**Category:** GENERAL INFO  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/9701-tsb-nes-gameplay-code/).

## Summary

this is the code that controls a games execution. i'm still unsure of what some of it does (???). ``` $2D = %.... ..TT ++-game type 0=preseason 1=probowl 2=season 3=playoff/superbowl .... .. = UNKNOWN ```

## Key facts

- $2D     = %.... ..TT
- $A0D4:20 A6 AD  JSR $ADA6                       ; goto coin toss screen/intro
- $A0D7:A5 2D     LDA $002D = #$80                ;   ???
- $A0D9:4A        LSR                             ;   ???
- $A0DA:4A        LSR                             ;   ???
- $A0DB:4A        LSR                             ;   ???
- $A0DC:4A        LSR                             ;   ???
- $A0DD:29 01     AND #$01                        ;   ???
- $A0DF:85 72     STA $0072 = #$00                ;   ???
- $A0E1:A9 03     LDA #$03                        ;   ???
- $A0E3:85 8C     STA $008C = #$03                ;   ???
- $A0E5:85 8D     STA $008D = #$03                ;   ???

## Topics

`playoff`

## Source

<https://tecmobowl.org/topic/9701-tsb-nes-gameplay-code/>
