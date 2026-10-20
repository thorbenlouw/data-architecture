---
type: Technology
id: azure-database-for-postgresql
title: Azure Database for PostgreSQL
description: Managed PostgreSQL (flexible server) with high availability, read replicas and extensions such as pgvector and DiskANN for vector search.
aliases: [Azure Database for PostgreSQL flexible server]
platform: platform-microsoft
kind: managed-service
availability: ga
realises: [operational-database, vector-search]
resource: https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Single Server was retired in 2025. Mirrors to Fabric.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Operational database integration](../../capabilities/serving/operational-database.md) (Serving and activation) (primary): Run transactional databases as part of the platform, with data flowing to and from analytical storage without separate pipelines.
- [Vector search](../../capabilities/generative-ai/vector-search.md) (Generative AI): Store embeddings and find the most similar items quickly.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Aurora](../aws/aws-aurora.md), [Amazon DynamoDB](../aws/aws-dynamodb.md), [Amazon S3 Vectors](../aws/aws-s3-vectors.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Firestore](../google-cloud/gcp-firestore.md), [AlloyDB for PostgreSQL](../google-cloud/gcp-alloydb.md), [Cloud SQL](../google-cloud/gcp-cloud-sql.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Postgres](../snowflake/snowflake-postgres.md), [Snowflake hybrid tables (Unistore)](../snowflake/snowflake-hybrid-tables.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakebase](../databricks/databricks-lakebase.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Managed Postgres](../clickhouse/clickhouse-managed-postgres.md) (preview), [ClickHouse vector similarity indexes](../clickhouse/clickhouse-vector-search.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Operational Database](../cloudera/cloudera-operational-database.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../oracle/oracle-database-multicloud.md), [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md), [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Astra DB (DataStax)](../ibm/ibm-astra-db.md), [IBM Db2](../ibm/ibm-db2.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS SpeedyStore](../sas/sas-speedystore.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [PostgreSQL](../open-source/postgresql.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [MongoDB Atlas](../independent/mongodb-atlas.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
