# Offensive Formation Fix for TSB Tool

**Source:** https://tecmobowl.org/forums/topic/55564-changing-a-teams-offensive-formation  
**Category:** GRAPHICS → Formations, Names  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/55564-changing-a-teams-offensive-formation).

## Summary

**OF FORMATIONS SETUP** Each Team has an Offensive formation depending on the position of their BACKS on the field: **3 WR**: **1** Rb / **3** Wrs / **1** TE - (*Chargers, Redskins, Cardinals*) **4 WR**: **1** Rb / **4** Wrs - (*Oilers, Lions, Falcons*) **PRO**: **2** Rbs/ **2** Wrs / **1** TE - (All of the rest) *Redskins* x**2164B** ,**0x31007** (**0E**)\*, *Cardinals* x**2164F,** **0x3100B** (**11**)\*

## Key facts

- Chargers* x**21647** (**0C**)\*,
- Redskins* x**2164B** ,**0x31007** (**0E**)\*,
- Cardinals* x**2164F,**  **0x3100B** (**11**)\*
- \*Changing to a differtent Team's number at this offset, will make this team have a **3 WR** **formation** ( team **00**=BUF, **1B**=ATL)
- Oilers* x**21654**, x**30FFB** (**07**)\*\*
- Lions* x**21658**, x**30FFF** (**14**)\*\*
- Falcons* x**2165C**, x**31003** (**1B**)\*\*  \*Changing to a differtent Team's number at these offsets, will make this team have a **4 WR** **formation** ( team **00**=BUF, **1B**=ATL)
- At x**21642** input: 8AA66EBCD09FAA4C5096 \*  (this will redirect to TEAMS' FORMATION at x**21FE0**)
- At x**21FE0**  it will be the new FORMATION SETUP for the Teams in ***BUF-ATL* order**.  (**00**=pro, **01**=4wr, **02**=3wr-1te) **Here you have to input 28 values** (+ 2 for All-PROs)
- At x**30FF8** input: 8AA66EBC709EAAC001F011C002F0134CFE8F \*  (this will redirect to  x**31E80**,  where PLAYERS' POSITION (*WR,RB,TE*) is assigned for the NEW FORMATION )
- At x**31E80**  it will assign the CORRECT position for each new FORMATION SETUP. ***BUF-ATL* order**.  (**00**=pro, **01**=4wr, **02**=3wr-1te).**Here you also have to input 28 values** (+ 2 for All-PROs)
- *Edited October 9, 20197 yr by bruddog**

## Topics

`formation`

## Source

<https://tecmobowl.org/forums/topic/55564-changing-a-teams-offensive-formation>
