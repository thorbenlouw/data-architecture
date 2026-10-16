---
type: Technology
id: cube-core
title: Cube Core
description: Semantic layer that defines data models and metrics once and serves them through SQL, REST and GraphQL APIs with caching and pre-aggregations.
aliases: [Cube]
formerly: [Cube.js]
platform: platform-open-source
kind: open-source
availability: ga
realises: [semantic-layer, metric-definitions, data-apis, query-acceleration]
resource: https://cube.dev/docs
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, company-led by Cube Dev, which sells [Cube Cloud](../independent/cube-cloud.md) with additional AI and governance features. Often used to give embedded analytics and AI agents a consistent set of metrics.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) (Analytics and BI) (primary): Define business entities, measures and relationships once so every tool calculates them the same way.
- [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md) (Analytics and BI): Define, certify and version key business metrics with owners and calculation logic.
- [Data APIs](../../capabilities/serving/data-apis.md) (Serving and activation): Expose datasets through managed REST or GraphQL APIs with authentication, paging and rate limits.
- [Query acceleration](../../capabilities/compute/query-acceleration.md) (Query and compute): Speed up repeated or selective queries using caches, precomputed results and indexes.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI semantic models](../microsoft/powerbi-semantic-models.md), [Azure Analysis Services](../microsoft/azure-analysis-services.md), [Fabric IQ ontology](../microsoft/fabric-iq-ontology.md) (preview) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Query acceleration](../../capabilities/compute/query-acceleration.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [LookML](../google-cloud/gcp-lookml.md) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake semantic views](../snowflake/snowflake-semantic-views.md), [Snowflake Horizon Context](../snowflake/snowflake-horizon-context.md) (preview) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog metric views](../databricks/databricks-metric-views.md) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud](../oracle/oracle-analytics-cloud.md), [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md), [SAP BW/4HANA](../sap/sap-bw4hana.md), [SAP Knowledge Graph](../sap/sap-knowledge-graph.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Ontology](../palantir/palantir-ontology.md) | [Data APIs](../../capabilities/serving/data-apis.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [AtScale](../independent/atscale.md), [Cube Cloud](../independent/cube-cloud.md), [dbt Semantic Layer](../independent/dbt-semantic-layer.md) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Query acceleration](../../capabilities/compute/query-acceleration.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
