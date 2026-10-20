---
type: Technology
id: clickhouse-sql-console
title: ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)
description: Browser workspace for writing and sharing queries, charting results, building parameterised dashboards from saved queries and asking an AI assistant to write SQL or explore data.
aliases: [ClickHouse Assistant]
platform: platform-clickhouse
kind: feature
availability: ga
realises: [ad-hoc-analysis, dashboards-reports, conversational-analytics, ai-assisted-development]
resource: https://clickhouse.com/docs/cloud/get-started/sql-console
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Dashboards became GA in June 2025. ClickHouse Assistant (AI Chat) has an Agent mode that reasons over schema and metadata and a Docs mode; AI features must be enabled per organisation. It is a working tool for engineers and analysts, not a replacement for a BI platform.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) (Analytics and BI) (primary): Explore data freely with SQL editors, pivots and visual exploration to answer one-off questions.
- [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) (Analytics and BI): Build and share visual, interactive dashboards with filters and drill-down.
- [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) (Analytics and BI): Ask questions of data in natural language and get answers, charts or SQL back.
- [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) (Development and DataOps): Use AI assistants to write, explain, fix and optimise code, SQL and pipelines.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga  
**Product family:** ClickHouse Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Unified Studio](../aws/aws-sagemaker-unified-studio.md), [Amazon SageMaker Data Agent](../aws/aws-sagemaker-data-agent.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI reports and dashboards](../microsoft/powerbi-reports.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery data canvas](../google-cloud/gcp-bigquery-data-canvas.md), [Google Data Studio](../google-cloud/gcp-data-studio.md), [BigQuery Studio](../google-cloud/gcp-bigquery-studio.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowsight dashboards](../snowflake/snowflake-snowsight-dashboards.md), [Snowsight Workspaces](../snowflake/snowflake-workspaces.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL](../databricks/databricks-sql.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE GPT](../informatica/informatica-claire-gpt.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md), [Cloudera Data Visualization](../cloudera/cloudera-data-visualization.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Contour and Quiver](../palantir/palantir-contour-quiver.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Visual Analytics](../sas/sas-visual-analytics.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku dashboards and Stories](../dataiku/dataiku-dashboards-stories.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Superset](../open-source/apache-superset.md), [Lightdash](../open-source/lightdash.md), [Metabase](../open-source/metabase.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Hex](../independent/hex.md), [Omni Analytics](../independent/omni.md), [Qlik Cloud Analytics](../independent/qlik-cloud-analytics.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
