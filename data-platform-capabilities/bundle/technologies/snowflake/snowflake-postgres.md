---
type: Technology
id: snowflake-postgres
title: Snowflake Postgres
description: Fully managed PostgreSQL instances, on versions 16 to 18, created and governed from Snowflake, running on dedicated Snowflake-managed machines with PgBouncer pooling and private networking.
platform: platform-snowflake
kind: managed-service
availability: ga
realises: [operational-database, low-latency-serving]
resource: https://docs.snowflake.com/en/user-guide/snowflake-postgres/about
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Built on the Crunchy Data acquisition (2025) and GA since 24 February 2026, on AWS and Azure only. Standard Postgres clients and ORMs work unchanged. It is a separate engine from hybrid tables.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Operational database integration](../../capabilities/serving/operational-database.md) (Serving and activation) (primary): Run transactional databases as part of the platform, with data flowing to and from analytical storage without separate pipelines.
- [Low-latency serving](../../capabilities/serving/low-latency-serving.md) (Serving and activation): Serve individual records or small result sets to applications in milliseconds.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake Postgres

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon DynamoDB](../aws/aws-dynamodb.md), [Amazon Aurora](../aws/aws-aurora.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure HorizonDB](../microsoft/azure-horizondb.md) (preview), [Cosmos DB in Microsoft Fabric](../microsoft/fabric-cosmos-db.md), [Azure Cosmos DB](../microsoft/azure-cosmos-db.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Firestore](../google-cloud/gcp-firestore.md), [Cloud SQL](../google-cloud/gcp-cloud-sql.md), [Spanner](../google-cloud/gcp-spanner.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakebase](../databricks/databricks-lakebase.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Managed Postgres](../clickhouse/clickhouse-managed-postgres.md) (preview) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Operational Database](../cloudera/cloudera-operational-database.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../oracle/oracle-database-multicloud.md), [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md), [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Astra DB (DataStax)](../ibm/ibm-astra-db.md), [IBM Db2](../ibm/ibm-db2.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS SpeedyStore](../sas/sas-speedystore.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [PostgreSQL](../open-source/postgresql.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [MongoDB Atlas](../independent/mongodb-atlas.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
