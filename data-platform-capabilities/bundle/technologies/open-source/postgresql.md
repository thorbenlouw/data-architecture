---
type: Technology
id: postgresql
title: PostgreSQL
description: Open-source relational database used as an operational system of record and, with extensions, for analytics, vectors, geospatial and time-series data.
aliases: [Postgres]
platform: platform-open-source
kind: open-source
availability: ga
realises:
- operational-database
- operational-data-store
- semi-structured-data
- change-data-capture
- row-level-security
resource: https://www.postgresql.org/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

PostgreSQL Licence (permissive), run by the PostgreSQL Global Development Group. PostgreSQL 18 is the current major version and 19 reached release candidate in October 2026. Logical decoding is the basis for Debezium CDC, and extensions (pgvector, PostGIS, Apache AGE for graph queries, columnar engines) add specialised workloads.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Operational database integration](../../capabilities/serving/operational-database.md) (Serving and activation) (primary): Run transactional databases as part of the platform, with data flowing to and from analytical storage without separate pipelines.
- [Operational data store](../../capabilities/serving/operational-data-store.md) (Serving and activation): Hold a current, integrated view of data from several operational systems for operational reporting and lookups.
- [Semi-structured data](../../capabilities/storage/semi-structured-data.md) (Storage and table management): Store and query nested data such as JSON without flattening it first.
- [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) (Ingestion and integration): Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.
- [Row-level security](../../capabilities/security/row-level-security.md) (Security and access): Restrict which rows each user sees based on who they are.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Aurora](../aws/aws-aurora.md), [Amazon DynamoDB](../aws/aws-dynamodb.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Cosmos DB in Microsoft Fabric](../microsoft/fabric-cosmos-db.md), [Azure HorizonDB](../microsoft/azure-horizondb.md) (preview), [Azure Database for PostgreSQL](../microsoft/azure-database-for-postgresql.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Cloud SQL](../google-cloud/gcp-cloud-sql.md), [Firestore](../google-cloud/gcp-firestore.md), [AlloyDB for PostgreSQL](../google-cloud/gcp-alloydb.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake hybrid tables (Unistore)](../snowflake/snowflake-hybrid-tables.md), [Snowflake Postgres](../snowflake/snowflake-postgres.md) | [Operational data store](../../capabilities/serving/operational-data-store.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakebase](../databricks/databricks-lakebase.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Managed Postgres](../clickhouse/clickhouse-managed-postgres.md) (preview) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Operational Database](../cloudera/cloudera-operational-database.md) | [Operational data store](../../capabilities/serving/operational-data-store.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md), [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../oracle/oracle-database-multicloud.md), [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Db2](../ibm/ibm-db2.md), [IBM Astra DB (DataStax)](../ibm/ibm-astra-db.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [MongoDB Atlas](../independent/mongodb-atlas.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
