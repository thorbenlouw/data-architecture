---
type: Technology
id: snowflake-hybrid-tables
title: Snowflake hybrid tables (Unistore)
description: A row-oriented table type with enforced primary, unique and foreign keys, indexes and row locking, for low-latency point reads and writes in the same engine as analytical tables.
aliases: [Unistore]
platform: platform-snowflake
kind: feature
availability: ga
realises: [operational-database, low-latency-serving, operational-data-store]
resource: https://docs.snowflake.com/en/user-guide/tables-hybrid
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

AWS and Azure commercial regions only. A primary key is required, and storage is larger than for columnar tables. Transactions can span hybrid and standard tables. Snowflake Postgres is now the option for full PostgreSQL compatibility.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Operational database integration](../../capabilities/serving/operational-database.md) (Serving and activation) (primary): Run transactional databases as part of the platform, with data flowing to and from analytical storage without separate pipelines.
- [Low-latency serving](../../capabilities/serving/low-latency-serving.md) (Serving and activation): Serve individual records or small result sets to applications in milliseconds.
- [Operational data store](../../capabilities/serving/operational-data-store.md) (Serving and activation): Hold a current, integrated view of data from several operational systems for operational reporting and lookups.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Aurora](../aws/aws-aurora.md), [Amazon DynamoDB](../aws/aws-dynamodb.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure HorizonDB](../microsoft/azure-horizondb.md) (preview), [Cosmos DB in Microsoft Fabric](../microsoft/fabric-cosmos-db.md), [Azure Cosmos DB](../microsoft/azure-cosmos-db.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Firestore](../google-cloud/gcp-firestore.md), [Cloud SQL](../google-cloud/gcp-cloud-sql.md), [Spanner](../google-cloud/gcp-spanner.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakebase](../databricks/databricks-lakebase.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Managed Postgres](../clickhouse/clickhouse-managed-postgres.md) (preview) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Operational Database](../cloudera/cloudera-operational-database.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational data store](../../capabilities/serving/operational-data-store.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../oracle/oracle-database-multicloud.md), [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md), [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Astra DB (DataStax)](../ibm/ibm-astra-db.md), [IBM Db2](../ibm/ibm-db2.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS SpeedyStore](../sas/sas-speedystore.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [PostgreSQL](../open-source/postgresql.md) | [Operational data store](../../capabilities/serving/operational-data-store.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [MongoDB Atlas](../independent/mongodb-atlas.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
