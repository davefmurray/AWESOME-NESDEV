# Start here

You do not need to install an NES toolchain to start. You need one server, one skill, and a ROM to look at.

## Who this is for

- You have a coding agent (Claude Code, Codex, Cursor, opencode, T3 Code, anything that speaks MCP) and want it to build or inspect NES software.
- You know some programming, maybe no 6502. That is fine for a first homebrew ROM; the examples are C and the agent can explain the assembly.
- You want to hack a ROM you own, and you want a repeatable process rather than random poking.

## Prerequisites

| Tool | Version | Needed for | Notes |
|---|---|---|---|
| Node.js | 24+ | romdev | `npx romdevtools`; bundles all compilers/emulators as WASM |
| Python | 3.10–3.13 | Mesen MCP bridge, GhidraMCP headless, re-skill | 3.8+ is enough for re-skill scripts |
| .NET SDK | 10 | Nes.Mcp | `dnx Nes.Mcp --yes` |
| Ghidra | 12.1.4 | GhidraMCP | Plus the GhidraMCP extension |
| BizHawk | 2.6.2+ | mcp-bizhawk | Older builds use a different socket format |
| git, make | any | everything | `make` only for plain-cc65 projects |

You do **not** need cc65, SDCC, a C compiler, or an emulator installed to use romdev. It ships them as WebAssembly. Install a host toolchain only if you want to work outside the agent loop.

## Install order

1. **romdev** — the build/run/inspect loop.
2. **The NES skill pack** (`Yuki001/nes-skills`) — format, 6502, FCEUX Lua, retrodisasm.
3. **A debugger MCP** only if you need one: Mesen MCP on Windows, mcp-bizhawk elsewhere.
4. **GhidraMCP** only when you need decompiler output.

Full commands are in [The agent stack](agent-stack.md) and [MCP servers](mcp-servers.md).

## Your first 30 minutes

### 1. Start the server (1 min)

```bash
npx romdevtools
# romdev (v0.150.2) listening on http://localhost:7331/mcp
```

Leave it running. First run downloads the package; platform binaries (cc65, fceumm) load on first use.

### 2. Save the skill and register the MCP (2 min)

```bash
mkdir -p ~/.claude/skills/romdev
curl -s http://127.0.0.1:7331/skills/romdev/SKILL.md > ~/.claude/skills/romdev/SKILL.md
claude mcp add --transport http romdev http://127.0.0.1:7331/mcp
```

Other harnesses: see [configs](agent-stack.md#configs).

### 3. Fork, build, look (5 min)

Ask the agent:

```text
Use romdev. Fork the nes/platformer example into ./mygame, then build it
with output "run" for 240 frames and show me the screenshot.
```

Expected: a 32 KB NROM with CHR-RAM, running title screen, and a screenshot. If you get a black screen at 30 frames, that is usually just boot timing — run 120–240 frames.

### 4. Change something (10 min)

```text
Open main.c in ./mygame. Change the background color to dark green,
rebuild, run 240 frames, and show me the result.
```

The point is the loop: **one change → rebuild → screenshot**. Keep the working ROM as your oracle.

### 5. Read the docs the example shipped (10 min)

Every romdev fork includes `MENTAL_MODEL.md` and `TROUBLESHOOTING.md` for that platform. Read them before writing your own PPU code. They are better than generic NES advice because they match the runtime you are actually using.

## OS notes

### macOS

- Everything except Mesen MCP works natively. Mesen's MCP fork publishes Windows x64 builds; building the macOS app from source is possible but not a one-liner.
- Use **mcp-bizhawk** for live debugging on macOS, or romdev's own breakpoints.
- If `npx` fails with `EPERM` on `~/.npm/_cacache`, npm's cache has root-owned files. Use a project-local cache rather than `sudo`:

```bash
npm_config_cache="$PWD/.npmcache" npx romdevtools
```

### Linux

- Same as macOS. Mesen's Linux build needs SDL2 (`sudo apt install libsdl2-2.0-0` or equivalent).
- Headless CI: romdev is the easiest option because it needs no display.

### Windows

- romdev, Mesen MCP, Nes.Mcp and mcp-bizhawk all run natively. Mesen MCP is the strongest debugger here.
- Paths in MCP configs need escaped backslashes or forward slashes in JSON.
- If you use WSL for the agent but Windows for the emulator, they are different machines as far as file paths and loopback ports are concerned. Pick one side.

## Conventions this wiki assumes

- **One session id per task** for romdev, e.g. `nes-platformer-color`, sent as `x-romdev-session`. It labels your work on the live observer page and keeps your emulator state.
- **Project-local paths.** ROMs, disassembly projects and screenshots live next to the project, not in `/tmp`.
- **Pin versions.** Put the romdev version and the skill commit in your project README. These tools move fast.
- **No secrets in configs.** MCP configs are plain JSON and get committed by accident.

## Legal and ethical baseline

- Dump your own cartridges. Do not download ROMs.
- Do not redistribute ROMs or patched ROMs of commercial games.
- Homebrew you write is yours; check the licenses of the runtime libraries you link (romdev's bundled libraries are permissive, its recompiled carts are not — see the NOTICE in that repo).
- Reverse engineering for interoperability and personal study is one thing; distributing someone else's game is another. Know which one you are doing.
---

Part of [AWESOME NESDEV](../README.md) · [Start here](start-here.md) · [MCP servers](mcp-servers.md) · [Skills](agent-skills.md) · [Homebrew](homebrew.md) · [ROM hacking](romhacking.md)
