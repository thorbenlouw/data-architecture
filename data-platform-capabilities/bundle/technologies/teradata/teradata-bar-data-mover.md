---
type: Technology
id: teradata-bar-data-mover
title: Teradata Backup, Archive and Restore and Data Mover
description: Tools for backing up Teradata systems, restoring them, and copying tables and databases between systems for disaster recovery or environment refresh.
aliases: [Teradata BAR, Teradata Data Mover, Teradata DSA, Data Stream Architecture]
platform: platform-teradata
kind: software
availability: ga
realises: [backup-restore, cross-region-failover, test-data-management]
resource: https://www.teradata.com/platform
tags: [teradata]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Managed for customers in Teradata Cloud; on premises, DSA-based BAR and Data Mover are the usual tools. The open-source MCP server includes backup tools for agents.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Backup and restore](../../capabilities/platform-operations/backup-restore.md) (Platform operations) (primary): Take point-in-time backups of data and metadata and restore them when needed.
- [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) (Platform operations): Replicate data and configuration to another region and fail over when needed.
- [Test data management](../../capabilities/development-lifecycle/test-data-management.md) (Development and DataOps): Provide realistic, safe data for development and testing through subsetting, masking or generation.

**Platform:** [Teradata](../../platforms/platform-teradata.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Backup](../aws/aws-backup.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure SQL Database](../microsoft/azure-sql.md), [Azure Backup](../microsoft/azure-backup.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery table snapshots](../google-cloud/gcp-bigquery-table-snapshots.md), [BigQuery time travel](../google-cloud/gcp-bigquery-time-travel.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Fail-safe](../snowflake/snowflake-fail-safe.md), [Snowflake backups](../snowflake/snowflake-backups.md), [Snowflake Time Travel](../snowflake/snowflake-time-travel.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks managed disaster recovery](../databricks/databricks-managed-disaster-recovery.md) (preview), [Databricks table clone (shallow and deep clone)](../databricks/databricks-table-clone.md), [Lakebase](../databricks/databricks-lakebase.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md), [Test data management](../../capabilities/development-lifecycle/test-data-management.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud backups and BACKUP/RESTORE](../clickhouse/clickhouse-backups.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Replication Manager](../cloudera/cloudera-replication-manager.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database](../oracle/oracle-autonomous-ai-database.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
