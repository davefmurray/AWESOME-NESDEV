# Add Tackles to Save Stats

**Source:** https://tecmobowl.org/topic/9460-recording-tackles/  
**Category:** STATS & SAVE STATES → Tackles & Injuries  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/9460-recording-tackles/).

## Summary

Here is some code for recording the number of tackles for each defensive player during a played game (NOT a simmed game). I've been using this for testing play design coding but it has a few bugs. I thought someone might find it useful or be able to expand upon it. I haven't checked the erase code location for 100% correctness thoroughly though I expect no problems. \*Added code for the Pro Bowl game, changed entry point to start of stats not cleanup to fix a bug, changed back fumble code, and added code to fix previous bugs\* Note: Do not use this on cxrom's 32-team rom as locations listed are being used and you'll ruin the rom. Also I'm not aware of the exact SRAM locations he used.

## Key facts

- Note: Do not use this on cxrom's 32-team rom as locations listed are being used and you'll ruin the rom. Also I'm not aware of the exact SRAM locations he used.
- 4C 90 FF   JMP $FF90
- Change Banks for Tackle Code:
- A9 06      LDA #$06
- 8D 00 80   STA $8000
- A9 01      LDA #$01
- 8D 01 80   STA $8001
- 20 E0 9C   JSR $9CE0 ; Go to Tackle code
- A9 12      LDA #$12
- A5 70      LDA $70
- 4C 3E 9C   JMP $9C3E ; Go back to Player 2
- 4C E0 9A : JMP $9AE0 ; Go back to Player 1

## Topics

`sim`, `32-team`, `pro bowl`

## Source

<https://tecmobowl.org/topic/9460-recording-tackles/>
