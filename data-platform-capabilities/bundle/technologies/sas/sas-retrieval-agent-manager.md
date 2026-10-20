---
type: Technology
id: sas-retrieval-agent-manager
title: SAS Retrieval Agent Manager
description: No-code retrieval-augmented generation product that ingests documents, tests and selects retrieval configurations, and serves cited answers through an API, chatbot or retrieval agents.
aliases: [RAM, SAS RAM]
platform: platform-sas
kind: software
availability: ga
realises: [retrieval-pipelines, genai-evaluation, document-processing, permission-aware-retrieval]
resource: https://www.sas.com/en_us/software/retrieval-agent-manager.html
tags: [sas]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:10:17Z'}
---

Announced in September 2025 and sold as a standalone product, with integration into SAS Viya planned. It reads PDF, Office, HTML, email and scanned files with OCR (legacy .doc and .ppt files are not supported), stores vectors in PGVector or Weaviate, and calls models through OpenAI, Azure OpenAI, Amazon Bedrock or Ollama. Role-based access applies from source documents to agents, and it runs in public or private clouds, on premises or air-gapped. Retrieval agents can call tools through the Model Context Protocol.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) (Generative AI) (primary): Parse, chunk, embed and index content, and keep indexes in step as sources change.
- [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) (Generative AI): Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges.
- [Document processing](../../capabilities/processing/document-processing.md) (Processing and transformation): Extract text, tables and fields from documents such as PDFs, scans and images.
- [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md) (Generative AI): Filter retrieved content by each user's permissions in the source systems so AI answers never reveal what the user could not open.

**Platform:** [SAS](../../platforms/platform-sas.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock Knowledge Bases](../aws/aws-bedrock-knowledge-bases.md) | [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Foundry IQ](../microsoft/azure-foundry-iq.md), [Azure AI Search](../microsoft/azure-ai-search.md) | [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Document AI](../google-cloud/gcp-document-ai.md), [Google Cloud Agent Search](../google-cloud/gcp-agent-search.md), [Agent Platform RAG Engine](../google-cloud/gcp-rag-engine.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Functions for documents (AI_PARSE_DOCUMENT, AI_EXTRACT)](../snowflake/snowflake-cortex-document-functions.md), [Snowflake Cortex Search](../snowflake/snowflake-cortex-search.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks ai_parse_document](../databricks/databricks-ai-parse-document.md), [Databricks AI Search](../databricks/databricks-ai-search.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Studios (RAG, Fine Tuning and Synthetic Data Studios)](../cloudera/cloudera-ai-studios.md) (preview) | [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise Vector Store](../teradata/teradata-enterprise-vector-store.md) | [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [IBM](../../platforms/platform-ibm.md) | [OpenSearch and OpenRAG in IBM watsonx.data](../ibm/ibm-watsonx-data-opensearch-openrag.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Knowledge Banks](../dataiku/dataiku-knowledge-banks.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Docling](../open-source/docling.md), [LangChain](../open-source/langchain.md), [LlamaIndex](../open-source/llamaindex.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [LlamaParse](../independent/llamaparse.md), [Unstructured.io](../independent/unstructured.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
