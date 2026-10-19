# Super Bowl Palettes Information

**Source:** https://tecmobowl.org/topic/13429-super-bowl-palettes/  
**Category:** GRAPHICS → Background & Design Palettes, Cut Scene Colors  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/13429-super-bowl-palettes/).

## Summary

Trying to keep this answer fairly short. TSB has a draw screen routine that handles the screen and effects. The relevant draw section for the screen you want is: ﻿ .BYTE $FD, <L_7_ADF9, >L_7_ADF9 ; Commands to Draw Team Name

## Key facts

- ﻿  .BYTE $C8
- ﻿  .BYTE $F1
- ﻿  .BYTE $F7, $20
- ﻿  .BYTE $C0, $01, $88, $18, $1A
- ﻿  .BYTE $F9, $02, $B6, $B7
- ﻿  .BYTE $F6
- ﻿  .BYTE $8A, $42
- ﻿  .BYTE $FD, <L_7_ADF9, >L_7_ADF9 ; Commands to Draw Team Name
- ﻿  .BYTE $FA, $1B                  ; Set Team Colors
- ﻿  .BYTE $E5, $FF
- ﻿  .BYTE $F3, $44
- ﻿  .BYTE $FB, $F0

## Topics

`palette`

## Source

<https://tecmobowl.org/topic/13429-super-bowl-palettes/>
