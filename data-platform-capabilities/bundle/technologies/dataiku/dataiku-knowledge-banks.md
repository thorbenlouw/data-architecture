---
type: Technology
id: dataiku-knowledge-banks
title: Dataiku Knowledge Banks
description: Retrieval stores built by recipes that extract text and fields from documents, split and embed them, and index them for retrieval-augmented generation and agents.
aliases: [Embed documents recipe, Extract Content recipe]
platform: platform-dataiku
kind: feature
availability: ga
realises: [retrieval-pipelines, embedding-generation, document-processing]
resource: https://doc.dataiku.com/dss/latest/generative-ai/knowledge/index.html
tags: [dataiku]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

Can use built-in vector stores or, as unmanaged knowledge banks, existing indexes in services such as Azure AI Search, Elasticsearch, OpenSearch, Pinecone, pgvector, Vertex Vector Search, Snowflake Cortex Search and Databricks AI Search. Retrieval supports model-based reranking and document-level security. The Extract Content recipe, added in version 14.3, pulls text and, since 14.5, structured fields from PDFs and other documents.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) (Generative AI) (primary): Parse, chunk, embed and index content, and keep indexes in step as sources change.
- [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) (Generative AI): Turn text, images or other content into vector embeddings for search and retrieval.
- [Document processing](../../capabilities/processing/document-processing.md) (Processing and transformation): Extract text, tables and fields from documents such as PDFs, scans and images.

**Platform:** [Dataiku](../../platforms/platform-dataiku.md)  
**Availability:** ga  
**Product family:** Dataiku Platform for AI Success, Dataiku LLM Mesh

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock Knowledge Bases](../aws/aws-bedrock-knowledge-bases.md) | [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure AI Search](../microsoft/azure-ai-search.md), [Foundry IQ](../microsoft/azure-foundry-iq.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery vector search](../google-cloud/gcp-bigquery-vector-search.md), [Google Cloud Document AI](../google-cloud/gcp-document-ai.md), [Agent Platform RAG Engine](../google-cloud/gcp-rag-engine.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Document processing](../../capabilities/processing/document-processing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Functions for documents (AI_PARSE_DOCUMENT, AI_EXTRACT)](../snowflake/snowflake-cortex-document-functions.md), [Snowflake Cortex Search](../snowflake/snowflake-cortex-search.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks ai_parse_document](../databricks/databricks-ai-parse-document.md), [Databricks AI Search](../databricks/databricks-ai-search.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Studios (RAG, Fine Tuning and Synthetic Data Studios)](../cloudera/cloudera-ai-studios.md) (preview) | [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise Vector Store](../teradata/teradata-enterprise-vector-store.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [IBM](../../platforms/platform-ibm.md) | [OpenSearch and OpenRAG in IBM watsonx.data](../ibm/ibm-watsonx-data-opensearch-openrag.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Retrieval Agent Manager](../sas/sas-retrieval-agent-manager.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Docling](../open-source/docling.md), [LangChain](../open-source/langchain.md), [LlamaIndex](../open-source/llamaindex.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Unstructured.io](../independent/unstructured.md), [LlamaParse](../independent/llamaparse.md) | [Document processing](../../capabilities/processing/document-processing.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
