# Keep quarter scores intact if game goes into Overtime

**Source:** https://tecmobowl.org/forums/topic/60297-keeps-quarter-scores-intact-if-game-goes-to-ot/  
**Category:** GAMEPLAY → Gameplay Clock, Playbook Clock, Quarter scores  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/60297-keeps-quarter-scores-intact-if-game-goes-to-ot/).

## Summary

This would be something useful for league box scores or TPC uploads. As you know if you go to overtime the scores for each quarter are erased. **Prevents quarter scores from being cleared in OT**

## Key facts

- *Prevents quarter scores from being cleared in OT**
- SET(0x2215A,0xEAEAEAEAEAEAEAEAEAEAEAEAEAEAEAEA)
- SET(0x2217B,0x4E)
- SET(0x221C8,0x4E)
- *Makes it so score in OT only gets added to total for P1**
- SET(0x25359,0xB00D)
- *Makes it so score in OT only gets added to total for P2**
- SET(0x2537A,0xB00D)
- > On 11/18/2016 at 10:59 AM, bruddog said:
- > [@averagetsbplayer](https://tecmobowl.org/profile/5418-averagetsbplayer/) [@manyo360](https://tecmobowl.org/profile/9034-manyo360/)
- It's tough to tell the difference between a game that was 0-0 going into OT from a game that had it's only score in the first quarter.
- *Edited March 1, 20242 yr by averagetsbplayer**

## Topics

`event`

## Source

<https://tecmobowl.org/forums/topic/60297-keeps-quarter-scores-intact-if-game-goes-to-ot/>
