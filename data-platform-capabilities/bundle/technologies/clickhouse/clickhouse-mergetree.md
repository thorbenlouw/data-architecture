---
type: Technology
id: clickhouse-mergetree
title: MergeTree table engine family
description: Core storage engines that write sorted, compressed column parts, merge them in the background, and index them with a sparse primary index, with variants that deduplicate, sum, aggregate or collapse rows during merges.
platform: platform-clickhouse
kind: feature
availability: ga
realises:
- columnar-storage
- partitioning-clustering
- table-maintenance
- row-level-updates
- data-skipping-indexes
- idempotent-loading
resource: https://clickhouse.com/docs/engines/table-engines/mergetree-family
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Variants include ReplicatedMergeTree (replication and insert deduplication), ReplacingMergeTree (keeps the latest row per sorting key, used as the target for CDC and upserts), CoalescingMergeTree, SummingMergeTree, AggregatingMergeTree, CollapsingMergeTree, VersionedCollapsingMergeTree and GraphiteMergeTree. Deduplication and aggregation happen asynchronously at merge time, so queries need FINAL or GROUP BY for exact results. The sorting key (ORDER BY) matters far more than PARTITION BY for performance.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Columnar storage](../../capabilities/storage/columnar-storage.md) (Storage and table management) (primary): Store data column by column with compression and statistics so analytical queries read only what they need.
- [Partitioning and clustering](../../capabilities/storage/partitioning-clustering.md) (Storage and table management): Organise table data by key columns so queries can skip data they do not need.
- [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) (Storage and table management): Compact small files, remove obsolete files and reorganise data so tables stay fast and cheap.
- [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md) (Storage and table management): Update, delete and merge individual rows in large tables efficiently.
- [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) (Query and compute): Use indexes, statistics and filters to avoid scanning data that cannot match a query.
- [Deduplication and idempotent loading](../../capabilities/ingestion-integration/idempotent-loading.md) (Ingestion and integration): Make loads safe to retry or replay by removing duplicates on write so nothing is counted twice.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga  
**Product family:** ClickHouse table engines

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift](../aws/aws-redshift.md) | [Columnar storage](../../capabilities/storage/columnar-storage.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Delta table optimization and V-Order](../microsoft/fabric-delta-optimisation-v-order.md) | [Columnar storage](../../capabilities/storage/columnar-storage.md), [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery managed storage](../google-cloud/gcp-bigquery-managed-storage.md) | [Columnar storage](../../capabilities/storage/columnar-storage.md), [Partitioning and clustering](../../capabilities/storage/partitioning-clustering.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake micro-partitioned table storage](../snowflake/snowflake-managed-storage.md) | [Columnar storage](../../capabilities/storage/columnar-storage.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md) | [Columnar storage](../../capabilities/storage/columnar-storage.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database](../teradata/teradata-database.md) | [Columnar storage](../../capabilities/storage/columnar-storage.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Db2](../ibm/ibm-db2.md) | [Columnar storage](../../capabilities/storage/columnar-storage.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache ORC](../open-source/apache-orc.md), [Apache Parquet](../open-source/apache-parquet.md), [Vortex](../open-source/vortex.md) | [Columnar storage](../../capabilities/storage/columnar-storage.md) |
