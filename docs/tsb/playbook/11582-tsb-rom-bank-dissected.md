# TSB ROM Bank Dissected

**Source:** https://tecmobowl.org/topic/11582-tecmo-nes-rom-mapping-project/  
**Category:** PLAYBOOK → Play Code, Pointers, Data Tables  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/11582-tecmo-nes-rom-mapping-project/).

## Summary

[viewtopic.php?f=5&t=13405&p=107143#p107130](https://tecmobowl.org/forum//viewtopic.php?f=5&t=13405&p=107143#p107130)

## Key facts

- [viewtopic.php?f=5&t=13405&p=107143#p107130](https://tecmobowl.org/forum//viewtopic.php?f=5&t=13405&p=107143#p107130)
- Tecmo Juice added
- High level rom map
- ROM LOC HEX   = actual location in ROM
- TYP BANK          = Bank its typically loaded into in RAM (only two banks can be in memory at any one time hence lots of bank swapping occurs)
- SWP                   = How the assemble code references the bank
- FCE                    = How FCEUX debugger references the bank in the debug display. It references it in 4KB chunks
- STOUT               = lets you know which bank stout dissambly refers two
- DESCRIPTION    = this is a very high level description. It may not detail everything that goes on in the bank.
- ![0925634c3f.png](http://puu.sh/dh4d9/0925634c3f.png)[bank\_locations\_tsb.xls](https://tecmobowl.org/applications/core/interface/file/attachment.php?id=11951)
- > On 3/19/2010 at 2:24 PM, jstout said:
- > [TSB\_Code.zip](https://tecmobowl.org/applications/core/interface/file/attachment.php?id=5227)

## Source

<https://tecmobowl.org/topic/11582-tecmo-nes-rom-mapping-project/>
