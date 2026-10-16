---
type: Technology
id: clickhouse-vector-search
title: ClickHouse vector similarity indexes
description: HNSW indexes on embedding columns for approximate nearest-neighbour search with L2, cosine or dot-product distance, alongside exact brute-force search and the QBit type.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [vector-search]
resource: https://clickhouse.com/docs/engines/table-engines/mergetree-family/annindexes
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The HNSW index is available from 25.8; the graph can be quantised (bf16 by default, down to binary) and QBit lets precision be chosen at query time. Quantised codecs such as RaBitQ are experimental. ClickHouse does not generate embeddings in Cloud; the beta aiEmbed function exists only for self-managed servers.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Vector search](../../capabilities/generative-ai/vector-search.md) (Generative AI) (primary): Store embeddings and find the most similar items quickly.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 Vectors](../aws/aws-s3-vectors.md), [Amazon Neptune Analytics](../aws/aws-neptune-analytics.md), [Amazon Aurora](../aws/aws-aurora.md) | [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Database for PostgreSQL](../microsoft/azure-database-for-postgresql.md), [Azure AI Search](../microsoft/azure-ai-search.md), [Cosmos DB in Microsoft Fabric](../microsoft/fabric-cosmos-db.md) | [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Vector Search](../google-cloud/gcp-vector-search.md), [BigQuery vector search](../google-cloud/gcp-bigquery-vector-search.md), [Memorystore](../google-cloud/gcp-memorystore.md) | [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Search](../snowflake/snowflake-cortex-search.md) | [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Search](../databricks/databricks-ai-search.md) | [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Vector Search](../oracle/oracle-ai-vector-search.md), [MySQL HeatWave AutoML and HeatWave GenAI](../oracle/oracle-heatwave-automl-genai.md) | [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud vector engine](../sap/sap-hana-cloud-vector-engine.md) | [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise Vector Store](../teradata/teradata-enterprise-vector-store.md) | [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [IBM](../../platforms/platform-ibm.md) | [OpenSearch and OpenRAG in IBM watsonx.data](../ibm/ibm-watsonx-data-opensearch-openrag.md), [IBM Astra DB (DataStax)](../ibm/ibm-astra-db.md), [IBM Db2](../ibm/ibm-db2.md) | [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [pgvector](../open-source/pgvector.md), [Qdrant](../open-source/qdrant.md), [Milvus](../open-source/milvus.md) | [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Weaviate Cloud](../independent/weaviate-cloud.md), [Pinecone](../independent/pinecone.md), [Neo4j Aura](../independent/neo4j-aura.md) | [Vector search](../../capabilities/generative-ai/vector-search.md) |
