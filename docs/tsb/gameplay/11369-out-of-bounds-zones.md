# Out of Bounds Zones

**Source:** https://tecmobowl.org/topic/11369-out-of-bounds-zones/  
**Category:** GAMEPLAY → Down & Distance  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/topic/11369-out-of-bounds-zones/).

## Summary

**[@buck](https://tecmobowl.org/profile/5602-buck/)** **Here are the values for the endzone locations in the OG rom:**

## Key facts

- *[@buck](https://tecmobowl.org/profile/5602-buck/)**
- *Here are the values for the endzone locations in the OG rom:**
- *Left endzone Front : high =0x06, low = 0x70**
- *Left endzone Back  : high =0x06, low = 0x20**
- *Right endzone Front : high =0x09, low = 0x90**
- *Right endzone Back :**  **high =0x09, low = 0xE0**
- *0x990(right endzone) -0x670(left endzone)= 0x320 = [3 \* 32 yards = 96 yards]  + [(0x20/0x08) = 4 yards] = 100 yards**
- low byte: 0x25046, default value=0x90
- high byte: 0x2504B, default value=0x09
- low byte: 0x25059, default value=0x71
- high byte: 0x2505e, default  value=0x06
- low byte: 0x2506A, default value=0x71

## Topics

`endzone`

## Source

<https://tecmobowl.org/topic/11369-out-of-bounds-zones/>
