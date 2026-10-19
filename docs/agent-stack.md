# The agent stack

An MCP server gives the model **hands**. A skill gives it a **procedure**. Your harness gives it **context** — and context is the scarce resource.

This page is about wiring those three together without stepping on your own feet.

## Division of labour

| Layer | What it does | Examples |
|---|---|---|
| MCP server | Executes operations with structured results: build, read memory, step, disassemble, screenshot | romdev, Mesen MCP, mcp-bizhawk |
| Skill | Teaches a workflow, a format, or a tool's CLI: "read header → dump CHR → capture CDL → disassemble" | nes-skills, re-skill, romdev's SKILL.md |
| Project files | Ground truth: source, linker config, symbols, `REVERSE.md`, notes | your repo |

A common failure is installing an MCP server and expecting it to know NES. It does not. That is what the skill is for. The reverse is also true: a skill that tells the model to run `ca65` will fail if `ca65` is not on `PATH` — unless the MCP server bundles it.

## Three stacks

### Stack A — build a game (recommended default)

```
romdev (MCP)  +  romdev SKILL.md
```

- Builds with bundled cc65, runs fceumm, screenshots, reads memory.
- No host toolchain, no emulator install.
- The skill's hard rule — *never install a host compiler* — is what keeps the agent from wandering off to `brew install` in the middle of a task.

**Use when:** you are writing a homebrew ROM, converting assets, or you want a fast iterate loop.

### Stack B — debug someone else's code

```
romdev (build/run)  +  Mesen MCP (Windows) or mcp-bizhawk (any OS)
```

- romdev handles assembly and quick screenshots.
- The debugger MCP handles breakpoints, symbols, hooks, call stacks, PPU/OAM inspection.
- On Windows, Mesen MCP is the better surface. On macOS/Linux, BizHawk is the practical one.

**Use when:** you have a ROM that boots but misbehaves, or you are hunting a specific RAM address.

### Stack C — a reverse-engineering campaign

```
re-skill (process)  +  nes-skills (FCEUX Lua + retrodisasm)  +  romdev or GhidraMCP (analysis)
```

- `re-skill` keeps a `REVERSE.md` task ledger and a `labels.csv` that compounds across sessions.
- FCEUX Lua gets you screenshots, CHR dumps, execution traces and CDL coverage.
- retrodisasm turns CDL into reassemblable assembly; GhidraMCP adds decompiler pseudocode when 6502 stops being readable.

**Use when:** the job will take more than one sitting, or you need a reproducible RE workspace.

## Configs

### Claude Code

```bash
claude mcp add --transport http romdev http://127.0.0.1:7331/mcp
claude mcp add bizhawk --scope user mcp-bizhawk
claude mcp list
```

Mesen is a stdio bridge, so it goes in `.mcp.json` (project) rather than `claude mcp add`:

```json
{
  "mcpServers": {
    "mesen-inproc": {
      "command": "mesen-mcp-bridge",
      "env": {
        "MESEN_EXE": "C:/Mesen2/bin/win-x64/Release/Mesen.exe",
        "MESEN_ROM": "C:/games/yourgame.nes",
        "MESEN_CWD": "C:/games/your-project"
      }
    }
  }
}
```

### Codex CLI

`~/.codex/config.toml`:

```toml
[mcp_servers.romdev]
url = "http://127.0.0.1:7331/mcp"

[mcp_servers.bizhawk]
command = "mcp-bizhawk"
```

### opencode

`opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "romdev": {
      "type": "remote",
      "url": "http://127.0.0.1:7331/mcp",
      "enabled": true
    }
  }
}
```

### Cursor / VS Code (MCP JSON)

`.cursor/mcp.json` or `.vscode/mcp.json`:

```json
{
  "mcpServers": {
    "romdev": { "url": "http://127.0.0.1:7331/mcp" }
  }
}
```

VS Code's schema uses `"servers"` and `"type": "http"`; check your version.

### Skills go in different places

| Harness | User-level | Project-level |
|---|---|---|
| Claude Code | `~/.claude/skills/<name>/SKILL.md` | `.claude/skills/` |
| Codex | `~/.codex/skills/` | `.codex/skills/` |
| Copilot / VS Code | — | `.github/skills/` |
| Generic agents | `~/.agents/skills/` | `.agents/skills/` |

Each skill is a directory containing `SKILL.md` and optional `references/`, `scripts/`, `assets/`. Copy the whole directory, not just the Markdown.

## Session hygiene

**romdev sessions.** Every call needs an `x-romdev-session` header (the MCP client sends it as a session argument on the stateless revision). Use one descriptive id per task: `nes-platformer-color`, `rpg-text-hack`. Do not generate a new id per call — you will get a fresh, empty emulator and "No ROM loaded".

**Debugger sessions.** Mesen and BizHawk are single-instance. If two agents connect, they share one paused/running state and one breakpoint list. Run one emulator per agent, on separate ports and separate portable config directories.

**Pause before reading.** A running emulator advances between calls. Mesen's own docs put it bluntly: without `pause()`, two consecutive `read_memory` calls see different frames. romdev's `frame`/`memory` calls are synchronous, so this is less of an issue there.

**Determinism.** For regression checks, capture a save state, replay a fixed input sequence, and compare memory or a frame hash. Do not compare wall-clock timing.

**Context budget.** romdev exposes 38 tools; Mesen exposes 46. Some clients show every schema. Gearlynx has `--mcp-router` to hide advanced tools behind discovery. If your client supports tool search, use it; otherwise keep only one emulator MCP enabled at a time.

## Version pinning

Put this in your project README:

```markdown
## Tooling
- romdev 0.150.2 (npx romdevtools)
- nes-skills @ <commit sha>
- Mesen MCP mesen-mcp-v0.2
```

Why: the romdev SKILL.md is generated from the running server and will drift after an upgrade. Re-fetch it:

```bash
curl -s http://127.0.0.1:7331/skills/romdev/SKILL.md > ~/.claude/skills/romdev/SKILL.md
```

Check the server version:

```bash
curl -s http://127.0.0.1:7331/healthz
```

## A verification loop that catches lies

Models are confident about PPU timing. Make the emulator the judge:

1. **Build** — exit code 0 is necessary, not sufficient.
2. **Run N frames** — 2 at boot is not the same as 240.
3. **Read named memory** — use symbols or a known address, not a screenshot guess.
4. **Compare a hash or a saved frame** — for regressions.
5. **Re-run with input** — a title screen that renders is not a game that plays.

romdev has `frame({op:'verify'})` and `regression({op:'capture'|'check'})` for exactly this. Use them before you believe a "done".
---

Part of [AWESOME NESDEV](../README.md) · [Start here](start-here.md) · [MCP servers](mcp-servers.md) · [Skills](agent-skills.md) · [Homebrew](homebrew.md) · [ROM hacking](romhacking.md)
