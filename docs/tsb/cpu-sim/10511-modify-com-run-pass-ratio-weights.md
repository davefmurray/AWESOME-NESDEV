# Modify COM RUN / PASS RATIO Weights

**Source:** https://tecmobowl.org/forums/topic/10511-heavier-weighting-of-com-runpass-ratio  
**Category:** CPU & SIM → Attributes, Play Ratio, SIM Stats  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/10511-heavier-weighting-of-com-runpass-ratio).

## Summary

i believe this is the code. the run/pass ratio is saved into $A2 prior to executing $AA84. changing the **CMP #$99** and **CMP #$B3** should do the trick.

## Key facts

- i believe this is the code. the run/pass ratio is saved into $A2 prior to executing $AA84.
- changing the **CMP #$99** and **CMP #$B3** should do the trick.
- $AA84:A5 A2     LDA $00A2 = #$00	; get run/pass ratio
- $AA86:0A        ASL		;
- $AA87:AA        TAX		;
- $AA88:BD 4E AA  LDA $AA4E,X @ $AA4F = #$AA	; set jump address
- $AA8B:85 3E     STA $003E = #$00	;
- $AA8D:BD 4F AA  LDA $AA4F,X @ $AA50 = #$9E	;
- $AA90:85 3F     STA $003F = #$00					;
- $AA92:6C 3E 00  JMP ($003E) = $0000				; jump to code
- $AA95:A5 40     LDA $0040 = #$7C	; keep play index from 0 to 7
- $AA97:29 07     AND #$07	;

## Source

<https://tecmobowl.org/forums/topic/10511-heavier-weighting-of-com-runpass-ratio>
