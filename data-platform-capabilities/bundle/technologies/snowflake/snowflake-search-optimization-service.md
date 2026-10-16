---
type: Technology
id: snowflake-search-optimization-service
title: Snowflake Search Optimization Service
description: Builds and maintains a persistent search access path on chosen tables and columns, so point lookups, substring, semi-structured, geospatial and full-text SEARCH queries skip most micro-partitions.
aliases: [search optimization]
platform: platform-snowflake
kind: feature
availability: ga
realises: [data-skipping-indexes, full-text-search]
resource: https://docs.snowflake.com/en/user-guide/search-optimization-service
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Requires Enterprise Edition. It is billed for serverless maintenance compute and extra storage, so turn it on per column and per predicate type rather than for whole tables.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) (Query and compute) (primary): Use indexes, statistics and filters to avoid scanning data that cannot match a query.
- [Full-text search](../../capabilities/specialised-data/full-text-search.md) (Specialised data types): Index text for full-text search, relevance ranking and fast filtering.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery search indexes](../google-cloud/gcp-bigquery-search-indexes.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks liquid clustering](../databricks/databricks-liquid-clustering.md) | [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse text indexes (full-text search)](../clickhouse/clickhouse-text-indexes.md), [ClickHouse data skipping indexes](../clickhouse/clickhouse-skipping-indexes.md), [ClickHouse projections](../clickhouse/clickhouse-projections.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Exadata](../oracle/oracle-exadata.md) | [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Pinot](../open-source/apache-pinot.md) | [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) |
