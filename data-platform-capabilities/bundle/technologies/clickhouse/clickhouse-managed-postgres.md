---
type: Technology
id: clickhouse-managed-postgres
title: ClickHouse Managed Postgres
description: Managed PostgreSQL on local NVMe storage with high availability, read replicas and point-in-time recovery, wired to ClickHouse through built-in CDC and the pg_clickhouse extension.
formerly: [Postgres managed by ClickHouse]
platform: platform-clickhouse
kind: managed-service
availability: preview
realises: [operational-database, change-data-capture, query-federation]
resource: https://clickhouse.com/docs/cloud/managed-postgres
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Public beta on AWS from mid-2026 and private preview on GCP; built with Ubicloud. pg_clickhouse (Apache 2.0, usable with any Postgres 14+) pushes analytical queries down to ClickHouse from Postgres. Replication to ClickHouse is asynchronous, so Postgres stays the system of record.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Operational database integration](../../capabilities/serving/operational-database.md) (Serving and activation) (primary): Run transactional databases as part of the platform, with data flowing to and from analytical storage without separate pipelines.
- [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) (Ingestion and integration): Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.
- [Query federation](../../capabilities/compute/query-federation.md) (Query and compute): Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** preview  
**Product family:** ClickHouse Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Aurora](../aws/aws-aurora.md), [Amazon DynamoDB](../aws/aws-dynamodb.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure HorizonDB](../microsoft/azure-horizondb.md) (preview), [Azure Database for PostgreSQL](../microsoft/azure-database-for-postgresql.md), [SQL database in Microsoft Fabric](../microsoft/fabric-sql-database.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Cloud SQL](../google-cloud/gcp-cloud-sql.md), [Firestore](../google-cloud/gcp-firestore.md), [AlloyDB for PostgreSQL](../google-cloud/gcp-alloydb.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Postgres](../snowflake/snowflake-postgres.md), [Snowflake hybrid tables (Unistore)](../snowflake/snowflake-hybrid-tables.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakebase](../databricks/databricks-lakebase.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Operational Database](../cloudera/cloudera-operational-database.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md), [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../oracle/oracle-database-multicloud.md), [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Db2](../ibm/ibm-db2.md), [IBM Astra DB (DataStax)](../ibm/ibm-astra-db.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS SpeedyStore](../sas/sas-speedystore.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [PostgreSQL](../open-source/postgresql.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [MongoDB Atlas](../independent/mongodb-atlas.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
