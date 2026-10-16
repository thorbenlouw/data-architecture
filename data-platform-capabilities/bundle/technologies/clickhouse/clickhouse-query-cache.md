---
type: Technology
id: clickhouse-query-cache
title: ClickHouse query cache
description: Stores the results of SELECT queries in memory, or optionally on disk, and serves repeats until a time to live expires.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [result-caching]
resource: https://clickhouse.com/docs/operations/query-cache
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Opt-in per query, session or profile via use_query_cache; the default TTL is 60 seconds and results are not invalidated when data changes, so it is not transactionally consistent. In Cloud only query-level settings can change it.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Result caching](../../capabilities/compute/result-caching.md) (Query and compute) (primary): Return results of repeated queries from a cache without recomputing them.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Athena](../aws/aws-athena.md) | [Result caching](../../capabilities/compute/result-caching.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery BI Engine](../google-cloud/gcp-bigquery-bi-engine.md) | [Result caching](../../capabilities/compute/result-caching.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake persisted query results (result cache)](../snowflake/snowflake-result-cache.md) | [Result caching](../../capabilities/compute/result-caching.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL warehouses (serverless, pro and classic)](../databricks/databricks-sql-warehouses.md) | [Result caching](../../capabilities/compute/result-caching.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md) | [Result caching](../../capabilities/compute/result-caching.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [ThoughtSpot Analyst Studio](../independent/thoughtspot-analyst-studio.md), [dbt Semantic Layer](../independent/dbt-semantic-layer.md) | [Result caching](../../capabilities/compute/result-caching.md) |
