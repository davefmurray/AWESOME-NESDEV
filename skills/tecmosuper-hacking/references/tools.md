# TSB tooling

| Tool | Use | Link |
|---|---|---|
| TSBTool Supreme | Text-file roster/team editor; applies `SET` commands; 28/32-team | [topic](https://tecmobowl.org/forums/topic/11106-tsb-editor-tsbtool-supreme-season-generator/) |
| TSB Editor | GUI roster/team editor (older workflow) | same topic |
| asm6f | Rebuild the disassembly | [asm6f](https://github.com/freem/asm6f) |
| Mesen | Debugger, memory viewer, accurate PPU | [mesen.ca](https://www.mesen.ca/) |
| FCEUX | Lua, CDL, hex editor, familiar UI | [fceux.com](https://fceux.com/) |
| HxD / 010 Editor | Direct file edits | [HxD](https://mh-nexus.de/en/hxd/) |
| YY-CHR | CHR/tile editing | [YY-CHR](https://www.romhackplaza.org/index.php/utilities/yy-chr-utility) |
| Flips | IPS/BPS patch creation | [Flips](https://github.com/Alcaro/Flips) |

## TSBTool workflow

1. Export or write a text file with team/player fields and `SET` lines.
2. Open the ROM in TSBTool, load the text, check for overlapping SETs.
3. Save to a **copy**.
4. Test in Mesen/FCEUX.
5. Diff the copy against pristine; only the intended bytes should change.

## Disassembly workflow

```bash
git clone https://github.com/bruddog/Tecmo_Super_Bowl_NES_Disassembly
cd Tecmo_Super_Bowl_NES_Disassembly
# put your original ROM here as TSB.nes
asm6f_32.exe master_build.asm -L
```

`asm6f_32.exe` is Windows; use a native asm6f build elsewhere. The build reads graphics and samples from `TSB.nes`, so the ROM is required.

## Documentation

- [TSB Hacks directory](https://tecmobowl.org/forums/topic/9725-tsb-hacks-documentation-directory-updated-01182023/)
- [ROM hex location index](https://tecmobowl.org/topic/53101-tsb-rom-hex-location-index/)
- [Many various ROM locations](https://tecmobowl.org/topic/53112-many-various-rom-locations/)
- [Cutscene/event editing](https://tecmobowl.org/topic/13387-an-easy-guide-to-changing-and-deleting-various-cutscenes/)
