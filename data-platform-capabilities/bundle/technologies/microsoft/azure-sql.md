---
type: Technology
id: azure-sql
title: Azure SQL Database
description: Managed SQL Server engine in single database, elastic pool and Hyperscale forms, with Azure SQL Managed Instance for near-full SQL Server compatibility.
aliases: [Azure SQL, Azure SQL Managed Instance, Azure SQL Database Hyperscale]
platform: platform-microsoft
kind: managed-service
availability: ga
realises: [operational-database, backup-restore, cross-region-failover]
resource: https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Point-in-time restore, geo-replication and failover groups built in. Mirrors to Fabric.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Operational database integration](../../capabilities/serving/operational-database.md) (Serving and activation) (primary): Run transactional databases as part of the platform, with data flowing to and from analytical storage without separate pipelines.
- [Backup and restore](../../capabilities/platform-operations/backup-restore.md) (Platform operations): Take point-in-time backups of data and metadata and restore them when needed.
- [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) (Platform operations): Replicate data and configuration to another region and fail over when needed.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Aurora](../aws/aws-aurora.md), [Amazon DynamoDB](../aws/aws-dynamodb.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Cloud SQL](../google-cloud/gcp-cloud-sql.md), [Firestore](../google-cloud/gcp-firestore.md), [AlloyDB for PostgreSQL](../google-cloud/gcp-alloydb.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Postgres](../snowflake/snowflake-postgres.md), [Snowflake hybrid tables (Unistore)](../snowflake/snowflake-hybrid-tables.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakebase](../databricks/databricks-lakebase.md), [Databricks managed disaster recovery](../databricks/databricks-managed-disaster-recovery.md) (preview) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Operational database integration](../../capabilities/serving/operational-database.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Managed Postgres](../clickhouse/clickhouse-managed-postgres.md) (preview) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Operational Database](../cloudera/cloudera-operational-database.md), [Cloudera Replication Manager](../cloudera/cloudera-replication-manager.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../oracle/oracle-database-multicloud.md), [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md), [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Backup, Archive and Restore and Data Mover](../teradata/teradata-bar-data-mover.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Db2](../ibm/ibm-db2.md), [IBM Astra DB (DataStax)](../ibm/ibm-astra-db.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS SpeedyStore](../sas/sas-speedystore.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [PostgreSQL](../open-source/postgresql.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [MongoDB Atlas](../independent/mongodb-atlas.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
