---
type: Technology
id: cloudera-replication-manager
title: Cloudera Replication Manager
description: Service that schedules replication of HDFS, Hive, Iceberg and HBase data and metadata between clusters and to cloud storage.
platform: platform-cloudera
kind: managed-service
availability: ga
realises: [cross-region-failover, backup-restore, bulk-data-transfer, platform-migration]
resource: https://docs.cloudera.com/
tags: [cloudera]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Used for disaster recovery and for on-premises to cloud migration. On premises the separate Data Recovery service backs up and restores Data Services workloads.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) (Platform operations) (primary): Replicate data and configuration to another region and fail over when needed.
- [Backup and restore](../../capabilities/platform-operations/backup-restore.md) (Platform operations): Take point-in-time backups of data and metadata and restore them when needed.
- [Bulk and offline transfer](../../capabilities/ingestion-integration/bulk-data-transfer.md) (Ingestion and integration): Move very large datasets into the platform over high-throughput links or physical transfer devices.
- [Platform migration](../../capabilities/platform-operations/platform-migration.md) (Platform operations): Assess, convert and move workloads, code and data from a legacy platform to a new one, with automated validation.

**Platform:** [Cloudera](../../platforms/platform-cloudera.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Backup](../aws/aws-backup.md), [Amazon Managed Streaming for Apache Kafka](../aws/aws-msk.md), [Amazon Aurora](../aws/aws-aurora.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake disaster recovery](../microsoft/fabric-onelake-disaster-recovery.md), [Azure SQL Database](../microsoft/azure-sql.md), [Azure Cosmos DB](../microsoft/azure-cosmos-db.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md), [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery managed disaster recovery](../google-cloud/gcp-bigquery-managed-disaster-recovery.md), [Google Cloud Storage](../google-cloud/gcp-cloud-storage.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake replication and failover groups](../snowflake/snowflake-replication-failover.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks managed disaster recovery](../databricks/databricks-managed-disaster-recovery.md) (preview) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database](../oracle/oracle-autonomous-ai-database.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Backup, Archive and Restore and Data Mover](../teradata/teradata-bar-data-mover.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud](../ibm/confluent-cloud.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Pulsar](../open-source/apache-pulsar.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redis Cloud](../independent/redis-cloud.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
