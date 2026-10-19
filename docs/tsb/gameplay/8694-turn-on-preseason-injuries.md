# Turn On Preseason Injuries

**Source:** https://tecmobowl.org/forums/topic/8694-preseason-injuries/  
**Category:** GAMEPLAY → Injuries  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/8694-preseason-injuries/).

## Summary

> On 7/2/2015 at 5:06 PM, bruddog said: > > This it a slightly more more correct way to do the preseason injuries hack....the other way sort of changes something that might have a possible side effect. > > @0x25EA1 > > **ORIGINAL CODE** > > LDA $2D ; LOAD GAME STATUS > AND #$03 ; PRESERVE LAST TWO BITS > CMP #$02 ; IS SEASON or PLAYOFFS? (0= preseason, 1=pro bowl, 2= season, 3 = playoffs) > BCC @Loop1 ; NO->BRANCH TO NO INJURY > > A52D2903C902901E > > **NEW CODE (INJURIES IN ALL MODES)** > > NOP x8 ; CPU cycle waste no-op > > SET (0x25EA1, 0xEAEAEAEAEAEAEAEA) > > NEW CODE (NO INJURIES INJUIRES IN PROBOWL ONLY) > > LDA $2D ; LOAD GAME STATUS > AND #$01 ; > CMP #$01 ; IS PROBOWL? (0= preseason, 1=pro bowl) > BEQ @Loop1 ; NO->BRANCH TO NO INJURY > > SET (0x25EA1,A52D2901C901F01E) It seems…

## Key facts

- > On 7/2/2015 at 5:06 PM, bruddog said:
- > @0x25EA1
- > LDA $2D                     ; LOAD GAME STATUS
- > AND #$03                   ; PRESERVE LAST TWO BITS
- > CMP #$02                   ; IS SEASON or PLAYOFFS? (0= preseason, 1=pro bowl, 2= season, 3 = playoffs)
- > SET (0x25EA1, 0xEAEAEAEAEAEAEAEA)
- > AND #$01                   ;
- > CMP #$01                   ; IS PROBOWL? (0= preseason, 1=pro bowl)
- > SET (0x25EA1,A52D2901C901F01E)
- (Also, will SET (0x25EA1,A52D2901C901F01E) leave injuries on for playoffs as well?)
- SET (0x25EA1,A52D2900C901F01E) # Clear bits in register and CMP #$01 -> non-zero
- SET (0x25EA1,A52D2903C904F01E) # CMP #$04 which should always be non-zero regardless of game mode

## Topics

`playoff`, `pro bowl`

## Source

<https://tecmobowl.org/forums/topic/8694-preseason-injuries/>
