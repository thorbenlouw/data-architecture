---
type: Reference
id: using-this-bundle
title: Using this bundle
description: What the bundle contains, how it is organised and how to answer the common questions with it.
order: 1
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

This bundle is a map of what a data platform can do. It separates **what** (capabilities, which are vendor-neutral) from **how** (technologies, which are named products and features), and connects both to the people who need them, the use cases that depend on them and the way maturity grows.

It is an [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) (OKF) bundle: a folder of Markdown files, one concept per file, each with YAML frontmatter. People can read it in any Markdown viewer; agents can parse the frontmatter and follow the links.

# What is in it

| Type | Folder | What it is |
|---|---|---|
| Capability | `capabilities/<domain>/` | Something a data platform can do, stated without naming a product. Arranged in a hierarchy from 20 top-level domains down to detailed sub-capabilities. |
| Technology | `technologies/<platform>/` | A named product, service, feature, open-source project or open standard, linked to the capabilities it realises. |
| Platform | `platforms/` | A vendor or group of technologies, with its product families and how it names capabilities. |
| Pattern | `patterns/` | An architecture or modelling approach, such as lakehouse or medallion architecture, and the capabilities it relies on. |
| Persona | `personas/` | A kind of person who uses or runs the platform, and the capabilities they care about most. |
| Use case | `use-cases/` | A business outcome, the capabilities it requires (with a minimum maturity level and a reason) and those that help. |
| Maturity track | `maturity/` | Five observable levels of maturity for one area, and the capabilities typically introduced at each level. |
| Framework | `frameworks/` | An external framework, standard or regulation, mapped area by area onto capabilities. |
| Reference | `about/`, `maturity/` | Guidance pages like this one. |

Every concept has a short `id` that never changes, a `title`, and a one-sentence `description`. Capabilities, patterns, personas and use cases also have a longer explanation in the body.

# How to answer common questions

**Which capabilities does this use case need?** Start from the closest use case in `use-cases/` and adapt its *Required capabilities* table. For a new use case, follow [mapping a use case to capabilities](mapping-a-use-case.md).

**How mature are we at X?** Open the maturity track for the area in `maturity/` and assess against its criteria, not the level names. [Running a maturity assessment](assessing-maturity.md) sets out the method and the [maturity scale](../maturity/maturity-scale.md) explains the levels.

**What is the difference between X and Y?** [Choosing between similar capabilities](similar-capabilities.md) sets out the groups that are easy to confuse. For how applications should read from and publish to the platform, see [read paths for applications](application-read-paths.md).

**What does platform Y offer for capability X?** Open the capability. Its *How platforms provide it* table lists the technologies on each platform, marks preview and deprecated ones, and gives the name each vendor uses.

**What is the equivalent of product P on another platform?** Open the technology. Its *Equivalents on other platforms* table lists the closest technologies on each platform, ranked by how many of the same capabilities they realise.

**How well does platform Y fit use case Z?** The use case's *Platform fit* table counts how many required capabilities each platform's technologies realise. Treat it as a prompt for questions, not a verdict: coverage is only as good as the mapping.

**What does persona P need?** Open the persona. It lists goals, recurring jobs, pain points, questions and the capabilities they rely on most.

**Which capabilities does regulation R touch?** Open the framework in `frameworks/`. Each area, principle or article is mapped to capabilities, and the framework lists the use cases and personas it applies to.

# Tools

With Python and PyYAML, the repository's `tools/dpc.py` answers the same questions from the command line, for example `python tools/dpc.py search lineage`, `python tools/dpc.py show column-lineage`, `python tools/dpc.py usecase usecase-fraud-detection --platform platform-databricks` and `python tools/dpc.py coverage platform-snowflake`. Add `--json` to `show` for machine-readable output. `python tools/dpc.py export` writes a graph file, CSVs, SKOS, a mind map and a single-file HTML explorer.

# How far to trust it

Everything was drafted on 16 October 2026 by an AI research and writing process and has **not yet been reviewed by people**. Each file says so: `status: draft` and no `verified` entry. Technology entries also carry `stale_after`, after which product names, availability and features should be rechecked. See [sources and method](sources-and-method.md) for how it was built and its known limits, and [conventions](conventions.md) for how to review and change it.
