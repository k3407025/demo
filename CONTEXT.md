# CONTEXT

Glossary for the CEO Code-Space Demo Kit. A glossary only — no implementation details, no decisions.

## Core concepts

- **Release gate** — the role the AI coding agent plays in the demos: it converts code into a release decision before production, rather than just describing the code.
- **Release decision** — the three-valued outcome the agent returns: **PASS**, **BLOCK**, or **needs evidence** (an approval that must be supplied outside the code). Not a binary yes/no.
- **CEO takeaway** — the single non-technical insight a demo must leave the audience with.
- **Talk track** — the ~2 minute spoken narration the presenter delivers for a demo.
- **Live-run frame** — the deck slide held while the agent runs live in the IDE; it carries the "what we're asking / what it's doing" beat so the audience isn't watching a spinner.

## Presentation

- **Deck-primary, IDE-as-proof** — the slide deck is the sole carrier of insight the CEO sees; the live IDE is secondary, split-screen on the right, and can be pointed at as proof but is never required to be understood.
- **Standalone demo** — each demo is a self-contained section of the deck with its

The one idea (the release gate) seen through three business lenses. Each is a standalone demo.

- **Financial lens** (demo 1, vendor update) — a vendor's code change could cause a direct monetary loss; the agent catches the regression before release.
- **Security lens** (demo 2, hardcoded secret) — a key committed in source can escape; the agent returns the incident response, not just a warning.
- **Governance lens** (demo 3, policy) — the code may collect/export personal data it shouldn't; the agent checks it against an approved policy and distinguishes a code violation from missing evidence.

## Audience

- **Non-technical CEO** — the intended audience. In this kit's framing, "zero code fluency": the audience never reads files, lines, or variables; every finding is translated to business terms.
