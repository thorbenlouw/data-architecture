---
type: Technology
id: fabric-real-time-dashboards
title: Fabric Real-Time Dashboard
description: Dashboards built on KQL queries over Eventhouse data, refreshing continuously for operational monitoring.
platform: platform-microsoft
kind: feature
availability: ga
realises: [dashboards-reports, real-time-analytics]
resource: https://learn.microsoft.com/en-us/fabric/real-time-intelligence/dashboard-real-time-create
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Live refresh became GA in June 2026; Copilot-generated visuals are preview. Distinct from Power BI reports and better for second-level freshness.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) (Analytics and BI) (primary): Build and share visual, interactive dashboards with filters and drill-down.
- [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) (Query and compute): Answer analytical queries in milliseconds over fresh, high-volume data, often for user-facing applications.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Microsoft Fabric Real-Time Intelligence

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick Sight](../aws/aws-quick-sight.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Data Studio](../google-cloud/gcp-data-studio.md), [Looker](../google-cloud/gcp-looker.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowsight dashboards](../snowflake/snowflake-snowsight-dashboards.md), [Streamlit in Snowflake](../snowflake/snowflake-streamlit.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI/BI dashboards](../databricks/databricks-ai-bi-dashboards.md), [Genie One](../databricks/databricks-genie-one.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data source plugin for Grafana](../clickhouse/clickhouse-grafana-plugin.md), [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md), [ClickStack](../clickhouse/clickhouse-clickstack.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Visualization](../cloudera/cloudera-data-visualization.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud](../oracle/oracle-analytics-cloud.md), [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Analytics Cloud](../sap/sap-analytics-cloud.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Contour and Quiver](../palantir/palantir-contour-quiver.md), [Palantir Workshop](../palantir/palantir-workshop.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Visual Analytics](../sas/sas-visual-analytics.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku dashboards and Stories](../dataiku/dataiku-dashboards-stories.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Superset](../open-source/apache-superset.md), [Lightdash](../open-source/lightdash.md), [Metabase](../open-source/metabase.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt Charts](../independent/dbt-charts.md) (unconfirmed), [Domo](../independent/domo.md), [Qlik Cloud Analytics](../independent/qlik-cloud-analytics.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
