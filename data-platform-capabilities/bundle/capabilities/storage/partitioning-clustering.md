---
type: Capability
id: partitioning-clustering
title: Partitioning and clustering
description: Organise table data by key columns so queries can skip data they do not need.
aliases: [liquid clustering, Z-order, sort keys, clustering keys]
broader: [storage, open-table-formats]
related:
- data-skipping-indexes
- columnar-storage
- table-maintenance
- query-performance-analysis
- cost-optimisation
tags: [storage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Partitioning splits a table into separate groups of files by a column's value, usually a date, so a query for one day reads only that day's files. Clustering sorts or groups rows with similar values within and across files, so each file's statistics cover a narrow range and most files can be skipped. Techniques range from a plain sort order to Z-ordering and Hilbert curves, which interleave several columns at once. Newer table formats support hidden partitioning: the table derives partitions from a column, such as the month of `event_time`, without users filtering on a separate partition column.

Layout is the main lever on query speed and cost for large tables, because skipped data costs nothing to read. The classic mistake is partitioning on a column with many values, such as customer id, which creates millions of tiny files. Partitioning suits a few coarse, frequently filtered columns; clustering handles finer or multiple columns. Some platforms choose and adjust clustering automatically from observed queries.

# Key considerations

- Partition only on low-cardinality columns that nearly every query filters on, and aim for partitions of at least several hundred megabytes.
- Changing a large table's partitioning can mean rewriting it, unless the format supports partition evolution.
- Clustering decays as new, unsorted data arrives. Budget compute for re-clustering.
- A layout that suits one team's filters may do nothing for another's. Very different access paths may need materialised views or a second copy.

# Questions to ask

- Which columns appear in filters on the largest tables, and how selective are they?
- How much data does a typical query scan compared with what it returns?
- Do the main consumers query by time, by entity, or both?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Storage and table management](storage.md) |
| Broader | [Storage and table management](storage.md), [Open table formats](open-table-formats.md) |
| Related | [Columnar storage](columnar-storage.md), [Cost optimisation](../platform-operations/cost-optimisation.md), [Data modelling and design](../development-lifecycle/data-modelling.md), [Distributed processing](../processing/distributed-processing.md), [Indexes and data skipping](../compute/data-skipping-indexes.md), [Query acceleration](../compute/query-acceleration.md), [Query and job performance analysis](../platform-operations/query-performance-analysis.md), [Table maintenance and optimisation](table-maintenance.md) |

# Where it appears

- **Patterns:** [One big table](../../patterns/one-big-table.md)
- **Maturity tracks:** [Storage and table management](../../maturity/track-storage.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery managed storage](../../technologies/google-cloud/gcp-bigquery-managed-storage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | clustering keys and Automatic Clustering | [Snowflake clustering keys and Automatic Clustering](../../technologies/snowflake/snowflake-clustering-keys.md) |
| [Databricks](../../platforms/platform-databricks.md) | Liquid clustering | [Databricks liquid clustering](../../technologies/databricks/databricks-liquid-clustering.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | PARTITION BY and the sorting key (ORDER BY / primary key) | [MergeTree table engine family](../../technologies/clickhouse/clickhouse-mergetree.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Apache Iceberg in Cloudera](../../technologies/cloudera/cloudera-lakehouse-iceberg.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Iceberg](../../technologies/open-source/apache-iceberg.md) |
