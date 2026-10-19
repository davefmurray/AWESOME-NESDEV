---
name: tecmosuper-events
description: "Tecmo Super Bowl event and cutscene engine: bank/scene IDs, $C390/$C3A2/$C3AF calls, cutscene sequences, and the full event library. Use when triggering or editing TSB cutscenes, menus, halftime shows, touchdown scenes, or when an event call does nothing or crashes."
---

# Tecmo Super Bowl events

TSB calls its cutscenes, menus, scoreboards, halftime shows and message-bar slides **events**. An event is a **draw script** — it changes the screen, not the score, possession, or stats.

The single most common mistake is treating the event number as global. It is not. **The group is the draw-script bank, and the event is the scene ID inside that bank.** `$38` in bank 6 is a rushing touchdown; `$38` in bank 15 is an offensive-starter screen.

## Two layers, do not confuse them

| Layer | What it is | Where |
|---|---|---|
| **Sequence index** | Which cutscene *sequence* to play (punt, sack, FG…) | `CUTSCENE_TO_DRAW`, indexes `CUTSCENE_ADDR` |
| **Scene ID** | One drawing event inside a sequence | byte array in bank 6, terminated by `$FC`–`$FF` |

A sequence is just a list of scene IDs:

```asm
PUNT_CUT_SEQ:        .DB $03,$FE
QB_SACK_CUT_SEQ:     .DB $26,$FF
P2_FG_DOWN_MIDDLE:   .DB $04,$0E,$10,$11,$FF
```

`$03` is the punt scene, `$04` the field-goal scene, `$0E` the kick-toward-uprights scene. `$FE`/`$FF` end the list. This is why changing "the punt cutscene" means changing the array, not the `CUTSCENE_TO_DRAW` index.

## Calling an event

Arguments: **A = scene ID**, **X = bank ID**. All three entry points clobber A and X.

| Legacy address | Disassembly label | Behaviour |
|---|---|---|
| `$C390` | `END_OLD_SCENE_DRAW_NEW_SCENE` | Queue the scene and return immediately |
| `$C3A2` | `DRAW_SCENE_UNTIL_ENDED` | Queue and block until the draw task finishes |
| `$C3AF` | `DRAW_SCENE_RETURN_PREV_8000_BANK` | Save `$8000` bank, swap to bank `$17` (draw engine), draw, restore |

```asm
; single scene, wait for it
LDA #$38                 ; rushing touchdown
LDX #$06                 ; CUTSCENE_DRAW_SCRIPT_BANK
JSR DRAW_SCENE_UNTIL_ENDED

; menu / player-data screen: *** in the old list, needs the bank-swap call
LDA #$24                 ; QB data screen
LDX #$0F                 ; MENU_DRAW_SCRIPT_BANK
JSR DRAW_SCENE_RETURN_PREV_8000_BANK
```

Raw-ROM equivalents: `JSR $C390`, `JSR $C3A2`, `JSR $C3AF`.

### Which call?

- **Default:** `DRAW_SCENE_UNTIL_ENDED`. The next instruction runs after the scene is done.
- **Fire-and-forget:** `END_OLD_SCENE_DRAW_NEW_SCENE` only if you have a task/state machine that will wait; otherwise the next scene can overwrite this one.
- **`***` events:** `DRAW_SCENE_RETURN_PREV_8000_BANK`. These need bank 23 (`$17`) mapped while drawing menus and data screens. Using `$C3A2` for them is the classic "menu draws garbage" bug.

## The event library

- [`references/events-library.md`](references/events-library.md) — all 306 slots (228 named) in banks `06`, `07`, `0F`, with flags and canonical disassembly labels.
- [`references/events.csv`](references/events.csv) — same data, machine-readable. Columns: `bank_hex,bank_name,event_hex,name,flags,disassembly_label`.
- [`references/events.json`](references/events.json) — JSON for scripts.

Flags: `bank_swap` (`***`), `direction_left/right` (FG scenes), `unused`, `unassigned`.

Quick picks:

| Scene | Bank | ID | Use |
|---|---|---|---|
| Rushing TD | 6 | `38` | touchdown |
| Receiving TD | 6 | `39` | touchdown |
| First down (ref) | 6 | `3E` / `3F` | measurement |
| QB sack | 6 | `26` / `27` | sack, side change |
| Injury | 6 | `37` | injury |
| Halftime blimp | 6 | `49` | halftime |
| Scoreboard (no qtrs) | 7 | `1C` | injury/scoreboard |
| Final scoreboard (OT) | 7 | `4F` | end of game |
| Main menu | 15 | `00` | menu |
| Team data | 15 | `19` | menu |
| QB data | 15 | `24` | menu |

