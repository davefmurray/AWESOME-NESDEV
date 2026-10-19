# COM vs COM Grappling Differential

**Source:** https://tecmobowl.org/forums/topic/10241-snes-tsb-i-improved-grappling-code/  
**Category:** CPU & SIM → Attributes, Play Ratio, SIM Stats  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/10241-snes-tsb-i-improved-grappling-code/).

## Summary

As requested, I took a look at the SNES version and ported my NES code over. The following is the same as the NES version posted and any of the other grappling methods (mine, Buck, Bruddog, etc) could be ported using the equivalent values (let me know if you would like the other codes options listed). I would appreciate if any of the SNES guys could try this out and let me know that everything worked as expected. I anticipate no problems as the SNES code was almost exact.

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
