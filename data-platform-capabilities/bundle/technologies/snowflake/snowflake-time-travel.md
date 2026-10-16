---
type: Technology
id: snowflake-time-travel
title: Snowflake Time Travel
description: Queries, clones or undrops tables, schemas and databases as they were at an earlier point within a retention period of up to 90 days.
platform: platform-snowflake
kind: feature
availability: ga
realises: [time-travel, backup-restore]
resource: https://docs.snowflake.com/en/user-guide/data-time-travel
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Retention is 1 day on Standard Edition and up to 90 days on Enterprise Edition and above. Longer retention adds storage cost for changed micro-partitions.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Time travel](../../capabilities/storage/time-travel.md) (Storage and table management) (primary): Query or restore a table as it was at an earlier point in time or version.
- [Backup and restore](../../capabilities/platform-operations/backup-restore.md) (Platform operations): Take point-in-time backups of data and metadata and restore them when needed.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 Tables](../aws/aws-s3-tables.md) | [Time travel](../../capabilities/storage/time-travel.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Time travel in Fabric Data Warehouse](../microsoft/fabric-warehouse-time-travel.md) | [Time travel](../../capabilities/storage/time-travel.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery time travel](../google-cloud/gcp-bigquery-time-travel.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Time travel](../../capabilities/storage/time-travel.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Delta Lake on Databricks](../databricks/databricks-delta-lake.md) | [Time travel](../../capabilities/storage/time-travel.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../clickhouse/clickhouse-data-lake.md), [ClickHouse Cloud backups and BACKUP/RESTORE](../clickhouse/clickhouse-backups.md) | [Time travel](../../capabilities/storage/time-travel.md), [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Apache Iceberg in Cloudera](../cloudera/cloudera-lakehouse-iceberg.md) | [Time travel](../../capabilities/storage/time-travel.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Iceberg](../open-source/apache-iceberg.md), [DuckLake](../open-source/ducklake.md), [Delta Lake](../open-source/delta-lake.md) | [Time travel](../../capabilities/storage/time-travel.md) |
