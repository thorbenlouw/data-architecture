---
type: Technology
id: apache-ossie
title: Apache Ossie (incubating)
description: Vendor-neutral specification for exchanging semantic models, metrics, dimensions and relationships between BI, semantic layer and AI tools.
aliases: [Ossie, OSI]
formerly: [Open Semantic Interchange]
platform: platform-open-source
kind: open-standard
availability: preview
realises: [semantic-model-interchange, metric-definitions]
resource: https://ossie.apache.org/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0. Launched as Open Semantic Interchange (OSI) in September 2025 by Snowflake, Salesforce, dbt Labs and others, with specification v0.1 published in January 2026. It took the name Apache Ossie on entering the ASF Incubator. The specification is still early, so check which tools actually import and export it.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Semantic model interchange](../../capabilities/analytics-bi/semantic-model-interchange.md) (Analytics and BI) (primary): Exchange semantic models and metric definitions between BI tools, semantic layers and AI tools in a standard format.
- [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md) (Analytics and BI): Define, certify and version key business metrics with owners and calculation logic.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** preview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake semantic views](../snowflake/snowflake-semantic-views.md), [Snowflake Horizon Context](../snowflake/snowflake-horizon-context.md) (preview) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic model interchange](../../capabilities/analytics-bi/semantic-model-interchange.md) |
