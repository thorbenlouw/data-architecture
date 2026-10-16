---
type: Technology
id: atscale
title: AtScale
description: Universal semantic layer platform that presents governed dimensional models to Power BI, Excel, Tableau, Looker and AI agents, and generates aggregates to speed up queries.
platform: platform-independent
vendor: AtScale
kind: software
availability: ga
realises: [semantic-layer, metric-definitions, query-acceleration, agent-tool-access, ai-context-layer]
resource: https://www.atscale.com/product/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Models are written in the open-source Semantic Modeling Language (SML). It provides XMLA connectivity for Excel and Power BI, and supports MCP for agents.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) (Analytics and BI) (primary): Define business entities, measures and relationships once so every tool calculates them the same way.
- [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md) (Analytics and BI): Define, certify and version key business metrics with owners and calculation logic.
- [Query acceleration](../../capabilities/compute/query-acceleration.md) (Query and compute): Speed up repeated or selective queries using caches, precomputed results and indexes.
- [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) (Generative AI): Give agents governed access to data and actions through tools and protocols such as MCP.
- [AI context layer](../../capabilities/metadata/ai-context-layer.md) (Metadata and discovery): Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI semantic models](../microsoft/powerbi-semantic-models.md), [Fabric IQ ontology](../microsoft/fabric-iq-ontology.md) (preview), [Azure Analysis Services](../microsoft/azure-analysis-services.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Query acceleration](../../capabilities/compute/query-acceleration.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [LookML](../google-cloud/gcp-lookml.md) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake semantic views](../snowflake/snowflake-semantic-views.md), [Snowflake Horizon Context](../snowflake/snowflake-horizon-context.md) (preview) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog metric views](../databricks/databricks-metric-views.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud](../oracle/oracle-analytics-cloud.md), [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md), [SAP Knowledge Graph](../sap/sap-knowledge-graph.md), [SAP BW/4HANA](../sap/sap-bw4hana.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Query acceleration](../../capabilities/compute/query-acceleration.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Ontology](../palantir/palantir-ontology.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Cube Core](../open-source/cube-core.md), [Lightdash](../open-source/lightdash.md) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Query acceleration](../../capabilities/compute/query-acceleration.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
