---
type: Technology
id: aws-quick-sight
title: Amazon Quick Sight
description: Serverless BI for building interactive dashboards, pixel-perfect paginated reports and embedded analytics, with natural-language questions over curated topics.
formerly: [Amazon QuickSight, Amazon Q in QuickSight]
platform: platform-aws
kind: feature
availability: ga
realises:
- dashboards-reports
- paginated-reports
- embedded-analytics
- conversational-analytics
- data-alerting
- external-identity
- ai-context-layer
resource: https://docs.aws.amazon.com/quicksight/latest/user/welcome.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

SPICE is its in-memory engine; row- and column-level security restrict datasets; threshold alerts and scheduled reports notify users; ML insights flag anomalies. Existing QuickSight APIs are unchanged by the rebrand.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) (Analytics and BI) (primary): Build and share visual, interactive dashboards with filters and drill-down.
- [Paginated reports](../../capabilities/analytics-bi/paginated-reports.md) (Analytics and BI): Produce formatted, printable reports with precise layout for operational and regulatory use.
- [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) (Analytics and BI): Put dashboards and analytics inside other applications and portals, often for external customers.
- [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) (Analytics and BI): Ask questions of data in natural language and get answers, charts or SQL back.
- [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) (Analytics and BI): Notify people when data crosses thresholds, or deliver reports to them on a schedule.
- [External user and tenant identity](../../capabilities/security/external-identity.md) (Security and access): Manage identities, tenants and permissions for customers and partners who use data products or embedded analytics.
- [AI context layer](../../capabilities/metadata/ai-context-layer.md) (Metadata and discovery): Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon Quick

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI reports and dashboards](../microsoft/powerbi-reports.md), [Power BI scorecards and goals](../microsoft/powerbi-scorecards.md), [Fabric Real-Time Dashboard](../microsoft/fabric-real-time-dashboards.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Looker](../google-cloud/gcp-looker.md), [Google Data Studio](../google-cloud/gcp-data-studio.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md), [External user and tenant identity](../../capabilities/security/external-identity.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowsight dashboards](../snowflake/snowflake-snowsight-dashboards.md), [Streamlit in Snowflake](../snowflake/snowflake-streamlit.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI/BI dashboards](../databricks/databricks-ai-bi-dashboards.md), [Genie One](../databricks/databricks-genie-one.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data source plugin for Grafana](../clickhouse/clickhouse-grafana-plugin.md), [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md), [ClickStack](../clickhouse/clickhouse-clickstack.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Visualization](../cloudera/cloudera-data-visualization.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud](../oracle/oracle-analytics-cloud.md), [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Paginated reports](../../capabilities/analytics-bi/paginated-reports.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Analytics Cloud](../sap/sap-analytics-cloud.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Workshop](../palantir/palantir-workshop.md), [Palantir Contour and Quiver](../palantir/palantir-contour-quiver.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Visual Analytics](../sas/sas-visual-analytics.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku dashboards and Stories](../dataiku/dataiku-dashboards-stories.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Superset](../open-source/apache-superset.md), [Metabase](../open-source/metabase.md), [Lightdash](../open-source/lightdash.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Qlik Cloud Analytics](../independent/qlik-cloud-analytics.md), [Tableau Cloud](../independent/tableau-cloud.md), [Omni Analytics](../independent/omni.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Paginated reports](../../capabilities/analytics-bi/paginated-reports.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
