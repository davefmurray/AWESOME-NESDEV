# Player-2 Condition Fix

**Source:** https://tecmobowl.org/topic/10436-player-2-conditions-fix/  
**Category:** 32-TEAM ROM FIXES → NFC West "SIM" Bugs  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/10436-player-2-conditions-fix/).

## Summary

> How does one implement code fixes presented like that to a rom? Can I just overwrite the string starting at 0x30E55 with 20 80 9F for instance? > > I understand if the hacking vets on these boards find questions like this to be annoying, etc., but it would surely prevent future "how do you do this and that?" if I got some help understanding the immense resourses available here... yes, but leave out the right-most column (jstouts descriptions)

## Key facts

- > How does one implement code fixes presented like that to a rom? Can I just overwrite the string starting at 0x30E55 with 20 80 9F for instance?
- SET(0x30e55, 0x20809f)
- SET(0x31f90, 0xa66ee46df00218603860)
- A6 6E      LDX $6E ; Load Current Player
- E4 6D      CPX $6D ; Load Player 2
- How does one implement code fixes presented like that to a rom? Can I just overwrite the string starting at 0x30E55 with 20 80 9F for instance?

## Topics

`event`

## Source

<https://tecmobowl.org/topic/10436-player-2-conditions-fix/>
