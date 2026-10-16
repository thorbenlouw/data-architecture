---
type: Technology
id: sap-hana-cloud
title: SAP HANA Cloud
description: Managed in-memory, multi-model database on SAP BTP for transactional and analytical work across relational, document, spatial, graph, time-series and vector data.
aliases: [HANA Cloud]
platform: platform-sap
kind: managed-service
availability: ga
realises:
- operational-database
- sql-query-engine
- geospatial-data
- semi-structured-data
- query-federation
- temporal-data
- graph-data
- time-series-data
resource: https://www.sap.com/products/data-cloud/hana.html
tags: [sap]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Federates and replicates other sources through smart data access and smart data integration. Calculation views can be shared into BDC. Native Storage Extension and the data lake reduce cost for warm data. MCP support (announced November 2025) lets Joule agents use its engines.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Operational database integration](../../capabilities/serving/operational-database.md) (Serving and activation) (primary): Run transactional databases as part of the platform, with data flowing to and from analytical storage without separate pipelines.
- [SQL query engine](../../capabilities/compute/sql-query-engine.md) (Query and compute): Run analytical SQL over large datasets with parallel, optimised execution.
- [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) (Specialised data types): Store, index and analyse location and shape data with spatial types and functions.
- [Semi-structured data](../../capabilities/storage/semi-structured-data.md) (Storage and table management): Store and query nested data such as JSON without flattening it first.
- [Query federation](../../capabilities/compute/query-federation.md) (Query and compute): Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.
- [Bitemporal data](../../capabilities/specialised-data/temporal-data.md) (Specialised data types): Store and query data as it was true in the real world and as it was recorded in the system.
- [Graph data](../../capabilities/specialised-data/graph-data.md) (Specialised data types): Model and query connected data as nodes and relationships.
- [Time-series data](../../capabilities/specialised-data/time-series-data.md) (Specialised data types): Store and query time-stamped measurements efficiently, with time-based functions and retention.

**Platform:** [SAP](../../platforms/platform-sap.md)  
**Availability:** ga  
**Product family:** SAP HANA Cloud, SAP Business Technology Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Aurora](../aws/aws-aurora.md), [Amazon DynamoDB](../aws/aws-dynamodb.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Cosmos DB in Microsoft Fabric](../microsoft/fabric-cosmos-db.md), [Azure HorizonDB](../microsoft/azure-horizondb.md) (preview), [Azure Database for PostgreSQL](../microsoft/azure-database-for-postgresql.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Spanner](../google-cloud/gcp-spanner.md), [Cloud SQL](../google-cloud/gcp-cloud-sql.md), [Firestore](../google-cloud/gcp-firestore.md) | [Graph data](../../capabilities/specialised-data/graph-data.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Postgres](../snowflake/snowflake-postgres.md), [Snowflake hybrid tables (Unistore)](../snowflake/snowflake-hybrid-tables.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakebase](../databricks/databricks-lakebase.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Managed Postgres](../clickhouse/clickhouse-managed-postgres.md) (preview) | [Operational database integration](../../capabilities/serving/operational-database.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Operational Database](../cloudera/cloudera-operational-database.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md), [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md), [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../oracle/oracle-database-multicloud.md) | [Bitemporal data](../../capabilities/specialised-data/temporal-data.md), [Geospatial data](../../capabilities/specialised-data/geospatial-data.md), [Graph data](../../capabilities/specialised-data/graph-data.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database](../teradata/teradata-database.md) | [Bitemporal data](../../capabilities/specialised-data/temporal-data.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Db2](../ibm/ibm-db2.md), [IBM Astra DB (DataStax)](../ibm/ibm-astra-db.md) | [Bitemporal data](../../capabilities/specialised-data/temporal-data.md), [Operational database integration](../../capabilities/serving/operational-database.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [PostgreSQL](../open-source/postgresql.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [MongoDB Atlas](../independent/mongodb-atlas.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
