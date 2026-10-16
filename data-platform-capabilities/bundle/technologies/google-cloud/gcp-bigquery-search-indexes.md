---
type: Technology
id: gcp-bigquery-search-indexes
title: BigQuery search indexes
description: Indexes text and JSON columns so the SEARCH function and equality or LIKE filters can find matching rows without full scans.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [data-skipping-indexes, full-text-search]
resource: https://docs.cloud.google.com/bigquery/docs/search-intro
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Designed for point lookups in logs and semi-structured data, not fuzzy search. Index builds are free below a per-organisation size limit; above it they need a reservation. Column-granularity indexes went GA in April 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) (Query and compute) (primary): Use indexes, statistics and filters to avoid scanning data that cannot match a query.
- [Full-text search](../../capabilities/specialised-data/full-text-search.md) (Specialised data types): Index text for full-text search, relevance ranking and fast filtering.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Search Optimization Service](../snowflake/snowflake-search-optimization-service.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks liquid clustering](../databricks/databricks-liquid-clustering.md) | [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse text indexes (full-text search)](../clickhouse/clickhouse-text-indexes.md), [ClickHouse data skipping indexes](../clickhouse/clickhouse-skipping-indexes.md), [ClickHouse projections](../clickhouse/clickhouse-projections.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Exadata](../oracle/oracle-exadata.md) | [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Pinot](../open-source/apache-pinot.md) | [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) |
