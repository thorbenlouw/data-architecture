---
type: Technology
id: clickhouse-skipping-indexes
title: ClickHouse data skipping indexes
description: Per-block minmax, set and Bloom filter indexes that let queries skip granules which cannot match a filter, after the primary index has pruned data.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [data-skipping-indexes]
resource: https://clickhouse.com/docs/optimize/skipping-indexes
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Effective only when the indexed column correlates with the sorting key. The token and n-gram Bloom filter types are deprecated in favour of the text index.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) (Query and compute) (primary): Use indexes, statistics and filters to avoid scanning data that cannot match a query.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery search indexes](../google-cloud/gcp-bigquery-search-indexes.md) | [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Search Optimization Service](../snowflake/snowflake-search-optimization-service.md) | [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks liquid clustering](../databricks/databricks-liquid-clustering.md) | [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Exadata](../oracle/oracle-exadata.md) | [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Pinot](../open-source/apache-pinot.md) | [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) |
