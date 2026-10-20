---
type: Capability
id: incremental-processing
title: Incremental processing
description: Process only new or changed data instead of recomputing everything each run.
aliases: [incremental models, merge loads]
broader: [processing]
related: [change-data-capture, change-feeds, materialised-views, backfill-replay, idempotent-loading]
tags: [processing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Each run works out what has changed since the previous one and processes only that. Common mechanisms are high-water marks (rows with `updated_at` later than the last run), change feeds from tables, detection of changed partitions, and engines that track which inputs each result depends on and refresh only the affected parts. A daily revenue table, for example, is updated by merging today's new and corrected orders instead of rebuilding three years of history.

It cuts compute cost and run time, often by orders of magnitude, and makes frequent refreshes affordable. The difficulty is staying correct. Late data, deletes, updates to old records and changes to the logic must all be handled, or the incremental result drifts away from what a full rebuild would give. Append-only aggregates are easy; joins and window functions over changing inputs are hard. It sits between full recomputation and continuous stream processing, and is the mechanism behind declarative pipelines and many materialised views.

# Key considerations

- Keep a tested full-rebuild path and compare its output with the incremental result from time to time to catch drift.
- Deletes in sources are often missed. Use change feeds, CDC or soft-delete flags that carry them through.
- Reprocess a recent lookback period on each run so late-arriving data is picked up.
- A change to the logic usually needs a backfill. Plan it as part of the release.

# Questions to ask

- How large are the tables you rebuild on every run, and what share of them changes?
- Do sources provide reliable change timestamps, change feeds or CDC?
- How late can corrections to old data arrive?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Processing and transformation](processing.md) |
| Broader | [Processing and transformation](processing.md) |
| Related | [Backfill and reprocessing](../orchestration/backfill-replay.md), [Batch ingestion](../ingestion-integration/batch-ingestion.md), [Change data capture](../ingestion-integration/change-data-capture.md), [Change feeds](../serving/change-feeds.md), [Data-aware orchestration](../orchestration/asset-based-orchestration.md), [Deduplication and idempotent loading](../ingestion-integration/idempotent-loading.md), [Materialised views](../compute/materialised-views.md), [Read-optimised views](../serving/read-optimised-views.md), [Retrieval pipelines](../generative-ai/retrieval-pipelines.md), [Row-level updates and deletes](../storage/row-level-updates.md), [SQL transformation](sql-transformation.md) |
| Needed by | [Declarative pipelines](declarative-pipelines.md) |

# Where it appears

- **Use cases:** [Customer-facing analytics](../../use-cases/usecase-customer-facing-analytics.md) (requires, level 2) · [Operational reporting](../../use-cases/usecase-operational-reporting.md) (requires, level 3)
- **Patterns:** [Data Vault](../../patterns/data-vault.md) · [ELT](../../patterns/elt.md) · [Medallion architecture](../../patterns/medallion-architecture.md) · [Metadata-driven pipelines](../../patterns/metadata-driven-pipelines.md) · [One big table](../../patterns/one-big-table.md) · [Slowly changing dimensions](../../patterns/slowly-changing-dimensions.md)
- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md) · [Data engineer](../../personas/persona-data-engineer.md)
- **Maturity tracks:** [Transformation engineering](../../maturity/track-transformation.md) (from level 3, Defined)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 5 – Timeliness

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Redshift materialized views](../../technologies/aws/aws-redshift-materialized-views.md), [AWS Glue Data Catalog materialized views](../../technologies/aws/aws-glue-materialized-views.md), [AWS Glue ETL](../../technologies/aws/aws-glue-etl.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric Copy job](../../technologies/microsoft/fabric-copy-job.md), [Fabric Dataflow Gen2](../../technologies/microsoft/fabric-dataflow-gen2.md), [Fabric materialized lake views](../../technologies/microsoft/fabric-materialized-lake-views.md), [OneLake shortcut transformations](../../technologies/microsoft/fabric-onelake-shortcut-transformations.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery change history (APPENDS and CHANGES)](../../technologies/google-cloud/gcp-bigquery-change-history.md), [BigQuery materialized views](../../technologies/google-cloud/gcp-bigquery-materialized-views.md), [Dataform](../../technologies/google-cloud/gcp-dataform.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Dynamic Tables](../../technologies/snowflake/snowflake-dynamic-tables.md), [Snowflake streams](../../technologies/snowflake/snowflake-streams.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Auto Loader](../../technologies/databricks/databricks-auto-loader.md), [Databricks change data feed](../../technologies/databricks/databricks-change-data-feed.md), [Lakeflow pipelines](../../technologies/databricks/databricks-lakeflow-pipelines.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse incremental materialized views](../../technologies/clickhouse/clickhouse-materialized-views.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Iceberg tables in Palantir Foundry](../../technologies/palantir/palantir-iceberg-tables.md) (preview), [Palantir Pipeline Builder](../../technologies/palantir/palantir-pipeline-builder.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku Flow and visual recipes](../../technologies/dataiku/dataiku-flow-visual-recipes.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Hudi](../../technologies/open-source/apache-hudi.md), [dbt Core (v1.x)](../../technologies/open-source/dbt-core.md), [Spark Declarative Pipelines](../../technologies/open-source/apache-spark-declarative-pipelines.md), [Spark Structured Streaming](../../technologies/open-source/apache-spark-structured-streaming.md), [SQLMesh](../../technologies/open-source/sqlmesh.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [dbt v2 engine](../../technologies/independent/dbt-fusion-engine.md), [Materialize](../../technologies/independent/materialize.md) |
