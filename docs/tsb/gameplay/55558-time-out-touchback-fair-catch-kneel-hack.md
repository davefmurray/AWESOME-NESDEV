# Time Out / Touchback / Fair Catch/ Kneel Hack

**Source:** https://tecmobowl.org/topic/55558-time-out-touchback-fair-catch-kneel-hack/  
**Category:** GAMEPLAY → Kicking, Punting  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/55558-time-out-touchback-fair-catch-kneel-hack/).

## Summary

1. **KICKOFFS** in the endzone can be **TOUCHBACKED** by **PRESSING B** 2. **PUNTS** are now **RETURNABLE** if they go into the **ENDZONE** . **PRESSING B** will give you a **TOUCHBACK** like a kickoff.

## Key facts

- *TEST THE ROM PLEASE!**
- Someone might want to double check the locations below as well as check for bugs...as my eyes are bleeding from looking at hex for far too long.
- [TSB 2007-32\_special teams hacks\_ver D.nes](https://tecmobowl.org/applications/core/interface/file/attachment.php?id=9178)
- 0x26def  A5 93 C9 DE A5 94 E9 09 90 04 20 70 90 60 4C A0 AF
- jumps to start button check depending where coming from
- x269D0     20308B20308E60               (From P1 Play Select)
- x269D7     20308B204E8E60                  (From P2 Play Select)
- x26930     2030ABA078A2084C2C80   (From On Field P1)
- x2693A    2030ABA088A2074CB487    (From On Field P2)
- so basically, this ROM crashes after the 2nd half.  2 times in a row.
- [![post-5602-0-91671800-1372475350_thumb.gi](https://tecmobowl.org/uploads/monthly_06_2013/post-5602-0-91671800-1372475350_thumb.gif)](https://tecmobowl.org/uploads/monthly_06_2013/post-5602-0-91671800-1372475350.gif)
- *Edited June 29, 201313 yr by buck**

## Topics

`face`, `event`, `kick`, `punt`, `clock`, `endzone`

## Source

<https://tecmobowl.org/topic/55558-time-out-touchback-fair-catch-kneel-hack/>
