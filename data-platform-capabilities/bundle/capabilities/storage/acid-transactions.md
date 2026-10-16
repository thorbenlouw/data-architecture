---
type: Capability
id: acid-transactions
title: ACID transactions
description: Commit concurrent writes atomically so readers never see partial or conflicting results.
broader: [open-table-formats]
related: [row-level-updates, idempotent-loading, time-travel, table-catalogue, change-data-capture]
tags: [storage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ACID stands for atomicity, consistency, isolation and durability. In a table format, a writer first writes new data files, then commits by switching the table's pointer from the old snapshot to a new one in a single atomic step, usually a conditional update in the catalogue or a put-if-absent write to storage. If another writer committed first, the commit fails; the writer checks whether the two changes conflict and retries if they do not. Readers only ever see complete snapshots, so a job that fails halfway leaves nothing visible behind.

Without transactions, readers can see half a load, two jobs can overwrite each other's files, and failed jobs leave stray rows that need cleaning up by hand. Most lake formats give snapshot isolation through optimistic concurrency, which works well for appends and less well when many writers update the same partitions. Transactions usually cover one table. Changing several tables atomically needs multi-table transactions in the catalogue or engine, which fewer platforms offer.

# Key considerations

- With optimistic concurrency, conflicting writers retry. Frequent updates to the same rows or partitions can fail repeatedly, so design write patterns that do not overlap.
- Know the isolation level. Snapshot isolation allows some anomalies that serialisable isolation prevents, which matters for read-modify-write jobs.
- Atomic commits depend on the catalogue or a storage primitive. Check what still holds when several engines write through different paths.
- Single-table transactions do not keep related tables in step. Load facts and dimensions in a set order, or use multi-table transactions, so reports never mix versions.

# Questions to ask

- How many processes write to the same tables at the same time?
- Do consumers need several tables updated together as one unit?
- What happens today when a load fails halfway through?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Storage and table management](storage.md) |
| Broader | [Open table formats](open-table-formats.md) |
| Related | [Change data capture](../ingestion-integration/change-data-capture.md), [Deduplication and idempotent loading](../ingestion-integration/idempotent-loading.md), [Row-level updates and deletes](row-level-updates.md), [Table catalogue](table-catalogue.md), [Time travel](time-travel.md) |
| Needed by | [Deduplication and idempotent loading](../ingestion-integration/idempotent-loading.md), [Row-level updates and deletes](row-level-updates.md) |

# Where it appears

- **Patterns:** [Lakehouse](../../patterns/lakehouse.md) · [Write-audit-publish](../../patterns/write-audit-publish.md)
- **Maturity tracks:** [Storage and table management](../../maturity/track-storage.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon S3 Tables](../../technologies/aws/aws-s3-tables.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric Data Warehouse](../../technologies/microsoft/fabric-data-warehouse.md), [Fabric Lakehouse](../../technologies/microsoft/fabric-lakehouse.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery managed storage](../../technologies/google-cloud/gcp-bigquery-managed-storage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Apache Iceberg tables in Snowflake](../../technologies/snowflake/snowflake-iceberg-tables.md), [Snowflake micro-partitioned table storage](../../technologies/snowflake/snowflake-managed-storage.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Delta Lake on Databricks](../../technologies/databricks/databricks-delta-lake.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Iceberg](../../technologies/open-source/apache-iceberg.md), [Delta Lake](../../technologies/open-source/delta-lake.md), [DuckLake](../../technologies/open-source/ducklake.md), [Project Nessie](../../technologies/open-source/project-nessie.md) |
