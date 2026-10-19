# Bump Success Rate

**Source:** https://tecmobowl.org/topic/56716-changing-the-bumping-probability-success-rate/  
**Category:** GAMEPLAY → Player Attributes During Gameplay  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/56716-changing-the-bumping-probability-success-rate/).

## Summary

[Via this topic](https://tecmobowl.org/topic/56409-bumping-question/?p=374440) > Maybe I didn't post it on the forum or thought I did as I can't seem to find it. The game loads a random number. There is basically a 75% chance you free up the drone. > > > > > Change 0x2829a to change the %. This does is not coded exactly like some of the other probability events. It's doing a bitwise AND and checking to see if it gets a zero. > > > > > 0x2829a DEFAULT 03= defender freed ~75% > > > > > > If you wanted to change it by just changing that one value. > > > > > 02 or 01= defender freed ~50% > > > > 00= defender freed 0% > > > > > Otherwise more code for something less than 75% and other than 50% or 0%.

## Key facts

- [Via this topic](https://tecmobowl.org/topic/56409-bumping-question/?p=374440)
- > Change 0x2829a to change the %. This does is not coded exactly like some of the other probability events. It's doing a bitwise AND and checking to see if it gets a zero.
- > 0x2829a DEFAULT  03= defender freed ~75%

## Topics

`event`

## Source

<https://tecmobowl.org/topic/56716-changing-the-bumping-probability-success-rate/>
