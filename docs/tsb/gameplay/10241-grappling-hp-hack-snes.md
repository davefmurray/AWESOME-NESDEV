# Grappling: HP Hack (SNES)

**Source:** https://tecmobowl.org/forums/topic/10241-snes-tsb-i-improved-grappling-code/  
**Category:** GAMEPLAY → Player Attributes During Gameplay  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked forum post. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/10241-snes-tsb-i-improved-grappling-code/).

## Summary

At x1D010: MAN VS CPU GRAPPLING: A0 1C LDY #$1C B1 63 LDA ($63),Y ; LOAD PLAYER HP 4A LSR 4A LSR 4A LSR C8 INY 18 CLC 71 63 ADC ($63),Y ; HP/8 + Presses 91 63 STA ($63),Y 20 0E C4 JSR $C40E ; LOAD CPU PLAYER A0 1C LDY #$1C B1 03 LDA ($03),Y ; LOAD CPU HP 4A LSR 4A LSR 4A LSR C8 INY 91 03 STA ($03),Y ; HP/8 AD 02 02 LDA $0202 ; RANDOM NUMBER 29 0F AND #$0F ; Make Random x0-F 18 CLC 71 03 ADC ($03),Y ; HP/8 + RANDOM 91 03 STA ($03),Y ; RETURN TO NORMAL B1 63 LDA ($63),Y 60 RTS MAN VS MAN GRAPPLING: A0 1C LDY #$1C B1 63 LDA ($63),Y ; LOAD OFFENSE HP 4A LSR 4A LSR 4A LSR C8 INY 18 CLC 71 63 ADC ($63),Y ; HP/8 + Presses 91 63 STA ($63),Y AD 02 02 LDA $0202 ; RANDOM NUMBER 29 03 AND #$03 ; Make Random x0-3 18 CLC 71 63 ADC ($63),Y ; HP/8 + Presses + RANDOM 91 63 STA ($63),Y A0 1C LDY #$1C B1…

## Key facts

- TSB I rom with no header:
- 20 10 D0  JSR $D010 ; MAN VS CPU GRAPPLING
- D1 03     CMP ($03),Y
- 20 37 D0  JSR $D037 ; MAN VS MAN GRAPPLING
- D1 63     CMP ($63),Y
- A0 1C     LDY #$1C
- B1 63     LDA ($63),Y ; LOAD PLAYER HP
- 71 63     ADC ($63),Y ; HP/8 + Presses
- 91 63     STA ($63),Y
- 20 0E C4  JSR $C40E ; LOAD CPU PLAYER
- B1 03     LDA ($03),Y ; LOAD CPU HP
- 91 03     STA ($03),Y ; HP/8

## Source

<https://tecmobowl.org/forums/topic/10241-snes-tsb-i-improved-grappling-code/>
