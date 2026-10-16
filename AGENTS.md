# Instructions for AI agents

This repository holds an Open Knowledge Format (OKF v0.2) bundle of data platform capabilities in `bundle/`. Use it to answer data architects' questions and to keep it up to date.

## Reading the bundle

- Start at `bundle/index.md`, then `bundle/about/using-this-bundle.md` and `bundle/about/conventions.md`.
- Every concept is `bundle/<folder>/.../<id>.md`. The `id` in frontmatter is stable; titles and folders may change.
- Frontmatter holds the facts and the one-sided relationships. The section below the `<!-- dpc:generated ... -->` line is derived from the whole bundle (reverse links, platform tables, equivalents, use case fit); it is reliable for reading but must never be edited by hand.
- Prefer the CLI to scanning files: `python tools/dpc.py search <words> --long` (matches titles, aliases, former names, product families, and UK or US spellings), `python tools/dpc.py show <id> --json` (frontmatter, inbound links, realising technologies by platform, equivalents, use case fit), `python tools/dpc.py usecase <id> --platform <platform-id>` and `python tools/dpc.py coverage <platform-id>`.
- `dist/graph.json` (after `python tools/dpc.py export`) has every node and typed edge in one file.

## Answering questions

- Ground answers in the bundle and name the concept ids you used, so a person can check them.
- Keep capabilities (vendor-neutral) separate from technologies (products). When asked what a use case needs, answer in capabilities first, then map to technologies for the platform in question.
- Treat platform fit and coverage as counts of mappings, not as quality judgements. Say when a capability is covered only by a preview product or not mapped at all, and that "not mapped" may mean the bundle is incomplete.
- Content is `status: draft` and unreviewed unless a concept has a `verified` entry by a `human:` actor. Technology facts past `stale_after` may be out of date; check the `resource` URL before stating them as current.
- Regulatory mappings are general summaries, not legal advice.

## Changing the bundle

1. Search first, including aliases, so you do not create a duplicate. Read `bundle/about/similar-capabilities.md` before adding a capability.
2. Follow `bundle/about/conventions.md`: kebab-case ids equal to file names, one-sentence descriptions, plain UK English, third person, no hype, no description of how the content was produced.
3. Create files with `python tools/dpc.py new <type> <id> --title "..."`, write relationships on one side only, and never edit below the generated line.
4. Record provenance: set `generated: {by: <agent>/<version>, at: <UTC timestamp>}`, leave `status: draft`, and add `sources` (OKF v0.2) for facts you took from documents. Only people set `verified`.
5. Run `python tools/dpc.py build`, then `python tools/dpc.py validate --check-generated` and `python tools/test_dpc.py`. Fix every error; explain any new warning.
6. Add a dated line to `bundle/log.md` for notable changes.
