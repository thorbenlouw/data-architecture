---
type: Capability
id: retrieval-pipelines
title: Retrieval pipelines
description: Parse, chunk, embed and index content, and keep indexes in step as sources change.
aliases: [chunking, indexing pipelines, RAG ingestion]
broader: [retrieval-augmented-generation]
related:
- document-processing
- unstructured-ingestion
- incremental-processing
- change-feeds
- unstructured-lineage
depends_on: [embedding-generation, vector-search]
tags: [generative-ai]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A retrieval pipeline turns source content into a searchable index and keeps it current. It connects to sources, extracts text and structure from files such as PDFs, slides and spreadsheets, splits the text into chunks, attaches metadata such as title, owner, date and access list, embeds each chunk and writes it to the index. On later runs it processes new and changed documents and removes deleted ones. For example, a nightly job reads contracts changed that day, splits them by clause, embeds each clause and removes the vectors of contracts that were withdrawn.

The index sets the upper limit on answer quality, so pipeline choices have large effects. Chunking can use fixed sizes with overlap, follow document structure such as headings or clauses, split where the topic changes, or prepend a short document summary to each chunk. Platforms increasingly offer managed syncing from a table or folder to an index; custom pipelines give more control. Document processing covers extraction alone, and retrieval-augmented generation covers what happens at question time.

# Key considerations

- Deletions and permission changes must reach the index quickly. A pipeline that only adds content keeps serving withdrawn documents.
- Parsing quality for tables, scanned pages and diagrams varies widely between tools. Test on your most difficult documents, not the cleanest.
- Keep a link from every chunk to its source document and version, so answers can be traced and content reprocessed selectively.
- Chunk size trades precision against context. Tune it with an evaluation set rather than accepting a default.
- Detect changes with content hashes or change feeds so each run re-embeds only what changed.

# Questions to ask

- Which sources and file types must be indexed, and how inconsistent are they?
- How quickly must changes and deletions show up in answers?
- Can access lists be read from the source systems and carried into the index?
- Who maintains the pipeline when a source system changes its structure or API?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Generative AI](generative-ai.md) |
| Broader | [Retrieval-augmented generation](retrieval-augmented-generation.md) |
| Related | [Change feeds](../serving/change-feeds.md), [Document and unstructured lineage](../metadata/unstructured-lineage.md), [Document processing](../processing/document-processing.md), [Embedding generation](embedding-generation.md), [Incremental processing](../processing/incremental-processing.md), [Unstructured data ingestion](../ingestion-integration/unstructured-ingestion.md), [Unstructured data quality](../data-quality/unstructured-data-quality.md) |
| Depends on | [Embedding generation](embedding-generation.md), [Vector search](vector-search.md) |
| Needed by | [Permission-aware retrieval](permission-aware-retrieval.md) |

# Where it appears

- **Use cases:** [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (requires, level 3)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md)
- **Maturity tracks:** [Generative AI](../../maturity/track-genai.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Bedrock Knowledge Bases](../../technologies/aws/aws-bedrock-knowledge-bases.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure AI Search](../../technologies/microsoft/azure-ai-search.md), [Foundry IQ](../../technologies/microsoft/azure-foundry-iq.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform RAG Engine](../../technologies/google-cloud/gcp-rag-engine.md), [BigQuery vector search](../../technologies/google-cloud/gcp-bigquery-vector-search.md), [Google Cloud Agent Search](../../technologies/google-cloud/gcp-agent-search.md), [Google Cloud Document AI](../../technologies/google-cloud/gcp-document-ai.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Cortex AI Functions for documents (AI_PARSE_DOCUMENT, AI_EXTRACT)](../../technologies/snowflake/snowflake-cortex-document-functions.md), [Snowflake Cortex Search](../../technologies/snowflake/snowflake-cortex-search.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks AI Search](../../technologies/databricks/databricks-ai-search.md), [Databricks ai_parse_document](../../technologies/databricks/databricks-ai-parse-document.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera AI Studios (RAG, Fine Tuning and Synthetic Data Studios)](../../technologies/cloudera/cloudera-ai-studios.md) (preview) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Enterprise Vector Store](../../technologies/teradata/teradata-enterprise-vector-store.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [OpenSearch and OpenRAG in IBM watsonx.data](../../technologies/ibm/ibm-watsonx-data-opensearch-openrag.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Docling](../../technologies/open-source/docling.md), [LangChain](../../technologies/open-source/langchain.md), [LlamaIndex](../../technologies/open-source/llamaindex.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [LlamaParse](../../technologies/independent/llamaparse.md), [Unstructured.io](../../technologies/independent/unstructured.md) |
