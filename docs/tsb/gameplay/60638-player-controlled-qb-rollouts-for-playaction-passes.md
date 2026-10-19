# Player-controlled QB rollouts for playaction passes

**Source:** https://tecmobowl.org/forums/topic/60638-player-controlled-qb-rollouts-for-playaction-passes  
**Category:** GAMEPLAY → Player Attributes During Gameplay  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/60638-player-controlled-qb-rollouts-for-playaction-passes).

## Summary

This code will give the MAN player control over his QB immediately after the fake handoff on the four long rollout pass plays (Pro T Waggle R, Pro T Waggle L, Roll Out R, and Roll Out L), so you can choose to continue the prescribed rollout or break it off as necessary and do your own thing. If you do this, I recommend upgrading the blitz byte for the defense because, otherwise, calling the offense's play on defense is a BAD thing for the defense. They send all 11 players at the QB, relatively slowly, allowing the QB enough time to get the ball off to wide open receivers with nothing but green to the endzone. I would use the "DA" blitz byte because that sends the front seven defense to the QB and much faster, and drops all four defensive backs into coverage. So, here's the code for…

## Key facts

- SET(0x8db8,0xe4d800c0d808b8d818b0)
- SET(0x8502,0xe4d8e0c0d8d8c0)
- SET(0x881d,0xe4d8f8b8d800b0d810a8)
- SET(0x8b83,0xe4d8f8c8d8f4bcd8e8b4d8d8b0)
- SET(0x1dd14,0xda)
- SET(0x1dd24,0xda)
- SET(0x1dd2c,0xda)
- SET(0x1dd34,0xda)

## Topics

`playbook`, `endzone`

## Source

<https://tecmobowl.org/forums/topic/60638-player-controlled-qb-rollouts-for-playaction-passes>
