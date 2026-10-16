---
type: Technology
id: gcp-memorystore
title: Memorystore
description: Managed in-memory data stores (Memorystore for Valkey, Redis Cluster and Redis) for caching and sub-millisecond lookups.
aliases: [Memorystore for Valkey, Memorystore for Redis Cluster]
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [low-latency-serving, vector-search]
resource: https://docs.cloud.google.com/memorystore/docs
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Valkey and Redis offerings support vector search for semantic caching and retrieval. Memorystore for Memcached is deprecated.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Low-latency serving](../../capabilities/serving/low-latency-serving.md) (Serving and activation) (primary): Serve individual records or small result sets to applications in milliseconds.
- [Vector search](../../capabilities/generative-ai/vector-search.md) (Generative AI): Store embeddings and find the most similar items quickly.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon DynamoDB](../aws/aws-dynamodb.md), [Amazon S3 Vectors](../aws/aws-s3-vectors.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Cosmos DB in Microsoft Fabric](../microsoft/fabric-cosmos-db.md), [Azure Cosmos DB](../microsoft/azure-cosmos-db.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Postgres](../snowflake/snowflake-postgres.md), [Snowflake hybrid tables (Unistore)](../snowflake/snowflake-hybrid-tables.md), [Snowflake interactive tables and interactive warehouses](../snowflake/snowflake-interactive-tables.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Lakehouse Real-Time](../databricks/databricks-lakehouse-real-time.md) (preview), [Lakebase](../databricks/databricks-lakebase.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud Query API Endpoints](../clickhouse/clickhouse-query-api-endpoints.md), [ClickHouse dictionaries](../clickhouse/clickhouse-dictionaries.md), [ClickHouse vector similarity indexes](../clickhouse/clickhouse-vector-search.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Operational Database](../cloudera/cloudera-operational-database.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Astra DB (DataStax)](../ibm/ibm-astra-db.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Ontology](../palantir/palantir-ontology.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redis Cloud](../independent/redis-cloud.md), [K2view Data Product Platform](../independent/k2view-data-product-platform.md), [StarTree Cloud](../independent/startree-cloud.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
