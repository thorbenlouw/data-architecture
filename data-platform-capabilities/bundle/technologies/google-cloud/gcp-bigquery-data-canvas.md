---
type: Technology
id: gcp-bigquery-data-canvas
title: BigQuery data canvas
description: Visual canvas in BigQuery where users chain search, SQL, chart and insight nodes, driven by natural-language prompts to Gemini.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [ad-hoc-analysis, conversational-analytics]
resource: https://docs.cloud.google.com/bigquery/docs/data-canvas
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Aimed at analysts rather than business users. Uses Knowledge Catalog metadata to find tables; the chat assistant inside the canvas is in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) (Analytics and BI) (primary): Explore data freely with SQL editors, pivots and visual exploration to answer one-off questions.
- [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) (Analytics and BI): Ask questions of data in natural language and get answers, charts or SQL back.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Unified Studio](../aws/aws-sagemaker-unified-studio.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI reports and dashboards](../microsoft/powerbi-reports.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowsight Workspaces](../snowflake/snowflake-workspaces.md), [Snowsight dashboards](../snowflake/snowflake-snowsight-dashboards.md), [Snowflake Cortex Analyst](../snowflake/snowflake-cortex-analyst.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL](../databricks/databricks-sql.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Contour and Quiver](../palantir/palantir-contour-quiver.md), [AIP Analyst](../palantir/palantir-aip-analyst.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Project Jupyter (JupyterLab, Notebook, JupyterHub)](../open-source/jupyter.md), [Apache Superset](../open-source/apache-superset.md), [Lightdash](../open-source/lightdash.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Hex](../independent/hex.md), [ThoughtSpot Analyst Studio](../independent/thoughtspot-analyst-studio.md), [Omni Analytics](../independent/omni.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
