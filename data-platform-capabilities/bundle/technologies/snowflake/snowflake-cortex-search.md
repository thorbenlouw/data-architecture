---
type: Technology
id: snowflake-cortex-search
title: Snowflake Cortex Search
description: A managed hybrid vector and keyword search service, with reranking, that embeds, indexes and refreshes text from a query or stage on a target lag.
platform: platform-snowflake
kind: managed-service
availability: ga
realises: [vector-search, retrieval-pipelines, full-text-search]
resource: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Cortex Search is the retrieval layer for Cortex Agents and CoWork. Each service is limited to about 20 queries per second. Indexing files directly from a stage, and auto-suspend, are in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Vector search](../../capabilities/generative-ai/vector-search.md) (Generative AI) (primary): Store embeddings and find the most similar items quickly.
- [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) (Generative AI): Parse, chunk, embed and index content, and keep indexes in step as sources change.
- [Full-text search](../../capabilities/specialised-data/full-text-search.md) (Specialised data types): Index text for full-text search, relevance ranking and fast filtering.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake Cortex AI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 Vectors](../aws/aws-s3-vectors.md), [Amazon Bedrock Knowledge Bases](../aws/aws-bedrock-knowledge-bases.md), [Amazon OpenSearch Service](../aws/aws-opensearch-service.md) | [Vector search](../../capabilities/generative-ai/vector-search.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure AI Search](../microsoft/azure-ai-search.md), [Cosmos DB in Microsoft Fabric](../microsoft/fabric-cosmos-db.md), [Azure Cosmos DB](../microsoft/azure-cosmos-db.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery vector search](../google-cloud/gcp-bigquery-vector-search.md), [Google Cloud Agent Search](../google-cloud/gcp-agent-search.md), [Agent Platform Vector Search](../google-cloud/gcp-vector-search.md) | [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Vector search](../../capabilities/generative-ai/vector-search.md), [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Search](../databricks/databricks-ai-search.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse vector similarity indexes](../clickhouse/clickhouse-vector-search.md) | [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Vector Search](../oracle/oracle-ai-vector-search.md), [MySQL HeatWave AutoML and HeatWave GenAI](../oracle/oracle-heatwave-automl-genai.md) | [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud vector engine](../sap/sap-hana-cloud-vector-engine.md) | [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise Vector Store](../teradata/teradata-enterprise-vector-store.md) | [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [IBM](../../platforms/platform-ibm.md) | [OpenSearch and OpenRAG in IBM watsonx.data](../ibm/ibm-watsonx-data-opensearch-openrag.md), [IBM Astra DB (DataStax)](../ibm/ibm-astra-db.md), [IBM Db2](../ibm/ibm-db2.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Milvus](../open-source/milvus.md), [pgvector](../open-source/pgvector.md), [Qdrant](../open-source/qdrant.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Weaviate Cloud](../independent/weaviate-cloud.md), [Pinecone](../independent/pinecone.md), [MongoDB Atlas](../independent/mongodb-atlas.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
