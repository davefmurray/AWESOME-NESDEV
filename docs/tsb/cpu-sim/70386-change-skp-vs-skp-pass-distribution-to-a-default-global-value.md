# Change SKP vs SKP pass distribution to a default global value

**Source:** https://tecmobowl.org/forums/topic/70386-sim-target-distribution-hack  
**Category:** CPU & SIM → Attributes, Play Ratio, SIM Stats  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/70386-sim-target-distribution-hack).

## Summary

Contrary to prior belief(i think) the playbook definitely has no effect in skp vs skp mode for passing as far as what targets get thrown to. The target chance table is non-linear. This means the values are not evenly spaced apart. Also it means you have to make sure the starters target chances add up to a certain value or you will never get passes to the latter players since the game checks the targets in the following order If you gave RB1 and RB2 target chance ratings of 15 or 0F in hex. WR1, WR2 and the TE would never get targeted. This is because a target rating of 15 corresponds to a value of 128 decmail in the target chance lookup table. So 128+128 = 256 . It is only comparing the target chance to the random value and then subtracting that amount.

## Key facts

- If the random value was 255. 128 is less than 255. It would increment the target index and subtract 128 from the random value and use this value as the new value to compare to. This
- RB1 10%,        TABLE VALUE $19   (256 \*10% = 25. Converted to hex = $19)
- RB2 10%         TABLE VALUE $32   (256 \*10% = 25. Converted to hex = $19 + previous table value $19 = $3A)
- WR1 30%        TABLE VALUE $7F    (256 \*30% = 77. Converted to hex = $4d + previous table value $19 = $7F)
- WR2 30%        TABLE VALUE $CC    (256 \*30% = 77. Converted to hex = $4d + previous table value $19 = $CC)
- TE     20%        TABLE VALUE $FF    (no need to calculate it is the remaining percentage always leave at FF)
- SET(0x175a9, 0xA53DDD80BA9013E888D0F7)
- SET(0x19B90, 0x19327FCCFF19327FCCFF)
- This should work on any rom but double check the 19B90 location in case there is a hack there. It should be FF's
- > On 2/9/2019 at 1:08 PM, SBlueman said:

## Topics

`playbook`, `roster`, `sim`

## Source

<https://tecmobowl.org/forums/topic/70386-sim-target-distribution-hack>
