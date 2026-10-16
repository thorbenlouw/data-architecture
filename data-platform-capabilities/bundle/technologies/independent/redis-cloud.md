---
type: Technology
id: redis-cloud
title: Redis Cloud
description: Managed Redis in-memory database for sub-millisecond key-value, JSON, stream and vector workloads, with active-active geo-distribution.
platform: platform-independent
vendor: Redis
kind: managed-service
availability: ga
realises: [low-latency-serving, vector-search, online-feature-store, cross-region-failover]
resource: https://redis.io/docs/latest/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Redis Software is the self-managed edition. Redis Data Integration ingests changes from operational databases to keep Redis caches current. The Redis Query Engine and RedisVL provide vector search and AI application tooling.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Low-latency serving](../../capabilities/serving/low-latency-serving.md) (Serving and activation) (primary): Serve individual records or small result sets to applications in milliseconds.
- [Vector search](../../capabilities/generative-ai/vector-search.md) (Generative AI): Store embeddings and find the most similar items quickly.
- [Online feature store](../../capabilities/machine-learning/online-feature-store.md) (Machine learning development): Serve the latest feature values to models in milliseconds.
- [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) (Platform operations): Replicate data and configuration to another region and fail over when needed.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon DynamoDB](../aws/aws-dynamodb.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md), [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Online feature store](../../capabilities/machine-learning/online-feature-store.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Cosmos DB](../microsoft/azure-cosmos-db.md), [Cosmos DB in Microsoft Fabric](../microsoft/fabric-cosmos-db.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md), [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Memorystore](../google-cloud/gcp-memorystore.md), [Bigtable](../google-cloud/gcp-bigtable.md), [Firestore](../google-cloud/gcp-firestore.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Vector search](../../capabilities/generative-ai/vector-search.md), [Online feature store](../../capabilities/machine-learning/online-feature-store.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Postgres](../snowflake/snowflake-postgres.md), [Snowflake hybrid tables (Unistore)](../snowflake/snowflake-hybrid-tables.md), [Snowflake interactive tables and interactive warehouses](../snowflake/snowflake-interactive-tables.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Lakehouse Real-Time](../databricks/databricks-lakehouse-real-time.md) (preview), [Lakebase](../databricks/databricks-lakebase.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud Query API Endpoints](../clickhouse/clickhouse-query-api-endpoints.md), [ClickHouse dictionaries](../clickhouse/clickhouse-dictionaries.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Operational Database](../cloudera/cloudera-operational-database.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Astra DB (DataStax)](../ibm/ibm-astra-db.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Ontology](../palantir/palantir-ontology.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
