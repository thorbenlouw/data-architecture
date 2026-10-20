---
type: Technology
id: aws-aurora
title: Amazon Aurora
description: MySQL- and PostgreSQL-compatible relational database with distributed storage, read replicas, global databases and copy-on-write cloning.
platform: platform-aws
kind: managed-service
availability: ga
realises: [operational-database, cross-region-failover, zero-copy-cloning, vector-search]
resource: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Aurora PostgreSQL supports pgvector and can serve as a Bedrock Knowledge Bases vector store. Zero-ETL replicates to Redshift. Amazon RDS covers other engines; Aurora DSQL is a separate distributed variant.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Operational database integration](../../capabilities/serving/operational-database.md) (Serving and activation) (primary): Run transactional databases as part of the platform, with data flowing to and from analytical storage without separate pipelines.
- [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) (Platform operations): Replicate data and configuration to another region and fail over when needed.
- [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) (Storage and table management): Create an instant copy of a table, schema or database that shares storage with the original until either changes.
- [Vector search](../../capabilities/generative-ai/vector-search.md) (Generative AI): Store embeddings and find the most similar items quickly.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Database for PostgreSQL](../microsoft/azure-database-for-postgresql.md), [Azure Cosmos DB](../microsoft/azure-cosmos-db.md), [Azure SQL Database](../microsoft/azure-sql.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Vector search](../../capabilities/generative-ai/vector-search.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Firestore](../google-cloud/gcp-firestore.md), [AlloyDB for PostgreSQL](../google-cloud/gcp-alloydb.md), [Cloud SQL](../google-cloud/gcp-cloud-sql.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Postgres](../snowflake/snowflake-postgres.md), [Snowflake hybrid tables (Unistore)](../snowflake/snowflake-hybrid-tables.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakebase](../databricks/databricks-lakebase.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Managed Postgres](../clickhouse/clickhouse-managed-postgres.md) (preview) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Operational Database](../cloudera/cloudera-operational-database.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../oracle/oracle-database-multicloud.md), [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md), [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Db2](../ibm/ibm-db2.md), [IBM Astra DB (DataStax)](../ibm/ibm-astra-db.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS SpeedyStore](../sas/sas-speedystore.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [PostgreSQL](../open-source/postgresql.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [MongoDB Atlas](../independent/mongodb-atlas.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
