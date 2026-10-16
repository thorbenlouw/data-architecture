---
type: Technology
id: metabase
title: Metabase
description: BI tool for asking questions with a visual query builder or SQL and sharing dashboards, aimed at non-technical users.
platform: platform-open-source
kind: open-source
availability: ga
realises: [dashboards-reports, ad-hoc-analysis, embedded-analytics, data-alerting, data-writeback]
resource: https://www.metabase.com/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The open-source edition is AGPLv3; Pro and Enterprise editions (row-level permissions, advanced embedding, SSO) are commercial. Company-led by Metabase.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) (Analytics and BI) (primary): Build and share visual, interactive dashboards with filters and drill-down.
- [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) (Analytics and BI): Explore data freely with SQL editors, pivots and visual exploration to answer one-off questions.
- [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) (Analytics and BI): Put dashboards and analytics inside other applications and portals, often for external customers.
- [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) (Analytics and BI): Notify people when data crosses thresholds, or deliver reports to them on a schedule.
- [Data entry and write-back](../../capabilities/analytics-bi/data-writeback.md) (Analytics and BI): Let users enter or correct data in analytics tools and write it back to governed tables with an audit trail.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick Sight](../aws/aws-quick-sight.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI reports and dashboards](../microsoft/powerbi-reports.md), [Power BI scorecards and goals](../microsoft/powerbi-scorecards.md), [Fabric Real-Time Dashboard](../microsoft/fabric-real-time-dashboards.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Data entry and write-back](../../capabilities/analytics-bi/data-writeback.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Looker](../google-cloud/gcp-looker.md), [Google Data Studio](../google-cloud/gcp-data-studio.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md), [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowsight dashboards](../snowflake/snowflake-snowsight-dashboards.md), [Streamlit in Snowflake](../snowflake/snowflake-streamlit.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI/BI dashboards](../databricks/databricks-ai-bi-dashboards.md), [Genie One](../databricks/databricks-genie-one.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data source plugin for Grafana](../clickhouse/clickhouse-grafana-plugin.md), [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md), [ClickStack](../clickhouse/clickhouse-clickstack.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Visualization](../cloudera/cloudera-data-visualization.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud](../oracle/oracle-analytics-cloud.md), [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Analytics Cloud](../sap/sap-analytics-cloud.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Data entry and write-back](../../capabilities/analytics-bi/data-writeback.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Workshop](../palantir/palantir-workshop.md), [Palantir Contour and Quiver](../palantir/palantir-contour-quiver.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Data entry and write-back](../../capabilities/analytics-bi/data-writeback.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md), [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Tableau Cloud](../independent/tableau-cloud.md), [Sigma Computing](../independent/sigma.md), [Domo](../independent/domo.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md), [Data entry and write-back](../../capabilities/analytics-bi/data-writeback.md) |
