---
type: Technology
id: sas-visual-text-analytics
title: SAS Visual Text Analytics
description: Natural language processing application in SAS Viya that parses text, discovers topics, classifies documents, analyses sentiment and extracts information with linguistic rules, machine learning and LLMs.
platform: platform-sas
kind: feature
availability: ga
realises: [document-processing]
resource: https://www.sas.com/en_us/software/visual-text-analytics.html
tags: [sas]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:50:29Z'}
---

Included in SAS Viya Enterprise, with native support for 33 languages. Information is extracted with LITI, a SAS rule language, and classification can use LLMs. Its linguistic models can also prepare text for LLM fine-tuning and retrieval-augmented generation, and screen content for toxicity, bias and private data.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Document processing](../../capabilities/processing/document-processing.md) (Processing and transformation) (primary): Extract text, tables and fields from documents such as PDFs, scans and images.

**Platform:** [SAS](../../platforms/platform-sas.md)  
**Availability:** ga  
**Product family:** SAS Viya

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Textract](../aws/aws-textract.md), [Amazon Bedrock Data Automation](../aws/aws-bedrock-data-automation.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Document Intelligence in Foundry Tools](../microsoft/azure-document-intelligence.md), [Azure Content Understanding in Foundry Tools](../microsoft/azure-content-understanding.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Document AI](../google-cloud/gcp-document-ai.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Functions for documents (AI_PARSE_DOCUMENT, AI_EXTRACT)](../snowflake/snowflake-cortex-document-functions.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks ai_parse_document](../databricks/databricks-ai-parse-document.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [IBM](../../platforms/platform-ibm.md) | [OpenSearch and OpenRAG in IBM watsonx.data](../ibm/ibm-watsonx-data-opensearch-openrag.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir media sets and AIP Document Intelligence](../palantir/palantir-media-sets.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Knowledge Banks](../dataiku/dataiku-knowledge-banks.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Docling](../open-source/docling.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [LlamaParse](../independent/llamaparse.md), [Unstructured.io](../independent/unstructured.md), [MuleSoft Anypoint Platform](../independent/mulesoft-anypoint-platform.md) | [Document processing](../../capabilities/processing/document-processing.md) |
