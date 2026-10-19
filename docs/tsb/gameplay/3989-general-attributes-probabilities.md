# General Attributes Probabilities

**Source:** https://tecmobowl.org/topic/3989-player-attribute-probabilities/  
**Category:** GAMEPLAY → Player Attributes During Gameplay  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/3989-player-attribute-probabilities/).

## Summary

The section of the ROM around **0x2bee4** controls how the various attributes affect the play. Perhaps this is already known, but I found it while looking to see if PC could be modified to affect interceptions as opposed to PA controlling all the QB's stats. (Short answer is it cannot, because the same instructions load the data.) 0x2be74: Rushing Power (RP) 0x2be84: Running Speed (RS)

## Key facts

- 0x2be74: Rushing Power (RP)
- 0x2be84: Running Speed (RS)
- See thread for explanation: [http://tecmobowl.org/topic/7070-trying-to-explain-the-concept-of-rs-rp-and-ms-to-malferds/](https://tecmobowl.org/topic/7070-trying-to-explain-the-concept-of-rs-rp-and-ms-to-malferds/)
- 0x2bee4: Pass Block (APB)
- 0x2bef4: Kick Block (AKB)
- 0x2bf04: Fumbles (BC)
- See this thread for the explanation on these  [http://tecmobowl.org/topic/7066-passing-game-ratings/page-2](https://tecmobowl.org/topic/7066-passing-game-ratings/page-2)
- 0x2bf14: Pass Control (PC)
- 0x2bf24: Receptions (REC)
- 0x2bf34 Interceptions (INT)
- (Edit: Updated list with info from below.)
- 0x2a7a0: Speed of arrow (KA)

## Topics

`attribute`, `kick`

## Source

<https://tecmobowl.org/topic/3989-player-attribute-probabilities/>
