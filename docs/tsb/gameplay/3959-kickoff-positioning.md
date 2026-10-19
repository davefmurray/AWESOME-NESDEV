# Kickoff Positioning

**Source:** https://tecmobowl.org/forums/topic/3959-adjusting-kick-off-positions/  
**Category:** GAMEPLAY → Kicking, Punting  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/3959-adjusting-kick-off-positions/).

## Summary

> On 1/29/2017 at 6:13 PM, fgqb#19nyj said: > > Never mind, Buck, I got it. Thanks for the code. It worked like a charm. ![:)](https://tecmobowl.org/uploads/emoticons/default_smile.png ":)") > > (changing the kickoff location to the 30 or 40 yard line) > > -30 yard- > To change player 1 to the 30: 0x247B9: A0 60; 0x247BB: A2 07 > > To change player 2 to the 30: 0x24031: A0 A0; 0x24033: A2 08 > > -40 yard- > To change player 1 to the 40: 0x247B9: A0 B0; 0x247BB: A2 07 > > To change player 2 to the 40: 0x24031: A0 50; 0x24033: A2 08 > > Note: must use the 20 yard line to middle of end zone option otherwise the kickoff could go out of the end zone and award the opposing team a safety. > > (kickoff lengths) > > #ALL KICKOFFS RANGE FROM 16YD-LINE TO BACK OF ENDZONE > > SET(0x2A534,…

## Key facts

- > On 1/29/2017 at 6:13 PM, fgqb#19nyj said:
- > To change player 1 to the 30: 0x247B9: A0 60; 0x247BB: A2 07
- > To change player 2 to the 30: 0x24031: A0 A0; 0x24033: A2 08
- > To change player 1 to the 40: 0x247B9: A0 B0; 0x247BB: A2 07
- > To change player 2 to the 40: 0x24031: A0 50; 0x24033: A2 08
- > #ALL KICKOFFS RANGE FROM 16YD-LINE TO BACK OF ENDZONE
- > SET(0x2A534, 0x4C83BF)
- > SET(0x2BF93, 0xA5454AA5446A186992A8A9016900AA4C2FA5)
- > #ALL KICKOFFS RANGE FROM 20YD-LINE TO MIDDLE OF ENDZONE (2nd option is needed for 40y ko)
- > SET(0x2BF93, 0xA5454AA5446A186962A8A9016900AA4C2FA5)
- > I got all this from Buck and the Raja by the way. I just wanted them in one place is all.
- To change player 1 to the 30: 0x247B9: A0 60; 0x247BB: A2 07

## Topics

`sim`, `kick`, `endzone`

## Source

<https://tecmobowl.org/forums/topic/3959-adjusting-kick-off-positions/>
