# Better touchback hack and returnable endzone punts

**Source:** https://tecmobowl.org/forums/topic/55501-better-touchback-hackand-returnable-endzone-punts  
**Category:** INCOMPLETE HACKS → Still Developing  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/55501-better-touchback-hackand-returnable-endzone-punts).

## Summary

Just in the sake of cataloging SET commands, can someone verify this would be the correct code: ``` #Better touchbacks/Return punts out of endzone (28-team) #http://tecmobowl.org/forums/topic/55501-better-touchback-hackand-returnable-endzone-punts/ SET(0x2440B,0x20DF9F) SET(0x24B93,0x20FD9F) SET(0x25108,0x4C979F) SET(0x25117,0x4C9C9F) SET(0x25FA7,0xA2004C9E9FA201A588C918B00AA589C918900CA536B002A5352940C940F0034CC59FE001F0042057906020709060A017E001F00DB184C928900BC9C9B0074C0F91B186B0F14C1691A593C9DEA594E90990B320709060A593C920A594E906B004205790604C979F) ```

## Key facts

- SET(0x2440B,0x20DF9F)
- SET(0x24B93,0x20FD9F)
- SET(0x25108,0x4C979F)
- SET(0x25117,0x4C9C9F)
- *Edited February 12, 20179 yr by SBlueman**
- [tpc\_original\_punt\_b2.nes](https://tecmobowl.org/applications/core/interface/file/attachment.php?id=8733)
- Set 0x2440B (0x 20 DF 9F)  -Disable normal punt check for P2 Check for back of endzone otherwise do my b button check
- Set 0x24B93  (0x 20 FD 9F) - Disable normal punt checkfor P1.  Check for back of endzone otherwise do my b button check
- Set 0x25108  (0x4C979F) Jump to my b button touchback check before out of bounds compare. Pplayer 1
- Set 0x25117  (0x4C9C9F) Jump to my b button touchback check before out of bounds compare. Player 2
- Set0x25FA7(A2004C9E9FA201A588C918B00AA589C918900CA536B002A5352940C940F0034CC59FE001F0042057906020709060A017E001F00DB184C928900BC9C9B0074C0F91B186B0F14C1691A593C9DEA594E90990B320709060A593C920A594E906B004205790604C979F)
- "Set0x25FA7(A588C918B00CA201A589C918900EA536B004A535A2002940C940F0034CC29FE001F0042057906020709060A200A589C918B006C90B9002B002A201A017E001F00DB184C928900BC9C9B0074C0F91B186B0F14C1691A593C9DEA594E90990A120709060) "

## Topics

`punt`, `endzone`

## Source

<https://tecmobowl.org/forums/topic/55501-better-touchback-hackand-returnable-endzone-punts>
