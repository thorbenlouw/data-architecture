---
type: Technology
id: snowflake-workspaces
title: Snowsight Workspaces
description: A file-based editor in Snowsight for SQL, Python, notebooks, dbt projects, Streamlit apps and semantic views, with Git integration, sharing and AI code suggestions.
platform: platform-snowflake
kind: feature
availability: ga
realises: [ad-hoc-analysis, version-control, local-development]
resource: https://docs.snowflake.com/en/user-guide/ui-snowsight/workspaces
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Workspaces has permanently replaced Legacy Worksheets. Workspaces can be replicated (GA April 2026).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) (Analytics and BI) (primary): Explore data freely with SQL editors, pivots and visual exploration to answer one-off questions.
- [Version control integration](../../capabilities/development-lifecycle/version-control.md) (Development and DataOps): Keep code and configuration in Git and work with branches from inside the platform.
- [IDE and local development](../../capabilities/development-lifecycle/local-development.md) (Development and DataOps): Develop in your own editor and run against the platform, with debugging and local tests.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowsight

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Unified Studio](../aws/aws-sagemaker-unified-studio.md), [Amazon SageMaker Studio](../aws/aws-sagemaker-studio.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Version control integration](../../capabilities/development-lifecycle/version-control.md), [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI reports and dashboards](../microsoft/powerbi-reports.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery data canvas](../google-cloud/gcp-bigquery-data-canvas.md), [BigQuery Studio](../google-cloud/gcp-bigquery-studio.md), [Google Data Studio](../google-cloud/gcp-data-studio.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL](../databricks/databricks-sql.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Contour and Quiver](../palantir/palantir-contour-quiver.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Project Jupyter (JupyterLab, Notebook, JupyterHub)](../open-source/jupyter.md), [Apache Superset](../open-source/apache-superset.md), [Lightdash](../open-source/lightdash.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [ThoughtSpot Analyst Studio](../independent/thoughtspot-analyst-studio.md), [Sigma Computing](../independent/sigma.md), [Hex](../independent/hex.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
