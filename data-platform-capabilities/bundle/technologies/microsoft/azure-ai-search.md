---
type: Technology
id: azure-ai-search
title: Azure AI Search
description: A search service offering full-text, vector, hybrid and multimodal retrieval with indexers, integrated vectorisation and agentic retrieval.
formerly: [Azure Cognitive Search, Azure Search]
platform: platform-microsoft
kind: managed-service
availability: ga
realises:
- vector-search
- retrieval-pipelines
- full-text-search
- embedding-generation
- permission-aware-retrieval
resource: https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The retrieval engine underneath Foundry IQ. Agentic retrieval is GA with some parts preview; a serverless pricing model is preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Vector search](../../capabilities/generative-ai/vector-search.md) (Generative AI) (primary): Store embeddings and find the most similar items quickly.
- [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) (Generative AI): Parse, chunk, embed and index content, and keep indexes in step as sources change.
- [Full-text search](../../capabilities/specialised-data/full-text-search.md) (Specialised data types): Index text for full-text search, relevance ranking and fast filtering.
- [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) (Generative AI): Turn text, images or other content into vector embeddings for search and retrieval.
- [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md) (Generative AI): Filter retrieved content by each user's permissions in the source systems so AI answers never reveal what the user could not open.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock Knowledge Bases](../aws/aws-bedrock-knowledge-bases.md), [Amazon S3 Vectors](../aws/aws-s3-vectors.md), [Amazon OpenSearch Service](../aws/aws-opensearch-service.md) | [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Vector search](../../capabilities/generative-ai/vector-search.md), [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery vector search](../google-cloud/gcp-bigquery-vector-search.md), [Google Cloud Agent Search](../google-cloud/gcp-agent-search.md), [Agent Platform Vector Search](../google-cloud/gcp-vector-search.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Vector search](../../capabilities/generative-ai/vector-search.md), [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Search](../snowflake/snowflake-cortex-search.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Search](../databricks/databricks-ai-search.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse vector similarity indexes](../clickhouse/clickhouse-vector-search.md) | [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Vector Search](../oracle/oracle-ai-vector-search.md), [MySQL HeatWave AutoML and HeatWave GenAI](../oracle/oracle-heatwave-automl-genai.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud vector engine](../sap/sap-hana-cloud-vector-engine.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise Vector Store](../teradata/teradata-enterprise-vector-store.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [IBM](../../platforms/platform-ibm.md) | [OpenSearch and OpenRAG in IBM watsonx.data](../ibm/ibm-watsonx-data-opensearch-openrag.md), [IBM Astra DB (DataStax)](../ibm/ibm-astra-db.md), [IBM Db2](../ibm/ibm-db2.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Milvus](../open-source/milvus.md), [pgvector](../open-source/pgvector.md), [Qdrant](../open-source/qdrant.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Weaviate Cloud](../independent/weaviate-cloud.md), [Pinecone](../independent/pinecone.md), [MongoDB Atlas](../independent/mongodb-atlas.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
