# Schedule: Graphics / Number of Games

**Source:** https://tecmobowl.org/forums/topic/769-creating-historical-tsb-nes-seasons/  
**Category:** GRAPHICS → Game Schedule, Playoff Bracket, Game Modes  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/769-creating-historical-tsb-nes-seasons/).

## Summary

> So, After spending a couple hours figuring out what pointers were all about, I found the REAL pointers for the number of games per week. > > At offset 329A7 (The hex code starts out "CB 89 E7 89), there are 34 bytes, or two bytes per week. As i put above, CB 89 = Week 1, E7 89 = Week 2, etc. If you notice, since there are 14 games programmed in for Week 1, the difference between CB and E7 if you subtract them in Hex terms in 28....accounting for the 28 teams playing that week. If you want only 13 games that first week, Change the "E7" to "E5," showing where the pointer starts for Week 2's games. Since I wanted 14 games, or 28 teams a week, I just kept adding 28 to each byte until the end of the season. > > But, I found that the game won't let you leave a week blank (It freezes up on…

## Key facts

- > So, After spending a couple hours figuring out what pointers were all about, I found the REAL pointers for the number of games per week.
- > Yes, I know it's really complicated. So, to save the hard work of figuring out a regular 16 week schedule, I just did the pointers for you....
- > From 329A7:
- > And the games per week bytes at 329C9:
- The "real pointers" you're referring to are telling the game where the beginning of each week is.
- If you're erasing games from a week, all you do is change the number of games per week at 329C9. Then add correct number of FF's after the last game in said week. (as explained in earlier post)
- Yes, I know it's really complicated. So, to save the hard work of figuring out a regular 16 week schedule, I just did the pointers for you....
- From 329A7:
- And the games per week bytes at 329C9:

## Topics

`schedule`, `pointer`

## Source

<https://tecmobowl.org/forums/topic/769-creating-historical-tsb-nes-seasons/>
