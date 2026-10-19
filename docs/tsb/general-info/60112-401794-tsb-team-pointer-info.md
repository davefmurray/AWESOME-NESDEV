# TSB Team Pointer Info

**Source:** https://tecmobowl.org/topic/60112-team-location-namemascot-length-pointer/#entry401794  
**Category:** GENERAL INFO  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/60112-team-location-namemascot-length-pointer/#entry401794).

## Summary

I know there is a thread about the Pointers for this section (TEAMS' NAMES), but I dont know why the search for my browser sometimes freezes, So I could not find it in the Docs-Directory either. I think we all got used to the *TSB-TOOLS/EDITORS*, since they do all the dirty work for us. I dont have to worry about these pointers anymore. You also can trust all these editors when you want to change something within this section of the rom. These Editors help us creating some pointers "automatically". And most of these tools have been programmed so that you can not make mistakes when inputting the names. This means some editors wont let you "exceed" the "allowed" number for name's characters, simply because they will crash the game at some point. (If memory is exceeded or something like…

## Key facts

- I know there is a thread about the Pointers for this section (TEAMS' NAMES), but I dont know why the search for my browser sometimes freezes, So I could not find it in the Docs-Directory either.
- The pointers for this section are just above the offset you mention: **They start at offset x1FC10**, where it says $F0 BC.
- *F0BC** is the pointer for offset x**1FD00**. As you can see, pointers in this section "point" to their corresponding offset just by:
- *1.** switching the bytes from the pointer: F0 BC -> BCF0,
- *2.** then add the HEX value of **14010**: BCF0+14010= 1FD00.
- Now at offset **1FD00** is located the first "text" that the rom will read for this section, which is "**BUF.**"
- Right after the first pointer, comes the second pointer, it indicates F4BC, which points to offset 1FD04. On the "TEXT-window" from your HEX-Editor it reads "IND."
- [![post-9389-0-87634200-1398027127_thumb.pn](https://tecmobowl.org/uploads/monthly_04_2014/post-9389-0-87634200-1398027127_thumb.png)](https://tecmobowl.org/uploads/monthly_04_2014/post-9389-0-87634200-1398027127.png)
- Now **The lenght of these words is determined by the pointers themselves**:
- If you want to change the length of the text ***BUFFALO*** you will first need to know its location. (you know that your TEXT-Window will show the offset just by clicking the first letter of your text):
- [![post-9389-0-12634900-1398027179_thumb.pn](https://tecmobowl.org/uploads/monthly_04_2014/post-9389-0-12634900-1398027179_thumb.png)](https://tecmobowl.org/uploads/monthly_04_2014/post-9389-0-12634900-1398027179.png)
- This text: ***"BUFFALO"*** is located at offset x**1FD7C**, which means by reverting the process that the "pointer" you shall find is:

## Topics

`sim`, `pointer`, `text`

## Source

<https://tecmobowl.org/topic/60112-team-location-namemascot-length-pointer/#entry401794>
