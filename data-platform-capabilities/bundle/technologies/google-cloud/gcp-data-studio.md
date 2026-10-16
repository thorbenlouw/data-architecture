---
type: Technology
id: gcp-data-studio
title: Google Data Studio
description: Self-service reporting and dashboard tool with hundreds of connectors, free for individuals and sold as Data Studio Pro for organisations.
aliases: [Data Studio, Data Studio Pro]
formerly: [Looker Studio, Looker Studio Pro]
platform: platform-google-cloud
kind: saas
availability: ga
realises: [dashboards-reports, ad-hoc-analysis, conversational-analytics, data-consumer-portal]
resource: https://docs.cloud.google.com/data-studio/release-notes
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Called Google Data Studio until 2022 and Looker Studio from 2022 until April 2026, when it became Data Studio; its Gemini in Looker features were renamed Gemini in Data Studio. Its home page also lists BigQuery data agents and Colab data apps. Conversational analytics became generally available in July 2026. Data Studio Pro adds team workspaces, CMEK, data residency and audit logs.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) (Analytics and BI) (primary): Build and share visual, interactive dashboards with filters and drill-down.
- [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) (Analytics and BI): Explore data freely with SQL editors, pivots and visual exploration to answer one-off questions.
- [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) (Analytics and BI): Ask questions of data in natural language and get answers, charts or SQL back.
- [Data consumer portal](../../capabilities/analytics-bi/data-consumer-portal.md) (Analytics and BI): Give business users one place to find the dashboards, apps and AI agents shared with them, without engineering tools.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick Sight](../aws/aws-quick-sight.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI reports and dashboards](../microsoft/powerbi-reports.md), [Power BI scorecards and goals](../microsoft/powerbi-scorecards.md), [Fabric Real-Time Dashboard](../microsoft/fabric-real-time-dashboards.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Data consumer portal](../../capabilities/analytics-bi/data-consumer-portal.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowsight dashboards](../snowflake/snowflake-snowsight-dashboards.md), [Streamlit in Snowflake](../snowflake/snowflake-streamlit.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Genie One](../databricks/databricks-genie-one.md), [Databricks AI/BI dashboards](../databricks/databricks-ai-bi-dashboards.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Data consumer portal](../../capabilities/analytics-bi/data-consumer-portal.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md), [ClickHouse data source plugin for Grafana](../clickhouse/clickhouse-grafana-plugin.md), [ClickStack](../clickhouse/clickhouse-clickstack.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Visualization](../cloudera/cloudera-data-visualization.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud](../oracle/oracle-analytics-cloud.md), [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Analytics Cloud](../sap/sap-analytics-cloud.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Contour and Quiver](../palantir/palantir-contour-quiver.md), [Palantir Workshop](../palantir/palantir-workshop.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Superset](../open-source/apache-superset.md), [Lightdash](../open-source/lightdash.md), [Metabase](../open-source/metabase.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Qlik Cloud Analytics](../independent/qlik-cloud-analytics.md), [Tableau Cloud](../independent/tableau-cloud.md), [dbt Charts](../independent/dbt-charts.md) (unconfirmed) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
