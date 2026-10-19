# Sources

Every claim in this wiki traces to one of these. Dates are when the source was read (October 2026), not necessarily when it was published.

## Directly verified

These were executed while building this wiki, on macOS, Node 26.7, romdev 0.150.2:

| Check | Result |
|---|---|
| `npx romdevtools` starts and serves `/mcp` | ✅ `initialize` handshake returned serverInfo `romdev 0.150.2` |
| `GET /skills/romdev/SKILL.md` | ✅ 426 lines, version-stamped |
| `examples({op:'fork', example:'nes/platformer'})` | ✅ 44 files, builds unmodified |
| `build({output:'run', frames:240})` | ✅ 32,784-byte NROM, title screen |
| `disasm({target:'functions'})` on the result | ✅ 124 functions, 6502 |
| `build({output:'project'})` to a `.nes` | ✅ 32,784 bytes, mapper 0, CHR-RAM |

Not verified by execution: Mesen MCP, mcp-bizhawk, Nes.Mcp, GhidraMCP, Gearlynx, retrodisasm, FCEUX Lua, the plain-cc65 skeleton. Those sections are based on the projects' own documentation, with caveats stated where they matter.

## Primary sources

| Source | Used for | Version / date |
|---|---|---|
| [monteslu/romdev](https://github.com/monteslu/romdev) | Architecture, platform table, NES ratings, tool list, bundled packages | repo, Oct 16 2026 |
| [romdevtools on npm](https://www.npmjs.com/package/romdevtools) | Version, install, package description | 0.150.2, Oct 16 2026 |
| romdev `SKILL.md` | Session rules, tool reference, "never install a host compiler" | generated at 0.150.2 |
| [astrobleem/Mesen2](https://github.com/astrobleem/Mesen2) | 46 tools, MCP transport, builds, limitations | `mesen-mcp-v0.2`, May 4 2026 |
| [mesen_mcp AGENTS.md](https://github.com/astrobleem/SNES-SuperMonkeyIsland/blob/master/tools/mesen_mcp/AGENTS.md) | First-call protocol, pitfalls, env vars | repo, 2026 |
| [dmang-dev/mcp-bizhawk](https://github.com/dmang-dev/mcp-bizhawk) | Architecture, tool list, NES memory domains, latency | npm 0.1.x, Oct 2026 |
| [Nes.Mcp on NuGet](https://www.nuget.org/packages/Nes.Mcp) | Version, tool list, mapper limits | 0.0.11, Oct 3 2026 |
| [SuperJMN/Zafiro.Nes.Debug](https://github.com/SuperJMN/Zafiro.Nes.Debug) | Nes.Mcp source / current repo name | repo, Oct 2026 |
| [LaurieWired/GhidraMCP](https://github.com/LaurieWired/GhidraMCP) | Install, headless mode, Ghidra version | repo, Oct 2026 |
| [sadnescity/mesence-claude-plugin](https://github.com/sadnescity/mesence-claude-plugin) | MesenCE plugin, 57 tools, 14 skills, install | plugin 3.1.1, Sep 23 2026 |
| [sadnescity/MesenCE](https://github.com/sadnescity/MesenCE) | Mesen2 fork with built-in MCP | 0★, Sep 23 2026 |
| [sadnescity/romhacking-claude-plugin](https://github.com/sadnescity/romhacking-claude-plugin) | Translation method, phases, Python scripts | 1.0.1 MIT, Sep 23 2026 |
| [sadnescity/claude-plugins](https://github.com/sadnescity/claude-plugins) | Marketplace entries and versions | Sep 2026 |
| [thomasjvu/mcp-nes](https://github.com/thomasjvu/mcp-nes) | Gameplay-only MCP tool list | 1★, Feb 10 2026 |
| [Gearlynx romhacking skill](https://github.com/drhelius/Gearlynx/tree/main/skills/gearlynx-romhacking) | Genre template, search loop, reference library | Gearlynx 78★, Oct 16 2026 |
| [skilldb: ROM Hacking](https://skilldb.dev/skills/retro-gaming-skills/rom-hacking) | Generic craft knowledge, paywall | page, 68 lines, 2026 |
| [scotbearss/poryrom](https://github.com/scotbearss/poryrom) | Docker-build + headless-verify + screenshot loop (GBA) | 1★ MIT, Sep 8 2026 |
| [spiiin/NesBlockFinder](https://github.com/spiiin/NesBlockFinder) | Block/screen locator and FCEUX dump workflow | 6★, 2017, no license |
| [drhelius/Gearlynx](https://github.com/drhelius/Gearlynx) | 6502 debugger tool surface, transports | `MCP_README.md`, 2026 |
| [Yuki001/nes-skills](https://github.com/Yuki001/nes-skills) | Four skills, bundled binaries, workflow | repo, Jun 2026 |
| [vgrichina/re-skill](https://github.com/vgrichina/re-skill) | Phases, scaffold, loop script | repo, Mar 2026 |
| [jonathanpeppers/dotnes](https://github.com/jonathanpeppers/dotnes) | Skills, decompiler scope, disasm scripts | repo, Sep 2026 |
| [jaymcgavren/ai-skills-marketplace](https://github.com/jaymcgavren/ai-skills-marketplace) | retro-build plugin | repo, Sep 2026 |
| [hwatkins/my-skills](https://github.com/hwatkins/my-skills) | 6502-assembly reference skill | repo, 2026 |
| [skills.rest: 6502-assembly](https://skills.rest/skill/6502-assembly) | Install command, skill summary | page, Feb 2026 |
| [Jay McGavren: Claude Code for NES Development](https://jay.mcgavren.com/2026/05/25/claude-code-for-nes-development.html) | Verified hello-world, nes.cfg, Makefile | May 25 2026 |
| [NESdev wiki](https://www.nesdev.org/wiki/) | Memory map, PPU registers, iNES, mappers, APU, palettes | continuously updated |
| [NESdev wiki: 64 core pages](https://www.nesdev.org/wiki/) | Source for the seven installable skills in `skills/` | fetched 2026-10-19 |
| [Nerdy Nights](https://nerdy-nights.nes.science/) | Learning path | archived course |
| [nesdoug](https://nesdoug.com/) | C tutorials | site, 2026 |
| [cc65](https://cc65.github.io/) | Assembler/linker behavior | docs, 2026 |
| [FamiStudio](https://www.famistudio.org/) | Audio tooling | site, 2026 |
| [Flips](https://github.com/Alcaro/Flips) | IPS/BPS patching | repo, 2026 |

## Derived skills

The `skills/` library was distilled from 64 NESdev Wiki pages fetched on 2026-10-19. The page list is in [`skills/nesdev-wiki-guide/references/page-index.md`](../skills/nesdev-wiki-guide/references/page-index.md). Prose was rewritten and tables reformatted; no wiki article is copied verbatim. The wiki retains its own terms — link back to it rather than mirroring sections.

## Repository metrics

Star counts and last-push dates were read from the GitHub API on **October 18, 2026** and are recorded in the pages where they matter, to give a sense of maturity — not as a quality score. A 23-star project (romdev) is the most capable option here; a 1-star project (nes-skills) has the most NES-specific content.

## Corrections from the field notes

Three claims in the source notes that did not survive a direct check:

1. **"sadnescity/claude-plugins mesen2 — 33 tools."** The current marketplace entry is `mesence` **3.1.1 with 57 tools** (sourced from `sadnescity/mesence-claude-plugin`). The 33-tool `mesen2` 2.0.1 plugin is superseded. The 57/14 numbers come from the plugin's own README and the marketplace JSON.
2. **"drhelius/gearlynx-romhacking."** There is no standalone repository by that name. The skill lives at `drhelius/Gearlynx/skills/gearlynx-romhacking`, alongside a debugging skill and a hardware reference library.
3. **"Future-dated marketplace timestamps."** Checked against the GitHub API on 2026-10-18: MesenCE and both plugins were pushed 2026-09-23; Gearlynx 2026-10-16. Not future-dated at the time of writing. Re-check before relying on activity claims.

Star counts recorded here are from the GitHub API on 2026-10-18, not marketplace pages.

## How claims were graded

- **Verified** — executed; output observed.
- **Documented** — stated by the project in its README, manual or release notes.
- **Inferred** — follows from the above, but not directly tested (e.g. "works on macOS" derived from a Python package plus a macOS-capable emulator).
- **Judgement** — explicitly opinion: "best", "weakest", "worth installing".

Where a project contradicts itself (e.g. README vs npm description on platform count), the versioned package and the running server win.

## Corrections

If something here is wrong or has moved, open an issue or a PR. Include the version you tested and the output you saw. "It didn't work" is not actionable; a log line is.
---

Part of [AWESOME NESDEV](../README.md) · [Start here](start-here.md) · [MCP servers](mcp-servers.md) · [Skills](agent-skills.md) · [Homebrew](homebrew.md) · [ROM hacking](romhacking.md) · [Cold ROM](cold-rom-playbook.md)
