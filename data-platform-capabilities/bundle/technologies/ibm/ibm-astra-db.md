---
type: Technology
id: ibm-astra-db
title: IBM Astra DB (DataStax)
description: Managed Apache Cassandra database with vector search, offered as the operational NoSQL engine in watsonx.data and as a standalone service.
aliases: [DataStax Astra DB, Astra DB]
platform: platform-ibm
kind: managed-service
availability: ga
realises: [low-latency-serving, operational-database, vector-search]
resource: https://www.ibm.com/products/watsonx-data
tags: [ibm]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Came from the DataStax acquisition, announced in February 2025 and completed later that year. Langflow, also from DataStax, is IBM's open-source visual builder for agent and RAG flows.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Low-latency serving](../../capabilities/serving/low-latency-serving.md) (Serving and activation) (primary): Serve individual records or small result sets to applications in milliseconds.
- [Operational database integration](../../capabilities/serving/operational-database.md) (Serving and activation): Run transactional databases as part of the platform, with data flowing to and from analytical storage without separate pipelines.
- [Vector search](../../capabilities/generative-ai/vector-search.md) (Generative AI): Store embeddings and find the most similar items quickly.

**Platform:** [IBM](../../platforms/platform-ibm.md)  
**Availability:** ga  
**Product family:** IBM watsonx.data

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon DynamoDB](../aws/aws-dynamodb.md), [Amazon Aurora](../aws/aws-aurora.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Cosmos DB in Microsoft Fabric](../microsoft/fabric-cosmos-db.md), [Azure Cosmos DB](../microsoft/azure-cosmos-db.md), [Azure Database for PostgreSQL](../microsoft/azure-database-for-postgresql.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Firestore](../google-cloud/gcp-firestore.md), [Memorystore](../google-cloud/gcp-memorystore.md), [Spanner](../google-cloud/gcp-spanner.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Postgres](../snowflake/snowflake-postgres.md), [Snowflake hybrid tables (Unistore)](../snowflake/snowflake-hybrid-tables.md), [Snowflake interactive tables and interactive warehouses](../snowflake/snowflake-interactive-tables.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakebase](../databricks/databricks-lakebase.md), [Databricks Lakehouse Real-Time](../databricks/databricks-lakehouse-real-time.md) (preview) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud Query API Endpoints](../clickhouse/clickhouse-query-api-endpoints.md), [ClickHouse dictionaries](../clickhouse/clickhouse-dictionaries.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Operational Database](../cloudera/cloudera-operational-database.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Ontology](../palantir/palantir-ontology.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redis Cloud](../independent/redis-cloud.md), [K2view Data Product Platform](../independent/k2view-data-product-platform.md), [StarTree Cloud](../independent/startree-cloud.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
