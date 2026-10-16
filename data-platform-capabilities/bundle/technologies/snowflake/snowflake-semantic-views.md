---
type: Technology
id: snowflake-semantic-views
title: Snowflake semantic views
description: Schema-level objects that define logical tables, relationships, facts, dimensions and metrics, queried with SQL and used by Cortex Analyst, agents and BI tools.
platform: platform-snowflake
kind: feature
availability: ga
realises: [semantic-layer, metric-definitions, semantic-model-interchange, ai-context-layer]
resource: https://docs.snowflake.com/en/user-guide/views-semantic/overview
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

They can be authored with Semantic View Autopilot (which can import Tableau or Power BI models), in Semantic Studio (GA September 2026), with SQL or with DCM Projects. Materialisations, OSI YAML format and Tableau TDS export are in preview. Semantic views can be shared through listings.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) (Analytics and BI) (primary): Define business entities, measures and relationships once so every tool calculates them the same way.
- [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md) (Analytics and BI): Define, certify and version key business metrics with owners and calculation logic.
- [Semantic model interchange](../../capabilities/analytics-bi/semantic-model-interchange.md) (Analytics and BI): Exchange semantic models and metric definitions between BI tools, semantic layers and AI tools in a standard format.
- [AI context layer](../../capabilities/metadata/ai-context-layer.md) (Metadata and discovery): Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI semantic models](../microsoft/powerbi-semantic-models.md), [Azure Analysis Services](../microsoft/azure-analysis-services.md), [Fabric IQ ontology](../microsoft/fabric-iq-ontology.md) (preview) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [LookML](../google-cloud/gcp-lookml.md) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog metric views](../databricks/databricks-metric-views.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud](../oracle/oracle-analytics-cloud.md), [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Knowledge Graph](../sap/sap-knowledge-graph.md), [Dremio Cloud](../sap/dremio-cloud.md), [SAP BW/4HANA](../sap/sap-bw4hana.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Ontology](../palantir/palantir-ontology.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Cube Core](../open-source/cube-core.md), [Lightdash](../open-source/lightdash.md), [Apache Ossie (incubating)](../open-source/apache-ossie.md) (preview) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md), [Semantic model interchange](../../capabilities/analytics-bi/semantic-model-interchange.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [AtScale](../independent/atscale.md), [dbt Semantic Layer](../independent/dbt-semantic-layer.md), [Cube Cloud](../independent/cube-cloud.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
