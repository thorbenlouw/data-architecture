---
type: Technology
id: ibm-watsonx-data-opensearch-openrag
title: OpenSearch and OpenRAG in IBM watsonx.data
description: Vector and keyword search engine in watsonx.data, with OpenRAG tooling for document processing, hybrid search and agentic retrieval for grounding AI applications.
platform: platform-ibm
kind: feature
availability: ga
realises:
- vector-search
- retrieval-pipelines
- retrieval-augmented-generation
- full-text-search
- document-processing
resource: https://www.ibm.com/products/watsonx-data
tags: [ibm]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

[OpenSearch](../open-source/opensearch.md) is the main vector engine in IBM's 2026 messaging; earlier watsonx.data deployments may use the [Milvus](../open-source/milvus.md) engine instead.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Vector search](../../capabilities/generative-ai/vector-search.md) (Generative AI) (primary): Store embeddings and find the most similar items quickly.
- [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) (Generative AI): Parse, chunk, embed and index content, and keep indexes in step as sources change.
- [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) (Generative AI): Ground model answers in your own content by retrieving relevant passages at query time.
- [Full-text search](../../capabilities/specialised-data/full-text-search.md) (Specialised data types): Index text for full-text search, relevance ranking and fast filtering.
- [Document processing](../../capabilities/processing/document-processing.md) (Processing and transformation): Extract text, tables and fields from documents such as PDFs, scans and images.

**Platform:** [IBM](../../platforms/platform-ibm.md)  
**Availability:** ga  
**Product family:** IBM watsonx.data

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock Knowledge Bases](../aws/aws-bedrock-knowledge-bases.md), [Amazon S3 Vectors](../aws/aws-s3-vectors.md), [Amazon OpenSearch Service](../aws/aws-opensearch-service.md) | [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md), [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure AI Search](../microsoft/azure-ai-search.md), [Cosmos DB in Microsoft Fabric](../microsoft/fabric-cosmos-db.md), [Azure Cosmos DB](../microsoft/azure-cosmos-db.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Search](../google-cloud/gcp-agent-search.md), [BigQuery vector search](../google-cloud/gcp-bigquery-vector-search.md), [Agent Platform Vector Search](../google-cloud/gcp-vector-search.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Search](../snowflake/snowflake-cortex-search.md), [Snowflake Cortex AI Functions for documents (AI_PARSE_DOCUMENT, AI_EXTRACT)](../snowflake/snowflake-cortex-document-functions.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Vector search](../../capabilities/generative-ai/vector-search.md), [Document processing](../../capabilities/processing/document-processing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Search](../databricks/databricks-ai-search.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse vector similarity indexes](../clickhouse/clickhouse-vector-search.md) | [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Vector Search](../oracle/oracle-ai-vector-search.md), [MySQL HeatWave AutoML and HeatWave GenAI](../oracle/oracle-heatwave-automl-genai.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud vector engine](../sap/sap-hana-cloud-vector-engine.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise Vector Store](../teradata/teradata-enterprise-vector-store.md) | [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Milvus](../open-source/milvus.md), [pgvector](../open-source/pgvector.md), [Qdrant](../open-source/qdrant.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Pinecone](../independent/pinecone.md), [Weaviate Cloud](../independent/weaviate-cloud.md), [MongoDB Atlas](../independent/mongodb-atlas.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
