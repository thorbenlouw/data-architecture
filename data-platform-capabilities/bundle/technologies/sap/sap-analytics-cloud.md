---
type: Technology
id: sap-analytics-cloud
title: SAP Analytics Cloud
description: SaaS service that combines BI stories and dashboards, enterprise planning and predictive analysis, with live connections to SAP sources and Joule for natural-language questions.
aliases: [SAC]
platform: platform-sap
kind: saas
availability: ga
realises:
- dashboards-reports
- conversational-analytics
- augmented-analytics
- embedded-analytics
- spreadsheet-integration
- enterprise-planning
- data-writeback
resource: https://www.sap.com/products/data-cloud/cloud-analytics.html
tags: [sap]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Planning (budgeting and forecasting with write-back) is a main reason customers choose it. Includes Just Ask natural-language queries, smart insights and an add-in for Microsoft Office. Available standalone or inside BDC.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) (Analytics and BI) (primary): Build and share visual, interactive dashboards with filters and drill-down.
- [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) (Analytics and BI): Ask questions of data in natural language and get answers, charts or SQL back.
- [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md) (Analytics and BI): Use automation and machine learning to surface insights, anomalies and explanations without being asked.
- [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) (Analytics and BI): Put dashboards and analytics inside other applications and portals, often for external customers.
- [Spreadsheet integration](../../capabilities/analytics-bi/spreadsheet-integration.md) (Analytics and BI): Work with governed platform data directly from spreadsheet tools.
- [Planning and forecasting](../../capabilities/analytics-bi/enterprise-planning.md) (Analytics and BI): Build budgets, forecasts and plans over governed data, with versions, allocations and approval workflows.
- [Data entry and write-back](../../capabilities/analytics-bi/data-writeback.md) (Analytics and BI): Let users enter or correct data in analytics tools and write it back to governed tables with an audit trail.

**Platform:** [SAP](../../platforms/platform-sap.md)  
**Availability:** ga  
**Product family:** SAP Business Data Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick Sight](../aws/aws-quick-sight.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI reports and dashboards](../microsoft/powerbi-reports.md), [Power BI scorecards and goals](../microsoft/powerbi-scorecards.md), [Fabric Real-Time Dashboard](../microsoft/fabric-real-time-dashboards.md) | [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Data entry and write-back](../../capabilities/analytics-bi/data-writeback.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Data Studio](../google-cloud/gcp-data-studio.md), [Looker](../google-cloud/gcp-looker.md), [Conversational Analytics in Looker](../google-cloud/gcp-looker-conversational-analytics.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md), [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowsight dashboards](../snowflake/snowflake-snowsight-dashboards.md), [Streamlit in Snowflake](../snowflake/snowflake-streamlit.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI/BI dashboards](../databricks/databricks-ai-bi-dashboards.md), [Genie One](../databricks/databricks-genie-one.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Spreadsheet integration](../../capabilities/analytics-bi/spreadsheet-integration.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data source plugin for Grafana](../clickhouse/clickhouse-grafana-plugin.md), [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md), [ClickStack](../clickhouse/clickhouse-clickstack.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Visualization](../cloudera/cloudera-data-visualization.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud](../oracle/oracle-analytics-cloud.md), [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Workshop](../palantir/palantir-workshop.md), [Palantir Contour and Quiver](../palantir/palantir-contour-quiver.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Data entry and write-back](../../capabilities/analytics-bi/data-writeback.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Visual Analytics](../sas/sas-visual-analytics.md) | [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md), [Spreadsheet integration](../../capabilities/analytics-bi/spreadsheet-integration.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku dashboards and Stories](../dataiku/dataiku-dashboards-stories.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Metabase](../open-source/metabase.md), [Apache Superset](../open-source/apache-superset.md), [Lightdash](../open-source/lightdash.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Data entry and write-back](../../capabilities/analytics-bi/data-writeback.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Qlik Cloud Analytics](../independent/qlik-cloud-analytics.md), [Tableau Cloud](../independent/tableau-cloud.md), [dbt Charts](../independent/dbt-charts.md) (unconfirmed) | [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
