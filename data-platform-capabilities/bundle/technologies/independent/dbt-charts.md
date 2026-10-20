---
type: Technology
id: dbt-charts
title: dbt Charts
description: Dashboard product in which each dashboard is a YAML file of queries, charts and layout, kept beside dbt models and validated in CI, with a hosted platform for editing, sharing and chat.
platform: platform-independent
vendor: Fivetran + dbt Labs
kind: saas
availability: unconfirmed
realises: [dashboards-reports, version-control, conversational-analytics, dashboards-as-code]
resource: https://www.getdbt.com/product/dbtcharts
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Announced at dbt Summit 2026, with a free workspace to start from. The YAML language is open source under Apache 2.0, and the collaborative platform is commercial. dbt does not publish a release stage for the product.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) (Analytics and BI) (primary): Build and share visual, interactive dashboards with filters and drill-down.
- [Version control integration](../../capabilities/development-lifecycle/version-control.md) (Development and DataOps): Keep code and configuration in Git and work with branches from inside the platform.
- [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) (Analytics and BI): Ask questions of data in natural language and get answers, charts or SQL back.
- [Dashboards as code](../../capabilities/analytics-bi/dashboards-as-code.md) (Analytics and BI): Define dashboards in version-controlled files that are reviewed and tested alongside the models they use.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** unconfirmed

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick Sight](../aws/aws-quick-sight.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI scorecards and goals](../microsoft/powerbi-scorecards.md), [Power BI reports and dashboards](../microsoft/powerbi-reports.md), [Fabric Real-Time Dashboard](../microsoft/fabric-real-time-dashboards.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Dashboards as code](../../capabilities/analytics-bi/dashboards-as-code.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Data Studio](../google-cloud/gcp-data-studio.md), [Looker](../google-cloud/gcp-looker.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowsight dashboards](../snowflake/snowflake-snowsight-dashboards.md), [Streamlit in Snowflake](../snowflake/snowflake-streamlit.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI/BI dashboards](../databricks/databricks-ai-bi-dashboards.md), [Genie One](../databricks/databricks-genie-one.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Dashboards as code](../../capabilities/analytics-bi/dashboards-as-code.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data source plugin for Grafana](../clickhouse/clickhouse-grafana-plugin.md), [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md), [ClickStack](../clickhouse/clickhouse-clickstack.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Visualization](../cloudera/cloudera-data-visualization.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud](../oracle/oracle-analytics-cloud.md), [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Analytics Cloud](../sap/sap-analytics-cloud.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Contour and Quiver](../palantir/palantir-contour-quiver.md), [Palantir Workshop](../palantir/palantir-workshop.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Visual Analytics](../sas/sas-visual-analytics.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku dashboards and Stories](../dataiku/dataiku-dashboards-stories.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Lightdash](../open-source/lightdash.md), [Apache Superset](../open-source/apache-superset.md), [Metabase](../open-source/metabase.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Dashboards as code](../../capabilities/analytics-bi/dashboards-as-code.md) |
