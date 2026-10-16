---
type: Capability
id: columnar-storage
title: Columnar storage
description: Store data column by column with compression and statistics so analytical queries read only what they need.
broader: [file-formats]
related:
- data-skipping-indexes
- partitioning-clustering
- native-execution-acceleration
- table-maintenance
- sql-query-engine
tags: [storage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Instead of writing each row's values together, a columnar layout stores all values of one column together, in chunks. A query that sums `amount` for one month reads only the `amount` and `order_date` columns, not the other forty. Values in one column are similar, so they compress well with encodings such as dictionary, run-length and delta. Files also keep minimum, maximum and null counts for each chunk, so readers can skip chunks that cannot match a filter. Parquet, for example, splits a file into row groups, each holding one chunk per column, with statistics in a footer.

This layout is why analytical engines can scan billions of rows quickly: they read less from storage and process values in tight, vectorised loops. The costs fall on writes and single-record access. Building chunks needs buffering, changing one row means rewriting a chunk, and fetching a whole record touches every column. Row stores remain the right choice for transactional workloads. Columnar layouts are used both in open file formats and inside managed storage.

# Key considerations

- Statistics help only when similar values sit together. Sorting or clustering on common filter columns makes min/max skipping effective.
- Very wide tables with hundreds of columns inflate metadata and writer memory. Consider moving rarely used columns to a separate table.
- Pick compression for the workload: faster codecs for interactive queries, stronger ones for cold data where storage cost dominates.
- Streaming writers produce small files that compress poorly. Plan compaction to rebuild them into well-sized files.

# Questions to ask

- Do typical queries read a few columns from many rows, or whole records?
- Which columns appear most often in filters and joins?
- How fresh must the data be, and can writes be batched into larger files?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Storage and table management](storage.md) |
| Broader | [Open file formats](file-formats.md) |
| Related | [Indexes and data skipping](../compute/data-skipping-indexes.md), [Partitioning and clustering](partitioning-clustering.md), [Semi-structured data](semi-structured-data.md), [SQL query engine](../compute/sql-query-engine.md), [Table maintenance and optimisation](table-maintenance.md), [Vectorised native execution](../compute/native-execution-acceleration.md) |

# Where it appears

- **Patterns:** [Data warehouse](../../patterns/data-warehouse.md) · [Dimensional modelling](../../patterns/dimensional-modelling.md) · [Lakehouse](../../patterns/lakehouse.md) · [One big table](../../patterns/one-big-table.md)
- **Maturity tracks:** [Storage and table management](../../maturity/track-storage.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Redshift](../../technologies/aws/aws-redshift.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric Delta table optimization and V-Order](../../technologies/microsoft/fabric-delta-optimisation-v-order.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery managed storage](../../technologies/google-cloud/gcp-bigquery-managed-storage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake micro-partitioned table storage](../../technologies/snowflake/snowflake-managed-storage.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [MergeTree table engine family](../../technologies/clickhouse/clickhouse-mergetree.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [MySQL HeatWave](../../technologies/oracle/oracle-mysql-heatwave.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Database](../../technologies/teradata/teradata-database.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM Db2](../../technologies/ibm/ibm-db2.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Arrow](../../technologies/open-source/apache-arrow.md), [Apache ORC](../../technologies/open-source/apache-orc.md), [Apache Parquet](../../technologies/open-source/apache-parquet.md), [Lance](../../technologies/open-source/lance.md), [Vortex](../../technologies/open-source/vortex.md) |
