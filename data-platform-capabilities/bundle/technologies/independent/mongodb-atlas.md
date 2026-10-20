---
type: Technology
id: mongodb-atlas
title: MongoDB Atlas
description: Managed MongoDB document database with integrated full-text search, vector search and automated embedding generation using Voyage AI models.
aliases: [Atlas Vector Search, Atlas Search]
platform: platform-independent
vendor: MongoDB
kind: managed-service
availability: ga
realises: [operational-database, vector-search, embedding-generation, full-text-search, semi-structured-data]
resource: https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-overview/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Vector Search runs through the $vectorSearch aggregation stage, with pre-filtering and hybrid search. Separate Search Nodes isolate search workloads. Automated embedding keeps vectors in sync as documents change. Atlas Stream Processing handles stream processing.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Operational database integration](../../capabilities/serving/operational-database.md) (Serving and activation) (primary): Run transactional databases as part of the platform, with data flowing to and from analytical storage without separate pipelines.
- [Vector search](../../capabilities/generative-ai/vector-search.md) (Generative AI): Store embeddings and find the most similar items quickly.
- [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) (Generative AI): Turn text, images or other content into vector embeddings for search and retrieval.
- [Full-text search](../../capabilities/specialised-data/full-text-search.md) (Specialised data types): Index text for full-text search, relevance ranking and fast filtering.
- [Semi-structured data](../../capabilities/storage/semi-structured-data.md) (Storage and table management): Store and query nested data such as JSON without flattening it first.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Aurora](../aws/aws-aurora.md), [Amazon DynamoDB](../aws/aws-dynamodb.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Cosmos DB in Microsoft Fabric](../microsoft/fabric-cosmos-db.md), [Azure Database for PostgreSQL](../microsoft/azure-database-for-postgresql.md), [Azure Cosmos DB](../microsoft/azure-cosmos-db.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Operational database integration](../../capabilities/serving/operational-database.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Spanner](../google-cloud/gcp-spanner.md), [Firestore](../google-cloud/gcp-firestore.md), [AlloyDB for PostgreSQL](../google-cloud/gcp-alloydb.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Operational database integration](../../capabilities/serving/operational-database.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Postgres](../snowflake/snowflake-postgres.md), [Snowflake hybrid tables (Unistore)](../snowflake/snowflake-hybrid-tables.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakebase](../databricks/databricks-lakebase.md), [Databricks AI Search](../databricks/databricks-ai-search.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Managed Postgres](../clickhouse/clickhouse-managed-postgres.md) (preview) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Operational Database](../cloudera/cloudera-operational-database.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md), [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../oracle/oracle-database-multicloud.md), [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Operational database integration](../../capabilities/serving/operational-database.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Db2](../ibm/ibm-db2.md), [IBM Astra DB (DataStax)](../ibm/ibm-astra-db.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS SpeedyStore](../sas/sas-speedystore.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [PostgreSQL](../open-source/postgresql.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
