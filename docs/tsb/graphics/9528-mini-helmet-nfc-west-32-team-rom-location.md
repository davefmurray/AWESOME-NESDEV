# Mini-Helmet: NFC West 32-Team ROM Location

**Source:** https://tecmobowl.org/forums/topic/9528-mini-helmets-for-nfc-west-cxrom-32-team-nes-tsb/  
**Category:** GRAPHICS → Uniforms, Helmets, Portraits  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forums/topic/9528-mini-helmets-for-nfc-west-cxrom-32-team-nes-tsb/).

## Summary

> 2 minutes ago, bruddog said: > > The highlighted 3C isn't actually the tile. Here is the FCEUX logic I went through. I'm working off a slightly different rom but the logic is the same. Knowing the tile ID for the sprite **I did a quick search in sprite memory** ($200-$2FF) > > The data is layed out as follows > > Y coord, tile ID, attributes, x coord > > Then I found the tile ID F9 at 0x2FD. Then I set a write breakpoint for that address. You'd want to set the breakpoint once you are at the main menu. Ideally if you know the tile you could add a further condition like A==#F9. A is the accumulator and is usually loaded with the data to be stored. > > Once it breaks you get this in the FCEUX window > > 08:A7F6:B9 52 BC LDA $BC52,Y @ $BCDA = #$F9 > 08:A7F9:9D 01 02 STA $0201,X @ $02FD =…

## Key facts

- > Y coord, tile ID, attributes, x coord
- >  08:A7F6:B9 52 BC  LDA $BC52,Y @ $BCDA = #$F9
- >  08:A7F9:9D 01 02  STA $0201,X @ $02FD = #$F9
- > If you hover over the A7F6 with the cursor you'll see at the bottom of the debug window the offset in the rom its executing from which in this case is
- > 0x22806. So where is it getting the data from? Well in that line we see @BCDA. B would add 0x1000 to the current offset+ the head offset of 0x10 so the tile data is
- > at 0x23CEA. The Y coordinate is the byte before that at 0x23CE9.
- thanks for the tips, I will have to try this method out sometime.  by "sprite memory" do you mean the PPU Memory?
- Y coord, tile ID, attributes, x coord
- 08:A7F6:B9 52 BC  LDA $BC52,Y @ $BCDA = #$F9
- 08:A7F9:9D 01 02  STA $0201,X @ $02FD = #$F9
- If you hover over the A7F6 with the cursor you'll see at the bottom of the debug window the offset in the rom its executing from which in this case is
- 0x22806. So where is it getting the data from? Well in that line we see @BCDA. B would add 0x1000 to the current offset+ the head offset of 0x10 so the tile data is

## Topics

`helmet`, `tile`, `attribute`, `sprite`

## Source

<https://tecmobowl.org/forums/topic/9528-mini-helmets-for-nfc-west-cxrom-32-team-nes-tsb/>
