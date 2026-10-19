# Quarter Length

**Source:** https://tecmobowl.org/topic/9111-how-to-change-5mins-to-7mins/#entry339861  
**Category:** GAMEPLAY → Gameplay Clock, Playbook Clock, Quarter scores  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/9111-how-to-change-5mins-to-7mins/#entry339861).

## Summary

I was looking for this some time ago, I dont know why some of of these links dont work anymore, but here's what JSTOUT found: For the NES version, just open up the rom in a hex editor and go to **x2224B** where you'll see **05** 85 6B. The 05 is how many minutes for the quarter. So replace that with 06 or 07 and the time will be changed. I'm putting this in case s1 (like me) needs it again. THX jstout! And, to change the **on-screen** **clock** for NES version: **0x222A5** is the nmi timer reload value. it gets reloaded to #**$14** (#20) everytime the "seconds" variable ($41) is decreased (actually when X==#00). the timer is held entirely in the X register but gets preserved on the stack during function calls. it gets decremented every frame sometime between scanlines 8 and 20. the nes…

## Key facts

- For the NES version, just open up the rom in a hex editor and go to **x2224B** where you'll see **05** 85 6B. The 05 is how many minutes for the quarter. So replace that with 06 or 07 and the time will be changed.
- the nes ppu renders ~60fps so change the reload value to #$3C (#60) to get a more realistic clock.
- THANKS. to CXROM for that.
- SET( **0x222D6**) , **1E** default speed
- SET( 0x222D6, 0x?? ) lower value for faster, higher value for slower
- Here is that location: x**222D2** Default **0A**=ten seconds
- *Edited February 25, 201313 yr by Knobbe**

## Topics

`clock`

## Source

<https://tecmobowl.org/topic/9111-how-to-change-5mins-to-7mins/#entry339861>
