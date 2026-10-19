# First Down Yardage

**Source:** https://tecmobowl.org/forums/topic/3960-changing-first-down-yardage/  
**Category:** GAMEPLAY → Down & Distance  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/3960-changing-first-down-yardage/).

## Summary

To change the amount of yards needed to gain a first down edit the byte at **0x24FDF**. The default value is 0x50 (or 80 in decimal, 8 \* 10). To change to 20 yards, change the value to 0xA0 (160 in decimal, 8 \* 20). Each yard is worth 8 "points". Therefore, the possible range is 0 to 32 yards. This does *not* update all aspects of the game. The chains still show up ten yards apart, and it says 1st and 10. If you gain 9.9 yards, the ref will measure anyway. If you gain over 10 yards and under the new yardage, it will be X down and 99. The game plays fine though. It appeared to affect both players, including the CPU. Obviously, the CPU has no clue that it now needs to gain more than 10 yards.

## Key facts

- On second thought, probably only the chain measure will follow one of those three bytes because the other areas (distance from chain, 1st and X) probably are the result of some arithmetic.
- With arithmetic in mind, I found the chain markers. They are at **0x26471** and **0x2649B**, using the same yardage system as above.
- And finally, to update the text '1st and X', change the value at **0x2E495** and **0x2E4C4**.
- [@TheRaja](https://tecmobowl.org/profile/10259-theraja/)
- SET (0x24F7D, 0xEAEAEAEAEA)
- SET (0x24FC5, 0xEAEAEAEAEA)
- SET (0x25004, 0xEAEAEAEAEAEAEAEAEAEAEAEAEAEAEA)
- I added this to my Rom but noticed that the ref is still measuring at 9.9 yards instead of 15.9 yards (Im using 1st and 16). Am I missing something or does the yard markers not update that part?
- *Edited May 12, 20179 yr by TheRaja**

## Topics

`text`

## Source

<https://tecmobowl.org/forums/topic/3960-changing-first-down-yardage/>
