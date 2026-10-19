# INTs, Deflections, Covered Catches

**Source:** https://tecmobowl.org/topic/7066-passing-game-ratings/  
**Category:** GAMEPLAY → Player Attributes During Gameplay  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/7066-passing-game-ratings/).

## Summary

Here is the code (I removed anything useless in learning) of one player vs one player standing (no dives, jumping, no while running, etc). It is really too much to explain (I added notes where possible) but you can check it out and I can explain any ASM you don't get. For those wondering, it basically is Pass Control + Reception - Interception and adjusting the number based upon random numbers. If the final number is 33 or less a INT happens, 34 to 50 then a deflection, else a reception.

## Key facts

- LDA $BF04,Y ; Load Pass Control Value
- STA $DC
- LDA $BF14,Y ; Load Reception Value
- ADC $DC ; Pass Control + Reception
- SBC $BF24,Y ; (Pass Control + Reception) - Load Interception Value
- BCS $9EA4
- LDA #$00
- TAX ; <- $9EA4
- LDA $3B ; Random Number
- ADC #$83
- STA $3B
- LDA $3C ; Random Number

## Source

<https://tecmobowl.org/topic/7066-passing-game-ratings/>
