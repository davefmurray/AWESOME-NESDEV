# Troubleshooting

The error messages you will actually see, grouped by where they come from. If a fix refers to a config file, the examples are in [The agent stack](agent-stack.md#configs).

## First, three questions

1. **Is the server running?** `curl -s http://127.0.0.1:7331/healthz`
2. **Is the client connected?** Restart it. Most clients only enumerate MCP servers at startup.
3. **Did you change the version?** Re-fetch skills and restart the server after an upgrade.

## romdev

| Symptom | Cause | Fix |
|---|---|---|
| `401` on every `/tool/...` call | Missing `x-romdev-session` header | Send one stable id on every call: `-H 'x-romdev-session: my-task'` |
| "No ROM loaded" mid-task | A new session id per call | Use the same id; the emulator is per-session |
| `EADDRINUSE` on 7331 | Another romdev server is running | `PORT=7332 npx romdevtools`, or kill the old one |
| `npx` fails with `EPERM` on `~/.npm/_cacache` | Root-owned npm cache | `npm_config_cache="$PWD/.npmcache" npx romdevtools`; do not `sudo` |
| Build succeeds, screen is black at 30 frames | Boot timing | Run 120–240 frames before judging |
| Black screen at 240 frames | Palette, CHR-RAM, or rendering never enabled | See [PPU bring-up](homebrew.md#ppu-bring-up-checklist) |
| `examples({op:'fork'})` says path exists | Directory already there | Pass `overwrite:true` or a new path |
| Build output is huge / omitted | Large payloads default to files | Pass `outputPath`, or `inline:true` for small ones |
| Agent tries `brew install cc65` | Its skill is not loaded | Install romdev's generated `SKILL.md`; it contains the "never install a host compiler" rule |
| First build takes a minute | Platform WASM binaries download on first use | Expected; subsequent builds are fast |
| Screenshot is a solid color | Game is on a solid background or still booting | Check `frame({op:'verify'})`, then read palette/nametable |

## Mesen MCP

| Symptom | Cause | Fix |
|---|---|---|
| "connect timed out" | Mesen did not open the TCP listener | Confirm you are running the **astrobleem/Mesen2 fork** with `--mcp`, not stock Mesen |
| Timeout with the fork | Stale build or mismatched DLLs | `Mesen.exe`, `Mesen.dll`, `MesenCore.dll` must be a matched set |
| Tools return `null` | Server-side exception | Read `mcp_server.log` in Mesen's home folder |
| "sym file not found" | Relative path resolved against `MESEN_CWD` | Use an absolute path |
| Hook never fires | Wrong address/mask, or hook not registered | Call `hook_diag()`; check `totalCalls` vs `totalMatches` |
| Emulator stalls during hooks | Stderr pipe filled with `[CPU]` warnings | Use the Python bridge (it drains stderr) or drain it yourself |
| Reads shift between calls | Emulator running between calls | `pause` first |
| Hook floods the socket | Executing per-frame loop entry | Add `matchValue`/`matchValueMask`, or use `add_frame_hook` |

## mcp-bizhawk

| Symptom | Cause | Fix |
|---|---|---|
| Tool calls hang ~10 s then time out | `bridge.lua` is not loaded | BizHawk → Tools → Lua Console → Open Script → `lua/bridge.lua`; look for `frame loop active` |
| Bridge loaded but calls still time out | BizHawk older than 2.6.2 | Upgrade; the socket wire format changed |
| "FATAL: comm.socketServer* not available" | BizHawk not launched with socket flags | `EmuHawk --socket_ip=127.0.0.1 --socket_port=8766` or Settings → Customize → External Tools |
| Memory reads are zeros | Emulator has not advanced yet | `bizhawk_frame_advance` a few frames; check `get_info.framecount` |
| `unknown memory domain` | Wrong name for this core | `bizhawk_list_memory_domains`; names are case-sensitive |
| Tools missing in client | Client enumerated before the server existed | Restart the client |

## Nes.Mcp

| Symptom | Cause | Fix |
|---|---|---|
| `dnx` not found | .NET 10 SDK missing | Install the .NET 10 SDK |
| ROM loads but nothing runs | Mapper unsupported | Only NROM/MMC1/UxROM/CNROM |
| No sprite/PPU data | Not implemented | Use Mesen/BizHawk/romdev for PPU inspection |
| Disassembly shows `.db` | Opcode not in its small table | Expected; use retrodisasm or romdev |

## GhidraMCP

| Symptom | Cause | Fix |
|---|---|---|
| Analysis is nonsense | Imported with the wrong base address or language | PRG at `$8000`, language 6502, add vectors; analyze from RESET |
| No xrefs to code | Code not disassembled | Create functions from the RESET vector, then re-analyze |
| Banked code overlaps | One flat import for a banked cart | One memory block per bank, or overlays |
| Extension missing in Ghidra | Not enabled | File → Configure → Developer → enable GhidraMCP; restart |
| Headless import fails | `GHIDRA_INSTALL_DIR` unset or Python version | Set it; use Python 3.10–3.13 |

## cc65 / ld65

| Symptom | Cause | Fix |
|---|---|---|
| `ld65: Error: Missing memory area assignment` | Segment not in the config | Add the segment to `SEGMENTS`, or remove it |
| `Segment 'CODE' overflows memory area 'PRG'` | ROM too small | Increase PRG size in header and config, or use a mapper |
| ROM builds but does nothing | Vectors missing or wrong order | `.word nmi, reset, irq` at `$FFFA` |
| `ca65: Illegal addressing mode` | Syntax differs between assemblers | ca65 uses `#$00`, not `#$00` with NESASM-style directives |
| Works in emulator, not on hardware | Header/mapper/timing | Check header, mapper init, and real PPU timing; test on a flash cart |

## ROM hacking

| Symptom | Cause | Fix |
|---|---|---|
| Disassembly is mostly garbage | Code/data not separated | Capture CDL and pass `-cdl`; disassemble from known entry points |
| Patch has no effect | Changed a mirror, not the real variable | Write-breakpoint the address; patch the writer |
| Game reboots after patch | Checksum or reset loop | Fix the checksum; check for a watchdog-style verify routine |
| Graphics corrupt after patch | CHR bank or compression | Check mapper state; re-inject compressed assets with a format-aware tool |
| Reassembly differs from original | Not byte-exact | `retrodisasm -verify`; fix data regions before editing |

## Agent behaviour

| Symptom | Cause | Fix |
|---|---|---|
| Agent installs tools you did not ask for | No skill loaded, or a broad prompt | Install the relevant `SKILL.md`; state "use romdev, do not install a toolchain" |
| Agent claims success without evidence | No verification step | Require a screenshot, a memory read, or a passing regression |
| Agent loops on the same failure | No dead-end log | Use re-skill's `dead_ends.md`, or tell it to stop and summarize |
| Two agents fight over the emulator | Shared single-instance debugger | One emulator per agent; separate ports and portable config dirs |
| Context fills with tool schemas | Too many MCP servers enabled | Keep one emulator MCP active; use tool search or a router |

## Still stuck?

- romdev: `GET /documentation` (browsable console) and `platform({op:'doc', platform:'nes', name:'troubleshooting'})`.
- Mesen: the fork's `README.MCP.md` and `python/AGENTS.md`.
- BizHawk: the mcp-bizhawk README's troubleshooting table.
- NES itself: [NESdev wiki](https://www.nesdev.org/wiki/) and the [forums](https://forums.nesdev.org/).
---

Part of [AWESOME NESDEV](../README.md) · [Start here](start-here.md) · [MCP servers](mcp-servers.md) · [Skills](agent-skills.md) · [Homebrew](homebrew.md) · [ROM hacking](romhacking.md)
