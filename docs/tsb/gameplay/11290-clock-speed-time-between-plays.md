# Clock speed/time between plays

**Source:** https://tecmobowl.org/forums/topic/11290-playcall-screen-clock-speed/  
**Category:** GAMEPLAY → Gameplay Clock, Playbook Clock, Quarter scores  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/11290-playcall-screen-clock-speed/).

## Summary

Here is how to adjust the clock speed on the playcall screen for TSB1 NES & SNES: SET( 0x222D6, 0x?? ) lower value for faster, higher value for slower

## Key facts

- SET( 0x222D6, 0x1E ) default speed
- SET( 0x222D6, 0x?? ) lower value for faster, higher value for slower
- SET( 0x2496D, 0x1E ) default speed
- SET( 0x2496D, 0x?? ) lower value for faster, higher value for slower
- [@bruddog](https://tecmobowl.org/profile/4675-bruddog/)ust so I am clear on this, if I want to go from 10 seconds to 5 would I use this command:
- SET(0x222D2,0x05)
- The comparable locations in TSB3 for the hex addresses posted above are listed here : [viewtopic.php?f=3&t=10476](http://www.tecmobowl.org/forum/viewtopic.php?f=3&t=10476)

## Topics

`clock`

## Source

<https://tecmobowl.org/forums/topic/11290-playcall-screen-clock-speed/>
