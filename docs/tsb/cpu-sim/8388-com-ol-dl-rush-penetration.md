# COM OL / DL Rush Penetration

**Source:** https://tecmobowl.org/topic/8388-changing-the-differential-for-popcorning-dl-busting-through/  
**Category:** CPU & SIM  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/8388-changing-the-differential-for-popcorning-dl-busting-through/).

## Summary

The OL/DL grapple routine lives at 0x28360. The original compares offensive and defensive HP and throws one side when the gap is large; the community hack narrows the constants so an even matchup can still produce a popcorn or a quick DL penetration. Two SET variants and a SNES port are in the thread.

## Key facts

- Routine: `0x28360` (file offset) through about `0x28383`; it compares HP from `0x3DFFF–0x3E00E`.
- BRUDDOG variant: `SET(0x28360,0xB1AE91AEA53D291F1871AEF13E9008C91DB007C904B0064C84844C0F842036B1EAEAEAEAEAEA)`
- Earlier variant: `SET(0x28360,0xB1AE38F13E91AE...)`; the thread explains which constants to widen/narrow.
- Lower the red value → defender thrown more; raise blue toward red → offense thrown more.
- SNES port: `SET(0x18DB8, ...)`; not NES.

## Source

<https://tecmobowl.org/topic/8388-changing-the-differential-for-popcorning-dl-busting-through/>
