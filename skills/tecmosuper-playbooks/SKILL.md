---
name: tecmosuper-playbooks
description: "Tecmo Super Bowl playbooks and play design: offensive/defensive play scripts, play pointers, default playbook tables, play names, formation data and run/pass slots. Use when changing a team's plays, designing a play, swapping playbooks, or debugging a play that runs the wrong script."
---

# Tecmo Super Bowl playbooks

A TSB play is four linked pieces:

```
playbook slot → play index → play name/pointer → per-player script
```

Change the slot and you change *which* play; change the script and you change *what the players do*. Most broken playbook hacks change one without the other.

## Where plays live

| Piece | Location | Notes |
|---|---|---|
| Formations / offensive play pointers | bank `02` (`0x4010+`) | formation positions + pointer table |
| Offensive play scripts | bank `04` (`0x8010–0x9FFF`) | per-player command bytecode |
| Defensive play pointers | bank `03` (`0x6010+`) | point into bank 5 |
| Defensive play scripts | bank `05` (`0xA010–0xBFFF`) | per-player command bytecode |
| Team default playbooks | `0x1D310` | which plays each team starts with |
| Play names + pointers | `0x1D410–0x1DA10` | name table and play index mapping |
| Defensive reaction bytes | `0x1DC10` | AI reaction per play |
| Playbook menu | bank `0F` script | visual list; not the play data |

All offsets are file offsets in the 28-team USA ROM; 32-team ROMs relocate some tables.

## Play script format

Offensive and defensive scripts are bytecode consumed by the play-command engine (banks 20–22). A script is a sequence of commands: move, block, rush, cover, targeted player, duration. The "Play Design / HEX Guide" and "Offensive Playbook HEX Guide" decode the opcodes; the "Offensive Playbook Design Guide" explains the design constraints.

Do not invent opcodes. Copy a working play and change one command at a time.

## Workflow

1. **Decide the layer:**
   - Different play for a team → playbook slot.
   - Same play, different behavior → script.
   - Different defensive reaction → reaction bytes.
2. **Map the slot:** read the team's entry in the default playbook table (`0x1D310`), get the play index.
3. **Map the index:** use the play-name/pointer table (`0x1D410`) to find the script address.
4. **Edit or swap:**
   - swap the pointer to an existing play (safest)
   - edit a copy of the script in free space (more control)
5. **Defensive reaction:** if the play is new, set the reaction bytes so the AI knows what it is.
6. **Test:** exhibition vs COM, exhibition vs human, then a season game. Check the play name and the actual behavior.

## Playbook slots

- TSB's playbook has a fixed number of run and pass slots; the "RUN / PASS Slots Code" and "Change The Number of Run and Pass Plays" cards cover the limits.
- Changing the count changes menu layout and AI expectations, not just the list.
- The Pro Bowl uses a separate playbook table.
- 32-team ROMs may use different default tables.

## Doc map

Start with the [playbook category index](../../docs/tsb/README.md#playbook).

| Topic | Card |
|---|---|
| Design guide | [Offensive Playbook Design Guide](../../docs/tsb/playbook/10528-offensive-playbook-design-guide.md) |
| Hex/opcode guide | [Play Design / HEX Guide](../../docs/tsb/playbook/7218-play-design-hex-guide.md) · [Offensive Playbook HEX Guide](../../docs/tsb/playbook/854-offensive-playbook-hex-guide.md) |
| Default playbooks | [Default Playbook Points / ROM Data](../../docs/tsb/playbook/7563-default-playbook-points-rom-data.md) |
| Run/pass slots | [RUN / PASS Slots Code](../../docs/tsb/playbook/52877-run-pass-slots-code.md) · [Change the Number of Run and Pass Plays](../../docs/tsb/playbook/7059-change-the-number-of-run-and-pass-plays.md) |
| Bank structure | [TSB ROM Bank Dissected](../../docs/tsb/playbook/11582-tsb-rom-bank-dissected.md) |
| Pro Bowl | [Pro Bowl Playbooks](../../docs/tsb/playbook/11494-100649-pro-bowl-playbooks.md) |

## Checks

- Does the playbook slot point at the play you think?
- Does the play pointer land on a valid script boundary?
- Did you update the defensive reaction bytes?
- Is the play name table still consistent (no shifted strings)?
- Did you test vs COM **and** vs a human?
- Does the play still work after a quarter change or a season game?
- For 32-team, are the tables relocated?

## Failure modes

| Symptom | Cause |
|---|---|
| Wrong play runs | Slot points at a different index |
| Players stand still | Bad script pointer or unsupported opcode |
| Defense does nothing | Reaction bytes not set |
| Menu shows wrong name | Play-name table index mismatch |
| Crash on play call | Pointer into the middle of a script |
| Works in exhibition, not season | Different playbook table / 32-team relocation |

## References

- [Playbook category index](../../docs/tsb/README.md#playbook) — all 11 cards
- [Disassembly](https://github.com/bruddog/Tecmo_Super_Bowl_NES_Disassembly) — `Bank5_6_off_def_play_data.asm`, `Bank15_faces_playbooks.asm`
- [ROM map](../tecmosuper-rom-map/SKILL.md) · [Gameplay](../tecmosuper-gameplay/SKILL.md)
