# MCP servers

Six servers are worth knowing. One covers the whole NES loop; two are emulator debuggers; one is a minimal NES core; one is a general reverse-engineering tool; one is a 6502 reference implementation you can learn from.

## Comparison

| Server | Systems | Transport | NES depth | Install | State |
|---|---|---|---|---|---|
| **romdev** | 19 retro systems | Streamable HTTP (localhost:7331) | Build + run + debug + disassemble + patch | `npx romdevtools` | ✅ |
| **Mesen MCP** | NES, SNES, GB/GBC/GBA, PCE, SMS/GG, WS | TCP JSON-RPC + Python stdio bridge | Deep debugger: hooks, symbols, PPU/OAM renders | Build fork / Windows zip | ✅ Windows |
| **MesenCE** | NES, SNES, GB/GBA, PCE, SMS/GG, WS | Streamable HTTP (localhost:9100) | 57 tools + 14 skills: CDL, labels, TBL text search, patching | MesenCE + plugin marketplace | 🧪 0★ |
| **mcp-bizhawk** | NES, SNES, GB/GBC/GBA, Genesis, N64, PSX, Atari, Lynx, … | stdio + Lua bridge in BizHawk | Memory, input, savestates, screenshots | `npm i -g mcp-bizhawk` | ✅ |
| **Nes.Mcp** | NES only | stdio | CPU step, breakpoints, memory, screen | `dnx Nes.Mcp --yes` | 🧪 early |
| **GhidraMCP** | Any Ghidra target | HTTP + stdio client | Static analysis only; 6502 via Ghidra | Ghidra extension + `uvx` | ✅ |
| **Gearlynx** | Atari Lynx | stdio or HTTP | 6502 debugger reference, not NES | `.mcpb` / binary | ✅ |

---

## romdev

**Repo:** <https://github.com/monteslu/romdev> · **Version:** 0.150.2 (Oct 16, 2026) · **License:** MIT for its own code; bundled third-party notices apply

The only server here that can take you from an empty directory to a patched, reassembled ROM without installing a compiler. Toolchains (cc65, SDCC, RGBDS, asar, gcc for m68k/ARM/MIPS/SH, and SDKs) and emulator cores (fceumm, gambatte, bsnes, genesis_plus_gx, …) are compiled to WebAssembly and loaded per platform on first use.

### NES capabilities

| Job | Tool | Notes |
|---|---|---|
| Fork a working project | `examples({op:'fork', example:'nes/platformer'})` | 44 files: C sources, crt0, linker config, runtime, docs |
| Build | `build({output:'rom'|'run'|'project'|'reassemble'})` | `run` builds, loads, runs and screenshots in one call |
| Run / step / screenshot | `frame`, `state`, `loadMedia` | libretro fceumm core |
| Inspect | `memory`, `cpu`, `sprites`, `palette`, `background` | Read/write RAM, PPU, OAM; tilemap and palette decode |
| Breakpoints | `breakpoint({on:'exec'|'read'|'write'|'pc'})` | Also `{on:'jumptable'}` to resolve computed jumps by running |
| Watch | `watch({on:'range'|'pc'|'copy'|'dma'})` | Find the routine that touches a range |
| Disassemble | `disasm({target:'...'})` | `project` = byte-exact rebuildable; `functions`, `cfg`, `xrefs`, `reachable`, `decompile` |
| Symbols | `symbols({op:'analyze'|'resolve'|...})` | Rizin/Ghidra-backed |
| Patch | `romPatch({op:...})` | Includes re-injection of compressed assets |
| Assets | `encodeArt`, `importArt`, `encodeAudio` | PNG/Aseprite/Tiled → tiles, tilemaps, palettes; FamiTone2 audio |
| Regression | `regression({op:'capture'|'check'})`, `frame({op:'verify'|'verifyRecompile'})` | Frame/memory/audio checks |

