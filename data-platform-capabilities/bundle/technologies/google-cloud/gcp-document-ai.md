---
type: Technology
id: gcp-document-ai
title: Google Cloud Document AI
description: Document processing service with OCR, form, layout and custom extraction and classification processors for PDFs and images.
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [document-processing, retrieval-pipelines, unstructured-ingestion]
resource: https://docs.cloud.google.com/document-ai/docs/overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The Layout Parser chunks documents for RAG and is used by RAG Engine and Agent Search. Custom extractors use generative AI and can be trained with few examples in Document AI Workbench.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Document processing](../../capabilities/processing/document-processing.md) (Processing and transformation) (primary): Extract text, tables and fields from documents such as PDFs, scans and images.
- [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) (Generative AI): Parse, chunk, embed and index content, and keep indexes in step as sources change.
- [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) (Ingestion and integration): Bring documents, images, audio and other unstructured content into the platform together with their metadata.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock Data Automation](../aws/aws-bedrock-data-automation.md), [Amazon Textract](../aws/aws-textract.md) | [Document processing](../../capabilities/processing/document-processing.md), [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Document Intelligence in Foundry Tools](../microsoft/azure-document-intelligence.md), [Azure Content Understanding in Foundry Tools](../microsoft/azure-content-understanding.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Functions for documents (AI_PARSE_DOCUMENT, AI_EXTRACT)](../snowflake/snowflake-cortex-document-functions.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks ai_parse_document](../databricks/databricks-ai-parse-document.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) |
| [IBM](../../platforms/platform-ibm.md) | [OpenSearch and OpenRAG in IBM watsonx.data](../ibm/ibm-watsonx-data-opensearch-openrag.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir media sets and AIP Document Intelligence](../palantir/palantir-media-sets.md) | [Document processing](../../capabilities/processing/document-processing.md), [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Visual Text Analytics](../sas/sas-visual-text-analytics.md), [SAS Retrieval Agent Manager](../sas/sas-retrieval-agent-manager.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Knowledge Banks](../dataiku/dataiku-knowledge-banks.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Docling](../open-source/docling.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Unstructured.io](../independent/unstructured.md), [LlamaParse](../independent/llamaparse.md), [MuleSoft Anypoint Platform](../independent/mulesoft-anypoint-platform.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) |
