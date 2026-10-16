---
type: Technology
id: clickhouse-lightweight-updates-deletes
title: ClickHouse lightweight updates and deletes
description: Changes or removes individual rows in MergeTree tables by writing small patch parts or a deleted-row mask that queries apply at once, instead of rewriting whole parts.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [row-level-updates]
resource: https://clickhouse.com/docs/sql-reference/statements/update
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Lightweight DELETE sets a hidden _row_exists mask. Lightweight UPDATE, added in 2025 and newer than DELETE, writes patch parts that later merges fold in. Both suit small, batched changes (roughly up to 10% of a table); larger changes should use ALTER TABLE ... UPDATE/DELETE mutations. Primary and partition key columns cannot be updated, and projections restrict their use.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md) (Storage and table management) (primary): Update, delete and merge individual rows in large tables efficiently.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 Tables](../aws/aws-s3-tables.md) | [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Lakehouse](../microsoft/fabric-lakehouse.md) | [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery change data capture](../google-cloud/gcp-bigquery-cdc.md), [BigQuery tables for Apache Iceberg](../google-cloud/gcp-bigquery-iceberg-managed-tables.md) | [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake micro-partitioned table storage](../snowflake/snowflake-managed-storage.md), [Apache Iceberg tables in Snowflake](../snowflake/snowflake-iceberg-tables.md) | [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Delta Lake on Databricks](../databricks/databricks-delta-lake.md) | [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Apache Iceberg in Cloudera](../cloudera/cloudera-lakehouse-iceberg.md) | [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Hudi](../open-source/apache-hudi.md), [Apache Paimon](../open-source/apache-paimon.md), [Apache Pinot](../open-source/apache-pinot.md) | [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md) |
