# Fumble Probability Table

**Source:** https://tecmobowl.org/forums/topic/58620-fumble-probabilities-table  
**Category:** GAMEPLAY → Player Attributes During Gameplay  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/58620-fumble-probabilities-table).

## Summary

[Expanding on the content from here](https://tecmobowl.org/topic/3989-player-attribute-probabilities/) The Ball Control attribute can vary from 06-100 (16 total) and those values correspond to a table located from 0x2bf04 to 0x2bf13

## Key facts

- [Expanding on the content from here](https://tecmobowl.org/topic/3989-player-attribute-probabilities/)
- The Ball Control attribute can vary from 06-100 (16 total) and those values correspond to a table located from 0x2bf04 to 0x2bf13
- SET (0x2BF04, FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF)
- SET (0x2BF04, 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00)
- [The BC for QBs and PR are controlled at x286E7 and the default setting is 0C, which is 44 BC.](https://tecmobowl.org/topic/7010-qb-and-punt-returner-ball-control/#p61757)
- You can set the PR's BC based on the PR/QB BC posting information given by Jstout.  You set a location @2869e as the PR's location after spliting the two (you can also customize the QB rating @286e7).
- > Does this apply to **PR** as well?, Or we still use this? [http://tecmobowl.org/topic/7010-qb-and-punt-returner-ball-control/#p61757](https://tecmobowl.org/topic/7010-qb-and-punt-returner-ball-control/#p61757)

## Topics

`attribute`, `punt`

## Source

<https://tecmobowl.org/forums/topic/58620-fumble-probabilities-table>
