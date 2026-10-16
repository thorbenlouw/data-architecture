---
type: Capability
id: data-skipping-indexes
title: Indexes and data skipping
description: Use indexes, statistics and filters to avoid scanning data that cannot match a query.
aliases: [search optimisation, bloom filters, zone maps]
broader: [query-acceleration]
related:
- partitioning-clustering
- columnar-storage
- full-text-search
- low-latency-serving
- query-performance-analysis
tags: [compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data skipping lets an engine decide, before reading, that a file, row group or block cannot hold matching rows. Min/max statistics are the commonest form: if a file's `order_date` values run from March to April, a query for June skips it. Bloom filters answer "is this value definitely absent?" for high-cardinality columns such as ids. Traditional indexes such as B-trees map values to row locations for fast lookups, and specialised indexes cover text, geospatial shapes and vectors. Partition pruning is the coarsest form, skipping whole partitions.

Skipping is how analytical engines answer selective queries without reading everything, and it can turn a terabyte scan into a gigabyte one. Its effect depends on layout: statistics are selective only when similar values are stored together through sorting or clustering. Indexes speed up reads but cost storage and write time, and in lake formats they must stay consistent with each commit. Single-record lookups at application latency usually need a serving store rather than an analytical index.

# Key considerations

- Measure how much data queries actually skip. Statistics on unsorted columns usually skip almost nothing.
- Use bloom filters or secondary indexes for selective lookups on columns that cannot be clustered, such as ids.
- Index upkeep adds write cost. Check whether indexes update with each commit or lag behind it.
- Statistics and indexes written by one engine may be ignored by another. Check which skipping structures each engine reads.

# Questions to ask

- Which queries filter on highly selective values, such as a customer or order id?
- How much data do typical queries scan compared with what they return?
- Are tables sorted or clustered on the columns used in filters?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Query and compute](compute.md) |
| Broader | [Query acceleration](query-acceleration.md) |
| Related | [Specialised data types](../specialised-data/specialised-data.md), [Columnar storage](../storage/columnar-storage.md), [Full-text search](../specialised-data/full-text-search.md), [Low-latency serving](../serving/low-latency-serving.md), [Partitioning and clustering](../storage/partitioning-clustering.md), [Query and job performance analysis](../platform-operations/query-performance-analysis.md) |

# Where it appears

- **Maturity tracks:** [Compute and workload management](../../maturity/track-compute.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery search indexes](../../technologies/google-cloud/gcp-bigquery-search-indexes.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | Search Optimization Service and micro-partition pruning | [Snowflake Search Optimization Service](../../technologies/snowflake/snowflake-search-optimization-service.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks liquid clustering](../../technologies/databricks/databricks-liquid-clustering.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | Primary (sparse) index and data skipping indexes | [ClickHouse data skipping indexes](../../technologies/clickhouse/clickhouse-skipping-indexes.md), [ClickHouse projections](../../technologies/clickhouse/clickhouse-projections.md), [ClickHouse text indexes (full-text search)](../../technologies/clickhouse/clickhouse-text-indexes.md), [MergeTree table engine family](../../technologies/clickhouse/clickhouse-mergetree.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Exadata](../../technologies/oracle/oracle-exadata.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Pinot](../../technologies/open-source/apache-pinot.md) |
