---
name: tecmosuper-sim
description: "Tecmo Super Bowl simulation and CPU logic: COM juice, run/pass weights, sim attributes, play calling, coverage and season simulation. Use when tuning CPU difficulty, sim stats, playoff outcomes, or when a change works in a played game but not in sim."
---

# Tecmo Super Bowl sim and COM logic

The **sim** engine (skipped/coached games) is not the on-field engine. It reads its own attributes, weights and juice values. A gameplay hack that feels right in exhibition can have zero effect on a simulated season.

## Where sim lives

| Area | Location | Notes |
|---|---|---|
| Sim code | file `0x18163–0x1869F` | play call, timeout, sub, stats, skip mode |
| Sim data / situational | bank `0B`/`0C` | per-team weights, stats update |
| COM juice | per-team values | difficulty boost applied in season/playoffs |
| Sim attributes | documented table | separate from on-field ratings |
| COM play calling | bank `0C` + bank `19` | run/pass, go-for-it, punt/FG |
| Defensive coverage | banks `12`–`16` | reaction, pursuit, coverage |

## The three knobs

1. **Juice** — flat boosts applied to COM players. The "COM Defensive Juice" cards give the hex locations and a helper spreadsheet/workflow.
2. **Weights** — run/pass ratio, go-for-it, punt/FG decisions. These are probabilities, not constants.
3. **Attributes** — sim uses its own attribute table; changing the on-field rating may not change the sim.

Change one knob at a time. Juice and weights interact: raising juice without adjusting weights can make COM pass every down.

## Workflow

1. **Baseline.** Sim a season (or 20 games) with the unmodified ROM; record W-L, points, pass/run split, sacks, turnovers.
2. **Pick one knob.** Juice, run/pass weight, go-for-it, or a sim attribute.
3. **Change one value** in a copy.
4. **Re-run the same schedule** with the same teams and settings.
5. **Compare distributions**, not one game. A single 42–7 result is noise.
6. **Check the played game** if the hack touches shared code; sim-only values should not change exhibition.
7. **Check playoffs/OT** if the change affects clock or decisions.

## Doc map

Start with the [CPU & SIM category index](../../docs/tsb/README.md#cpu-and-sim).

| Topic | Card |
|---|---|
| Juice intro | [COM Defensive Juice: Introduction](../../docs/tsb/cpu-sim/10781-com-defensive-juice-introduction.md) |
| Juice hex | [COM Defensive Juice: HEX Locations](../../docs/tsb/cpu-sim/7144-65571-com-defensive-juice-hex-locations.md) |
| Juice helper | [COM Defensive Juice Modification Helper](../../docs/tsb/cpu-sim/11363-com-defensive-juice-modification-helper.md) |
| Run/pass ratio | [COM RUN / PASS Ratio](../../docs/tsb/cpu-sim/6677-com-run-pass-ratio.md) · [Weights](../../docs/tsb/cpu-sim/10511-modify-com-run-pass-ratio-weights.md) |
| Sim attributes | [COM Sim Attribute Locations](../../docs/tsb/cpu-sim/12519-com-sim-attribute-locations.md) |
| Play calling | [COM Play Calling/Go For It](../../docs/tsb/cpu-sim/10793-com-play-calling-go-for-it-general-logic.md) |
| Coverage | [COM Enhanced Coverage](../../docs/tsb/cpu-sim/10781-94279-com-enhanced-coverage.md) · [Find Open Receiver](../../docs/tsb/cpu-sim/53837-com-find-open-receiver.md) |
| Ultra logic | [COM Ultra Logic Hack](../../docs/tsb/cpu-sim/11474-com-ultra-logic-hack.md) |
| Movement | [COM Control Movement Logic Summary](../../docs/tsb/cpu-sim/63064-com-control-movement-logic-summary.md) |
| SKP vs SKP | [SKP pass distribution](../../docs/tsb/cpu-sim/70386-change-skp-vs-skp-pass-distribution-to-a-default-global-value.md) |

## Checks

- Did you change a **sim** table or a **played-game** table?
- Is the value per-team or global?
- Did you test a full season, not one game?
- Does the change alter playoff seeding or OT?
- Did juice and weights both change (double-tuning)?
- Is the 32-team ROM using the same sim table?

## Failure modes

| Symptom | Cause |
|---|---|
| Played game changes, sim does not | Edited the on-field table |
| Sim changes, played game does not | Edited a sim-only weight |
| CPU unstoppable | Juice too high, or weights collapsed to one play |
| Stats absurd | Sim attribute scale differs from on-field rating |
| One team affected | Per-team table, not global |

## References

- [CPU & SIM index](../../docs/tsb/README.md#cpu-and-sim) — all 14 cards
- [Set commands list](https://tecmobowl.org/forums/topic/69338-set-commands-list-for-nes-tsb-updated-91725/)
- [Gameplay](../tecmosuper-gameplay/SKILL.md) · [Data](../tecmosuper-data/SKILL.md)