NES is rated **Hard** to build and **Medium** to hack in romdev's own docs. The PPU is the reason: OAM/NMI timing and CHR-RAM give you no partial credit. The disassembler is mapper-aware, and many NES games store data plainly, which is why hacking rates easier than building.

### Install and connect

```bash
npx romdevtools          # Node 24+, listens on 127.0.0.1:7331
```

- MCP: `http://127.0.0.1:7331/mcp`
- Plain HTTP: `POST /tool/{name}` with `x-romdev-session: <id>` (401 without it)
- Schema: `GET /openapi.json`, `GET /documentation`
- Agent skill: `GET /skills/romdev/SKILL.md`
- Live observer: `http://127.0.0.1:7331/livestream`

### Example: a full session

Verified while writing this wiki:

```text
examples({op:'fork', example:'nes/platformer', name:'nesdemo', path:'./nesdemo'})
build({output:'run', platform:'nes', path:'./nesdemo', frames:240})
disasm({target:'functions', path:'./nesdemo/nesdemo.nes', outputPath:'./functions.json'})
```

Result: 32,784-byte NROM (16 B header + 32 KB PRG, CHR-RAM, mapper 0), title screen after 240 frames, 124 functions detected by the 6502 analysis.

### Gotchas

- **Local paths only.** `path`, `outputPath` etc. are filesystem paths on the machine running the server, not uploads.
- **Session id required.** Use one descriptive id for the whole task. A new id per call means a new empty emulator.
- **Big outputs default to files.** Pass `outputPath` (or `inline:true`) for ROM bytes, disassembly, memory dumps.
- **First use downloads platform binaries** for that platform. Budget a minute on first build.
- **`npx` cache permissions.** If npm's cache has root-owned files, use `npm_config_cache="$PWD/.npmcache"`.
- **One server, many agents.** Sessions isolate emulators, but CPU/GPU contention is real. Two agents building 3D consoles at once will be slow.

---

## Mesen MCP

**Repo:** <https://github.com/astrobleem/Mesen2> · **Release:** `mesen-mcp-v0.2` (May 4, 2026) · **License:** GPL-3.0 (inherits Mesen)

A fork of Mesen 2 with a native MCP server inside the emulator. This is the deepest debugger surface available to an agent: 46 JSON-RPC tools, frame-exact execution, and hooks that push events to the client mid-frame instead of being polled.

### Why it is good

- **Frame-exact `run_frames`** — no `sleep(2)` guessing under max-speed emulation.
- **Hooks with notifications** — `add_exec_hook`, `add_read_hook`, `add_write_hook`, `add_frame_hook`, with server-side `matchValue`/`matchValueMask` filtering so a hot address does not flood the socket.
- **Symbols** — WLA-DX `.sym` lookup, `symbolic_dump` over an address range, and Pansy metadata support.
- **Visual state** — `render_tilemap`, `render_tile_sheet`, `render_oam`, `render_palette`, `take_screenshot`, `render_filmstrip`.
- **Determinism** — save states, movie record/playback, `memory_diff` over N frames, audio capture with SHA-256 fingerprints.
- **Disassembly and trace** — `disassemble`, `trace_log`, `run_until`, `read_dma_state`.

### Install

Windows, easiest: download the `Mesen-MCP-Windows-x64-mesen-mcp-v0.2.zip` release. It contains a matched `Mesen.exe`, `Mesen.dll`, `MesenCore.dll`, the Python client and notes.

From source (any OS, more work):

```bash
git clone --branch mesen-mcp-v0.2 https://github.com/astrobleem/Mesen2
# build native + managed per COMPILING.md, then:
pip install -e Mesen2/python
```

### Configure

`.mcp.json`:

```json
{
  "mcpServers": {
    "mesen-inproc": {
      "command": "mesen-mcp-bridge",
      "env": {
        "MESEN_EXE": "/path/to/Mesen.exe",
        "MESEN_ROM": "/path/to/game.nes",
        "MESEN_CWD": "/path/to/project",
        "MESEN_PORT": "7333"
      }
    }
  }
}
```

