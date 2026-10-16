---
type: Technology
id: azure-analysis-services
title: Azure Analysis Services
description: A managed tabular model server for enterprise semantic models consumed by Power BI, Excel and other tools.
aliases: [AAS]
platform: platform-microsoft
kind: managed-service
availability: ga
realises: [semantic-layer]
resource: https://learn.microsoft.com/en-us/analysis-services/azure-analysis-services/analysis-services-overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Still met in older estates; Microsoft recommends moving models to Power BI semantic models on Fabric capacity, which have the same engine and more features.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) (Analytics and BI) (primary): Define business entities, measures and relationships once so every tool calculates them the same way.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [LookML](../google-cloud/gcp-lookml.md) | [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Horizon Context](../snowflake/snowflake-horizon-context.md) (preview), [Snowflake semantic views](../snowflake/snowflake-semantic-views.md) | [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog metric views](../databricks/databricks-metric-views.md) | [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud](../oracle/oracle-analytics-cloud.md), [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP BW/4HANA](../sap/sap-bw4hana.md), [SAP Knowledge Graph](../sap/sap-knowledge-graph.md), [Dremio Cloud](../sap/dremio-cloud.md) | [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Ontology](../palantir/palantir-ontology.md) | [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Cube Core](../open-source/cube-core.md), [Lightdash](../open-source/lightdash.md) | [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [AtScale](../independent/atscale.md), [dbt Semantic Layer](../independent/dbt-semantic-layer.md), [Cube Cloud](../independent/cube-cloud.md) | [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
