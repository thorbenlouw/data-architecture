---
type: Capability
id: time-travel
title: Time travel
description: Query or restore a table as it was at an earlier point in time or version.
aliases: [snapshots, point-in-time query]
broader: [data-versioning]
related: [backup-restore, data-retention, table-maintenance, acid-transactions, temporal-data]
tags: [storage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Because a table format or managed store keeps each committed snapshot until it expires, a query can ask for an earlier one by timestamp or version number, typically with an `AS OF` clause (exact syntax varies by engine). The engine then reads that snapshot's file list instead of the current one. The same mechanism restores a table by committing an old snapshot as the new current state, so an accidental `DELETE` or a bad load can be undone in seconds without going to backups. Some platforms add a further recovery period, after time travel ends, from which only the provider can restore.

It is the quickest way to undo mistakes within the retention window, and it helps with debugging, auditing and reproducing training data. The retention window is the main decision: longer windows mean more stored history and longer survival of deleted data. Time travel looks back along one table's own history. Cloning and branching create new, separately changeable tables from a point in that history.

# Key considerations

- Retention is set per table or account and is often short by default. Set it from recovery needs rather than accepting the default.
- Snapshot expiry and vacuum jobs end time travel for older versions. Align maintenance settings with the window you promise users.
- Schema changes complicate queries on older versions. Check how each engine reads old snapshots after columns were renamed or dropped.
- Time travel is not a backup. Dropping the table, the account or the storage can remove the history too.

# Questions to ask

- How far back do people realistically need to look or restore: hours, days or weeks?
- Do privacy obligations require deleted records to leave history within a set time?
- Is time travel used for recovery today, and has a restore been tested?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Storage and table management](storage.md) |
| Broader | [Data versioning](data-versioning.md) |
| Related | [ACID transactions](acid-transactions.md), [Backfill and reprocessing](../orchestration/backfill-replay.md), [Backup and disaster recovery](../platform-operations/business-continuity.md), [Backup and restore](../platform-operations/backup-restore.md), [Bitemporal data](../specialised-data/temporal-data.md), [Change feeds](../serving/change-feeds.md), [Data subject requests](../governance/data-subject-requests.md), [Model lineage](../metadata/model-lineage.md), [Offline feature store](../machine-learning/offline-feature-store.md), [Platform-managed storage](managed-storage.md), [Point-in-time correct joins](../machine-learning/point-in-time-joins.md), [Retention and disposal](../governance/data-retention.md), [Table maintenance and optimisation](table-maintenance.md), [Zero-copy cloning](zero-copy-cloning.md) |

# Where it appears

- **Use cases:** [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (benefits from) · [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (benefits from)
- **Patterns:** [Lakehouse](../../patterns/lakehouse.md) · [Slowly changing dimensions](../../patterns/slowly-changing-dimensions.md)
- **Personas:** [Risk and compliance officer](../../personas/persona-risk-compliance.md)
- **Maturity tracks:** [Storage and table management](../../maturity/track-storage.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon S3 Tables](../../technologies/aws/aws-s3-tables.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Time travel in Fabric Data Warehouse](../../technologies/microsoft/fabric-warehouse-time-travel.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery time travel](../../technologies/google-cloud/gcp-bigquery-time-travel.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | Time Travel | [Snowflake Time Travel](../../technologies/snowflake/snowflake-time-travel.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Delta Lake on Databricks](../../technologies/databricks/databricks-delta-lake.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../../technologies/clickhouse/clickhouse-data-lake.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Apache Iceberg in Cloudera](../../technologies/cloudera/cloudera-lakehouse-iceberg.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Iceberg](../../technologies/open-source/apache-iceberg.md), [Delta Lake](../../technologies/open-source/delta-lake.md), [DuckLake](../../technologies/open-source/ducklake.md) |
