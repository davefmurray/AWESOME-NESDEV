# Team Control - MAN/SKP/COA/COM

**Source:** https://tecmobowl.org/topic/51704-team-control-manskpcoacom-refrence/  
**Category:** GAMEPLAY → Game-types  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/51704-team-control-manskpcoacom-refrence/).

## Summary

For my hack I wanted to have 24 teams, so I decided to removed BUF, IND, N.O., and ATL. That way the AFC and NFC would still have equal number teams. I used the following [this thread](http://tecmobowl.org/topic/7850-removing-teams-from-the-menu/#p126299) to remove those teams. Sure those teams still exist, but they were no longer visible or clickable. -NFL Standings don't matter if a team doesn't PLAY so I just removed the 4 teams from the schedule. So if a team or player never sees play they will never be listed in these menus. Just need to find out how to change how many teams are in each conference.

## Key facts

- X2397c change from 00 0E to XX YY (where xx = the first team in the nfc and where yy = 1 plus the number of teams in both leagues)
- X23980 change from 00 0E to XX YY (where xx = the first team in the nfc and where yy = 1 plus the last team in the afc)
- X23985 change from 0E 1C to XX YY (where xx = the first team in the nfc and yy = 1 plus the last team in the nfc)
- X23989 change from 00 0E to XX YY (where xx = the first team in the nfc and where yy = 1 plus the number of teams in both league)
- X2398B change from 00 0E to XX YY (where xx = the first team in the nfc and where yy = 1 plus the last team in the afc)
- X23990 change from 0E 1C to XX YY (where xx = the first team in the nfc and yy = 1 plus the last team in the nfc)
- Its basic NES PPU Locations. $2000 is top left, $201F is top right, $23A0 is bottom left, $23BF is bottom right. Each x01 is one space left and each x20 is one space down.
- BUF = E6 20 ($20E6) IND = 26 21 ($2126) etc.
- > Its basic NES PPU Locations. $2000 is top left, $201F is top right, $23A0 is bottom left, $23BF is bottom right. Each x01 is one space left and each x20 is one space down.
- > BUF = E6 20 ($20E6) IND = 26 21 ($2126) etc.

## Topics

`helmet`, `formation`, `schedule`, `pointer`

## Source

<https://tecmobowl.org/topic/51704-team-control-manskpcoacom-refrence/>
