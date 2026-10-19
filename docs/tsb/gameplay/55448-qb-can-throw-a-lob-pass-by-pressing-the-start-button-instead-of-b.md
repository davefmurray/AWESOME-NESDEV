# QB can throw a lob pass by pressing the Start button instead of B

**Source:** https://tecmobowl.org/forums/topic/55448-use-start-instead-of-b-button-to-throw-lob-passes/  
**Category:** GAMEPLAY → Player Attributes During Gameplay  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/55448-use-start-instead-of-b-button-to-throw-lob-passes/).

## Summary

This will work on 32 team rom provided no other hacks are occupying 2BFE0. Press start by itself: If QB pass speed is > 44 he can throw a lob pass at 44 PS

## Key facts

- This will work on 32 team rom provided no other hacks are occupying 2BFE0.
- SET 0x2912D   0x50 player 1
- SET 0x291D4   0x50 player 2
- SET 0x2B2C1   0xE0 BF EA
- SET 0X2BFF0  0X20AADDAAE0**07**900C2008A12910C910D003A0**06**608AA860
- Other notes: a108 routine in the bank gets the player appropriate joypad data.
- [tpc\_original\_pass\_loft\_hack.nes](https://tecmobowl.org/applications/core/interface/file/attachment.php?id=8743)
- > hey bruddog you think you could apply this hack to a rom ive been working on and am about to release
- > This will work on 32 team rom provided no other hacks are occupying 2BFE0.
- If the start of jstouts pass/run code could be moved over 3 bytes to the right (so that it starts at x2BFBE instead of 2BFBB).  but I'm not sure how easy it is to move this, probably needs updated by stout.
- *Edited June 26, 201313 yr by buck**

## Topics

`face`

## Source

<https://tecmobowl.org/forums/topic/55448-use-start-instead-of-b-button-to-throw-lob-passes/>
