---
type: Technology
id: powerbi-reports
title: Power BI reports and dashboards
description: Interactive reports authored in Power BI Desktop or the web and shared in the Power BI service, with apps, subscriptions and data alerts.
platform: platform-microsoft
kind: saas
availability: ga
realises:
- dashboards-reports
- ad-hoc-analysis
- data-alerting
- augmented-analytics
- dashboards-as-code
- data-writeback
- data-consumer-portal
resource: https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

AI visuals such as key influencers and decomposition tree provide augmented analytics. Licensing is per user (Pro, PPU) or capacity (F64+ for free viewers).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) (Analytics and BI) (primary): Build and share visual, interactive dashboards with filters and drill-down.
- [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) (Analytics and BI): Explore data freely with SQL editors, pivots and visual exploration to answer one-off questions.
- [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) (Analytics and BI): Notify people when data crosses thresholds, or deliver reports to them on a schedule.
- [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md) (Analytics and BI): Use automation and machine learning to surface insights, anomalies and explanations without being asked.
- [Dashboards as code](../../capabilities/analytics-bi/dashboards-as-code.md) (Analytics and BI): Define dashboards in version-controlled files that are reviewed and tested alongside the models they use.
- [Data entry and write-back](../../capabilities/analytics-bi/data-writeback.md) (Analytics and BI): Let users enter or correct data in analytics tools and write it back to governed tables with an audit trail.
- [Data consumer portal](../../capabilities/analytics-bi/data-consumer-portal.md) (Analytics and BI): Give business users one place to find the dashboards, apps and AI agents shared with them, without engineering tools.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Power BI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick Sight](../aws/aws-quick-sight.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Data Studio](../google-cloud/gcp-data-studio.md), [Looker](../google-cloud/gcp-looker.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Data consumer portal](../../capabilities/analytics-bi/data-consumer-portal.md), [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowsight dashboards](../snowflake/snowflake-snowsight-dashboards.md), [Streamlit in Snowflake](../snowflake/snowflake-streamlit.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI/BI dashboards](../databricks/databricks-ai-bi-dashboards.md), [Genie One](../databricks/databricks-genie-one.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Dashboards as code](../../capabilities/analytics-bi/dashboards-as-code.md), [Data consumer portal](../../capabilities/analytics-bi/data-consumer-portal.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data source plugin for Grafana](../clickhouse/clickhouse-grafana-plugin.md), [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md), [ClickStack](../clickhouse/clickhouse-clickstack.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Visualization](../cloudera/cloudera-data-visualization.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud](../oracle/oracle-analytics-cloud.md), [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Analytics Cloud](../sap/sap-analytics-cloud.md) | [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Data entry and write-back](../../capabilities/analytics-bi/data-writeback.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Contour and Quiver](../palantir/palantir-contour-quiver.md), [Palantir Workshop](../palantir/palantir-workshop.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Data entry and write-back](../../capabilities/analytics-bi/data-writeback.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Metabase](../open-source/metabase.md), [Apache Superset](../open-source/apache-superset.md), [Lightdash](../open-source/lightdash.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Data entry and write-back](../../capabilities/analytics-bi/data-writeback.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Qlik Cloud Analytics](../independent/qlik-cloud-analytics.md), [dbt Charts](../independent/dbt-charts.md) (unconfirmed), [Tableau Cloud](../independent/tableau-cloud.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Dashboards as code](../../capabilities/analytics-bi/dashboards-as-code.md) |
