---
type: Capability
id: semantic-model-interchange
title: Semantic model interchange
description: Exchange semantic models and metric definitions between BI tools, semantic layers and AI tools in a standard format.
aliases: [Open Semantic Interchange, OSI, Apache Ossie]
broader: [semantic-layer, metadata-interoperability]
related: [metric-definitions, ai-context-layer, platform-migration]
tags: [analytics-bi]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A finance team might define its metrics once in a code-based semantic layer, then have two BI tools, a spreadsheet add-in and an AI agent read those definitions instead of each keeping its own copy. That needs a documented, tool-independent format for entities, dimensions, measures, metrics and joins, plus importers or query interfaces in each tool. Today the formats are mostly YAML specifications published by open-source semantic layers, alongside cross-vendor efforts to agree a common one.

It matters when an organisation runs more than one BI tool, is migrating between tools, or wants AI tools to use the same definitions as dashboards. Without it, definitions are copied by hand and drift. Standards are young and support is uneven, so translation is often partial: simple measures move cleanly, while tool-specific calculations, formatting and security rules do not. It differs from general metadata interoperability, which exchanges catalogue metadata such as descriptions and lineage rather than executable calculations.

# Key considerations

- Test round trips, not only import. A model that loses joins, filters or time logic in translation will produce different numbers.
- Choose one system as the source of truth for definitions and treat the others as readers, or definitions will fork.
- Prefer plain-text, version-controlled formats, so translation can be scripted if the chosen standard changes.
- Shared definitions do not guarantee identical results. Engines differ in null handling, time zones and rounding, so compare outputs side by side.

# Questions to ask

- How many tools need to share the same metric definitions now, and in two years?
- Is a BI tool migration planned, where portable models would reduce rework?
- Which formats do your current BI tools, semantic layer and AI tools actually read and write?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Analytics and BI](analytics-bi.md) |
| Broader | [Semantic layer](semantic-layer.md), [Metadata interoperability](../metadata/metadata-interoperability.md) |
| Related | [AI context layer](../metadata/ai-context-layer.md), [Governed metric definitions](metric-definitions.md), [Platform migration](../platform-operations/platform-migration.md) |

# Where it appears

- **Use cases:** [Conversational analytics for business users](../../use-cases/usecase-conversational-bi.md) (benefits from)
- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md)
- **Maturity tracks:** [Analytics and BI](../../maturity/track-analytics-bi.md) (from level 5, Optimising)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Horizon Context](../../technologies/snowflake/snowflake-horizon-context.md) (preview), [Snowflake semantic views](../../technologies/snowflake/snowflake-semantic-views.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Ossie (incubating)](../../technologies/open-source/apache-ossie.md) (preview) |
