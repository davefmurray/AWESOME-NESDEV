# COM Defensive Juice: HEX Locations

**Source:** https://tecmobowl.org/forum/topic/7144-how-tsb-decides-strength-of-cpu-opponent/page__hl__juice#entry65571  
**Category:** CPU & SIM → Attributes, Play Ratio, SIM Stats  
**Imported:** 2026-10-19  
**Format:** index card (summary + key facts)

> Distilled from the linked thread. Full text, images, attachments and replies: [source](https://tecmobowl.org/forum/topic/7144-how-tsb-decides-strength-of-cpu-opponent/page__hl__juice#entry65571).

> **Note:** The linked post is short or a question; the most technical reply is shown instead.

## Summary

the nes only has a 16-bit address bus so it can only access $0000 - $FFFF. you need to adjust that address in the \*.nes file for where it would be loaded in NES-rom. there are 4 banks: the conditional field is used to have the breakpoint fire in certain situations:

## Key facts

- the nes only has a 16-bit address bus so it can only access $0000 - $FFFF. you need to adjust that address in the \*.nes file for where it would be loaded in NES-rom. there are 4 banks:
- $8000 - $9FFF
- $A000 - $BFFF
- $C000 - $DFFF
- $E000 - $FFFF
- $8A != #0
- (A == #1) && ($8A != #0)
- 2. only when mem location $8A doesn't equal zero
- (5:25:17 PM) snatches1: remember, my comments all come from a COA perspective
- (5:27:31 PM) Jlstout123: Yeah, 2 versions are out there at the moment. The original and the SP version which added some features to the debugger
- As someone who usually plays the CPU, I loathe the early season games in which the CPU plays at the level of a brain dead rat and a MAN can run off 60-0 without trying. Two questions regarding ways to avoid this:
- 1) Is there a way to edit the rom up the level of CPU crack?

## Source

<https://tecmobowl.org/forum/topic/7144-how-tsb-decides-strength-of-cpu-opponent/page__hl__juice#entry65571>
