---
type: Capability
id: result-caching
title: Result caching
description: Return results of repeated queries from a cache without recomputing them.
broader: [query-acceleration]
related: [dashboards-reports, semantic-layer, row-level-security, embedded-analytics, materialised-views]
tags: [compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

When a query arrives, the engine checks whether an identical query ran recently against data that has not changed since. If so, it returns the stored result without scanning data and, on some platforms, without starting any compute. Caches exist at other levels too: copies of data files on compute nodes' local disks or memory, and caches in BI tools and semantic layers that hold dashboard results. A dashboard opened by 500 people each morning may run its queries once and serve everyone else from cache.

Result caching cuts cost and latency for dashboards and repeated reports with almost no effort. Its limits come from how matches work. Queries usually must match exactly, including literal values, and functions such as `CURRENT_TIMESTAMP` or any change to the underlying tables invalidate the entry, so frequently updated tables get few hits. Caching data files on compute nodes is different: it speeds up reading raw data for every query, not repeats of one query.

# Key considerations

- Check invalidation rules. Any write to a source table, even to an unrelated partition, may clear its cached results.
- Caches must respect permissions. Confirm that a cached result is returned only to users entitled to it, especially under row-level security.
- BI tool caches can serve data older than the warehouse holds. Show cache age to users, or align it with data refresh.
- Slightly different queries miss the cache. A semantic layer that generates consistent SQL raises hit rates.

# Questions to ask

- Which dashboards and reports are opened by many users with the same filters?
- How often do their underlying tables change?
- Are there separate caches in BI tools, semantic layers and the engine, and which one is authoritative?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Query and compute](compute.md) |
| Broader | [Query acceleration](query-acceleration.md) |
| Related | [Dashboards and interactive reports](../analytics-bi/dashboards-reports.md), [Embedded analytics](../analytics-bi/embedded-analytics.md), [Materialised views](materialised-views.md), [Row-level security](../security/row-level-security.md), [Semantic layer](../analytics-bi/semantic-layer.md) |

# Where it appears

- **Use cases:** [Customer-facing analytics](../../use-cases/usecase-customer-facing-analytics.md) (benefits from) · [Self-service BI](../../use-cases/usecase-self-service-bi.md) (benefits from)
- **Maturity tracks:** [Compute and workload management](../../maturity/track-compute.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Athena query result reuse | [Amazon Athena](../../technologies/aws/aws-athena.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery BI Engine](../../technologies/google-cloud/gcp-bigquery-bi-engine.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | persisted query results | [Snowflake persisted query results (result cache)](../../technologies/snowflake/snowflake-result-cache.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks SQL warehouses (serverless, pro and classic)](../../technologies/databricks/databricks-sql-warehouses.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | Query cache | [ClickHouse query cache](../../technologies/clickhouse/clickhouse-query-cache.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Warehouse](../../technologies/cloudera/cloudera-data-warehouse.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [dbt Semantic Layer](../../technologies/independent/dbt-semantic-layer.md), [ThoughtSpot Analyst Studio](../../technologies/independent/thoughtspot-analyst-studio.md) |
