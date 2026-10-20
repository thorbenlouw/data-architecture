---
type: Technology
id: aws-backup
title: AWS Backup
description: Central policy-based backup for AWS services such as S3, DynamoDB, Aurora, RDS, Redshift and EFS, with cross-Region and cross-account copies.
platform: platform-aws
kind: managed-service
availability: ga
realises: [backup-restore, cross-region-failover, data-retention, immutable-backups, resilience-testing]
resource: https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Vault Lock makes backups immutable; logically air-gapped vaults and restore testing support ransomware recovery plans. Backup Audit Manager reports on compliance with backup policies.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Backup and restore](../../capabilities/platform-operations/backup-restore.md) (Platform operations) (primary): Take point-in-time backups of data and metadata and restore them when needed.
- [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) (Platform operations): Replicate data and configuration to another region and fail over when needed.
- [Retention and disposal](../../capabilities/governance/data-retention.md) (Governance and compliance): Keep data for as long as required, then delete it reliably, including from history, snapshots and backups, with legal holds when needed.
- [Immutable backups](../../capabilities/platform-operations/immutable-backups.md) (Platform operations): Keep backups that nobody can delete or change before they expire, with legal holds, to protect against ransomware.
- [Resilience and recovery testing](../../capabilities/platform-operations/resilience-testing.md) (Platform operations): Test backup, recovery and failover regularly and record the results as evidence.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Backup](../microsoft/azure-backup.md), [Azure SQL Database](../microsoft/azure-sql.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Immutable backups](../../capabilities/platform-operations/immutable-backups.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery table snapshots](../google-cloud/gcp-bigquery-table-snapshots.md), [BigQuery time travel](../google-cloud/gcp-bigquery-time-travel.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake backups](../snowflake/snowflake-backups.md), [Snowflake Fail-safe](../snowflake/snowflake-fail-safe.md), [Snowflake Time Travel](../snowflake/snowflake-time-travel.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Immutable backups](../../capabilities/platform-operations/immutable-backups.md), [Retention and disposal](../../capabilities/governance/data-retention.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks managed disaster recovery](../databricks/databricks-managed-disaster-recovery.md) (preview), [Databricks table clone (shallow and deep clone)](../databricks/databricks-table-clone.md), [Lakebase](../databricks/databricks-lakebase.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud backups and BACKUP/RESTORE](../clickhouse/clickhouse-backups.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Replication Manager](../cloudera/cloudera-replication-manager.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database](../oracle/oracle-autonomous-ai-database.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Backup, Archive and Restore and Data Mover](../teradata/teradata-bar-data-mover.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Cloud Stacks and Fleet Manager](../dataiku/dataiku-cloud-stacks.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
