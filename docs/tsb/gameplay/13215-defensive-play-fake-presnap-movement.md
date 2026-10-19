# Defensive Play Fake Presnap Movement

**Source:** https://tecmobowl.org/topic/13215-defense-play-fake-and-presnap-movement-hex-question/  
**Category:** GAMEPLAY → Custom Defensive Formations, Reactions  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/13215-defense-play-fake-and-presnap-movement-hex-question/).

## Summary

> 28 FD 90 is not a valid command. You cant jump to 90FD. the thing following the random byte "28" has to be a rom location > > not an action. you can only jump to somewhere beween A000- and BFFF > > Read the documents buck suggested. Especially E I don't understand why. I went to the first area where there were a series of FF FF FF...'s and typed in my own code (28 18 BE FF C2 AA FF/FE). Then I wrote a pointer to this location @fda0 (fda0-10 = fd90... 90fd). Is this a space that's used in the game for something? Also, half of the command worked (the 18 BE part), but the other half didn’t, which is why I’m confused. I think something isn’t looping correctly, which doesn't seem to have to do with the location of the command. I just can’t fix it.

## Key facts

- > 28 FD 90 is not a valid command. You cant jump to 90FD. the thing following the random byte "28" has to be a rom location
- > not an action. you can only jump to somewhere beween A000- and BFFF
- Lastly, I can get a player to approach the line presnap and then line-up across from X offensive player, but not in reverse order. Is this just not possible?
- YYYX MUST be between A000-BFFF. Technically between A010-C010 because of the 10 byte offset. Thats just the way it is.
- @bb2c: D0 C8 50 EC 28 E0 BB D7 00 20 FF E0 BB FF FF FF FF FF FF FF FF FF FF FF
- @bbf0: 28 18 BE FF C2 AA FE FE FE FE FE FE FF FF FF FF
- *Edited August 16, 201214 yr by quince3800**

## Topics

`formation`, `pointer`

## Source

<https://tecmobowl.org/topic/13215-defense-play-fake-and-presnap-movement-hex-question/>
