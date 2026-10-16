---
type: Technology
id: oracle-analytics-cloud
title: Oracle Analytics Cloud
description: Oracle's BI service for self-service visual analysis, governed dashboards, a semantic model, pixel-perfect reports and data preparation.
aliases: [OAC]
platform: platform-oracle
kind: saas
availability: ga
realises: [dashboards-reports, semantic-layer, paginated-reports, data-preparation, augmented-analytics]
resource: https://docs.oracle.com/en/cloud/paas/analytics-cloud/acswn
tags: [oracle]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The semantic model (formerly the RPD) is shared with Oracle Analytics Server on premises; Publisher provides paginated reports. Monthly updates add AI features.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) (Analytics and BI) (primary): Build and share visual, interactive dashboards with filters and drill-down.
- [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) (Analytics and BI): Define business entities, measures and relationships once so every tool calculates them the same way.
- [Paginated reports](../../capabilities/analytics-bi/paginated-reports.md) (Analytics and BI): Produce formatted, printable reports with precise layout for operational and regulatory use.
- [Self-service data preparation](../../capabilities/processing/data-preparation.md) (Processing and transformation): Let analysts profile, clean and reshape data interactively without engineering help.
- [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md) (Analytics and BI): Use automation and machine learning to surface insights, anomalies and explanations without being asked.

**Platform:** [Oracle](../../platforms/platform-oracle.md)  
**Availability:** ga  
**Product family:** Oracle Analytics

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick Sight](../aws/aws-quick-sight.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Paginated reports](../../capabilities/analytics-bi/paginated-reports.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI reports and dashboards](../microsoft/powerbi-reports.md), [Power BI scorecards and goals](../microsoft/powerbi-scorecards.md), [Fabric Real-Time Dashboard](../microsoft/fabric-real-time-dashboards.md) | [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Looker](../google-cloud/gcp-looker.md), [Google Data Studio](../google-cloud/gcp-data-studio.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Paginated reports](../../capabilities/analytics-bi/paginated-reports.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowsight dashboards](../snowflake/snowflake-snowsight-dashboards.md), [Streamlit in Snowflake](../snowflake/snowflake-streamlit.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI/BI dashboards](../databricks/databricks-ai-bi-dashboards.md), [Genie One](../databricks/databricks-genie-one.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data source plugin for Grafana](../clickhouse/clickhouse-grafana-plugin.md), [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md), [ClickStack](../clickhouse/clickhouse-clickstack.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Visualization](../cloudera/cloudera-data-visualization.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Analytics Cloud](../sap/sap-analytics-cloud.md) | [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Contour and Quiver](../palantir/palantir-contour-quiver.md), [Palantir Workshop](../palantir/palantir-workshop.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Lightdash](../open-source/lightdash.md), [Apache Superset](../open-source/apache-superset.md), [Metabase](../open-source/metabase.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Qlik Cloud Analytics](../independent/qlik-cloud-analytics.md), [Tableau Cloud](../independent/tableau-cloud.md), [dbt Charts](../independent/dbt-charts.md) (unconfirmed) | [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Paginated reports](../../capabilities/analytics-bi/paginated-reports.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
