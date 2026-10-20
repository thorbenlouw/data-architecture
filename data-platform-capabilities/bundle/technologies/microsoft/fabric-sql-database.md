---
type: Technology
id: fabric-sql-database
title: SQL database in Microsoft Fabric
description: A SaaS operational database on the Azure SQL Database engine whose tables are replicated automatically into OneLake for analytics.
platform: platform-microsoft
kind: feature
availability: ga
realises: [operational-database, database-replication]
resource: https://learn.microsoft.com/en-us/fabric/database/sql/overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Billed on Fabric capacity; intended for application back ends, metadata stores and write-back alongside analytics. Change event streaming and workspace private links are preview. A Database Hub and database agent are in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Operational database integration](../../capabilities/serving/operational-database.md) (Serving and activation) (primary): Run transactional databases as part of the platform, with data flowing to and from analytical storage without separate pipelines.
- [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) (Ingestion and integration): Replicate operational databases continuously into the analytical platform without building pipelines.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Fabric Databases

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Aurora](../aws/aws-aurora.md), [Amazon DynamoDB](../aws/aws-dynamodb.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Cloud SQL](../google-cloud/gcp-cloud-sql.md), [Firestore](../google-cloud/gcp-firestore.md), [AlloyDB for PostgreSQL](../google-cloud/gcp-alloydb.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Postgres](../snowflake/snowflake-postgres.md), [Snowflake hybrid tables (Unistore)](../snowflake/snowflake-hybrid-tables.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakebase](../databricks/databricks-lakebase.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Managed Postgres](../clickhouse/clickhouse-managed-postgres.md) (preview) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Operational Database](../cloudera/cloudera-operational-database.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../oracle/oracle-database-multicloud.md), [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md), [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Db2](../ibm/ibm-db2.md), [IBM Astra DB (DataStax)](../ibm/ibm-astra-db.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS SpeedyStore](../sas/sas-speedystore.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [PostgreSQL](../open-source/postgresql.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [MongoDB Atlas](../independent/mongodb-atlas.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
