---
type: Technology
id: databricks-ai-bi-dashboards
title: Databricks AI/BI dashboards
description: Built-in dashboards with AI-assisted authoring, cross-filtering and drill-through. They can be shared at account level, sent on schedules by email or Slack, and embedded in external applications.
formerly: [Lakeview dashboards]
platform: platform-databricks
kind: feature
availability: ga
realises: [dashboards-reports, embedded-analytics, data-alerting, dashboards-as-code]
resource: https://docs.databricks.com/aws/en/dashboards/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Dashboards can be deployed through Git and Declarative Automation Bundles. Dataset materialisation (Beta, October 2026) precomputes results for published dashboards. There is no paginated-report designer, so pixel-perfect reports need a partner tool.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) (Analytics and BI) (primary): Build and share visual, interactive dashboards with filters and drill-down.
- [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) (Analytics and BI): Put dashboards and analytics inside other applications and portals, often for external customers.
- [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) (Analytics and BI): Notify people when data crosses thresholds, or deliver reports to them on a schedule.
- [Dashboards as code](../../capabilities/analytics-bi/dashboards-as-code.md) (Analytics and BI): Define dashboards in version-controlled files that are reviewed and tested alongside the models they use.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Databricks AI/BI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick Sight](../aws/aws-quick-sight.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI reports and dashboards](../microsoft/powerbi-reports.md), [Power BI scorecards and goals](../microsoft/powerbi-scorecards.md), [Fabric Real-Time Dashboard](../microsoft/fabric-real-time-dashboards.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Dashboards as code](../../capabilities/analytics-bi/dashboards-as-code.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Looker](../google-cloud/gcp-looker.md), [Google Data Studio](../google-cloud/gcp-data-studio.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowsight dashboards](../snowflake/snowflake-snowsight-dashboards.md), [Streamlit in Snowflake](../snowflake/snowflake-streamlit.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data source plugin for Grafana](../clickhouse/clickhouse-grafana-plugin.md), [ClickStack](../clickhouse/clickhouse-clickstack.md), [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Visualization](../cloudera/cloudera-data-visualization.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud](../oracle/oracle-analytics-cloud.md), [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Analytics Cloud](../sap/sap-analytics-cloud.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Workshop](../palantir/palantir-workshop.md), [Palantir Contour and Quiver](../palantir/palantir-contour-quiver.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Visual Analytics](../sas/sas-visual-analytics.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku dashboards and Stories](../dataiku/dataiku-dashboards-stories.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Superset](../open-source/apache-superset.md), [Metabase](../open-source/metabase.md), [Lightdash](../open-source/lightdash.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md), [Dashboards as code](../../capabilities/analytics-bi/dashboards-as-code.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt Charts](../independent/dbt-charts.md) (unconfirmed), [Domo](../independent/domo.md), [Tableau Cloud](../independent/tableau-cloud.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Dashboards as code](../../capabilities/analytics-bi/dashboards-as-code.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
