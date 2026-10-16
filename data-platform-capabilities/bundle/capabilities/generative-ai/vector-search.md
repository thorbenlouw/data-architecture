---
type: Capability
id: vector-search
title: Vector search
description: Store embeddings and find the most similar items quickly.
aliases: [vector database, vector index, similarity search, hybrid search, reranking]
broader: [generative-ai, specialised-data]
related: [full-text-search, retrieval-augmented-generation, knowledge-graphs, multimodal-data-formats]
tags: [generative-ai]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

An embedding is a list of numbers that represents the meaning of a piece of content, so that similar items have nearby vectors. Vector search stores these vectors and returns the nearest ones to a query vector. Comparing a query with every vector is too slow at scale, so engines build approximate nearest neighbour (ANN) indexes, such as HNSW graphs, trading a little accuracy for large speed gains. For example, a help search embeds "my card was declined abroad" and finds articles about blocks on foreign transactions that share none of its words.

It underpins retrieval-augmented generation, semantic search, recommendations and near-duplicate detection. It is offered by dedicated vector databases and as a feature of relational databases, search engines and lakehouse tables. Production retrieval usually combines vector similarity with keyword ranking such as BM25, applies metadata filters and then reranks the results. Full-text search matches terms; vector search matches meaning, and each fails where the other succeeds, for example on product codes.

# Key considerations

- Filtering by tenant, date or permissions while searching an ANN index is hard. Filtering afterwards can leave too few results, so test how the engine handles filtered queries.
- Index memory grows with vector count and dimensions. Quantisation and shorter vectors reduce cost at some loss of accuracy.
- Changing the embedding model means re-embedding everything and rebuilding the index. Store the model and version with each vector.
- Measure recall against exact search on your own data rather than relying on published benchmarks.
- Vectors stored next to their source tables avoid synchronisation problems. A separate vector store may have more features but is another copy to secure and keep current.

# Questions to ask

- How many items will be indexed, how often do they change, and how soon must changes be searchable?
- Do queries need filters by permission, tenant or date?
- What query rate and response time are required?
- Do users also search for exact terms such as names, codes or identifiers?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Generative AI](generative-ai.md) |
| Broader | [Generative AI](generative-ai.md), [Specialised data types](../specialised-data/specialised-data.md) |
| Narrower | [Embedding generation](embedding-generation.md) |
| Related | [Agent memory](agent-memory.md), [Full-text search](../specialised-data/full-text-search.md), [Knowledge graphs](../specialised-data/knowledge-graphs.md), [Multimodal data formats](../storage/multimodal-data-formats.md), [Retrieval-augmented generation](retrieval-augmented-generation.md) |
| Needed by | [Retrieval pipelines](retrieval-pipelines.md), [Retrieval-augmented generation](retrieval-augmented-generation.md) |

# Where it appears

- **Use cases:** [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (requires, level 3) · [Personalised recommendations](../../use-cases/usecase-recommendations.md) (requires, level 2)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md)
- **Maturity tracks:** [Generative AI](../../maturity/track-genai.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | S3 Vectors; OpenSearch vector engine | [Amazon Aurora](../../technologies/aws/aws-aurora.md), [Amazon Bedrock Knowledge Bases](../../technologies/aws/aws-bedrock-knowledge-bases.md), [Amazon Neptune Analytics](../../technologies/aws/aws-neptune-analytics.md), [Amazon OpenSearch Service](../../technologies/aws/aws-opensearch-service.md), [Amazon S3 Vectors](../../technologies/aws/aws-s3-vectors.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure AI Search](../../technologies/microsoft/azure-ai-search.md), [Azure Cosmos DB](../../technologies/microsoft/azure-cosmos-db.md), [Azure Database for PostgreSQL](../../technologies/microsoft/azure-database-for-postgresql.md), [Cosmos DB in Microsoft Fabric](../../technologies/microsoft/fabric-cosmos-db.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform Vector Search](../../technologies/google-cloud/gcp-vector-search.md), [AlloyDB for PostgreSQL](../../technologies/google-cloud/gcp-alloydb.md), [BigQuery vector search](../../technologies/google-cloud/gcp-bigquery-vector-search.md), [Firestore](../../technologies/google-cloud/gcp-firestore.md), [Google Cloud Agent Search](../../technologies/google-cloud/gcp-agent-search.md), [Memorystore](../../technologies/google-cloud/gcp-memorystore.md), [Spanner](../../technologies/google-cloud/gcp-spanner.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | Cortex Search | [Snowflake Cortex Search](../../technologies/snowflake/snowflake-cortex-search.md) |
| [Databricks](../../platforms/platform-databricks.md) | AI Search | [Databricks AI Search](../../technologies/databricks/databricks-ai-search.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | Vector similarity index | [ClickHouse vector similarity indexes](../../technologies/clickhouse/clickhouse-vector-search.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [MySQL HeatWave AutoML and HeatWave GenAI](../../technologies/oracle/oracle-heatwave-automl-genai.md), [Oracle AI Vector Search](../../technologies/oracle/oracle-ai-vector-search.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP HANA Cloud vector engine](../../technologies/sap/sap-hana-cloud-vector-engine.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Enterprise Vector Store](../../technologies/teradata/teradata-enterprise-vector-store.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM Astra DB (DataStax)](../../technologies/ibm/ibm-astra-db.md), [IBM Db2](../../technologies/ibm/ibm-db2.md), [OpenSearch and OpenRAG in IBM watsonx.data](../../technologies/ibm/ibm-watsonx-data-opensearch-openrag.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Lance](../../technologies/open-source/lance.md), [Milvus](../../technologies/open-source/milvus.md), [OpenSearch](../../technologies/open-source/opensearch.md), [pgvector](../../technologies/open-source/pgvector.md), [Qdrant](../../technologies/open-source/qdrant.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Elastic Cloud](../../technologies/independent/elastic-cloud.md), [MongoDB Atlas](../../technologies/independent/mongodb-atlas.md), [Neo4j Aura](../../technologies/independent/neo4j-aura.md), [Pinecone](../../technologies/independent/pinecone.md), [Redis Cloud](../../technologies/independent/redis-cloud.md), [Weaviate Cloud](../../technologies/independent/weaviate-cloud.md) |

Narrower capabilities are realised by a further 20 technologies; see their pages.
