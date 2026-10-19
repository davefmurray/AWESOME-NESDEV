# SET commands

## Syntax

```text
SET(0xOFFSET,0xBYTES)
SET (0xOFFSET, 0xBYTES)   # spaces are accepted
#SET(0xOFFSET,0xBYTES)    # commented out
```

- `OFFSET` is a **file offset** in the ROM, including the 16-byte header.
- `BYTES` is written in order. One byte is two hex digits; `0xEAEA` writes two bytes.
- The file is patched in place when TSBTool saves.

## Examples from the community list

```text
SET(0x28293,0xEAEAEAEA)          # NOP four bytes
SET(0x246B0,0x1C)                # one-byte value change
SET(0x20038,0x4C8980)            # JMP $8089
SET(0x1897f,0x20)                # branch opcode change
```

## Safety

- Back up the ROM; TSBTool writes on save.
- Use the overlap checker before saving.
- Record every SET in your project notes with the source URL and what it does.
- Apply one group at a time and test; a batch makes bisecting impossible.
- SET offsets assume a specific base ROM (28/32 team, region, revision).
- A SET that writes code must match the CPU instruction boundaries; `0xEA` is NOP, not a universal undo.

## Where to find commands

- [Set commands list](https://tecmobowl.org/forums/topic/69338-set-commands-list-for-nes-tsb-updated-91725/)
- [TSB Hacks documentation directory](https://tecmobowl.org/forums/topic/9725-tsb-hacks-documentation-directory-updated-01182023/)
- Individual hack threads; the URL is usually in the command's comment.

## Converting a CPU address to a SET offset

For fixed bank 30 (`$C000–$DFFF`): `offset = 0x3C010 + (cpu - 0xC000)`.
For fixed bank 31 (`$E000–$FFFF`): `offset = 0x3E010 + (cpu - 0xE000)`.
For a switchable bank: `offset = 0x10 + bank*0x2000 + (cpu - window_base)` only while that bank is mapped.
