# Removing Teams

**Source:** https://tecmobowl.org/topic/54998-removing-teams-from-a-rom  
**Category:** GRAPHICS → Game Schedule, Playoff Bracket, Game Modes  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/54998-removing-teams-from-a-rom).

## Summary

> Or if someone was willing to drop in a 24 team rom (4 divisions of 6 teams or 6 of 4) that would be awesome. I can take care of the editing of helmets and logos, just can't figure out the first part... Everyone in here will tell you best way to do it is if YOU DO IT YOURSELF!

## Key facts

- > Or if someone was willing to drop in a 24 team rom (4 divisions of 6 teams or 6 of 4) that would be awesome.  I can take care of the editing of helmets and logos, just can't figure out the first part...
- So.. back to what you want: a 24 TEAMS (I think 6 teams per Division is almost impossible, but a 4-teams-per-division-rom sounds more feasable..)
- Or you could have it all rearranged like the 16T-roms, and re-assign AFC's last 4 teams to the NFC, and REMOVING NFC's last 4 teams.
- *22C36 - 22C53** - **TEAM SELECTED** ROSTER shown when "accesed" , ordered by "ROWS" : **00**  05  09...(EAST/ CENTRAL/ WEST)
- *23B4B - 23B94** - **CURSOR SETUP** (x:y coords) Every 2 bytes correspond a team. First offset "x", and the following the "y". **(AFC**: x23B4D, **NFC**: 23B53.) Teams start at offset x23B59 ordered by "ROWS" (E/ C/ W)
- *23D21 - 23D58** - **MINI Helmets coords**. every helmet uses 2 bytes (Y,X). the X seems to be multiplied by 2 to get the actual placement coordinate **\*\*THIS IS BUF-ATL ORDER**, first all AFC, then NFC.
- *1E943 - 1E960** - **TEXT POSITION** and pointers (this however is set by Divisions)
- *1F8B5 - 1F90A** - **TEXT FORMAT**
- *22C13 - 22C53** - **TEAM SELECTED**. Team that will appear on field  ordered by "ROWS" : **00**  05  09...(EAST/ CENTRAL/ WEST)
- *23E95 - 23ED0** - **CURSOR SETUP** (x:y coords) Every 2 bytes correspond a team. First offset "x", and the following the "y". ordered by "ROWS" (E/ C/ W)
- *23CE9 - 23D20** - **MINI Helmets coords**. every helmet uses 2 bytes (Y,X). the X seems to be multiplied by 2 to get the actual placement coordinate **\*\*THIS IS BUF-ATL ORDER**, first all AFC, then NFC.
- *23CE9 - 23D20** - **MINI Helmets coords.**

## Topics

`helmet`, `logo`, `tile`, `roster`, `playoff`, `sound`, `pointer`, `text`

## Source

<https://tecmobowl.org/topic/54998-removing-teams-from-a-rom>
