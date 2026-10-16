---
type: Technology
id: snowflake-result-cache
title: Snowflake persisted query results (result cache)
description: Returns the stored result of an identical earlier query, for 24 hours and up to 31 days with reuse, when the underlying data has not changed, without using warehouse compute.
platform: platform-snowflake
kind: feature
availability: ga
realises: [result-caching]
resource: https://docs.snowflake.com/en/user-guide/querying-persisted-results
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The cache is account-wide in the cloud services layer. It is separate from the local disk cache on each warehouse, which is lost when the warehouse suspends.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Result caching](../../capabilities/compute/result-caching.md) (Query and compute) (primary): Return results of repeated queries from a cache without recomputing them.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Athena](../aws/aws-athena.md) | [Result caching](../../capabilities/compute/result-caching.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery BI Engine](../google-cloud/gcp-bigquery-bi-engine.md) | [Result caching](../../capabilities/compute/result-caching.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL warehouses (serverless, pro and classic)](../databricks/databricks-sql-warehouses.md) | [Result caching](../../capabilities/compute/result-caching.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse query cache](../clickhouse/clickhouse-query-cache.md) | [Result caching](../../capabilities/compute/result-caching.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md) | [Result caching](../../capabilities/compute/result-caching.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [ThoughtSpot Analyst Studio](../independent/thoughtspot-analyst-studio.md), [dbt Semantic Layer](../independent/dbt-semantic-layer.md) | [Result caching](../../capabilities/compute/result-caching.md) |
