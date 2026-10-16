---
type: Technology
id: dbt-semantic-layer
title: dbt Semantic Layer
description: Defines metrics and semantic models alongside dbt models, using MetricFlow, and serves them through APIs to BI tools, spreadsheets and AI assistants.
platform: platform-independent
vendor: Fivetran + dbt Labs
kind: feature
availability: ga
realises: [semantic-layer, metric-definitions, agent-tool-access, result-caching, ai-context-layer]
resource: https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Requires a Starter, Enterprise or Enterprise+ plan. Metrics reach Claude, ChatGPT and other clients through the dbt MCP server. Supports result caching, declarative caching and scheduled exports to the warehouse.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) (Analytics and BI) (primary): Define business entities, measures and relationships once so every tool calculates them the same way.
- [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md) (Analytics and BI): Define, certify and version key business metrics with owners and calculation logic.
- [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) (Generative AI): Give agents governed access to data and actions through tools and protocols such as MCP.
- [Result caching](../../capabilities/compute/result-caching.md) (Query and compute): Return results of repeated queries from a cache without recomputing them.
- [AI context layer](../../capabilities/metadata/ai-context-layer.md) (Metadata and discovery): Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI semantic models](../microsoft/powerbi-semantic-models.md), [Fabric IQ ontology](../microsoft/fabric-iq-ontology.md) (preview), [Azure Analysis Services](../microsoft/azure-analysis-services.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [LookML](../google-cloud/gcp-lookml.md) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake semantic views](../snowflake/snowflake-semantic-views.md), [Snowflake Horizon Context](../snowflake/snowflake-horizon-context.md) (preview) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog metric views](../databricks/databricks-metric-views.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud](../oracle/oracle-analytics-cloud.md), [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Knowledge Graph](../sap/sap-knowledge-graph.md), [Dremio Cloud](../sap/dremio-cloud.md), [SAP BW/4HANA](../sap/sap-bw4hana.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Ontology](../palantir/palantir-ontology.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Cube Core](../open-source/cube-core.md), [Lightdash](../open-source/lightdash.md) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
