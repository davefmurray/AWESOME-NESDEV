# COM Punt Timing

**Source:** https://tecmobowl.org/topic/66645-com-punt-timing/#entry456338  
**Category:** GAMEPLAY → Kicking, Punting  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/66645-com-punt-timing/#entry456338).

## Summary

0x4C2493 ; Jumps to final COM random punt loop. In the OG rom this final loop makes sure the bar is at least half full. 0x1F ; Random value. If you make this zero com will always punt at the same length. Only use values like 0x0F, 0x1F, 0x3F. With 1F and 3F sometimes the com will let the punt bar go through once but mostly it will go on the first cycle. Basically this effects how long the com will hold the ball before punting.

## Key facts

- @29323
- 0x4C2493      ;  Jumps to final COM random punt loop. In the OG rom this final loop makes sure the bar is at least half full.
- @29337
- @29340
- 40                ; Check value for bar length ~77%. Max bar is ~ 0x5E
- SET(0x29323,0x4C2493)
- SET(0x29337,0x1F)
- SET(0x29340,0x40)

## Topics

`punt`

## Source

<https://tecmobowl.org/topic/66645-com-punt-timing/#entry456338>
