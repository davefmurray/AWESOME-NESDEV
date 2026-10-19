# Grappling: HP Hack (NES)

**Source:** https://tecmobowl.org/forums/topic/9586-nes-improved-grappling-code/  
**Category:** GAMEPLAY → Player Attributes During Gameplay  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/9586-nes-improved-grappling-code/).

## Summary

Here is some code I'm working on for improved human grappling. This code is loosely tested and I haven't looked at the 32-team rom to see if it fits. I would love to see any comments or suggestions from those that try this. HP has been added into the equation for the players.

## Key facts

- HP has been added into the equation for the players.
- HP is scaled from of 0 to 7 presses where 6 HP = 0 and 100 HP = 7
- CPU has random number of presses rather than 2. Presses will range from 0 to 15 presses. In comparison, I'm a horrible grappler online and get 6 presses normally in the emulator FCEUXD.
- NEW: Man vs Man now has random presses added in.
- 20 40 BF  JSR $BF40 ; MAN VS CPU GRAPPLING
- D1 3E     CMP ($3E),Y
- 20 66 BF  JSR $BF66 ; MAN VS MAN GRAPPLING
- D1 AE     CMP ($AE),Y
- A0 1C     LDY #$1C
- B1 AE     LDA ($AE),Y ; LOAD PLAYER HP
- 71 AE     ADC ($AE),Y ; HP/8 + Presses
- 91 AE     STA ($AE),Y

## Topics

`32-team`

## Source

<https://tecmobowl.org/forums/topic/9586-nes-improved-grappling-code/>
