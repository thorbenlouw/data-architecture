---
type: Technology
id: snowflake-clustering-keys
title: Snowflake clustering keys and Automatic Clustering
description: Lets you declare clustering columns on large tables, then reorganises micro-partitions in the background to keep them well clustered so pruning stays effective.
platform: platform-snowflake
kind: feature
availability: ga
realises: [partitioning-clustering, table-maintenance]
resource: https://docs.snowflake.com/en/user-guide/tables-clustering-keys
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Automatic Clustering is billed as serverless compute. It is worth it mainly for multi-terabyte tables that are filtered on predictable columns.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Partitioning and clustering](../../capabilities/storage/partitioning-clustering.md) (Storage and table management) (primary): Organise table data by key columns so queries can skip data they do not need.
- [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) (Storage and table management): Compact small files, remove obsolete files and reorganise data so tables stay fast and cheap.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery managed storage](../google-cloud/gcp-bigquery-managed-storage.md) | [Partitioning and clustering](../../capabilities/storage/partitioning-clustering.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks liquid clustering](../databricks/databricks-liquid-clustering.md) | [Partitioning and clustering](../../capabilities/storage/partitioning-clustering.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [MergeTree table engine family](../clickhouse/clickhouse-mergetree.md) | [Partitioning and clustering](../../capabilities/storage/partitioning-clustering.md), [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Apache Iceberg in Cloudera](../cloudera/cloudera-lakehouse-iceberg.md) | [Partitioning and clustering](../../capabilities/storage/partitioning-clustering.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Iceberg](../open-source/apache-iceberg.md) | [Partitioning and clustering](../../capabilities/storage/partitioning-clustering.md) |