`MESEN_EXE` must point at a folder with matched `Mesen.exe`, `Mesen.dll` and `MesenCore.dll`. Stale publish folders launch and then time out.

### First calls

```text
pause
get_state            # frameCount, isRunning, isPaused
read_memory          # after pausing, reads are coherent
run_frames(60)       # frame-exact
add_write_hook(0x...)
drain_notifications
take_screenshot
```

### Gotchas

- **Windows x64 prebuilt only.** The release workflow publishes one zip. macOS/Linux require building both native and managed sides; the README documents a Windows build primarily.
- **Pause before multi-call inspection.** Otherwise calls see different frames.
- **Drain stderr.** Mesen's `[CPU]` warnings can fill the pipe and stall the emulator thread; the Python bridge drains it for you.
- **Filter hot hooks.** An exec hook on a per-frame loop entry fires thousands of times per frame.
- **Symbol paths are absolute.** Relative paths resolve against `MESEN_CWD`, which defaults to the ROM directory.
- **Not on npm.** It is a Python package plus an emulator fork, not a `npx` one-liner.

An earlier, smaller fork exists — <https://github.com/crlsh/mesen-mcp> (6 tools, no event push). Useful as a reference for the typed-command-on-emulator-thread pattern; not the one to install today.

---

## MesenCE + mesence plugin

**Repo:** <https://github.com/sadnescity/MesenCE> · **Plugin:** `mesence` 3.1.1 (Sep 2026) · **License:** GPL-3.0

A Mesen2 fork with a built-in MCP server, plus a Claude Code plugin that ships the configuration and 14 reference skills. This is the closest thing to an end-to-end NES reverse-engineering kit: 57 tools, per-console workflows, and a dedicated NES skill.

### What you get

| Layer | Contents |
|---|---|
| MCP server | 57 tools: stepping, memory search/freeze, disassembly/assembly, labels, CDL, tracing, profiler, sprites/tilemaps, Lua, TBL text search, ROM patching |
| Skills | `mesen-setup`, `mesen-debug-execution`, `mesen-memory`, `mesen-disassembly`, `mesen-emulator`, `mesen-romhacking`, `mesen-console-reference`, and per-console workflows (`mesen-workflows-nes`, `-snes`, `-gb`, `-gba`, `-pce`, `-sms`, `-ws`) |
| Transport | Streamable HTTP on `localhost:9100` |

### Install

