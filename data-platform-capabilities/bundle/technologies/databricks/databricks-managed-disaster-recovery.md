---
type: Technology
id: databricks-managed-disaster-recovery
title: Databricks managed disaster recovery
description: Replicates Unity Catalog metadata, managed table data and workspace assets to a secondary region, behind a stable URL that survives failover.
platform: platform-databricks
kind: feature
availability: preview
realises: [cross-region-failover, backup-restore]
resource: https://docs.databricks.com/aws/en/release-notes/product/2026/june
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Public Preview since June 2026 and gated by the account team. It is managed from the Resilience section of the account console, and replication status is available as a system table. Before this, DR needed custom deep clones and Terraform.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) (Platform operations) (primary): Replicate data and configuration to another region and fail over when needed.
- [Backup and restore](../../capabilities/platform-operations/backup-restore.md) (Platform operations): Take point-in-time backups of data and metadata and restore them when needed.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** preview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Backup](../aws/aws-backup.md), [Amazon Managed Streaming for Apache Kafka](../aws/aws-msk.md), [Amazon Aurora](../aws/aws-aurora.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake disaster recovery](../microsoft/fabric-onelake-disaster-recovery.md), [Azure SQL Database](../microsoft/azure-sql.md), [Azure Cosmos DB](../microsoft/azure-cosmos-db.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md), [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery managed disaster recovery](../google-cloud/gcp-bigquery-managed-disaster-recovery.md), [Google Cloud Storage](../google-cloud/gcp-cloud-storage.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake replication and failover groups](../snowflake/snowflake-replication-failover.md), [Snowflake Fail-safe](../snowflake/snowflake-fail-safe.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md), [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud backups and BACKUP/RESTORE](../clickhouse/clickhouse-backups.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Replication Manager](../cloudera/cloudera-replication-manager.md), [Cloudera Streams Messaging](../cloudera/cloudera-streams-messaging.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database](../oracle/oracle-autonomous-ai-database.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Backup, Archive and Restore and Data Mover](../teradata/teradata-bar-data-mover.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud](../ibm/confluent-cloud.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Pulsar](../open-source/apache-pulsar.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redis Cloud](../independent/redis-cloud.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
