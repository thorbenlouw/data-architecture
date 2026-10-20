---
type: Technology
id: clickhouse-backups
title: ClickHouse Cloud backups and BACKUP/RESTORE
description: Scheduled Cloud backups restored to a new service, and SQL BACKUP and RESTORE statements that write full or incremental backups to disk, S3 or Azure in self-managed clusters.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [backup-restore]
resource: https://clickhouse.com/docs/cloud/manage/backups/overview
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Cloud takes a daily backup by default; Scale and Enterprise allow configurable schedules and export to the customer's own bucket, and UNDROP recovers dropped tables. Restores always create a new service. There is no built-in cross-region failover for Cloud services; that has to be designed with backups or dual ingestion.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Backup and restore](../../capabilities/platform-operations/backup-restore.md) (Platform operations) (primary): Take point-in-time backups of data and metadata and restore them when needed.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga  
**Product family:** ClickHouse Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Backup](../aws/aws-backup.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Backup](../microsoft/azure-backup.md), [Azure SQL Database](../microsoft/azure-sql.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery table snapshots](../google-cloud/gcp-bigquery-table-snapshots.md), [BigQuery time travel](../google-cloud/gcp-bigquery-time-travel.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Fail-safe](../snowflake/snowflake-fail-safe.md), [Snowflake backups](../snowflake/snowflake-backups.md), [Snowflake Time Travel](../snowflake/snowflake-time-travel.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks managed disaster recovery](../databricks/databricks-managed-disaster-recovery.md) (preview), [Databricks table clone (shallow and deep clone)](../databricks/databricks-table-clone.md), [Lakebase](../databricks/databricks-lakebase.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Replication Manager](../cloudera/cloudera-replication-manager.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database](../oracle/oracle-autonomous-ai-database.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Backup, Archive and Restore and Data Mover](../teradata/teradata-bar-data-mover.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Cloud Stacks and Fleet Manager](../dataiku/dataiku-cloud-stacks.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
