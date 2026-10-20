---
type: Technology
id: snowflake-cortex-document-functions
title: Snowflake Cortex AI Functions for documents (AI_PARSE_DOCUMENT, AI_EXTRACT)
description: AI_PARSE_DOCUMENT turns PDFs and images into text and layout, and AI_EXTRACT pulls named fields, tables and entities out of documents.
formerly: [Snowflake Document AI]
platform: platform-snowflake
kind: feature
availability: ga
realises: [document-processing, retrieval-pipelines]
resource: https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/overview
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The former Document AI documentation now points to these functions, and AI_EXTRACT does the work that Document AI model builds used to. Fine-tuning arctic-extract models became GA in April 2026. AI_PARSE_DOCUMENT handles up to 2,000 pages.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Document processing](../../capabilities/processing/document-processing.md) (Processing and transformation) (primary): Extract text, tables and fields from documents such as PDFs, scans and images.
- [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) (Generative AI): Parse, chunk, embed and index content, and keep indexes in step as sources change.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake Cortex AI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Textract](../aws/aws-textract.md), [Amazon Bedrock Data Automation](../aws/aws-bedrock-data-automation.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Document Intelligence in Foundry Tools](../microsoft/azure-document-intelligence.md), [Azure Content Understanding in Foundry Tools](../microsoft/azure-content-understanding.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Document AI](../google-cloud/gcp-document-ai.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks ai_parse_document](../databricks/databricks-ai-parse-document.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [IBM](../../platforms/platform-ibm.md) | [OpenSearch and OpenRAG in IBM watsonx.data](../ibm/ibm-watsonx-data-opensearch-openrag.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir media sets and AIP Document Intelligence](../palantir/palantir-media-sets.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Visual Text Analytics](../sas/sas-visual-text-analytics.md), [SAS Retrieval Agent Manager](../sas/sas-retrieval-agent-manager.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Knowledge Banks](../dataiku/dataiku-knowledge-banks.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Docling](../open-source/docling.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [LlamaParse](../independent/llamaparse.md), [Unstructured.io](../independent/unstructured.md), [MuleSoft Anypoint Platform](../independent/mulesoft-anypoint-platform.md) | [Document processing](../../capabilities/processing/document-processing.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
