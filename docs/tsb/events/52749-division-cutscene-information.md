# Division Cutscene Information

**Source:** https://tecmobowl.org/topic/52749-tsb-clinching-division-cutsceen/  
**Category:** EVENTS → In-Game  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/52749-tsb-clinching-division-cutsceen/).

## Summary

Found some info while searching the boards. Quote comes from [http://tecmobowl.org/topic/3569-editing-playoff-schedule-for-tsb-nes/?hl=x22e47#entry80324](https://tecmobowl.org/topic/3569-editing-playoff-schedule-for-tsb-nes/?hl=x22e47#entry80324) > firgured i'd post this here as well. all code is executed after a cmp #$09 at 0x22E4B if the week# > #$09. thanks to jstout for pointing me to the starting point. > > > ``` > $AE64:85 8E STA $008E = #$02 > $AE66:0A ASL > $AE67:A8 TAY > $AE68:B9 5D BF LDA $BF5D,Y @ $BF61 = #$08 > $AE6B:85 8F STA $008F = #$08 > $AE6D:85 90 STA $0090 = #$08 > $AE6F:B9 5E BF LDA $BF5E,Y @ $BF62 = #$04 > $AE72:85 91 STA $0091 = #$04 > $AE74:85 92 STA $0092 = #$00 > $AE76:A9 00 LDA #$00 > $AE78:85 93 STA $0093 = #$08 > ``` > > this code gets the starting index of…

## Key facts

- > firgured i'd post this here as well. all code is executed after a cmp #$09 at 0x22E4B if the week# > #$09. thanks to jstout for pointing me to the starting point.
- > $AE64:85 8E     STA $008E = #$02
- > $AE66:0A        ASL
- > $AE67:A8        TAY
- > $AE68:B9 5D BF  LDA $BF5D,Y @ $BF61 = #$08
- > $AE6B:85 8F     STA $008F = #$08
- > $AE6D:85 90     STA $0090 = #$08
- > $AE6F:B9 5E BF  LDA $BF5E,Y @ $BF62 = #$04
- > $AE72:85 91     STA $0091 = #$04
- > $AE74:85 92     STA $0092 = #$00
- > $AE76:A9 00     LDA #$00
- > $AE78:85 93     STA $0093 = #$08

## Topics

`schedule`, `playoff`

## Source

<https://tecmobowl.org/topic/52749-tsb-clinching-division-cutsceen/>
