---
type: Capability
id: materialised-views
title: Materialised views
description: Have the query engine store a query's result, refresh it as sources change and optionally use it to answer other queries.
aliases: [MVs, materialized views, incrementally maintained views, indexed views]
broader: [query-acceleration]
related:
- incremental-processing
- read-optimised-views
- declarative-pipelines
- streaming-sql
- sql-transformation
depends_on: [sql-query-engine]
tags: [compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

An ordinary view reruns its query on every read; a materialised view stores the result. One that sums daily sales by store over a billion-row sales table might hold a few hundred thousand rows, so dashboards read it in milliseconds. Refresh can be full, recomputing everything, or incremental, applying only the source changes since the last refresh. Some engines also rewrite queries automatically: a user querying the base table gets the answer from a matching view without knowing it exists.

Materialised views suit repeated aggregations and joins over large, slowly changing data, especially for BI. The main questions are freshness and refresh cost. Incremental refresh works well for simple aggregations and joins, but many engines fall back to full recomputation for window functions, outer joins or non-deterministic functions. They overlap with tables built by transformation pipelines; the difference is that the engine owns the refresh and can use the view to answer other queries.

# Key considerations

- Check which SQL constructs support incremental refresh. A view that quietly falls back to full refresh can cost more than the queries it replaces.
- Decide how stale results may be. Some engines combine the view with recent base data at query time; others return results only as fresh as the last refresh.
- Refresh cost recurs with every source change. Frequently updated sources can make a view dearer than querying directly.
- Materialised views are often specific to one engine. If several engines must read the result, a pipeline-built table is more portable.

# Questions to ask

- Which aggregations are queried repeatedly by many users?
- How fresh must those results be: seconds, minutes or daily?
- Who should own the logic: platform engineers through views, or analytics engineers through transformation code?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Query and compute](compute.md) |
| Broader | [Query acceleration](query-acceleration.md) |
| Related | [Approximate query processing](approximate-query-processing.md), [Declarative pipelines](../processing/declarative-pipelines.md), [Incremental processing](../processing/incremental-processing.md), [Read-optimised views](../serving/read-optimised-views.md), [Result caching](result-caching.md), [SQL transformation](../processing/sql-transformation.md), [Streaming SQL](../processing/streaming-sql.md) |
| Depends on | [SQL query engine](sql-query-engine.md) |

# Where it appears

- **Use cases:** [Customer-facing analytics](../../use-cases/usecase-customer-facing-analytics.md) (benefits from) · [Operational reporting](../../use-cases/usecase-operational-reporting.md) (benefits from)
- **Patterns:** [Separate read models](../../patterns/cqrs-read-models.md) · [Data marts](../../patterns/data-marts.md) · [One big table](../../patterns/one-big-table.md)
- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md)
- **Maturity tracks:** [Compute and workload management](../../maturity/track-compute.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Redshift materialized views](../../technologies/aws/aws-redshift-materialized-views.md), [AWS Glue Data Catalog materialized views](../../technologies/aws/aws-glue-materialized-views.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Materialized lake views (lakehouse); materialized views (Warehouse) | [Fabric materialized lake views](../../technologies/microsoft/fabric-materialized-lake-views.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery materialized views](../../technologies/google-cloud/gcp-bigquery-materialized-views.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | materialized views | [Snowflake materialized views](../../technologies/snowflake/snowflake-materialized-views.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Lakeflow pipelines](../../technologies/databricks/databricks-lakeflow-pipelines.md), [Unity Catalog metric views](../../technologies/databricks/databricks-metric-views.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | Materialized views (incremental) and refreshable materialized views | [ClickHouse incremental materialized views](../../technologies/clickhouse/clickhouse-materialized-views.md), [ClickHouse projections](../../technologies/clickhouse/clickhouse-projections.md), [ClickHouse refreshable materialized views](../../technologies/clickhouse/clickhouse-refreshable-materialized-views.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Warehouse](../../technologies/cloudera/cloudera-data-warehouse.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Doris](../../technologies/open-source/apache-doris.md), [RisingWave](../../technologies/open-source/risingwave.md), [Spark Declarative Pipelines](../../technologies/open-source/apache-spark-declarative-pipelines.md), [StarRocks](../../technologies/open-source/starrocks.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Materialize](../../technologies/independent/materialize.md), [Tinybird](../../technologies/independent/tinybird.md) |
