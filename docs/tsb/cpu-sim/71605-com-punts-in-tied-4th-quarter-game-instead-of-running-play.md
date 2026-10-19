# COM punts in tied 4th quarter game instead of running play

**Source:** https://tecmobowl.org/forums/topic/71605-how-can-you-edit-logic-so-com-doesnt-go-for-it-on-4th-down-in-a-tie-when-inside-their-own-end-of-the-field/  
**Category:** CPU & SIM → Attributes, Play Ratio, SIM Stats  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/71605-how-can-you-edit-logic-so-com-doesnt-go-for-it-on-4th-down-in-a-tie-when-inside-their-own-end-of-the-field/).

## Summary

> On 7/26/2020 at 1:54 AM, SBlueman said: > > Is it at all possible to edit the COM logic so when it's a tie game in the 4th quarter they don't go for it on 4th down and instead punt? I hate when you end up with a cheap win because they went for it on 4th and 12 inside their own 20. > > So I didn't know if there was a way to pull off fixing that annoying 4th down error. Anyone out there know if this can be done and if so, could we accomplish this with a set command that others can use too if they want? OK. Thanks to a steady supply of the Banquet Beer (on Christmas eve) and my love for the game (and SBlueman), I took a stab at mapping the COM play-picking logic section (by hand on paper and a spreadsheet) using the info/code pasted at the very bottom of this post . I'm not sure where I…

## Key facts

- > On 7/26/2020 at 1:54 AM, SBlueman said:
- To arrive at Loop22, first we start at Loop1 which is located at 0x18714.
- From here, if the ball is at or beyond the 41 yard line, it heads to Loop22.
- Now looking at Loop22, which is located at 0x0187F6:
- A576, LDA QUARTER
- C903, CMP  FOURTH\_QUARTER
- D011,  BNE @Loop23   If NOT 4th Quarter go to Loop23
- A56B,  LDA QUARTER\_MINUTES
- C902,  CMP  #$02
- B02F,  BCS  @Loop26  if Time >= 2 minutes, go to Loop26
- A5A0,  LDA  SCORE\_DEFENSE
- C59F,  CMP SCORE\_OFFENSE

## Topics

`CHR`, `event`, `punt`, `clock`, `pointer`

## Source

<https://tecmobowl.org/forums/topic/71605-how-can-you-edit-logic-so-com-doesnt-go-for-it-on-4th-down-in-a-tie-when-inside-their-own-end-of-the-field/>
