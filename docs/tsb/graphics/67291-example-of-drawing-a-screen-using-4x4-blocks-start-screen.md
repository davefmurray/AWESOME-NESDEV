# Example of drawing a screen using 4x4 blocks (Start Screen)

**Source:** https://tecmobowl.org/forum/topic/67291-example-of-meta-tile-drawing-4-tile-x-4-tile-blocks-start-screen  
**Category:** GRAPHICS → Background & Design Palettes, Cut Scene Colors  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forum/topic/67291-example-of-meta-tile-drawing-4-tile-x-4-tile-blocks-start-screen).

## Summary

Just wanted to give a quick example of how the " TECMO SUPER BOWL" text positioned in 4x4 blocks If we go to 0x05056 in the rom we get the following data: A5 b6. This is a pointer to the data sequence. Flipping it and andding 0x10 for the ines header offset we get 0xB6B5.

## Key facts

- If we go to 0x05056 in the rom we get the following data:  A5 b6. This is a pointer to the data sequence. Flipping it and andding 0x10 for the ines header offset we get 0xB6B5.
- Since 0x4000 is loaded in as a $A000 bank. B6B5 points to $56B5
- At 0x56b5 we have the following sequence
- 20 76                                    ; These first two bytes set which 0x0800 size banks from the CHR section of the rom (0x40010 onwards in 28 team)
- ; we will use that contain the tiles we need
- 02                                         ;  This byte tells us which bank will be used to draw the 4x4 tile sections
- 03, 06                                   ; These two bytes set (# of metatile rows, # length of the metatile sequence)
- 09                                         ; this byte sets the starting location for the metatiles (refer to the image below)
- 42 43 44 45 46 00 ; these are pointer indexes to draw the metatiles
- [![metatile.png](https://tecmobowl.org/uploads/monthly_2021_03/metatile.thumb.png.60e928f2ec0abb136c5f95264d585dd0.png)](https://tecmobowl.org/uploads/monthly_2021_03/metatile.png.235e6484b405f8054ad153b2b1e92531.png)
- [metatile.bmp](https://tecmobowl.org/applications/core/interface/file/attachment.php?id=14317)
- in GIMP or a more basic photo editor, erase all of the background - any background will make it harder for the color-reduction algorithms to make the face look good

## Topics

`face`, `tile`, `CHR`, `pointer`, `text`

## Source

<https://tecmobowl.org/forum/topic/67291-example-of-meta-tile-drawing-4-tile-x-4-tile-blocks-start-screen>
