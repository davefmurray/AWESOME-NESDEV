# Prevent Fumbling After TD

**Source:** https://tecmobowl.org/topic/12527-stopping-fumbles-after-touchdowns-beta/  
**Category:** GAMEPLAY → Player Attributes During Gameplay  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/12527-stopping-fumbles-after-touchdowns-beta/).

## Summary

Today I had a thought - since ball carriers never seem to fumble while being tackled out of bounds, shouldn't it be possible to stop fumbles from occurring after the ball carrier crosses into the End Zone as well? I posed this question to Jstout, and he first confirmed that fumbling while out of bounds is not possible in the orig rom, then whipped up some code right-quick for how to stop post-touchdown fumbles as well!

## Key facts

- Today I had a thought - since ball carriers never seem to fumble while being tackled out of bounds, shouldn't it be possible to stop fumbles from occurring after the ball carrier crosses into the End Zone as well?
- I posed this question to Jstout, and he first confirmed that fumbling while out of bounds is not possible in the orig rom, then whipped up some code right-quick for how to stop post-touchdown fumbles as well!
- x28698 ($8688):
- x2BF50 ($BF40):
- A5 73 LDA $73
- 29 20 AND $20
- A5 71 LDA $71
- 29 10 AND #$10
- C9 10 CMP #$10
- 4C E8 86 : JMP $86E8
- EDIT: IPS and Hacked Rom attached
- [No Post TD Fumbles.rar](https://tecmobowl.org/applications/core/interface/file/attachment.php?id=5842)

## Topics

`face`

## Source

<https://tecmobowl.org/topic/12527-stopping-fumbles-after-touchdowns-beta/>
