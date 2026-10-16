---
type: Capability
id: full-text-search
title: Full-text search
description: Index text for full-text search, relevance ranking and fast filtering.
aliases: [search engine, inverted index]
broader: [specialised-data]
related:
- vector-search
- retrieval-augmented-generation
- observability-analytics
- permission-aware-retrieval
- data-skipping-indexes
tags: [specialised-data]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Full-text search engines build an inverted index: for every word, a list of the documents that contain it. Text is analysed on the way in: split into words, lower-cased, reduced to word stems so "running" matches "run", and sometimes expanded with synonyms. Queries return matches ranked by relevance, typically scored with BM25, along with highlighted snippets, facets that count results by category, and fast filters on structured fields. Apache Lucene underlies many search engines.

Search serves product catalogues, support knowledge bases, log exploration and document discovery, where people type words rather than write queries. A SQL `LIKE` filter scans every row and cannot rank results, so it does not scale for this. Many systems now combine keyword and vector search, called hybrid search, because keywords handle exact terms, codes and names well while embeddings capture meaning. Search can run in a dedicated engine or as search indexes inside the analytical platform.

# Key considerations

- Relevance needs tuning and testing with real queries. Decide how it will be measured before launch.
- Text analysis differs by language. Check support for the languages you need and for product codes and names.
- Indexes update after a delay. Decide how soon a source change must appear in results.
- Search indexes must enforce the same access rules as their sources. Document-level security is often overlooked.

# Questions to ask

- Who searches, for what, and how will they judge whether results are good?
- How many documents or records, in which languages, and how often do they change?
- Do you need keyword search, semantic search or both?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Specialised data types](specialised-data.md) |
| Broader | [Specialised data types](specialised-data.md) |
| Related | [Indexes and data skipping](../compute/data-skipping-indexes.md), [Observability data analytics](observability-analytics.md), [Permission-aware retrieval](../generative-ai/permission-aware-retrieval.md), [Retrieval-augmented generation](../generative-ai/retrieval-augmented-generation.md), [Vector search](../generative-ai/vector-search.md) |

# Where it appears

- **Use cases:** [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (benefits from) · [Security and log analytics](../../use-cases/usecase-security-log-analytics.md) (requires, level 3)
- **Patterns:** [Separate read models](../../patterns/cqrs-read-models.md)
- **Maturity tracks:** [Specialised data](../../maturity/track-specialised-data.md) (from level 2, Managed)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Document and Content Management

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon OpenSearch Service](../../technologies/aws/aws-opensearch-service.md), [Amazon Kendra](../../technologies/aws/aws-kendra.md) (deprecated) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure AI Search](../../technologies/microsoft/azure-ai-search.md), [Azure Cosmos DB](../../technologies/microsoft/azure-cosmos-db.md), [Cosmos DB in Microsoft Fabric](../../technologies/microsoft/fabric-cosmos-db.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery search indexes](../../technologies/google-cloud/gcp-bigquery-search-indexes.md), [Google Cloud Agent Search](../../technologies/google-cloud/gcp-agent-search.md), [Spanner](../../technologies/google-cloud/gcp-spanner.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Cortex Search](../../technologies/snowflake/snowflake-cortex-search.md), [Snowflake Search Optimization Service](../../technologies/snowflake/snowflake-search-optimization-service.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks AI Search](../../technologies/databricks/databricks-ai-search.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | Text index | [ClickHouse text indexes (full-text search)](../../technologies/clickhouse/clickhouse-text-indexes.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle AI Database 26ai](../../technologies/oracle/oracle-ai-database-26ai.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [OpenSearch and OpenRAG in IBM watsonx.data](../../technologies/ibm/ibm-watsonx-data-opensearch-openrag.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Milvus](../../technologies/open-source/milvus.md), [OpenSearch](../../technologies/open-source/opensearch.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Elastic Cloud](../../technologies/independent/elastic-cloud.md), [MongoDB Atlas](../../technologies/independent/mongodb-atlas.md), [Pinecone](../../technologies/independent/pinecone.md), [Weaviate Cloud](../../technologies/independent/weaviate-cloud.md) |
