# COM Defensive Juice: Introduction

**Source:** https://tecmobowl.org/forums/topic/10781-com-defensive-coverage-late-in-season/  
**Category:** CPU & SIM → Attributes, Play Ratio, SIM Stats  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/10781-com-defensive-coverage-late-in-season/).

## Summary

This code is ran at the start of the game...I think it also sets the juice. ``` ; 0x034106 $80F6:A0 B2 LDY #$B2 ; $80F8:B1 3E LDA ($3E), Y ; wins $80FA:A0 B3 LDY #$B3 ; $80FC:38 SEC ; $80FD:F1 3E SBC ($3E), Y ; losses $80FF:B0 10 BCS $8111 ; if (wins - losses >= 0) goto $8111 $8101:4C 0F 81 JMP $810F $8104:20 58 81 JSR $8158 $8107:C9 30 CMP #$30 $8109:F0 04 BEQ $810F $810B:C9 03 CMP #$03 $810D:D0 2D BNE $813C $810F:A9 00 LDA #$00 ; else, set difference to zero $8111:8D 7D 66 STA $667D ; save difference ```

## Key facts

- ; 0x034106
- $80F6:A0 B2     LDY #$B2		 ;
- $80F8:B1 3E     LDA ($3E), Y	; wins
- $80FA:A0 B3     LDY #$B3		 ;
- $80FC:38        SEC				;
- $80FD:F1 3E     SBC ($3E), Y	; losses
- $80FF:B0 10     BCS $8111		; if (wins - losses >= 0) goto $8111
- $8101:4C 0F 81  JMP $810F
- $8104:20 58 81  JSR $8158
- $8107:C9 30     CMP #$30
- $8109:F0 04     BEQ $810F
- $810B:C9 03     CMP #$03

## Source

<https://tecmobowl.org/forums/topic/10781-com-defensive-coverage-late-in-season/>
