# Tecmo Super Bowl event library

Complete catalogue of the event/scene IDs documented in the TecmoBowl.org thread [“events”](https://tecmobowl.org/forums/topic/9946-events/) (cxrom, 2008), cross-referenced with the [bruddog disassembly](https://github.com/bruddog/Tecmo_Super_Bowl_NES_Disassembly).

**How to read this:** the group (`X`) is the draw-script **bank number**; the event (`A`) is the **scene ID** inside that bank. The same `A` value means something different in another bank.

- `bank-swap` — the thread marks this `***`; call it through the bank-swapping entry point rather than the plain one.
- `left` / `right` — drive direction for field-goal scenes.
- `unused` — labelled unused in the thread; may be incomplete, but the thread reports they do not crash.
- `canonical` — label from the disassembly's scene enum, when one exists.
- Empty IDs are listed as unassigned ranges at the end of each bank. They are not in the thread; treat them as unknown, not safe.

> The 2008 list predates the 2025 disassembly. Where they disagree, the disassembly is newer; the thread's names are kept because they are what the community uses.

## Cutscene bank — `CUTSCENE_DRAW_SCRIPT_BANK` (0x06)

Gameplay cutscenes: kicks, catches, touchdowns, injuries, halftime, chains. Called from the gameplay loop with bank 6.

| ID | Event | Flags | Canonical label |
|---|---|---|---|
| `00` | Opening |  | `INTRO_SCENE_ID` |
| `01` | Title Screen |  | `START_SCREEN_SCENE_ID` |
| `02` | Kickoff |  | `KICKOFF_SCENE_ID` |
| `03` | Punt |  | `PUNT_SCREEN_SCENE_ID` |
| `04` | Field Goal |  | `FG_SCREEN_SCENE_ID` |
| `05` | JJ Incomplete (missed) |  | `DEFENSE_JUMP_MISS_SCENE_ID` |
| `06` | JJ Incomplete (tipped) |  | `DEFENSE_JUMP_TIPPED_SCENE_ID` |
| `07` | Incomplete (bounced) |  | `DEFENSE_TIPPED_SCENE_ID` |
| `08` | Incomplete Dive (missed) |  | `DEFENSE_DIVE_MISS_SCENE_ID` |
| `09` | Attempted Blocked Punt/FG/Pass |  | `BLOCK_MISS_SCENE_ID` |
| `0A` | Blocked Punt |  | `BLOCK_PUNT_SCENE_ID` |
| `0B` | Blocked FG |  | `BLOCK_FG_SCENE_ID` |
| `0C` | Blocked PAT |  | `BLOCK_XP_SCENE_ID` |
| `0D` | Blocked Pass |  | `BLOCK_PASS_SCENE_ID` |
| `0E` | Long FG Attempt |  | `KICK_TOWARDS_UPRIGHTS_SCENE_ID` |
| `0F` | FG Through Uprights [->] | right | `P1_KICK_THROUGH_UPRIGHTS_SCENE_ID` |
| `10` | FG Through Uprights [<-] | left | `P2_KICK_THROUGH_UPRIGHTS_SCENE_ID` |
| `11` | FG Good |  | `FG_GOOD_SCENE_ID` |
| `14` | Doink Left Upright, Good [->] | right | `P1_LEFT_UPRIGHT_GOOD_SCENE_ID` |
| `15` | Doink Right Upright, Good [->] | right | `P1_RIGHT_UPRIGHT_GOOD_SCENE_ID` |
| `16` | Doink Left Upright, Missed [->] | right | `P1_LEFT_UPRIGHT_MISS_SCENE_ID` |
| `17` | Doink Right Upright, Missed [->] | right | `P1_RIGHT_UPRIGHT_MISS_SCENE_ID` |
| `18` | Missed Left [->] | right | `P1_LEFT_UPRIGHT_WIDE_SCENE_ID` |
| `19` | Missed Right [->] | right | `P1_RIGHT_UPRIGHT_WIDE_SCENE_ID` |
| `1A` | Short FG [->] | right | `P1_SHORT_UPRIGH_SCENE_ID` |
| `1B` | Referee - No Good |  | `REF_NO_GOOD_SIGNAL` |
| `1C` | Doink Right Upright, Good [<-] | left | `P2_RIGHT_UPRIGHT_GOOD_SCENE_ID` |
| `1D` | Doink Left Upright, Good [<-] | left | `P2_LEFT_UPRIGHT_GOOD_SCENE_ID` |
| `1E` | Doink Right Upright, Missed [<-] | left | `P2_RIGHT_UPRIGHT_MISS_SCENE_ID` |
| `1F` | Doink Left Upright, Missed [<-] | left | `P2_LEFT_UPRIGHT_MISS_SCENE_ID` |
| `20` | Missed Right [<-] | left | `P2_RIGHT_UPRIGHT_WIDE_SCENE_ID` |
| `21` | Missed Left [<-] | left | `P2_LEFT_UPRIGHT_WIDE_SCENE_ID` |
| `22` | Short FG [<-] | left | `P2_SHORT_UPRIGHT_SCENE_ID` |
| `23` | Successful Try |  | `XP_GOOD_SCENE_ID` |
| `26` | QB Sack |  | `QB_SACK_SCENE_ID` |
| `27` | QB Sack + Side Change |  | `QB_SACK_SIDE_CHANGE_SCENE_ID` |
| `28` | Safety |  | `QB_SACK_SAFETY_SCENE_ID` |
| `29` | Bullet Pass |  | `QB_PASS_SCENE_ID` |
| `2B` | JJ Catch |  | `OFFENSE_JUMP_CATCH_SCENE_ID` |
| `2C` | JJ Incomplete (missed) |  | `OFFENSE_JUMP_MISS_SCENE_ID` |
| `2D` | JJ Incomplete (tipped) |  | `OFFENSE_JUMP_TIPPED_SCENE_ID` |
| `2F` | Catch |  | `OFFENSE_CATCH_SIDEWAYS_SCENE_ID` |
| `30` | Incomplete (bounced) |  | `OFFENSE_TIP_SIDEWAYS_SCENE_ID` |
| `31` | Incomplete Pass |  | `WHIFF_INCOMPLETE_PASS_SCENE_ID` |
| `32` | Complete Dive |  | `OFFENSE_DIVE_CATCH_SCENE_ID` |
| `33` | Incomplete Dive (missed) |  | `OFFENSE_DIVE_MISS_SCENE_ID` |
| `34` | Incomplete Dive (tipped) |  | `OFFENSE_DIVE_TIPPED_SCENE_ID` |
| `37` | Injury |  | `INJURY_SCENE_ID` |
| `38` | Rushing TD |  | `RUSHING_TOUCHDOWN_SCENE_ID` |
| `39` | Receiving TD |  | `PASSING_TOUCHDOWN_SCENE_ID` |
| `3A` | AFC Champion |  | `AFC_CHAMPION_SCENE_ID` |
| `3B` | Super Champion |  | `SUPER_BOWL_CHAMPION_SCENE_ID` |
| `3E` | First Down (Ref. faces left) |  | `FIRST_DOWN_REF_ARM_SCENE_ID` |
| `3F` | First Down (Ref. faces forward) |  | `FIRST_DOWN_SCENE_ID` |
| `40` | Second Down |  | `SECOND_DOWN_SCENE_ID` |
| `41` | Third Down |  | `THIRD_DOWN_SCENE_ID` |
| `42` | Fourth Down |  | `FOURTH_DOWN_SCENE_ID` |
| `43` | JJ Interception |  | `DEFENSE_JUMP_INT_SCENE_ID` |
| `44` | Super JJ |  | `DOUBLE_JUMP_CATCH_SCENE_ID` |
| `45` | Super JJ (missed) |  | `DOUBLE_JUMP_MISS_SCENE_ID` |
| `46` | Super JJ (missed) |  | `DOUBLE_JUMP_TIP_SCENE_ID` |
| `47` | Super JJ, Int (missed) |  | `DOUBLE_JUMP_INT_SCENE_ID` |
| `48` | Interception |  | `DEFENSE_INTERCEPTION_SCENE_ID` |
| `49` | Halftime - Blimp |  | `HALF_TIME_BLIMP_SCENE_ID` |
| `4A` | Halftime - Wink |  | `HALF_TIME_GIRL_WINK_SCENE_ID` |
| `4B` | Halftime - Band |  | `HALF_TIME_BAND_SCENE_ID` |
| `4C` | Halftime - Toss Cheerleader |  | `HALF_TIME_CHEERLEADER_TOSS_SCENE_ID` |
| `4D` | Halftime - Parachute |  | `HALF_TIME_PARACHUTE_WAVE_SCENE_ID` |
| `4E` | QB Stats -UNUSED- | unused | `DRAW_PLAYER_PORTAIT_WITH_LABELS_SCENE_ID` |
| `4F` | Halftime - Cheerleaders x2 |  | `HALF_TIME_CHEERLEADER_KICK_SCENE_ID` |
| `50` | Halftime - Kiss |  | `HALF_TIME_GIRL_KISS_SCENE_ID` |
| `51` | Catch, Dive Int |  | `DEFENSE_DIVE_MISS_WR_CATCH_SCENE_ID` |
| `52` | Catch, JJ Int |  | `DEFENSE_JUMP_MISS_WR_CATCH_SCENE_ID` |
| `53` | Incomp, Dive Int |  | `DEFENSE_DIVE_MISS_BOUNCE_OFF_WR_SCENE_ID` |
| `54` | Incomp, JJ Int |  | `DEFENSE_JUMP_MISS_BOUNCE_OFF_WR_SCENE_ID` |
| `55` | Dive Int |  | `DEFENSE_DIVE_INTERCEPTION_SCENE_ID` |
| `56` | Division Champs |  | `DIVISION_CHAMP_SCENE_ID` |
| `57` | Flashing "Press Start" at title |  | `FLASH_START_GAME_SCENE_ID` |
| `58` | Special Halftime Show |  | `MIGHTY_BOMBJACK_HALFTIME_SCENE_ID` |
| `59` | Halftime Show (Blimp, Wink, Band, Kiss) |  | `HALFTIME_1_SCENE_ID` |
| `5A` | Halftime Show (Parachute, The Wave, Cheerleaders x2, Toss Cheerleader) |  | `HALFTIME_2_SCENE_ID` |
| `5B` | Halftime Show (Cheerleaders x2, Band, Blimp, Wink) |  | `HALFTIME_3_SCENE_ID` |
| `5C` | Halftime Show (Wink, Cheerleaders x2, Toss Cheerleader, Kiss) |  | `HALFTIME_4_SCENE_ID` |
| `5D` | Yards Rushed -UNUSED- | unused | `YARDS_RUSH_TODAY_UNUSED_SCENE_ID` |
| `5E` | Yards Returned -UNUSED- | unused | `YARDS_RETURN_TODAY_UNUSED_SCENE_ID` |
| `5F` | Yards Received -UNUSED- | unused | `YARDS_RECEIVE_TODAY_UNUSED_SCENE_ID` |
| `60` | Interception TD -UNUSED- | unused | `INT_TD_UNUSED_SCENE_ID` |
| `61` | Defensive TD -UNUSED- | unused | `DEFENSE_TD_UNUSED_SCENE_ID` |
| `62` | Rush Yards Today -UNUSED- | unused | `RUSHING_YARDS_TODAY_UNUSED_SCENE_ID` |
| `63` | Rec Yards Today -UNUSED- | unused | `REC_YARDS_TODAY_UNUSED_SCENE_ID` |
| `64` | Sacks Today -UNUSED- | unused | `SACKS_YARDS_TODAY_UNUSED_SCENE_ID` |
| `65` | Int Today -UNUSED- | unused | `INT_TODAY_UNUSED_SCENE_ID` |
| `66` | 000Yards Rusher -UNUSED- | unused | `YARDS_RUSHER_UNUSED_SCENE_ID` |
| `67` | 000Yards Receiver -UNUSED- | unused | `YARDS_RECEIVER_UNUSED_SCENE_ID` |
| `68` | 000Yards Passer -UNUSED- | unused | `YARDS_PASSER_UNUSED_SCENE_ID` |
| `69` | Yellow Flag-False Start -UNUSED- | unused | `FALSE_START_SCENE_ID` |
| `6A` | Yellow Flag-Offsides -UNUSED- | unused | `OFFSIDE_SCENE_ID` |
| `6B` | NFC Champion |  | `NFC_CHAMPION_SCENE_ID` |
| `6E` | Credits |  | `CREDITS_SCENE_ID` |
| `6F` | Sound Test |  | `SOUND_MODE_SCENE_ID` |
| `70` | Chains + 1st Down [->] | right | `P1_CHAINS_FIRST_DOWN_SCENE_ID` |
| `71` | Chains + 2nd Down [->] | right | `CHAINS_SECOND_DOWN_SCENE_ID` |
| `72` | Chains + 3rd Down [->] | right | `CHAINS_THIRD_DOWN_SCENE_ID` |
| `73` | Chains + 4th Down [->] | right | `CHAINS_FOURTH_DOWN_SCENE_ID` |
| `74` | Chains + Change Sides [->] | right | `CHAINS_CHANGE_SIDE_SCENE_ID` |
| `75` | Chains + First Down [<-] | left | `P2_CHAINS_FIRST_DOWN_SCENE_ID` |
| `7E` | Incomp (bounced), Dive |  |  |

**Unassigned in this bank:** `12`–`13`, `24`–`25`, `2A`, `2E`, `35`–`36`, `3C`–`3D`, `6C`–`6D`, `76`–`7D`, `7F`

## Season / scoreboard bank — `LEADERS_SCOREBOARD_SCHED_DRAW_SCRIPT_BANK` (0x07)

Leaders, scoreboards, coin toss, week screens, playoff text, final scores.

| ID | Event | Flags | Canonical label |
|---|---|---|---|
| `00` | NFL Leaders |  | `NFL_LEADERS_SCENE_ID` |
| `01` | Leading Passers |  | `LEADING_PASSERS_SCENE_ID` |
| `04` | Leading Receiving |  | `LEADING_RECEIVERS_SCENE_ID` |
| `05` | Leading Rushing |  | `LEADING_RUSHERS_SCENE_ID` |
| `06` | Scoring |  | `LEADING_SCORERS_SCENE_ID` |
| `07` | Leading Punting |  | `LEADING_PUNTERS_SCENE_ID` |
| `08` | Interceptions |  | `INTERCEPTION_LEADERS_SCENE_ID` |
| `09` | Leading Sacks |  | `SACK_LEADERS_SCENE_ID` |
| `0A` | Punt Returns |  | `PR_LEADERS_SCENE_ID` |
| `0B` | Kickoff Returns |  | `KR_LEADERS_SCENE_ID` |
| `21` | Scoreboard (1->2) |  | `SCOREBOARD_Q1_SCENE_ID` |
| `22` | Scoreboard (2->3) |  | `SCOREBOARD_Q2_SCENE_ID` |
| `23` | Scoreboard (3->4) |  | `SCOREBOARD_Q3_SCENE_ID` |
| `26` | Injury Recovery |  | `RECOVERED_FROM_INJURY_SCENE_ID` |
| `27` | ?Opening Coin Toss |  | `COIN_TOSS_INTRO_SCENE_ID` |
| `2A` | ?Choose Kick -or- Receive (P1) |  | `CHOOSE_KICK_OR_RET_P1_SCENE_ID` |
| `2B` | ?Choose Kick -or- Receive (P2) |  | `CHOOSE_KICK_OR_RET_P2_SCENE_ID` |
| `2C` | Opening Coin Toss/Choose Kick -or- Receive (P1 wins) |  | `P1_WINS_COIN_TOSS_SCENE_ID` |
| `2D` | Opening Coin Toss/Choose Kick -or- Receive (P2 wins) |  | `P2_WINS_COIN_TOSS_SCENE_ID` |
| `31` | Overtime Coin Toss/Choose Kick -or- Receive (P1 wins) |  | `OT_COIN_TOSS_P1_WINS_SCENE_ID` |
| `32` | Overtime Coin Toss/Choose Kick -or- Receive (P2 wins) |  | `OT_COIN_TOSS_P2_WINS_SCENE_ID` |
| `34` | Black intro screen - "PRESEASON" |  | `PRESEASON_LARGE_TXT_SCENE_ID` |
| `35` | Black intro screen - "PROBOWL" |  | `PROBOWL_LARGE_TXT_SCENE_ID` |
| `36` | Black intro screen - "REGULAR SEASON 1ST WEEK" |  | `REG_SEAS_WEEK_1_SCENE_ID` |
| `37` | Black intro screen - "REGULAR SEASON 2ND WEEK" |  | `REG_SEAS_WEEK_2_SCENE_ID` |
| `38` | Black intro screen - "REGULAR SEASON 3RD WEEK" |  | `REG_SEAS_WEEK_3_SCENE_ID` |
| `39` | Black intro screen - "REGULAR SEASON 4TH WEEK" |  | `REG_SEAS_WEEK_4_SCENE_ID` |
| `3A` | Black intro screen - "REGULAR SEASON 5TH WEEK" |  | `REG_SEAS_WEEK_5_SCENE_ID` |
| `3B` | Black intro screen - "REGULAR SEASON 6TH WEEK" |  | `REG_SEAS_WEEK_6_SCENE_ID` |
| `3C` | Black intro screen - "REGULAR SEASON 7TH WEEK" |  | `REG_SEAS_WEEK_7_SCENE_ID` |
| `3D` | Black intro screen - "REGULAR SEASON 8TH WEEK" |  | `REG_SEAS_WEEK_8_SCENE_ID` |
| `3E` | Black intro screen - "REGULAR SEASON 9TH WEEK" |  | `REG_SEAS_WEEK_9_SCENE_ID` |
| `3F` | Black intro screen - "REGULAR SEASON 10TH WEEK" |  | `REG_SEAS_WEEK_10_SCENE_ID` |
| `40` | Black intro screen - "REGULAR SEASON 11TH WEEK" |  | `REG_SEAS_WEEK_11_SCENE_ID` |
| `41` | Black intro screen - "REGULAR SEASON 12TH WEEK" |  | `REG_SEAS_WEEK_12_SCENE_ID` |
| `42` | Black intro screen - "REGULAR SEASON 13TH WEEK" |  | `REG_SEAS_WEEK_13_SCENE_ID` |
| `43` | Black intro screen - "REGULAR SEASON 14TH WEEK" |  | `REG_SEAS_WEEK_14_SCENE_ID` |
| `44` | Black intro screen - "REGULAR SEASON 15TH WEEK" |  | `REG_SEAS_WEEK_15_SCENE_ID` |
| `45` | Black intro screen - "REGULAR SEASON 16TH WEEK" |  | `REG_SEAS_WEEK_16_SCENE_ID` |
| `46` | Black intro screen - "REGULAR SEASON 17TH WEEK" |  | `REG_SEAS_WEEK_17_SCENE_ID` |
| `47` | Black intro screen - "REGULAR SEASON 18TH WEEK" |  | `REG_SEAS_WEEK_18_SCENE_ID` |
| `48` | Black intro screen - "REGULAR SEASON WEEK" (small letters) -UNUSED- | unused | `REG_SEAS_SMALL_SCENE_ID` |
| `4E` | Final Scoreboard (No O.T.) |  | `SCOREBOARD_4Q_THEN_STATS_SCENE_ID` |
| `4F` | Final Scoreboard (O.T.) |  | `SCOREBOARD_OT_THEN_STATS_SCENE_ID` |

**Unassigned in this bank:** `02`–`03`, `0C`–`20`, `24`–`25`, `28`–`29`, `2E`–`30`, `33`, `49`–`4D`

## Menu / message bank — `MENU_DRAW_SCRIPT_BANK` (0x0F)

Menus, team and player data, playcalling, standings, and the in-game message-bar slidebars at 0x4F–0x66.

| ID | Event | Flags | Canonical label |
|---|---|---|---|
| `00` | Main Menu |  | `MAIN_MENU_SCREEN_ID` |
| `01` | Main Menu - Preseason Dropdown |  | `PRESEASON_MENU_SCREEN_ID` |
| `02` | Preaeason - Team Select |  | `PRESEASON_SELECT_TEAM_SCREEN_ID` |
| `03` | Season Menu |  | `SEASON_MENU_SCREEN_ID` |
| `04` | Team Control |  | `TEAM_CONTROL_SCREEN_ID` |
| `05` | NFL Schedule |  | `NFL_SCHEDULE_HEADER_SCREEN_ID` |
| `06` | NFL Schedule - Dropdown {Auto Skip, Playoffs, Reset} |  | `SCHEDULE_MENU_SCREEN_ID` |
| `07` | NFL Schedule - Reset Warning |  | `FIRST_SCHEDULE_RESET_WARN_SCREEN_ID` |
| `08` | NFL Schedule - Reset Final Warning |  | `FINAL_SCHEDULE_RESET_WARN_SCREEN_ID` |
| `09` | NFL Schedule - Auto Skip # |  | `SKIP_TO_WEEK_SCREEN_ID` |
| `0A` | Season - NFL Standings |  | `STANDINGS_MENU_SCREEN_ID` |
| `0C` | Season - Team Rankings |  | `RANKINGS_MENU_SCREEN_ID_EXTRA` |
| `0D` | Playoff Bracket |  | `PLAYOFF_BRACKET_SEASON_NOT_OVER_SCREEN_ID_DUPE_ONE` |
| `10` | Playoff Bracket |  | `PLAYOFF_BRACKET_SEASON_NOT_OVER_SCREEN_ID` |
| `17` | Main Menu - Probowl Dropdown |  | `PROBOWL_TEAM_TYPE_SCREEN_ID` |
| `18` | Probowl - Team Select |  | `PRO_BOWL_TEAM_CHOICE_SCREEN_ID` |
| `19` | Team Data |  | `TEAM_DATA_SCREEN_ID` |
| `1A` | Team Roster |  | `ROSTER_SCREEN_ID` |
| `1D` | DF Starters |  | `DEFENSIVE_STARTERS_SCREEN_ID` |
| `1E` | Play Book |  | `PLAYBOOK_SCREEN_ID` |
| `1F` | Play Chooser |  | `PLAYBOOK_RUN_CHANGE_SCREEN_ID` |
| `21` | AFC/NFC All Stars |  | `PRO_BOWL_TEAM_DATA_SCREEN_ID` |
| `24` | Player Data Screen QB | bank-swap | `QB_DATA_SCREEN_ID` |
| `25` | Player Data Screen RB,WR,TE | bank-swap | `RB_WR_TE_DATA_SCREEN_ID` |
| `26` | Player Data Screen OL | bank-swap | `OL_DATA_SCREEN_ID` |
| `27` | Player Data Screen Defense | bank-swap | `DEFENDER_DATA_SCREEN_ID` |
| `28` | Player Data Screen K | bank-swap | `KICKER_DATA_SCREEN_ID` |
| `29` | Player Data Screen P | bank-swap | `PUNTER_DATA_SCREEN_ID` |
| `2A` | AFC East Standings |  | `AFC_EAST_STANDINGS_TEXT_SCREEN_ID` |
| `2B` | AFC Central Standings |  | `AFC_CENT_STANDINGS_TEXT_SCREEN_ID` |
| `2C` | AFC West Standings |  | `AFC_WEST_STANDINGS_TEXT_SCREEN_ID` |
| `2D` | NFC East Standings |  | `NFC_EAST_STANDINGS_TEXT_SCREEN_ID` |
| `2E` | NFC Central Standings |  | `NFC_CENT_STANDINGS_TEXT_SCREEN_ID` |
| `2F` | NFC West Standings |  | `NFC_WEST_STANDINGS_TEXT_SCREEN_ID` |
| `30` | Standings Screen |  | `FOUR_TEAM_DIV_STANDINGS_SCREEN_ID` |
| `32` | OF Starters | bank-swap | `OFF_STARTERS_2WR_SCREEN_ID` |
| `38` | OF Starters - Starter Reset | bank-swap | `OFF_STARTER_RESET_SCREEN_ID` |
| `3A` | Team Rankings - Offense NFL |  | `NFL_OFFENSIVE_TEAM_RANKINGS_SCREEN_ID` |
| `3B` | Team Rankings - Offense AFC |  | `AFC_OFFENSIVE_TEAM_RANKINGS_SCREEN_ID` |
| `3C` | Team Rankings - Offense NFC |  | `NFC_OFFENSIVE_TEAM_RANKINGS_SCREEN_ID` |
| `3D` | Team Rankings - Defense NFL |  | `NFL_DFFENSIVE_TEAM_RANKINGS_SCREEN_ID` |
| `3E` | Team Rankings - Defense AFC |  | `AFC_DFFENSIVE_TEAM_RANKINGS_SCREEN_ID` |
| `3F` | Team Rankings - Defense NFC |  | `NFC_DFFENSIVE_TEAM_RANKINGS_SCREEN_ID` |
| `40` | Play Select Screen |  | `PLAY_SELECT_SCREEN_ID` |
| `41` | P1, Off Dropdown Menu | bank-swap | `P1_OFF_MENU_SCREEN_ID` |
| `42` | P1, Off "Call Timeout" | bank-swap | `P1_OFF_TIMEOUT_SCREEN_ID` |
| `44` | P1, Def Dropdown Menu | bank-swap | `P1_DEF_MENU_SCREEN_ID` |
| `45` | P1, Def "Call Timeout" | bank-swap | `P1_DEF_TIMEOUT_SCREEN_ID` |
| `47` | P2, Off Dropdown Menu | bank-swap | `P2_OFF_MENU_SCREEN_ID` |
| `48` | P2, Off "Call Timeout" | bank-swap | `P2_OFF_TIMEOUT_SCREEN_ID` |
| `4A` | P2, Def Dropdown Menu | bank-swap | `P2_DEFENSIVE_MENU_SCREEN_ID` |
| `4B` | P2, Def "Call Timeout" | bank-swap | `P2_DEF_TIMEOUT_SCREEN_ID` |
| `4E` | ??? Clock Bkg | bank-swap | `CLOCK_BACKGROUND_SCREEN_ID` |
| `4F` | ??? "#th Down ##" slidebar | bank-swap | `DOWN_MARKERS_1ST_10_MESSAGE_BAR_ID` |
| `50` | "\\\Fumble///" slidebar | bank-swap | `FUMBLE_MESSAGE_BAR_ID` |
| `51` | "Punt Kick" slidebar | bank-swap | `PUNT_KICK_MESSAGE_BAR_ID` |
| `52` | "Field Goal" slidebar | bank-swap | `FIELD_GOAL_MESSAGE_BAR_ID` |
| `53` | "Successful Try" slidebar | bank-swap | `SUCCESSFUL_TRY_MESSAGE_BAR_ID` |
| `54` | "No Good" slidebar | bank-swap | `NO_GOOD_MESSAGE_BAR_ID` |
| `55` | "First Down" slidebar | bank-swap | `FIRST_DOWN_MESSAGE_BAR_ID` |
| `56` | "Side Change" + "Next Offense ... Next Defense" slidebar | bank-swap | `SIDE_CHG_NEXT_OFF_NEXT_DEF_MESSAGE_BAR_ID` |
| `57` | "Side Change" + "Next Defense ... Next Offense" slidebar | bank-swap | `SIDE_CHG_NEXT_DEF_NEXT_OFF_MESSAGE_BAR_ID` |
| `58` | "TOUCHDOWN" slidebar | bank-swap | `TOUCHDOWN_LARGE_LETTERS_MESSAGE_BAR_ID` |
| `59` | "Try For Point" slidebar | bank-swap | `TRY_FOR_POINT_MESSAGE_BAR_ID` |
| `5A` | "SAFETY" slidebar | bank-swap | `SAFETY_LARGE_LETTERS_MESSAGE_BAR_ID` |
| `5B` | "Incomplete Pass" slidebar | bank-swap | `INCOMPLETE_PASS_MESSAGE_BAR_ID` |
| `5C` | "Touchback" slidebar | bank-swap | `TOUCHBACK_MESSAGE_BAR_ID` |
| `5D` | "Interception" slidebar | bank-swap | `INTERCEPTION_MESSAGE_BAR_ID` |
| `5E` | "Field Goal" slidebar | bank-swap | `FIELD_GOAL_MESSAGE_BAR_ID_2` |
| `5F` | "Recover" slidebar | bank-swap | `RECOVER_MESSAGE_BAR_ID` |
| `60` | "QB Sack" slidebar | bank-swap | `QB_SACK_MESSAGE_BAR_ID` |
| `61` | "\\\Kick Block///" slidebar | bank-swap | `KICK_BLOCK_MESSAGE_BAR_ID` |
| `62` | "\\\Blocked Punt///" slidebar | bank-swap | `BLOCKED_PUNT_MESSAGE_BAR_ID` |
| `63` | "\\\Pass Block///" slidebar | bank-swap | `ONSIDE_KICK_MESSAGE_BAR_ID` |
| `64` | "\\\Onside Kick///" slidebar | bank-swap | `PENALTY_MESSAGE_BAR_ID` |
| `65` | "\\\Penalty///" slidebar | bank-swap | `OUT_OF_BOUNDS_OFFSCREEN_MESSAGE_BAR_ID` |
| `66` | "Out of Bounds" slidebar | bank-swap | `OUT_OF_BOUNDS_ONSCREEN_MESSAGE_BAR_ID` |

**Unassigned in this bank:** `0B`, `0E`–`0F`, `11`–`16`, `1B`–`1C`, `20`, `22`–`23`, `31`, `39`, `43`, `46`, `49`, `4C`–`4D`

## Quick picks

| Want | Bank | Event | Call |
|---|---|---|---|
| Touchdown (rushing) | 6 | `38` | `LDA #$38 : LDX #$06 : JSR DRAW_SCENE_UNTIL_ENDED` |
| Touchdown (receiving) | 6 | `39` | same |
| First down (referee) | 6 | `3E` / `3F` | same |
| QB sack | 6 | `26` / `27` | same |
| Injury | 6 | `37` | same |
| Halftime blimp / band / kiss | 6 | `49` / `4B` / `50` | same |
| Scoreboard (1→2) | 7 | `21` | same, bank 7 |
| Final scoreboard (OT) | 7 | `4F` | same, bank 7 |
| Main menu | 15 | `00` | bank-swap call, bank 15 |
| Team data | 15 | `19` | bank-swap call, bank 15 |
| Player data (QB) | 15 | `24` | bank-swap call, bank 15 |

## Sources and caveats

- [events thread](https://tecmobowl.org/forums/topic/9946-events/) — IDs, names, direction flags, `***` markers.
- [Disassembly `scene_ids.asm`](https://github.com/bruddog/Tecmo_Super_Bowl_NES_Disassembly/blob/main/constants_variables/scene_ids.asm) — canonical labels and the bank enum.
- The thread's list ends at `7E` for bank 6; the disassembly enum ends at `77`. Treat `78–7E` as unverified.
- The message-bar entries `4F–66` in bank 15 correspond to the disassembly's `IN_GAME_STATUS_BAR_SCENE_IDS` at `00–17` (offset `0x4F`).
- `$C390/$C3A2/$C3AF` are the legacy addresses from the thread; the disassembly names them `END_OLD_SCENE_DRAW_NEW_SCENE`, `DRAW_SCENE_UNTIL_ENDED`, and `DRAW_SCENE_RETURN_PREV_8000_BANK`.
