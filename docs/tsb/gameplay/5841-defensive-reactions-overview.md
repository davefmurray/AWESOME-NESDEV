# Defensive Reactions Overview

**Source:** https://tecmobowl.org/forums/topic/5841-defensive-reactions/  
**Category:** GAMEPLAY → Custom Defensive Formations, Reactions  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/5841-defensive-reactions/).

## Summary

> I think I follow you Jstout, but how do you explain the randomness with the defenders reactions? For example if you make all of the defensive bytes the same number, the defenders do react differently. If you call the same slot on defense they react differently. At times they cover everyone, other times they will double wrs, leaving others open, etc. > > Also, the A010 section? How does that relate to the 6000 section? The randomness is built into each player's design. For example, I created one defense for testing were the CB has one reaction to rush the QB and another to cover deep. D1 C0 28 EC (where to lineup) 27 55 A1 (My code for rushing the QB at xA165) FF 18 BE (My code for covering deep at xBE28). The computer goes through the list of commands one by one deciding to do it or…

## Key facts

- > Also, the A010 section? How does that relate to the 6000 section?
- The 6010 section like the offensive play area. It goes in order of reaction # and is a direct pointer (45AA points to xAA55).
- Run slot 1's play one has its 8 possible defensive reactions defined from x1DC10-x1DC17.
- Since the defense called run slot 2, we actually use x5A as our pointer. If the defense called run slot 1, we'd use x5B. If the defense called pass slot 1, we'd use x58.
- From here, we can see that each position has the following direct pointer for this defensive play:
- RE   - 10 A1 (xA120) [swap the two bytes, add x10 for the NES rom header]
- The same exact thing applies for defense. They bytes at 6000 are just more pointers to additional defensive actions.

## Topics

`pointer`

## Source

<https://tecmobowl.org/forums/topic/5841-defensive-reactions/>
