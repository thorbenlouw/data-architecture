---
type: Capability
id: ad-hoc-analysis
title: Ad hoc analysis
description: Explore data freely with SQL editors, pivots and visual exploration to answer one-off questions.
aliases: [self-service analytics, exploration]
broader: [analytics-bi]
related: [notebooks, workload-isolation, data-catalogue, spend-controls, data-preparation]
depends_on: [sql-query-engine, sql-access]
tags: [analytics-bi]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Ad hoc analysis is exploratory work where the question is not known in advance. An analyst investigating a drop in conversions might write SQL in a browser editor, pivot the result by channel and device, chart it, then join campaign data to test a theory. Tools include SQL editors with schema browsing and autocompletion, drag-and-drop exploration over a semantic model, pivot tables and notebooks.

Many valuable questions are one-offs, and forcing them through a dashboard request queue delays decisions. The architectural concerns are cost and safety: exploratory queries are unpredictable, can scan very large tables and may run alongside critical workloads. Good support means easy discovery of trusted tables, visible query cost, saved and shareable queries, and a route for turning a useful analysis into a governed dashboard. Ad hoc analysis differs from dashboards, which answer known questions repeatedly, and from data preparation, which reshapes data for later use rather than answering a question.

# Key considerations

- Isolate exploratory work from production pipelines and dashboards, with limits on query cost or run time.
- Point analysts at certified, documented tables, or they rebuild logic from raw data and get different answers.
- Saved queries turn into shadow reporting. Provide a route to promote useful analyses into governed content.
- Exploration over a semantic model is safer for people who do not write SQL. Raw SQL gives flexibility but needs stronger data literacy.

# Questions to ask

- How many people write SQL, and how many need point-and-click exploration?
- Have exploratory queries ever slowed production workloads or caused cost spikes?
- How do analysts find out which tables to trust?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Analytics and BI](analytics-bi.md) |
| Broader | [Analytics and BI](analytics-bi.md) |
| Related | [Analytical sandboxes](analytical-sandboxes.md), [Budgets and spend controls](../platform-operations/spend-controls.md), [Conversational analytics](conversational-analytics.md), [Data catalogue](../metadata/data-catalogue.md), [Experimentation and causal measurement](experimentation.md), [Notebooks](../development-lifecycle/notebooks.md), [Query federation](../compute/query-federation.md), [Self-service data preparation](../processing/data-preparation.md), [SQL and programmatic access](../serving/sql-access.md), [SQL query engine](../compute/sql-query-engine.md), [Workload isolation](../compute/workload-isolation.md) |
| Depends on | [SQL query engine](../compute/sql-query-engine.md), [SQL and programmatic access](../serving/sql-access.md) |

# Where it appears

- **Use cases:** [Self-service BI](../../use-cases/usecase-self-service-bi.md) (requires, level 2)
- **Personas:** [Data analyst](../../personas/persona-data-analyst.md)
- **Maturity tracks:** [Analytics and BI](../../maturity/track-analytics-bi.md) (from level 1, Initial)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 6 – Adaptability · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Warehousing and Business Intelligence

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Unified Studio](../../technologies/aws/aws-sagemaker-unified-studio.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Power BI reports and dashboards](../../technologies/microsoft/powerbi-reports.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery data canvas](../../technologies/google-cloud/gcp-bigquery-data-canvas.md), [BigQuery Studio](../../technologies/google-cloud/gcp-bigquery-studio.md), [Google Data Studio](../../technologies/google-cloud/gcp-data-studio.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowsight dashboards](../../technologies/snowflake/snowflake-snowsight-dashboards.md), [Snowsight Workspaces](../../technologies/snowflake/snowflake-workspaces.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks SQL](../../technologies/databricks/databricks-sql.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../../technologies/clickhouse/clickhouse-sql-console.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | Cloudera Data Explorer (Hue) | [Cloudera Data Warehouse](../../technologies/cloudera/cloudera-data-warehouse.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Databricks](../../technologies/sap/sap-databricks.md) (distribution of Databricks) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Contour and Quiver](../../technologies/palantir/palantir-contour-quiver.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS Visual Analytics](../../technologies/sas/sas-visual-analytics.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku dashboards and Stories](../../technologies/dataiku/dataiku-dashboards-stories.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Superset](../../technologies/open-source/apache-superset.md), [Lightdash](../../technologies/open-source/lightdash.md), [Metabase](../../technologies/open-source/metabase.md), [Project Jupyter (JupyterLab, Notebook, JupyterHub)](../../technologies/open-source/jupyter.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Hex](../../technologies/independent/hex.md), [Omni Analytics](../../technologies/independent/omni.md), [Qlik Cloud Analytics](../../technologies/independent/qlik-cloud-analytics.md), [Sigma Computing](../../technologies/independent/sigma.md), [Tableau Cloud](../../technologies/independent/tableau-cloud.md), [ThoughtSpot Analyst Studio](../../technologies/independent/thoughtspot-analyst-studio.md) |