## Recipes

### 1. Play one scene from your own code

```asm
LDA #SCENE_ID
LDX #BANK_ID
JSR DRAW_SCENE_UNTIL_ENDED
```

Put the call in code that runs outside NMI and outside vblank-critical PPU work. The wait loop can take many frames.

### 2. Replace a scene in an existing sequence

1. Find the sequence label in `Bank19_20_on_field_gameplay_loop.asm` (search `CUTSCENE_SEQ` or the `CUTSCENE_ADDR` table).
2. Change one `.DB` value to another scene ID from the same bank (6).
3. Keep the terminator (`$FC`–`$FF`) and the length within the original array's space.

Example: make the punt sequence show the punt then a first-down marker:

```asm
PUNT_CUT_SEQ:  .DB $03,$3F,$FE
```

Only do this when there is room; adding a byte shifts everything after it unless the array has slack.

### 3. Add a scene when there is no room

1. Copy the sequence to free space in the same bank (or the fixed bank if you update the pointer).
2. Insert the new scene ID before the terminator.
3. Repoint the sequence's entry in `CUTSCENE_ADDR` to the new address.
4. Verify no other pointer shared the old sequence.

`CUTSCENE_ADDR` is a `.WORD` table; a wrong entry sends the player into data.

### 4. Trigger a menu or data screen

Use bank `0F` and the bank-swap call. `***` in the library means this is required.

### 5. Remove a scene

- From a sequence: delete the ID and shift the rest left, keeping one terminator.
- From a call site: replace the `JSR` with `NOP NOP NOP` (same 3 bytes), or skip the branch that reaches it.
- Whole sequence: point `CUTSCENE_ADDR` at a two-byte terminator (`$FE`) if you have one.

## Patching rules

- A `JSR abs` is 3 bytes. Changing only the 16-bit operand is safe if the call target stays the same.
- To add a call, find free space (`$FF` padding or an unused bank) and `JMP`/`JSR` to a trampoline there; then jump back.
- Do not put event calls in NMI. They block and use the draw task system.
- Do not start a new scene while a draw task is still active. Check the task status or use the waiting call.
- Save A/X/Y if the surrounding code needs them; the event routines do not preserve them.
- If you change the bank, restore it. The `$C3AF` variant does this for you; a raw `$C390` does not.
- Scene IDs are per bank. Copying an ID from bank `0F` into a bank `06` sequence draws something else.

## What events do not do

- They do not add points, change possession, or update stats.
- They do not update the play result; the gameplay code decides that separately.
- They do not fix a broken game state. If the score is wrong, the bug is in the logic, not the cutscene.

If you want "show the TD scene and then kick the extra point", the sequence controls the visuals and the gameplay code controls the down/possession transition. Change both deliberately.

## Testing

1. Trigger the scene from a save state; screenshot it.
2. For a sequence, watch it play to the end and confirm the next game state is correct.
3. Check the draw task ends (no frozen screen, no repeated scene).
4. For bank `0F`, open the menu, back out, and confirm the previous bank is restored.
5. Re-test a normal play that uses the same sequence.

## Failure modes

| Symptom | Cause |
|---|---|
| Wrong scene | Wrong bank for that ID, or sequence index vs scene ID confusion |
| Nothing happens | Called the queue-only entry point and never waited, or wrong bank |
| Garbage menu | `***` event called without the bank-swap variant |
| Crash / reset | Bad `CUTSCENE_ADDR` pointer, missing terminator, or overwritten code |
| Frozen after scene | Waiting call never sees the task end; wrong bank or corrupt script |
| Score/possession wrong | Event engine is visual only; fix the gameplay logic |

## References

- [events thread](https://tecmobowl.org/forums/topic/9946-events/) — original 2008 documentation
- [Disassembly](https://github.com/bruddog/Tecmo_Super_Bowl_NES_Disassembly) — `scene_ids.asm`, `cutscene_sequence_ids.asm`, `Bank19_20_on_field_gameplay_loop.asm`
- [Editing cutscenes](https://tecmobowl.org/topic/13387-an-easy-guide-to-changing-and-deleting-various-cutscenes/) — community guide
- `references/events-library.md` · `references/events.csv` · `references/events.json`
