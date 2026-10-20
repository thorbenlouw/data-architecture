---
type: Technology
id: sas-visual-analytics
title: SAS Visual Analytics
description: Web application in SAS Viya for building interactive reports and dashboards, exploring data, and running automated explanations, forecasts and scenario analysis without code.
aliases: [SAS VA]
platform: platform-sas
kind: feature
availability: ga
realises:
- dashboards-reports
- ad-hoc-analysis
- augmented-analytics
- embedded-analytics
- spreadsheet-integration
resource: https://www.sas.com/en_us/software/visual-analytics.html
tags: [sas]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:10:17Z'}
---

Reports can be embedded in web applications through the SAS Visual Analytics SDK, viewed in iOS and Android apps, and opened in Excel and Outlook through SAS for Microsoft 365. [SAS Viya Copilot](sas-viya-copilot.md) builds dashboards, explores data and writes data stories from natural-language requests.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) (Analytics and BI) (primary): Build and share visual, interactive dashboards with filters and drill-down.
- [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) (Analytics and BI): Explore data freely with SQL editors, pivots and visual exploration to answer one-off questions.
- [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md) (Analytics and BI): Use automation and machine learning to surface insights, anomalies and explanations without being asked.
- [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) (Analytics and BI): Put dashboards and analytics inside other applications and portals, often for external customers.
- [Spreadsheet integration](../../capabilities/analytics-bi/spreadsheet-integration.md) (Analytics and BI): Work with governed platform data directly from spreadsheet tools.

**Platform:** [SAS](../../platforms/platform-sas.md)  
**Availability:** ga  
**Product family:** SAS Viya

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick Sight](../aws/aws-quick-sight.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI reports and dashboards](../microsoft/powerbi-reports.md), [Power BI scorecards and goals](../microsoft/powerbi-scorecards.md), [Fabric Real-Time Dashboard](../microsoft/fabric-real-time-dashboards.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Data Studio](../google-cloud/gcp-data-studio.md), [Looker](../google-cloud/gcp-looker.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowsight dashboards](../snowflake/snowflake-snowsight-dashboards.md), [Streamlit in Snowflake](../snowflake/snowflake-streamlit.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI/BI dashboards](../databricks/databricks-ai-bi-dashboards.md), [Genie One](../databricks/databricks-genie-one.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md), [Spreadsheet integration](../../capabilities/analytics-bi/spreadsheet-integration.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data source plugin for Grafana](../clickhouse/clickhouse-grafana-plugin.md), [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md), [ClickStack](../clickhouse/clickhouse-clickstack.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Visualization](../cloudera/cloudera-data-visualization.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud](../oracle/oracle-analytics-cloud.md), [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Analytics Cloud](../sap/sap-analytics-cloud.md) | [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md), [Spreadsheet integration](../../capabilities/analytics-bi/spreadsheet-integration.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Contour and Quiver](../palantir/palantir-contour-quiver.md), [Palantir Workshop](../palantir/palantir-workshop.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku dashboards and Stories](../dataiku/dataiku-dashboards-stories.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Superset](../open-source/apache-superset.md), [Metabase](../open-source/metabase.md), [Lightdash](../open-source/lightdash.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Qlik Cloud Analytics](../independent/qlik-cloud-analytics.md), [Tableau Cloud](../independent/tableau-cloud.md), [Sigma Computing](../independent/sigma.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
