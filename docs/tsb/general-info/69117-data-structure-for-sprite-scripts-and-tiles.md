# Data Structure for Sprite scripts and tiles

**Source:** https://tecmobowl.org/forums/topic/69117-data-structure-for-sprite-scripts-and-tiles/  
**Category:** GENERAL INFO  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/69117-data-structure-for-sprite-scripts-and-tiles/).

## Summary

This is for sprites only and not backgrounds and the overall screen scripts. **0X00-0X7F** = **FRAMES TO WAIT/ OR CONTINUE SCROLLING TIMES 2.**

## Key facts

- *0X00-0X7F** = **FRAMES TO WAIT/ OR CONTINUE SCROLLING TIMES 2.**
- *0X80-0X9F** = **SET DATA ADDR FOR SPR TILES +0x20** to high byte Example 0x8444 = 0x84+0x20= A4 = sets sprite TILE DATA address = 0xA444
- *0XA0-0XBF** = **JUMP TO NEW SPRITE  SCRIPT ADDRESS**               Example 0xA444 = sets sprite SCRIPT DATA address = 0xA444
- *0XC0-0XDF** = DO **SPRITE  SCRIPT AT ADDRESS AND RETURN** -0X20 to high byte      Example 0xD444 = sets sprite SCRIPT DATA address = 0xB444
- *0XE0-0XEF = WAIT # FRAMES ( 0 TO 15)** Example 0xE4= wait 4 frames
- *0XF0 SET SPR PAL AND SET TO FULLY FADED IN(SPR PAL INDEX)**
- *0XF1 SET SPRITE OFFSCREEN THRESHOLDS(0=TOP 1=BOT, THRESHOLD)**
- Example F1 00 80= Sets top of screen threshold to the middle of the screen (useful for vertically scrolling sprites to make them "appear" from behind something)
- *0XF2 START SCROLLING**
- *0XF3 SET SPRITE PRIORITY =  BEHIND BACKGROUND**
- *0XF4 SET SPRITE SIZE = 8X8**
- *0XF5 SET SPRITE SIZE = 8X16**

## Topics

`helmet`, `tile`, `CHR`, `cutscene`, `kick`, `sprite`

## Source

<https://tecmobowl.org/forums/topic/69117-data-structure-for-sprite-scripts-and-tiles/>
