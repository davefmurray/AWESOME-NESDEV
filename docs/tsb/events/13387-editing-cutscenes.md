# Editing Cutscenes

**Source:** https://tecmobowl.org/topic/13387-an-easy-guide-to-changing-and-deleting-various-cutscenes/  
**Category:** EVENTS → In-Game  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/13387-an-easy-guide-to-changing-and-deleting-various-cutscenes/).

## Summary

After getting fed up with my palette problem on cut scenes I decided to just eliminate them. There was some good general material on the board but no easy access to the data. I'm learning assembly from scratch and learned a ton from this epic thread [http://tecmobowl.org...ic/9946-events/](https://tecmobowl.org/forum/topic/9946-events/) but it's really hard for a beginner to understand so I made this easy spreadsheet as I went along and now get your cutscene editing done fast and maybe learn a little about assembly.

## Key facts

- After getting fed up with my palette problem on cut scenes I decided to just eliminate them. There was some good general material on the board but no easy access to the data.
- for the truly lazy who just want a quick edit to eliminate the ingame cutscenes goto offset x261EF with a hex program and change the 3 bytes of data to EA EA EA
- hopefully when I grow up, I can be just like jstout, xplozv, and cxrom ![:P](https://tecmobowl.org/uploads/emoticons/default_tongue.png)
- [Tecmo cutscenes.xls](https://tecmobowl.org/applications/core/interface/file/attachment.php?id=6783)
- *Edited September 8, 201214 yr by airkix72**
- The halftime show is part of the top level game loop in bank 18 (0x22000-0x24000)
- From there to the actual routine
- So long post short  at 0x22E33 type he following which will overwrite the random number generation with straight event index load.
- Change  highlighted byte in read to set the cutscene based on the events listed in [http://tecmobowl.org/forum/topic/9946-events/](https://tecmobowl.org/forum/topic/9946-events/)
- [cutscene demo.zip](https://tecmobowl.org/applications/core/interface/file/attachment.php?id=6785)
- *Edited September 9, 201214 yr by airkix72**

## Topics

`palette`, `face`, `cutscene`, `event`, `kick`, `punt`

## Source

<https://tecmobowl.org/topic/13387-an-easy-guide-to-changing-and-deleting-various-cutscenes/>
