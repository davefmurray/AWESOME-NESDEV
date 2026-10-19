# How Quickly Players Rise & How Far They Are Thrown

**Source:** https://tecmobowl.org/topic/52422-possible-to-edit-how-quickly-players-get-up/  
**Category:** GAMEPLAY → Player Movement, Positioning  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/52422-possible-to-edit-how-quickly-players-get-up/).

## Summary

all I know is there are a bunch of pointers that point to locations. each location is a different "fall down" animation. some just drop and get up quickly, some fall at angles, some are the "I got chop-blocked" falldown, etc. I never attempted to figure out any more. I know that you can replace the pointers with other pointers to replace fall-downs. In one of my minor-league roms I replaced all falldown animations with the "quick drop" (d8be).

## Key facts

- all I know is there are a bunch of pointers that point to locations.
- and this is from July 2010, and I have not looked at this since.
- 1B010	start the pointers (flip and add 0x10 to goto code)
- 1B090	start the codes
- POINTER DESCRIPTIONS
- 80b0	quick flip backwards left, shake head						3 yards
- b1b0	quick flip diag-up-left						3 yards
- dab0	straight vertical roll UP						3 yards
- 09b1	quick flip diag-up-right						3 yards
- 32b1	quick flip backwards, right						3 yards
- 63b1	quick flip backwards, down-right						3 yards
- 8ab1	straight vertical roll DOWN						3 yards

## Topics

`pointer`

## Source

<https://tecmobowl.org/topic/52422-possible-to-edit-how-quickly-players-get-up/>
