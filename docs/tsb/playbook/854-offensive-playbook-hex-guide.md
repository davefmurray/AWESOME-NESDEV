# Offensive Playbook HEX Guide

**Source:** https://tecmobowl.org/topic/854-how-to-modify-actual-plays-routes-blocking-etc/  
**Category:** PLAYBOOK → Play Code, Pointers, Data Tables  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/854-how-to-modify-actual-plays-routes-blocking-etc/).

## Summary

Well I located one sectoin of code that has to do with the actual plays but I now believe there is an additonal section but anyways I'm getting ahead of myself. The section of code that is respsonsible for this is section 04410-04BF7. Just like the sectoin prior to this which is resposible for the players physical locatoins on the screen in formations there are 11 two byte strings per play Without further ado here is the hex code for each play:

## Key facts

- ONEBACK SWEEP R (Alt) 6AAA 87AA C6AA CCAA 8EB7 4EBE 30BE 2EB8 93B7 2ABE 36BE
- ONEBACK SWEEP R 6AAA 87AA C6AA CCAA 8EB7 4EBE 30BE 2EB8 9CB7 2ABE 36BE
- WEAKSIDE OPEN 3EAB 87AA 55AB CCAA 66BE 5BAB 9CB7 30BE 36BE 2ABE 4EBE
- T OFFTACKLE R 16AC 21AC 58AC 9DA3 66BE 3CBE 30BE 42BE 9CB7 2ABE 36BE
- SHOTGUN DRAW 7EAC 81AC A5B7 B4B7 B9B7 BEB7 99BE DBAC BBBE E8AC EEAC
- R AND S SWEEP R FFAD 0AAE 44AE 9DA3 4AAE 53AE 9CB7 C3B7 77AE 89AE 8FAE
- T CROSS RUN L (ALT) F4AC 0BAD 17AD 59AD 01A9 5FAD 30BE 67AD 76AD 2ABE 9CB7
- T CROSS RUN L F4AC 0BAD 17AD 59AD 01A9 E8B7 30BE 67AD 2EB8 2ABE 9CB7
- SLOT OFFTACKLE 95AE A3AE B5AE 54BE 5FA6 36BE 7EA6 83A6 89A6 3CBE 9CB7
- CROSS OFFTACKLE F4AC 0BAD F1AE 59AD 01A9 5FA6 7EA6 83A6 89A6 3CBE 9CB7
- PITCH L OPEN (ALT) 26B8 66AF 2AAF 59AD 01A9 6CAF 42BE 67AD 76AD 2ABE 9CB7
- PITCH L OPEN 26B8 66AF 2AAF 59AD 01A9 6CAF 42BE 67AD 2EB8 2ABE 9CB7

## Topics

`formation`

## Source

<https://tecmobowl.org/topic/854-how-to-modify-actual-plays-routes-blocking-etc/>
