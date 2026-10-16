---
type: Technology
id: metricflow
title: MetricFlow
description: Metric definition and SQL generation engine that compiles semantic models and metrics into correct SQL for the target warehouse.
platform: platform-open-source
kind: open-source
availability: ga
realises: [metric-definitions]
resource: https://www.getdbt.com/licenses-faq
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Licence change. MetricFlow powers the [dbt Semantic Layer](../independent/dbt-semantic-layer.md) and was relicensed from the Business Source License to Apache 2.0 in October 2025. dbt Labs, now part of Fivetran + dbt Labs, also contributes it to [Apache Ossie](../open-source/apache-ossie.md), formerly Open Semantic Interchange.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md) (Analytics and BI) (primary): Define, certify and version key business metrics with owners and calculation logic.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI semantic models](../microsoft/powerbi-semantic-models.md) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [LookML](../google-cloud/gcp-lookml.md) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake semantic views](../snowflake/snowflake-semantic-views.md) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog metric views](../databricks/databricks-metric-views.md) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Tableau Pulse](../independent/tableau-pulse.md), [AtScale](../independent/atscale.md), [dbt Semantic Layer](../independent/dbt-semantic-layer.md) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md) |
