# Special Teams: KR XY Location

**Source:** https://tecmobowl.org/forums/topic/5852-kr-xy-location/  
**Category:** GAMEPLAY → Player Movement, Positioning  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/5852-kr-xy-location/).

## Summary

sorry the cpu will always run backwards i think and i really don't care to bother to figure out why since im not concerned with cpu games. MY fix only makes it so that the kr is waiting for the ball rather than still running to get there sometimes in man vs man play. Basically "In the ROM at 0x80FF is the command sequences for the KR. In goes like this, using my interpretation of the code:

## Key facts

- from konforce
- "In the ROM at 0x80FF is the command sequences for the KR. In goes like this, using my interpretation of the code:
- Set Pos From KO(01,00,48)
- Catch Ball from Kick
- Go to 80FF and find 48 in the hex near that location. CAhnge it to like 78. It starts the KR farther back. You can play with different values to see what works best.
- > Hey I was wondering if you could tell me how to fix the kick return hack to keep the cpu from running backwards first ? Thanks
- I assume there is a fix for this since it doesn't happen on any of the newer ROMs, but can't seem to find it. Anyone know?
- Hey I was wondering if you could tell me how to fix the kick return hack to keep the cpu from running backwards first ? Thanks

## Topics

`kick`

## Source

<https://tecmobowl.org/forums/topic/5852-kr-xy-location/>
