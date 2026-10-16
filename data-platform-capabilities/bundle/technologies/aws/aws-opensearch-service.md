---
type: Technology
id: aws-opensearch-service
title: Amazon OpenSearch Service
description: Managed OpenSearch for full-text search, log analytics and vector search, available as provisioned domains or OpenSearch Serverless collections.
aliases: [Amazon OpenSearch Serverless, Amazon OpenSearch Ingestion]
formerly: [Amazon Elasticsearch Service]
platform: platform-aws
kind: managed-service
availability: ga
realises: [full-text-search, vector-search, streaming-ingestion, real-time-analytics, observability-analytics]
resource: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

OpenSearch Ingestion provides managed Data Prepper pipelines, including zero-ETL from DynamoDB and S3. Can use S3 Vectors for cheaper vector storage. Older OpenSearch and Elasticsearch versions incur extended-support charges from 7 November 2026; versions up to 3.5 are available. Amazon CloudSearch is closed to new customers in favour of this service.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Full-text search](../../capabilities/specialised-data/full-text-search.md) (Specialised data types) (primary): Index text for full-text search, relevance ranking and fast filtering.
- [Vector search](../../capabilities/generative-ai/vector-search.md) (Generative AI): Store embeddings and find the most similar items quickly.
- [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) (Ingestion and integration): Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.
- [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) (Query and compute): Answer analytical queries in milliseconds over fresh, high-volume data, often for user-facing applications.
- [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md) (Specialised data types): Store and analyse logs, metrics and traces from applications and infrastructure at scale, with search, dashboards and alerts.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure AI Search](../microsoft/azure-ai-search.md), [Cosmos DB in Microsoft Fabric](../microsoft/fabric-cosmos-db.md), [Azure Cosmos DB](../microsoft/azure-cosmos-db.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Search](../google-cloud/gcp-agent-search.md), [Spanner](../google-cloud/gcp-spanner.md), [BigQuery search indexes](../google-cloud/gcp-bigquery-search-indexes.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Search](../snowflake/snowflake-cortex-search.md), [Snowflake Search Optimization Service](../snowflake/snowflake-search-optimization-service.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Search](../databricks/databricks-ai-search.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse text indexes (full-text search)](../clickhouse/clickhouse-text-indexes.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [IBM](../../platforms/platform-ibm.md) | [OpenSearch and OpenRAG in IBM watsonx.data](../ibm/ibm-watsonx-data-opensearch-openrag.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenSearch](../open-source/opensearch.md), [Milvus](../open-source/milvus.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Elastic Cloud](../independent/elastic-cloud.md), [Weaviate Cloud](../independent/weaviate-cloud.md), [MongoDB Atlas](../independent/mongodb-atlas.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
