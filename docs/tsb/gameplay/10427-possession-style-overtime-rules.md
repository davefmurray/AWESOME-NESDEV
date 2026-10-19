# Possession-style Overtime Rules

**Source:** https://tecmobowl.org/forums/topic/10427-possession-style-overtime/  
**Category:** GAMEPLAY → Gameplay Clock, Playbook Clock, Quarter scores  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/10427-possession-style-overtime/).

## Summary

Notes from working on a possession-style overtime (still in final thorough testing). Each team will have the same chance to score during overtime. Unlike NCAA, kickoffs will start possessions after scores and play will continue as normal. ``` .define P1_BALL #$00 .define P2_BALL #$01

## Key facts

- .define P1_BALL       #$00
- .define P2_BALL       #$01
- .define PLAY_SCREEN   #$05
- .define XP_PTS        #$01
- .define SAFETY_PTS    #$02
- .define FG_PTS        #$03
- .define TD_PTS        #$06
- .define SCORE1        $0395
- .defien FSCORE1       $0399
- .define SCORE2        $039A
- .define FSCORE2       $039E
- .define RESET         $7FC6

## Topics

`kick`, `field goal`, `text`

## Source

<https://tecmobowl.org/forums/topic/10427-possession-style-overtime/>
