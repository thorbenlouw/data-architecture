---
type: Technology
id: snowflake-fail-safe
title: Snowflake Fail-safe
description: Keeps a further non-configurable 7 days of historical data for permanent tables after Time Travel ends, recoverable only by Snowflake Support after a disaster.
platform: platform-snowflake
kind: feature
availability: ga
realises: [backup-restore]
resource: https://docs.snowflake.com/en/user-guide/data-failsafe
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Not a self-service backup. Transient and temporary tables have no Fail-safe, and Iceberg tables have it only when stored in Snowflake storage.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Backup and restore](../../capabilities/platform-operations/backup-restore.md) (Platform operations) (primary): Take point-in-time backups of data and metadata and restore them when needed.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Backup](../aws/aws-backup.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Backup](../microsoft/azure-backup.md), [Azure SQL Database](../microsoft/azure-sql.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery table snapshots](../google-cloud/gcp-bigquery-table-snapshots.md), [BigQuery time travel](../google-cloud/gcp-bigquery-time-travel.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks managed disaster recovery](../databricks/databricks-managed-disaster-recovery.md) (preview), [Databricks table clone (shallow and deep clone)](../databricks/databricks-table-clone.md), [Lakebase](../databricks/databricks-lakebase.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud backups and BACKUP/RESTORE](../clickhouse/clickhouse-backups.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Replication Manager](../cloudera/cloudera-replication-manager.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database](../oracle/oracle-autonomous-ai-database.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Backup, Archive and Restore and Data Mover](../teradata/teradata-bar-data-mover.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Cloud Stacks and Fleet Manager](../dataiku/dataiku-cloud-stacks.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
