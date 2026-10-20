---
type: Technology
id: teradata-enterprise-vector-store
title: Teradata Enterprise Vector Store
description: Vector storage and retrieval inside the Teradata platform, with hybrid keyword and semantic search across structured data and embeddings of text, images and audio.
platform: platform-teradata
kind: feature
availability: ga
realises: [vector-search, retrieval-pipelines, embedding-generation, retrieval-augmented-generation]
resource: https://www.teradata.com/platform/enterprise-vector-store
tags: [teradata]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Integrates with NVIDIA NIM for embeddings and reranking and with Unstructured for parsing and chunking; a LangChain integration is provided. Runs in cloud, on premises and hybrid.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Vector search](../../capabilities/generative-ai/vector-search.md) (Generative AI) (primary): Store embeddings and find the most similar items quickly.
- [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) (Generative AI): Parse, chunk, embed and index content, and keep indexes in step as sources change.
- [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) (Generative AI): Turn text, images or other content into vector embeddings for search and retrieval.
- [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) (Generative AI): Ground model answers in your own content by retrieving relevant passages at query time.

**Platform:** [Teradata](../../platforms/platform-teradata.md)  
**Availability:** ga  
**Product family:** Teradata AI Studio

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock Knowledge Bases](../aws/aws-bedrock-knowledge-bases.md), [Amazon S3 Vectors](../aws/aws-s3-vectors.md), [Amazon Neptune Analytics](../aws/aws-neptune-analytics.md) | [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure AI Search](../microsoft/azure-ai-search.md), [Azure Database for PostgreSQL](../microsoft/azure-database-for-postgresql.md), [Cosmos DB in Microsoft Fabric](../microsoft/fabric-cosmos-db.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery vector search](../google-cloud/gcp-bigquery-vector-search.md), [Agent Platform Vector Search](../google-cloud/gcp-vector-search.md), [Google Cloud Agent Search](../google-cloud/gcp-agent-search.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Vector search](../../capabilities/generative-ai/vector-search.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Search](../snowflake/snowflake-cortex-search.md) | [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Search](../databricks/databricks-ai-search.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse vector similarity indexes](../clickhouse/clickhouse-vector-search.md) | [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Vector Search](../oracle/oracle-ai-vector-search.md), [MySQL HeatWave AutoML and HeatWave GenAI](../oracle/oracle-heatwave-automl-genai.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud vector engine](../sap/sap-hana-cloud-vector-engine.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [IBM](../../platforms/platform-ibm.md) | [OpenSearch and OpenRAG in IBM watsonx.data](../ibm/ibm-watsonx-data-opensearch-openrag.md), [IBM Astra DB (DataStax)](../ibm/ibm-astra-db.md), [IBM Db2](../ibm/ibm-db2.md) | [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Knowledge Banks](../dataiku/dataiku-knowledge-banks.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [pgvector](../open-source/pgvector.md), [Qdrant](../open-source/qdrant.md), [Milvus](../open-source/milvus.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Pinecone](../independent/pinecone.md), [Weaviate Cloud](../independent/weaviate-cloud.md), [MongoDB Atlas](../independent/mongodb-atlas.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
