---
name: tecmosuper-gameplay
description: "Tecmo Super Bowl gameplay tuning: field goals, kickoffs, punting, quarter/clock length, first downs, injuries, fumbles, grappling, conditions and player movement. Use when changing TSB rules, probabilities or kicking behavior, or when a gameplay hack works in one mode but not another."
---

# Tecmo Super Bowl gameplay

TSB has two engines that look similar and are not: the **played game** (on-field loop, banks 18–22) and the **sim** (banks 11–12, 25). A hack that changes a played-game probability often does nothing in simulated games, and vice versa.

## Where gameplay lives

| Area | Banks / offsets | Notes |
|---|---|---|
| On-field loop | banks `12`–`16` (CPU `$8000` windows) | player movement, collisions, play result |
| Play commands | banks `04`, `05` | per-player scripts |
| Sim | banks `0B`, `0C`, `19` | sim logic, stats, COM decisions |
| Attributes | file `0x2BE74+` blocks | RP/RS/APB/AKB/BC/PC/REC/INT arrays |
| Kicking constants | `0x2A7A0` (arrow speed), `0x2A534`/`0x2BF93` (kickoff length) | file offsets |
| Menus/clock display | bank `0F` scripts | visual only |

Attribute block examples (file offsets, 16-byte stride per team/player group):

```
0x2BE74  Rushing Power (RP)
0x2BE84  Running Speed (RS)
0x2BEE4  Pass Block (APB)
0x2BEF4  Kick Block (AKB)
0x2BF04  Fumbles (BC)
0x2BF14  Pass Control (PC)
0x2BF24  Receptions (REC)
0x2BF34  Interceptions (INT)
```

Verify the block against the current ROM before writing; 32-team ROMs relocate some tables.

## Workflow

1. **Name the behavior** precisely: "CPU punts on 4th down in the 4th quarter", not "special teams".
2. **Decide played vs sim.** Both may need a change.
3. **Find the doc card** in [the gameplay index](../../docs/tsb/README.md#gameplay). It gives the offsets or the `SET` command.
4. **Change one value** in a copy.
5. **Test the trigger condition** in exhibition, then season/sim.
6. **Run enough trials.** Probability changes need dozens of plays; one game proves nothing.
7. **Test P1, P2 and COM.** Some code paths are side-specific.

## Kicking

- **FG accuracy** is a combination of kicker attributes, arrow speed and the accuracy check; the "Determining and Modifying FG Accuracy" card is the map.
- **FG length / arrow speed**: `0x2A7A0` is the arrow-speed value; the FG length thread has the distance check.
- **Kickoff length**: `SET(0x2A534,0x4C83BF)` plus a routine at `0x2BF93` is the common range hack. Keep the two writes together.
- **Punting**: length/coverage, directional punts and COM punt timing are separate hacks.
- **Extra point distance**: 15-yard XP is a documented `SET`; it changes the snap, not just the display.
- **Touchbacks/onside**: separate probabilities and field-position rules.

## Clock and rules

- Quarter length, clock speed and time-between-plays are separate values.
- First-down yardage, number of downs and OT rules are rule changes, not display changes.
- Changing quarter length can affect sim stats and season pacing.

## Injuries, fumbles, conditions

- Injury probability, injury return rate and skip-mode injuries are separate.
- Fumble probability, post-TD fumbles and recovery odds are separate.
- Condition changes (Excellent/Good/Average/Bad) are driven by probabilities and the condition table; "average condition permanently" is a different hack.
- Grappling has HP, time-limit and COM-differential hacks; they interact.

## Doc map

Start with the [gameplay category index](../../docs/tsb/README.md#gameplay).

| Topic | Card |
|---|---|
| FG accuracy | [Determining and Modifying FG Accuracy](../../docs/tsb/gameplay/70424-determining-and-modifying-fg-accuracy.md) |
| FG length | [Field Goal Length](../../docs/tsb/gameplay/4167-field-goal-length.md) |
| FG arrow speed | [Field Goal Arrow Speed](../../docs/tsb/gameplay/3989-field-goal-arrow-speed.md) |
| Kickoff length | [Kickoff Length](../../docs/tsb/gameplay/11291-kickoff-length.md) |
| Punting | [Punting Length / Coverage](../../docs/tsb/gameplay/4162-punting-length-coverage.md) · [Directional Punts](../../docs/tsb/gameplay/62839-directional-punts.md) |
| Quarter length | [Quarter Length](../../docs/tsb/gameplay/9111-339861-quarter-length.md) |
| Clock speed | [Clock Speed](../../docs/tsb/gameplay/11290-clock-speed-time-between-plays.md) |
| Injuries | [Injuries & Probabilities](../../docs/tsb/gameplay/4363-injuries-probabilities.md) · [Injury Return Rate](../../docs/tsb/gameplay/66654-injury-return-rate.md) |
| Fumbles | [Fumble Probability Table](../../docs/tsb/gameplay/58620-fumble-probability-table.md) |
| Conditions | [Conditions Change Explanation](../../docs/tsb/gameplay/58030-424391-conditions-change-explanation.md) |
| Grappling | [Grappling: Time Limit](../../docs/tsb/gameplay/11821-grappling-time-limit.md) · [HP Hack NES](../../docs/tsb/gameplay/9586-grappling-hp-hack-nes.md) |


## Checks

- Is the hack for played games, sim, or both?
- Does it apply to P1, P2 and COM?
- Did you test the exact down/distance/quarter trigger?
- Is the `SET` offset for your base ROM (28 vs 32 team)?
- Did another gameplay hack already write that byte?
- Does the change survive a full game and a quarter change?

## Failure modes

| Symptom | Cause |
|---|---|
| Nothing changes | Sim-only or played-only path; wrong trigger |
| Works once, then reverts | Another routine rewrites the value each play |
| Both teams affected | Shared table, not a side-specific value |
| Stats drift | Sim logic uses a different table than the played game |
| Crash on 4th down | Overwrote the punt/FG decision code, not a constant |

## References

- [Gameplay category index](../../docs/tsb/README.md#gameplay) — all 70 cards
- [Set commands list](https://tecmobowl.org/forums/topic/69338-set-commands-list-for-nes-tsb-updated-91725/)
- [ROM map](../tecmosuper-rom-map/SKILL.md) · [Sim](../tecmosuper-sim/SKILL.md)
