# KR Speed Change From RT to Actual KR Player

**Source:** https://tecmobowl.org/forums/topic/4006-changing-the-kr-speed/  
**Category:** GAMEPLAY → Kicking, Punting  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/4006-changing-the-kr-speed/).

## Summary

So I am STILL having this issue, and even went extra steps to try and resolve it. First, I got an Original TSB Rom with no changes (28 Teams)

## Key facts

- First, I got an Original TSB Rom with no changes (28 Teams)
- Then the only thing I changed was this 0x8100 code
- FROM: 00 48 EC E3 30 EF E1 00
- *Edited May 18, 201511 yr by TheRaja**
- In the ROM at 0x80FF is the command sequences for the KR. In goes like this, using my interpretation of the code:
- Set Pos From KO(01,00,48)
- Catch Ball from Kick
- However, this is where the glitch kicks in. Somehow TSB forgets that the 11th player is now the KR, and it loads the MS from the 11th slot (RT). Now, you have an ultra slow KR in most cases.
- 0x08100: 00 48 ec **ef e4**
- There may be other side effects from removing the EC command; I didn't test it completely.
- $AAE0 --- EF ---- E1
- $AAE1 --- E4 ---- 00

## Topics

`kick`

## Source

<https://tecmobowl.org/forums/topic/4006-changing-the-kr-speed/>