1. Install [MesenCE](https://github.com/sadnescity/MesenCE) (Windows/Linux/macOS).
2. Enable its MCP server: **Tools → MCP Server Config**, or launch with `--mcp` (optional `--mcp-port=PORT`).
3. In Claude Code:

```text
/plugin marketplace add sadnescity/claude-plugins
/plugin install mesence@sadnescity-plugins
```

### Why it matters

The NES workflow skill is the procedure layer that other emulator MCPs lack: it tells the model how to go from a cold ROM to a labelled address, while the tools supply memory search, write breakpoints and CDL. If you want one install for live NES hacking, try this after romdev.

### Caveats

- **0★, one author, no release history.** MesenCE is a separate fork — not upstream Mesen2, and not the astrobleem MCP fork. Pin the version and check ROM compatibility.
- The marketplace previously listed a `mesen2` plugin (2.0.1, 33 tools). It is superseded by `mesence` (3.1.1, 57 tools). A page showing 33 is stale.
- GPL-3.0; the plugin inherits the emulator's license.
- Its skills are reference workflows, not guarantees. Verify the addresses it suggests.

## mcp-bizhawk

**Repo:** <https://github.com/dmang-dev/mcp-bizhawk> · **Install:** npm · **License:** MIT

Drives BizHawk, the TAS community's emulator, through a Lua bridge. The transport is inverted: BizHawk's Lua has no server sockets, so the Node process listens and the Lua script dials in once per frame.

```
MCP client --stdio--> mcp-bizhawk --TCP:8766--> bridge.lua (inside BizHawk)
```

### Setup

```bash
npm install -g mcp-bizhawk

# launch BizHawk with the socket server enabled
EmuHawk.exe --socket_ip=127.0.0.1 --socket_port=8766 game.nes
```

Then in BizHawk: **Tools → Lua Console → Open Script → `lua/bridge.lua`**. Look for `frame loop active` in the console.

```bash
claude mcp add bizhawk --scope user mcp-bizhawk
```

### Tools

`bizhawk_ping`, `get_info`, `list_memory_domains`, `read8/16/32`, `write8/16/32`, `read_range`, `write_range`, `press_buttons`, `frame_advance`, `pause`, `unpause`, `reset`, `screenshot`, `save_state`, `load_state`.

### NES memory domains

| Domain | Contents |
|---|---|
| `RAM` | 2 KB CPU RAM |
| `PPU` | PPU address space (pattern tables, nametables, palettes) |
| `OAM` | sprite memory |
| `PRG ROM` | cartridge PRG |
| `CHR` | pattern tables (ROM or RAM) |

Use `bizhawk_list_memory_domains` to confirm names for the loaded core.

### Gotchas

- **~1 frame latency per call.** The bridge polls once per frame. Fine for RAM hunting and savestate experiments; not for cycle-level work.
- **BizHawk 2.6.2+** is required; older builds use a different socket wire format.
- **Hangs mean the Lua script is not loaded**, not that the MCP server is broken. Check the Lua console.
- **macOS/Linux work**, which makes this the practical debugger MCP outside Windows.

---

## mcp-nes

**Repo:** <https://github.com/thomasjvu/mcp-nes> · **Stars:** 1 · **License:** none declared · **Transport:** stdio or SSE

A pure-JavaScript NES emulator exposed as an MCP server, with a CRT-styled browser UI. No external emulator, no native dependency.

Tools: `load_rom`, `get_screen`, `press_up/down/left/right`, `press_a/b`, `press_start/select`, `wait_frames`, `is_rom_loaded`, `list_roms`.

**It cannot read memory.** That makes it a validation harness, not a hacking tool: useful for "does it boot", "does this input sequence reach the menu", or capturing a screenshot without installing an emulator. For memory work use MesenCE, Mesen MCP, BizHawk or romdev.

## Nes.Mcp

**Package:** NuGet `Nes.Mcp` 0.0.11 · **Repo:** <https://github.com/SuperJMN/Zafiro.Nes.Debug> · **License:** `MIT AND WTFPL AND GPL-3.0-or-later` (bundled components — check before redistributing)

A pure managed NES core (vendored ADNES) wrapped in a synchronous debug session. Small, cross-platform, no GUI — useful for CI or quick inspection on a machine where you do not want an emulator app.

### Install

```bash
dnx Nes.Mcp --yes       # requires .NET 10
```

stdio transport. Configure like any stdio server.

### Tools (16)

`load_rom`, `reset`, `step_instruction`, `run_frame`, `set_controller`, `press_buttons`, `continue_until_break`, `set_breakpoint`, `clear_breakpoint`, `list_breakpoints`, `get_state`, `read_registers`, `read_memory`, `write_memory`, `disassemble`, `capture_screen`.

### Limits

- Mappers: **NROM, MMC1, UxROM, CNROM** only.
- No PPU-register or OAM inspection; screen capture is the rendered framebuffer.
- No savestates, no watchpoints.
- Disassembler covers common opcodes; unknown bytes come back as `.db`.

Good for: a headless smoke test, a tiny homebrew ROM, a CI job that needs a CPU step. Not for commercial-ROM reverse engineering.

---

## GhidraMCP

**Repo:** <https://github.com/LaurieWired/GhidraMCP> · **Stars:** ~11.4k · **License:** Apache-2.0

Exposes Ghidra's decompiler, symbol renaming, function listing and xrefs to an MCP client. It is not NES-aware; it is a very good generic static-analysis backend.

### Install

1. Install Ghidra **12.1.4**.
2. Download the GhidraMCP release zip; **File → Install Extensions → +**; restart Ghidra; enable the plugin under **File → Configure → Developer**.
3. Add the MCP server:

```bash
claude mcp add ghidra -- uvx --from git+https://github.com/LaurieWired/GhidraMCP ghidra-mcp --ghidra-server http://127.0.0.1:8080/
```

Headless, no GUI:

```bash
GHIDRA_INSTALL_DIR=/path/to/ghidra \
uvx --python 3.13 --from "ghidra-mcp[headless] @ git+https://github.com/LaurieWired/GhidraMCP" \
  ghidra-mcp --headless --binary ./game.prg --project ./ghidra-project
```

### NES recipe

1. Strip the 16-byte iNES header; import the **PRG ROM only** as `Raw Binary`.
2. Language: **6502** (variant depending on your Ghidra version).
3. Base address: `0x8000` for a 32 KB PRG; `0xC000` for a 16 KB PRG mapped high.
4. For banked carts (MMC1/MMC3), import each 8/16 KB bank as its own memory block at its switchable window, or import the whole PRG once and create overlays. There is no iNES loader doing this for you.
5. Add the vectors: at `0xFFFA` NMI, `0xFFFC` RESET, `0xFFFE` IRQ/BRK (little-endian).
6. Start analysis at the RESET vector, not at offset 0.

### Limits

- No mapper awareness, no CHR decoding, no PPU semantics.
- 6502 decompiler output is rough; use it for structure, then read the assembly.
- Renaming and comments live in the Ghidra project — commit the `.gpr`/`.rep` if you want them to persist.

---

## Gearlynx

**Repo:** <https://github.com/drhelius/Gearlynx> · **License:** GPL-3.0

An Atari Lynx emulator with a first-class MCP server: CPU registers, multiple memory areas, breakpoints (exec/read/write/range/IRQ), call stack, trace log with hardware filters, profiler, rewind, symbols, screenshots, video recording, and the Lynx hardware reference as MCP resources.

**It is not an NES emulator.** It is included because its tool surface is the best worked example of what a 6502 debugger MCP should expose, and because Lynx homebrew is a pleasant second platform once NES PPU timing has annoyed you. The same author maintains Geargrafx (PC Engine), Gearcoleco and Gearboy with the same pattern.

Install: download the `.mcpb` for your platform, or run `gearlynx --mcp-stdio` / `gearlynx --mcp-http --headless --portable`. HTTP defaults to `127.0.0.1:7777/mcp`; loopback needs no token, non-loopback binds require `GEARLYNX_MCP_HTTP_TOKEN`.

---

## Choosing

- **Only one server?** romdev.
- **Want the deepest live NES debugger with a procedure layer?** MesenCE + the `mesence` plugin.
- **Windows and want the astrobleem fork?** romdev + Mesen MCP.
- **macOS/Linux and need breakpoints without building Mesen?** romdev + mcp-bizhawk, or MesenCE if the fork runs on your machine.
- **CI, no display?** romdev (best) or Nes.Mcp (smallest).
- **Only need to play a ROM and screenshot it?** mcp-nes.
- **Static analysis at scale?** GhidraMCP, fed by a romdev or retrodisasm project.
- **Learning what a debugger MCP should feel like?** read Gearlynx's tool list.
---

Part of [AWESOME NESDEV](../README.md) · [Start here](start-here.md) · [MCP servers](mcp-servers.md) · [Skills](agent-skills.md) · [Homebrew](homebrew.md) · [ROM hacking](romhacking.md) · [Cold ROM](cold-rom-playbook.md)
