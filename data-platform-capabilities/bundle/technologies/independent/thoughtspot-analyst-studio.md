---
type: Technology
id: thoughtspot-analyst-studio
title: ThoughtSpot Analyst Studio
description: Data preparation and modelling environment with a SQL IDE, Python and R notebooks, data mash-ups and cached snapshots for repeated querying.
aliases: [Analyst Studio]
formerly: [Mode]
platform: platform-independent
vendor: ThoughtSpot
kind: feature
availability: ga
realises: [ad-hoc-analysis, notebooks, data-preparation, result-caching]
resource: https://thoughtspot.com/press-releases/thoughtspot-launches-agentic-data-prep-to-accelerate-ai-readiness-with-next-generation-analyst-studio
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Built from Mode, which ThoughtSpot acquired in 2023. The next generation was announced in February 2026. SpotCache and mash-ups are GA. The spreadsheet experience and the data prep agent are in early access during 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) (Analytics and BI) (primary): Explore data freely with SQL editors, pivots and visual exploration to answer one-off questions.
- [Notebooks](../../capabilities/development-lifecycle/notebooks.md) (Development and DataOps): Develop interactively with code, results and narrative together, with collaboration and scheduling.
- [Self-service data preparation](../../capabilities/processing/data-preparation.md) (Processing and transformation): Let analysts profile, clean and reshape data interactively without engineering help.
- [Result caching](../../capabilities/compute/result-caching.md) (Query and compute): Return results of repeated queries from a cache without recomputing them.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Unified Studio](../aws/aws-sagemaker-unified-studio.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI reports and dashboards](../microsoft/powerbi-reports.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Studio](../google-cloud/gcp-bigquery-studio.md), [BigQuery data canvas](../google-cloud/gcp-bigquery-data-canvas.md), [Google Data Studio](../google-cloud/gcp-data-studio.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowsight Workspaces](../snowflake/snowflake-workspaces.md), [Snowsight dashboards](../snowflake/snowflake-snowsight-dashboards.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL](../databricks/databricks-sql.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Result caching](../../capabilities/compute/result-caching.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Contour and Quiver](../palantir/palantir-contour-quiver.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Project Jupyter (JupyterLab, Notebook, JupyterHub)](../open-source/jupyter.md), [Apache Superset](../open-source/apache-superset.md), [Lightdash](../open-source/lightdash.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
