---
type: Reference
id: conventions
title: Conventions
description: The frontmatter fields, relationship rules, naming rules and editorial rules every concept follows.
order: 2
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

These conventions sit on top of the [OKF v0.2 specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md). OKF requires only `type`; this bundle adds a stable `id` and typed relationships so that people and agents can reason over it reliably. The validator (`python tools/dpc.py validate`) enforces most of what follows.

# Identity

- `id` is lower-case kebab-case, unique across the whole bundle, and never changes once published. The file name is always `<id>.md`.
- The id does not encode the parent. Hierarchy lives in `broader`, so a capability can move without being renamed.
- Folders are for browsing only. A capability lives in the folder of its domain, found by following the first `broader` entry upwards. A technology lives in its platform's folder.
- Non-capability ids carry a type prefix where a clash is likely: `persona-`, `usecase-`, `track-`, `platform-`, `framework-`. Technology ids start with the platform or project name.

# Common fields

| Field | Meaning |
|---|---|
| `type` | Concept type (the one field OKF requires). |
| `id`, `title` | Stable identifier and display name. Titles use the name people use; technology titles carry the vendor or brand when the bare name is generic, and must be unique and differ from every capability title. |
| `description` | One sentence in plain English. For capabilities, it says what the platform can do, without naming products. |
| `aliases` | Other current names people use, including vendor terms, abbreviations and acronyms. Search uses them. |
| `formerly` | Technologies only: earlier official names after a rename. Search uses them too. |
| `tags` | The domain (capabilities) or platform folder (technologies). |
| `status` | OKF lifecycle: `draft`, `stable` or `deprecated`. |
| `generated`, `verified` | OKF trust fields: who wrote the content and who has checked it. A `verified` entry by `human:<id>` makes a concept human-reviewed. |
| `stale_after` | OKF freshness: when time-sensitive content (technologies, platforms, frameworks) should be rechecked. |
| `resource` | Canonical URL of the product, standard or regulation. |

# Technology fields

| Field | Meaning |
|---|---|
| `platform` | The platform group it belongs to. A technology sits under the platform of the company that sells it when that company has a platform page (so Confluent is under IBM and Dremio under SAP); otherwise under independent vendors, with the owner in `vendor`. Open-source projects and open standards sit under the open-source ecosystem. |
| `kind` | `managed-service`, `feature`, `software`, `open-source`, `open-standard` or `saas`. |
| `availability` | `ga`, `preview`, `unconfirmed` (the vendor states no release stage), `deprecated` or `retired`. |
| `realises` | Capabilities it provides, primary first. Map what the product itself does, not what its components or integrations do; map the most specific capability rather than both a parent and its child. |
| `distribution_of` | Set when the entry is another vendor's platform sold through this one, such as Azure Databricks. |

Coverage and fit tables count technologies that are `ga` or `unconfirmed`, show `preview` coverage separately, and ignore `deprecated` and `retired` technologies and redistributions.

# Relationships

Relationships are written on **one side only**. The build tool works out the reverse direction and writes it into each file's generated section.

| Type | Field | Points to | Meaning |
|---|---|---|---|
| Capability | `broader` | Capability | Parent(s). The first is the main parent; others make it appear in more than one place. Top-level domains have none. |
| Capability | `related` | Capability | Closely associated, not a parent or child. Treated as symmetric. |
| Capability | `depends_on` | Capability | Needs the other capability to work. |
| Technology | `realises` | Capability | The technology provides this capability. |
| Technology | `platform`, `distribution_of` | Platform | See above. |
| Pattern | `uses` | Capability | Capabilities the pattern relies on. |
| Pattern | `related` | Pattern | Related patterns. |
| Persona | `cares_about` | Capability | Capabilities the persona relies on most, most important first. |
| Persona | `patterns` | Pattern | Patterns relevant to them. |
| Use case | `requires` | Capability | List of `{capability, level, why}`: essential capabilities with the minimum maturity level (1-5) and the reason. |
| Use case | `benefits_from` | Capability | List of `{capability, why}`: helpful but not essential. |
| Use case | `personas`, `patterns` | Persona, Pattern | Who is involved and which patterns apply. |
| Maturity track | `covers` | Capability | Capabilities in scope. Every capability below the domains is covered by at least one track. |
| Maturity track | `levels[].capabilities` | Capability | Capabilities typically first relied on at that level. |
| Maturity track | `levels[].external_levels` | Framework | Map from framework id to the equivalent level in that framework, such as Microsoft's MLOps maturity model. |
| Maturity track | `related_tracks` | Maturity track | Tracks that are often assessed together. |
| Framework | `mappings[].capabilities` | Capability | Capabilities that address each area, control, principle or article. |
| Framework | `related`, `applies_to` | Framework; use case, persona or pattern | Frameworks used together, and where the framework applies. |
| Platform | `terminology` | Capability | Map from capability id to the platform's own name for it. |
| Platform | `families` | Technology | Umbrella product families (`name`, `aliases`, `technologies`) that people search for, such as Snowflake Cortex AI. |

Use cases, personas, patterns and frameworks point to specific capabilities, not to whole domains.

# Generated sections

Below the line `<!-- dpc:generated ... -->` in each file is content the tool writes: relationship tables, platform tables, equivalents, use case fit and the like. Edit above the line; run `python tools/dpc.py build` to refresh everything below it and every `index.md`. `python tools/dpc.py validate --check-generated` fails if anything is out of date.

# What counts as a capability

A capability is something the platform lets people or systems **do**, stated so that more than one product could provide it.

- Test: could two different vendors' products both realise it? If only one product could, it is a technology or feature, not a capability.
- Name it as an ability or a noun phrase for one ("Change data capture", "Column-level lineage"), not a product, a team or a project.
- Split a capability when vendors offer the parts separately or people assess them separately (table, column and document lineage). Do not split when the parts always come together.
- Prefer a facet in the text over a new child when variants differ only in degree, such as batch frequency.
- Architecture choices that combine several capabilities are patterns, not capabilities.
- Before adding one, search for it, including aliases (`python tools/dpc.py search <words>`), and read [choosing between similar capabilities](similar-capabilities.md).

# Writing style

Plain, succinct UK English. Explain an idea in plain words before using the technical term. Prefer concrete mechanisms and effects to adjectives. Avoid hype ("powerful", "seamless", "unlock") and filler. Write in the third person and never describe how the bundle was made inside a concept. Capability bodies have an explanation (two short paragraphs), *Key considerations* and *Questions to ask*.

# Reviewing and promoting content

1. Read the concept and check it against its `resource` or other sources.
2. Fix what is wrong above the generated line.
3. Add yourself to `verified`, for example `verified: {by: human:jsmith, at: 2026-11-02T10:00:00Z}`, and set `status: stable`.
4. Run `python tools/dpc.py build` and `python tools/dpc.py validate`, then commit. Add a line to `log.md` for notable changes.
