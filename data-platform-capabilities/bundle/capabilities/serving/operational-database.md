---
type: Capability
id: operational-database
title: Operational database integration
description: Run transactional databases as part of the platform, with data flowing to and from analytical storage without separate pipelines.
aliases: [HTAP, hybrid tables, OLTP integration]
broader: [serving]
related: [database-replication, data-applications, workload-isolation, low-latency-serving, data-writeback]
tags: [serving]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Transactional (OLTP) databases run as part of the platform or tightly connected to it, so applications and analytics share data without hand-built pipelines. Forms include managed relational databases inside the platform whose changes flow automatically into analytical tables; hybrid tables that support fast single-row transactions and analytical scans; and the reverse direction, where curated analytical data is synced into a transactional database for an application. HTAP (hybrid transactional and analytical processing) is the general term for one system that handles both.

It suits data applications that need transactions on current data and analytics over the same data, such as a pricing tool that records approved prices and reports on them. It removes separate replication pipelines and keeps one security and governance model. The trade-offs are that hybrid engines rarely match specialist transactional databases on throughput and features, and running both workloads together needs isolation. Database replication is narrower: it copies external databases into the platform.

# Key considerations

- Test write throughput, locking behaviour and latency before putting critical applications on hybrid tables.
- Isolate analytical queries from transactional work, or a large scan can slow the application.
- Confirm which direction data syncs, how quickly, and whether schema changes follow.
- Check backup, recovery and availability targets, which are usually stricter for operational databases than for analytical ones.

# Questions to ask

- Which applications need both transactional writes and analytics on the same data?
- What transaction rate and latency must the database support?
- Would the application team accept a database run as part of the data platform?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Serving and activation](serving.md) |
| Broader | [Serving and activation](serving.md) |
| Related | [Data application hosting](../development-lifecycle/data-applications.md), [Data entry and write-back](../analytics-bi/data-writeback.md), [Database replication and mirroring](../ingestion-integration/database-replication.md), [Low-latency serving](low-latency-serving.md), [Online feature store](../machine-learning/online-feature-store.md), [Operational data store](operational-data-store.md), [Workload isolation](../compute/workload-isolation.md) |

# Where it appears

- **Patterns:** [Transactional outbox](../../patterns/transactional-outbox.md)
- **Personas:** [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Data serving](../../maturity/track-serving.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Aurora](../../technologies/aws/aws-aurora.md), [Amazon DynamoDB](../../technologies/aws/aws-dynamodb.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Cosmos DB](../../technologies/microsoft/azure-cosmos-db.md), [Azure Database for PostgreSQL](../../technologies/microsoft/azure-database-for-postgresql.md), [Azure HorizonDB](../../technologies/microsoft/azure-horizondb.md) (preview), [Azure SQL Database](../../technologies/microsoft/azure-sql.md), [Cosmos DB in Microsoft Fabric](../../technologies/microsoft/fabric-cosmos-db.md), [SQL database in Microsoft Fabric](../../technologies/microsoft/fabric-sql-database.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [AlloyDB for PostgreSQL](../../technologies/google-cloud/gcp-alloydb.md), [Cloud SQL](../../technologies/google-cloud/gcp-cloud-sql.md), [Firestore](../../technologies/google-cloud/gcp-firestore.md), [Spanner](../../technologies/google-cloud/gcp-spanner.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | hybrid tables (Unistore) and Snowflake Postgres | [Snowflake hybrid tables (Unistore)](../../technologies/snowflake/snowflake-hybrid-tables.md), [Snowflake Postgres](../../technologies/snowflake/snowflake-postgres.md) |
| [Databricks](../../platforms/platform-databricks.md) | Lakebase | [Lakebase](../../technologies/databricks/databricks-lakebase.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | ClickHouse Managed Postgres | [ClickHouse Managed Postgres](../../technologies/clickhouse/clickhouse-managed-postgres.md) (preview) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Operational Database](../../technologies/cloudera/cloudera-operational-database.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [MySQL HeatWave](../../technologies/oracle/oracle-mysql-heatwave.md), [Oracle AI Database 26ai](../../technologies/oracle/oracle-ai-database-26ai.md), [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../../technologies/oracle/oracle-database-multicloud.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP HANA Cloud](../../technologies/sap/sap-hana-cloud.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM Astra DB (DataStax)](../../technologies/ibm/ibm-astra-db.md), [IBM Db2](../../technologies/ibm/ibm-db2.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS SpeedyStore](../../technologies/sas/sas-speedystore.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [PostgreSQL](../../technologies/open-source/postgresql.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [MongoDB Atlas](../../technologies/independent/mongodb-atlas.md) |
