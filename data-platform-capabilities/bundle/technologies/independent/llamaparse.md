---
type: Technology
id: llamaparse
title: LlamaParse
description: Hosted document processing that parses complex documents with vision and language models and offers extraction, splitting, classification and indexing services.
aliases: [LlamaCloud, LlamaExtract]
platform: platform-independent
vendor: LlamaIndex
kind: saas
availability: ga
realises: [document-processing, retrieval-pipelines]
resource: https://www.llamaindex.ai/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

LlamaParse is now the umbrella name for LlamaIndex's hosted document services (Parse, Extract, Split, Classify and Index), which were earlier marketed as LlamaCloud. LiteParse is a separate open-source local parser, and the [LlamaIndex](../open-source/llamaindex.md) framework is open source.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Document processing](../../capabilities/processing/document-processing.md) (Processing and transformation) (primary): Extract text, tables and fields from documents such as PDFs, scans and images.
- [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) (Generative AI): Parse, chunk, embed and index content, and keep indexes in step as sources change.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Textract](../aws/aws-textract.md), [Amazon Bedrock Data Automation](../aws/aws-bedrock-data-automation.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Document Intelligence in Foundry Tools](../microsoft/azure-document-intelligence.md), [Azure Content Understanding in Foundry Tools](../microsoft/azure-content-understanding.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Document AI](../google-cloud/gcp-document-ai.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Functions for documents (AI_PARSE_DOCUMENT, AI_EXTRACT)](../snowflake/snowflake-cortex-document-functions.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks ai_parse_document](../databricks/databricks-ai-parse-document.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [IBM](../../platforms/platform-ibm.md) | [OpenSearch and OpenRAG in IBM watsonx.data](../ibm/ibm-watsonx-data-opensearch-openrag.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir media sets and AIP Document Intelligence](../palantir/palantir-media-sets.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Visual Text Analytics](../sas/sas-visual-text-analytics.md), [SAS Retrieval Agent Manager](../sas/sas-retrieval-agent-manager.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Knowledge Banks](../dataiku/dataiku-knowledge-banks.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Docling](../open-source/docling.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
