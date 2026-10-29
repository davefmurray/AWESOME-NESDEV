# Integrating an art replacement

## Keep the patch reviewable

For an existing ROM, preserve a known input and produce a separate output.
Guard its header/layout, the replaced instructions, called stock routines
and entire claimed free-space regions. Record `(bank, address, expected,
replacement)` entries and assert that all changed bytes lie inside them.
Do not insert bytes into a ROM image and shift later banks or vectors.

Guard fonts borrowed from the input separately. Prefer references or glyph
extraction at build time over committing commercial font bytes. Original
artwork and reproducible sources can be tracked independently of the ROM.

Check all references before claiming a CHR bank. A data-table preset may
select it indirectly even if there is no literal register write. Combine
static bank/scene analysis with a mapper trace of relevant screens. Report
what was traced; a tour cannot prove every computed path unreachable.

## Preserve execution contracts

Trace entry state and every exit, including cancel, title return, attract,
active-series resume and held buttons. Identify live registers, stack depth,
zero-page scratch, mapper shadows, NMI guards, PPU control/scroll state and
pending display-list length. Clear a pending list only when that matches the
screen contract; do not discard a later scene's work.

Write PPU data with rendering disabled or within a measured vblank budget.
For an interactive update, count interrupt entry, OAM DMA stalls, mapper
writes and the worst update payload. NTSC vblank is roughly 2,273 CPU cycles;
that is not a portable PAL/Dendy budget. Restore PPU address/scroll latches
and interrupt guards in the order the surrounding engine requires.

A faster replacement draw can change how long a held button lasts or when a
song advances. Compare frame-by-frame scene, input and APU traces before
adding timing compensation. If preserving an exact interval is necessary,
measure and test it at the final code placement, including page-crossing
costs. Never copy another game's delay constant.

Keep audio ownership explicit. If the NMI already updates the stock music,
a new loop must not tick it again. If an existing menu disabled music with
NMI, establish a measured once-per-frame update and bank-restoration
contract before adding sound. These are engine decisions, not pxl features.

## Make regeneration safe

Render pxl to a fresh temporary directory. Discover the full generated file
set, including nested sprites. Validate all destinations as one batch before
installing any output. Include JSON, previews, screenshots and future PNG
paths, not only existing files.

Reject output/input collisions after resolving symlinked parents; check
existing files for shared inode identity as well as path identity. Reject
an initially missing generated PNG chosen as the explicit JSON or preview
target. A hardlink can overwrite a ROM even when the filenames differ.
Use sibling temporary files and atomic replacement for installation instead
of writing through existing symlinks or hardlinks. Atomic replacement is
per file; it does not make a multi-file publish transactional.

A check-only command should render in scratch storage, compare with tracked
assets and leave them untouched. Screenshot probes need the same boundary
checks before contacting an emulator. Test refusals using disposable copies
and verify that protected contents remain unchanged.

## Acceptance evidence

Use tests proportional to the change. For a static recolor, reuse existing
checks. For a new renderer or layout, useful layers are:

| Layer | What it establishes |
|---|---|
| Source regeneration | Pinned pxl plus layout recreates the same assets |
| Asset decode | Tile/attribute/palette bytes reproduce intended pixels |
| ROM execution | Real writers format edge values and retain state/exits |
| Negative controls | Removing a guard or moving a field actually fails |
| Emulator tour | Visible entry, redraw, input, audio and return paths work |
| Gameplay regression | Art changes do not break the surrounding game loop |

Compare against the old ROM for behavior intended to stay unchanged. Use
independent expected values for new layout rules. Reject test execution into
RAM or data when a probe should be in ROM; an incorrect entry point can
wander into unrelated code and still appear to pass.

Stamp logs with ROM SHA, tool version, command/options and scenario type.
Record RAM-injected fixtures separately from controller-played cases. Use
screenshots plus palette, nametable and OAM checks where available. A CPU
model with simplified PPU behavior is not hardware validation.

See [PPU rendering](https://www.nesdev.org/wiki/PPU_rendering) for timing and
[this project's worked example](little-league.md) for measured tradeoffs.
