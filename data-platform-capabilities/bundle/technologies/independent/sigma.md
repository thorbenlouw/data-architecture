---
type: Technology
id: sigma
title: Sigma Computing
description: Warehouse-native BI and apps service with a spreadsheet interface that compiles to SQL, input tables that write back to the warehouse, and AI agents and apps.
aliases: [Sigma]
platform: platform-independent
vendor: Sigma Computing
kind: saas
availability: ga
realises:
- ad-hoc-analysis
- spreadsheet-integration
- data-applications
- dashboards-reports
- embedded-analytics
- data-writeback
- analytical-sandboxes
resource: https://www.sigmacomputing.com/product
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

All queries run in the customer's warehouse, so warehouse permissions apply. Writeback runs INSERT, UPDATE and DELETE against warehouse tables. It also offers pixel-perfect reports, a React embedding SDK and Python.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) (Analytics and BI) (primary): Explore data freely with SQL editors, pivots and visual exploration to answer one-off questions.
- [Spreadsheet integration](../../capabilities/analytics-bi/spreadsheet-integration.md) (Analytics and BI): Work with governed platform data directly from spreadsheet tools.
- [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) (Development and DataOps): Build and host interactive data applications next to the data, under platform security.
- [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) (Analytics and BI): Build and share visual, interactive dashboards with filters and drill-down.
- [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) (Analytics and BI): Put dashboards and analytics inside other applications and portals, often for external customers.
- [Data entry and write-back](../../capabilities/analytics-bi/data-writeback.md) (Analytics and BI): Let users enter or correct data in analytics tools and write it back to governed tables with an audit trail.
- [Analytical sandboxes](../../capabilities/analytics-bi/analytical-sandboxes.md) (Analytics and BI): Give analysts and teams governed spaces on the platform where they can upload files, create tables and try out analyses, with quotas, expiry and the platform's access controls.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Unified Studio](../aws/aws-sagemaker-unified-studio.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Analytical sandboxes](../../capabilities/analytics-bi/analytical-sandboxes.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI reports and dashboards](../microsoft/powerbi-reports.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Data entry and write-back](../../capabilities/analytics-bi/data-writeback.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery data canvas](../google-cloud/gcp-bigquery-data-canvas.md), [BigQuery Studio](../google-cloud/gcp-bigquery-studio.md), [Google Data Studio](../google-cloud/gcp-data-studio.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowsight Workspaces](../snowflake/snowflake-workspaces.md), [Snowsight dashboards](../snowflake/snowflake-snowsight-dashboards.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL](../databricks/databricks-sql.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Analytics Cloud](../sap/sap-analytics-cloud.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Data entry and write-back](../../capabilities/analytics-bi/data-writeback.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md), [Spreadsheet integration](../../capabilities/analytics-bi/spreadsheet-integration.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Contour and Quiver](../palantir/palantir-contour-quiver.md), [Palantir Workshop](../palantir/palantir-workshop.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Data application hosting](../../capabilities/development-lifecycle/data-applications.md), [Data entry and write-back](../../capabilities/analytics-bi/data-writeback.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Metabase](../open-source/metabase.md), [Apache Superset](../open-source/apache-superset.md), [Lightdash](../open-source/lightdash.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Data entry and write-back](../../capabilities/analytics-bi/data-writeback.md), [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
