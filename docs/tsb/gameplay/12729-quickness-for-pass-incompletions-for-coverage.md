# Quickness for Pass Incompletions for Coverage

**Source:** https://tecmobowl.org/topic/12729-use-quickness-for-pass-incompletions/  
**Category:** GAMEPLAY → Player Attributes During Gameplay  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/12729-use-quickness-for-pass-incompletions/).

## Summary

The code below should use the defender's pass interception ability to intercept passes and the defender's quickness ability to cause incomplete passes. The following is loosely tested. FIRST: ; x2BFCA A6 DD LDX $DD A5 E6 LDA $E6 20 ED BF JSR CHECK A4 E6 LDY $E6 C9 50 CMP #$50 90 23 BCC EXIT 4C 83 9D JMP $9D83

## Key facts

- A6 DD     LDX $DD
- A5 E6     LDA $E6
- A4 E6     LDY $E6
- C9 50     CMP #$50
- 4C 83 9D  JMP $9D83
- A5 E7     LDA $E7
- A4 E7     LDY $E7
- 4C 96 9D  JMP $9D96
- A5 E8     LDA $E8
- A4 E8     LDY $E8
- 4C A9 9D  JMP $9DA9
- 4C EE 9D  JMP $9DEE

## Source

<https://tecmobowl.org/topic/12729-use-quickness-for-pass-incompletions/>
