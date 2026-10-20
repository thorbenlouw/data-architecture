---
type: Technology
id: cube-cloud
title: Cube Cloud
description: Managed semantic layer and agentic analytics platform that defines governed metrics once and serves them to BI tools, applications and AI agents through SQL and chat APIs.
platform: platform-independent
vendor: Cube Dev
kind: saas
availability: ga
realises:
- semantic-layer
- metric-definitions
- query-acceleration
- sql-access
- conversational-analytics
- ai-context-layer
resource: https://docs.cube.dev/docs/introduction
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Built on the open-source [Cube Core](../open-source/cube-core.md), and models move between the two unchanged. The SQL API is Postgres-compatible with MEASURE extensions. Pre-aggregations do the query acceleration.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) (Analytics and BI) (primary): Define business entities, measures and relationships once so every tool calculates them the same way.
- [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md) (Analytics and BI): Define, certify and version key business metrics with owners and calculation logic.
- [Query acceleration](../../capabilities/compute/query-acceleration.md) (Query and compute): Speed up repeated or selective queries using caches, precomputed results and indexes.
- [SQL and programmatic access](../../capabilities/serving/sql-access.md) (Serving and activation): Connect tools and code to the platform through standard drivers and protocols.
- [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) (Analytics and BI): Ask questions of data in natural language and get answers, charts or SQL back.
- [AI context layer](../../capabilities/metadata/ai-context-layer.md) (Metadata and discovery): Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI semantic models](../microsoft/powerbi-semantic-models.md), [Azure Analysis Services](../microsoft/azure-analysis-services.md), [Fabric IQ ontology](../microsoft/fabric-iq-ontology.md) (preview) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Query acceleration](../../capabilities/compute/query-acceleration.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [LookML](../google-cloud/gcp-lookml.md) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake semantic views](../snowflake/snowflake-semantic-views.md), [Snowflake Horizon Context](../snowflake/snowflake-horizon-context.md) (preview) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog metric views](../databricks/databricks-metric-views.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud](../oracle/oracle-analytics-cloud.md), [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md), [SAP Knowledge Graph](../sap/sap-knowledge-graph.md), [SAP BW/4HANA](../sap/sap-bw4hana.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Query acceleration](../../capabilities/compute/query-acceleration.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Ontology](../palantir/palantir-ontology.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Semantic Models](../dataiku/dataiku-semantic-models.md) (unconfirmed) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Cube Core](../open-source/cube-core.md), [Lightdash](../open-source/lightdash.md) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Query acceleration](../../capabilities/compute/query-acceleration.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
