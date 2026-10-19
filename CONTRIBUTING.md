# Contributing

This is a field guide, not a link farm. The bar is simple: **you ran it, and you can say what happened.**

## What belongs here

- An MCP server, skill, tool or workflow that helps an agent do NES/Famicom work.
- A correction to something that is wrong, outdated, or overstated.
- A caveat that cost you an afternoon.

## What does not

- ROMs, patches, or copyrighted assets.
- "I heard this works" without a version.
- Link-only entries with no explanation of what the thing is for.
- Hype. Star counts are recorded, but they are not the argument.

## Adding an entry

Use this shape, in the relevant page:

````markdown
## Tool name

**Repo:** <https://...> · **Version:** x.y.z (date) · **License:** MIT

One paragraph: what it is, what it is for.

### NES capabilities
- ...

### Install
```bash
...
```

### Gotchas
- ...

### Verdict
One or two sentences. Who should use it, who should not.
````

Then add a row to the comparison table at the top of the page and to the status board in `README.md`.

## Verification standard

Say which of these you did:

- **Ran it** — built/ran/inspected something and saw output.
- **Read the source** — behavior confirmed in code.
- **Read the docs** — stated by the project, not tested.
- **Judgement** — opinion, labelled as such.

Include the version and OS. "Works on my machine" is fine if you say which machine.

## Style

- Second person, present tense. "Run `npx romdevtools`", not "the user should run".
- Commands in fenced blocks with the language tag.
- Tables for comparisons; prose for reasoning.
- Link to the upstream repo, not a blog repost, when both exist.
- Date-stamp anything that will rot: versions, star counts, "last push".
- Keep pages under ~250 lines. If it grows, split it and link.

## Link checks

Before opening a PR, check that new links resolve:

```bash
# one-off, no dependencies
while read -r url; do
  printf '%s %s\n' "$(curl -sL -o /dev/null -m 10 -w '%{http_code}' "$url")" "$url"
done < <(grep -rhoE 'https?://[^) >]+' docs README.md | sort -u)
```

`000` usually means the site is down, not that the URL is wrong; verify in a browser before deleting.

## Legal

- No ROMs, no patches, no ripped graphics or audio.
- Do not link to ROM download sites.
- Tool binaries are fine to link, not to vendor unless their license allows it.

## Review

A maintainer will check: does it run, is the version stated, is the caveat honest, does it fit the page. If it is a new page, add it to `README.md` and to the nav line at the top of each page if you are touching them anyway.
