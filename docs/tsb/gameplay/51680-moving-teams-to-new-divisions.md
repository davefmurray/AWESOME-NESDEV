# Moving Teams to New Divisions

**Source:** https://tecmobowl.org/topic/51680-moving-teams-to-different-divisions/  
**Category:** GAMEPLAY → Game-types  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/51680-moving-teams-to-different-divisions/).

## Summary

I think you need this article: [http://tecmobowl.org/topic/7850-removing-teams-from-the-menu/page\_\_hl\_\_%20nfl%20%20standings#entry71010](https://tecmobowl.org/topic/7850-removing-teams-from-the-menu/page__hl__%20nfl%20%20standings#entry71010) Here ill quote the one I think is what you need to change:

## Key facts

- > 	.org $AF34	; @ 0x22F44 in rom
- > 	LDA $45		; *1
- > 	LDA $BF5D,Y	; *2
- > 	LDX $BF5E,Y	; *3
- > 	STX $90
- > 	JSR $B3EC
- > 0x23F6D - 0x23F78 (12bytes)
- > $00, $04 = division starts at BUF and ends with N.E.
- > the length byte has to be $04 or $05 or the screen will stay black, but it won't crash. it'll still let you back out to the main menu.
- .org $AF34 ; @ 0x22F44 in rom
- LDA $45 ; **\*1**
- LDA $BF5D,Y ; \*2

## Source

<https://tecmobowl.org/topic/51680-moving-teams-to-different-divisions/>
