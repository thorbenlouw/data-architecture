---
type: Technology
id: databricks-liquid-clustering
title: Databricks liquid clustering
description: A data layout method that clusters table files by key columns you can change at any time, replacing partitioning and Z-ordering. With CLUSTER BY AUTO, Databricks chooses the keys from query history.
platform: platform-databricks
kind: feature
availability: ga
realises: [partitioning-clustering, data-skipping-indexes]
resource: https://docs.databricks.com/aws/en/delta/clustering
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA for Delta tables on Runtime 15.4 LTS and later, and Public Preview for Iceberg tables. Automatic key selection requires predictive optimisation.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Partitioning and clustering](../../capabilities/storage/partitioning-clustering.md) (Storage and table management) (primary): Organise table data by key columns so queries can skip data they do not need.
- [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) (Query and compute): Use indexes, statistics and filters to avoid scanning data that cannot match a query.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Delta Lake on Databricks

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery managed storage](../google-cloud/gcp-bigquery-managed-storage.md) | [Partitioning and clustering](../../capabilities/storage/partitioning-clustering.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake clustering keys and Automatic Clustering](../snowflake/snowflake-clustering-keys.md) | [Partitioning and clustering](../../capabilities/storage/partitioning-clustering.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [MergeTree table engine family](../clickhouse/clickhouse-mergetree.md), [ClickHouse data skipping indexes](../clickhouse/clickhouse-skipping-indexes.md) | [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md), [Partitioning and clustering](../../capabilities/storage/partitioning-clustering.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Apache Iceberg in Cloudera](../cloudera/cloudera-lakehouse-iceberg.md) | [Partitioning and clustering](../../capabilities/storage/partitioning-clustering.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Iceberg](../open-source/apache-iceberg.md) | [Partitioning and clustering](../../capabilities/storage/partitioning-clustering.md) |
