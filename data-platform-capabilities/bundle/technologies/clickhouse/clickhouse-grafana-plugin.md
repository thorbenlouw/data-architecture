---
type: Technology
id: clickhouse-grafana-plugin
title: ClickHouse data source plugin for Grafana
description: Signed Grafana data source with a query builder for building dashboards and exploring logs and traces stored in ClickHouse.
platform: platform-clickhouse
kind: open-source
availability: ga
realises: [dashboards-reports, platform-observability]
resource: https://clickhouse.com/docs/integrations/grafana
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Supported by ClickHouse; version 4 migrates older configurations. ClickHouse Cloud also exposes Prometheus endpoints that Grafana can scrape for service metrics.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) (Analytics and BI) (primary): Build and share visual, interactive dashboards with filters and drill-down.
- [Platform observability](../../capabilities/platform-operations/platform-observability.md) (Platform operations): Monitor jobs, queries, services and usage across the platform with logs, metrics and traces.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick Sight](../aws/aws-quick-sight.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI scorecards and goals](../microsoft/powerbi-scorecards.md), [Fabric Real-Time Dashboard](../microsoft/fabric-real-time-dashboards.md), [Maps in Microsoft Fabric](../microsoft/fabric-maps.md) (preview) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Data Studio](../google-cloud/gcp-data-studio.md), [Looker](../google-cloud/gcp-looker.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowsight dashboards](../snowflake/snowflake-snowsight-dashboards.md), [Streamlit in Snowflake](../snowflake/snowflake-streamlit.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI/BI dashboards](../databricks/databricks-ai-bi-dashboards.md), [Genie One](../databricks/databricks-genie-one.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Visualization](../cloudera/cloudera-data-visualization.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud](../oracle/oracle-analytics-cloud.md), [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Analytics Cloud](../sap/sap-analytics-cloud.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Contour and Quiver](../palantir/palantir-contour-quiver.md), [Palantir Workshop](../palantir/palantir-workshop.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Visual Analytics](../sas/sas-visual-analytics.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku dashboards and Stories](../dataiku/dataiku-dashboards-stories.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Superset](../open-source/apache-superset.md), [Lightdash](../open-source/lightdash.md), [Metabase](../open-source/metabase.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt Charts](../independent/dbt-charts.md) (unconfirmed), [Domo](../independent/domo.md), [Qlik Cloud Analytics](../independent/qlik-cloud-analytics.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
