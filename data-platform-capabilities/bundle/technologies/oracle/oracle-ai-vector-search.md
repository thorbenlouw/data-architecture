---
type: Technology
id: oracle-ai-vector-search
title: Oracle AI Vector Search
description: Native VECTOR data type, vector indexes and similarity functions in Oracle AI Database, combinable with relational, text, JSON, graph and spatial predicates in one SQL query.
platform: platform-oracle
kind: feature
availability: ga
realises: [vector-search, embedding-generation, retrieval-augmented-generation]
resource: https://www.oracle.com/database/ai-native-database-26ai/
tags: [oracle]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Embeddings can be generated in the database with imported ONNX models or by calling external providers. Unified hybrid vector search combines keyword and vector retrieval. Avoids running a separate vector database next to Oracle.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Vector search](../../capabilities/generative-ai/vector-search.md) (Generative AI) (primary): Store embeddings and find the most similar items quickly.
- [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) (Generative AI): Turn text, images or other content into vector embeddings for search and retrieval.
- [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) (Generative AI): Ground model answers in your own content by retrieving relevant passages at query time.

**Platform:** [Oracle](../../platforms/platform-oracle.md)  
**Availability:** ga  
**Product family:** Oracle AI Database

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 Vectors](../aws/aws-s3-vectors.md), [Amazon Bedrock Knowledge Bases](../aws/aws-bedrock-knowledge-bases.md), [Amazon Neptune Analytics](../aws/aws-neptune-analytics.md) | [Vector search](../../capabilities/generative-ai/vector-search.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure AI Search](../microsoft/azure-ai-search.md), [Azure Database for PostgreSQL](../microsoft/azure-database-for-postgresql.md), [Cosmos DB in Microsoft Fabric](../microsoft/fabric-cosmos-db.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Vector Search](../google-cloud/gcp-vector-search.md), [BigQuery vector search](../google-cloud/gcp-bigquery-vector-search.md), [Google Cloud Agent Search](../google-cloud/gcp-agent-search.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Search](../snowflake/snowflake-cortex-search.md) | [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Search](../databricks/databricks-ai-search.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse vector similarity indexes](../clickhouse/clickhouse-vector-search.md) | [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud vector engine](../sap/sap-hana-cloud-vector-engine.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise Vector Store](../teradata/teradata-enterprise-vector-store.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [IBM](../../platforms/platform-ibm.md) | [OpenSearch and OpenRAG in IBM watsonx.data](../ibm/ibm-watsonx-data-opensearch-openrag.md), [IBM Astra DB (DataStax)](../ibm/ibm-astra-db.md), [IBM Db2](../ibm/ibm-db2.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [pgvector](../open-source/pgvector.md), [Qdrant](../open-source/qdrant.md), [Milvus](../open-source/milvus.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Pinecone](../independent/pinecone.md), [Weaviate Cloud](../independent/weaviate-cloud.md), [MongoDB Atlas](../independent/mongodb-atlas.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
