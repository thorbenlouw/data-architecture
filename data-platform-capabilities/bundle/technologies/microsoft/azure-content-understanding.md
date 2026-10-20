---
type: Technology
id: azure-content-understanding
title: Azure Content Understanding in Foundry Tools
description: Uses generative models to extract structured fields and descriptions from documents, images, audio and video through configurable analysers.
formerly: [Azure AI Content Understanding]
platform: platform-microsoft
kind: managed-service
availability: ga
realises: [document-processing, audio-video-processing]
resource: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

API version 2025-11-01 is GA; 2026-06-01-preview adds agentic mode and more. Overlaps with Document Intelligence, with a migration path from it.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Document processing](../../capabilities/processing/document-processing.md) (Processing and transformation) (primary): Extract text, tables and fields from documents such as PDFs, scans and images.
- [Audio and video processing](../../capabilities/specialised-data/audio-video-processing.md) (Specialised data types): Transcribe and extract content from audio and video at scale for analysis and retrieval.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Foundry Tools

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock Data Automation](../aws/aws-bedrock-data-automation.md), [Amazon Textract](../aws/aws-textract.md) | [Audio and video processing](../../capabilities/specialised-data/audio-video-processing.md), [Document processing](../../capabilities/processing/document-processing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Document AI](../google-cloud/gcp-document-ai.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Functions for documents (AI_PARSE_DOCUMENT, AI_EXTRACT)](../snowflake/snowflake-cortex-document-functions.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks ai_parse_document](../databricks/databricks-ai-parse-document.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [IBM](../../platforms/platform-ibm.md) | [OpenSearch and OpenRAG in IBM watsonx.data](../ibm/ibm-watsonx-data-opensearch-openrag.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir media sets and AIP Document Intelligence](../palantir/palantir-media-sets.md) | [Audio and video processing](../../capabilities/specialised-data/audio-video-processing.md), [Document processing](../../capabilities/processing/document-processing.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Visual Text Analytics](../sas/sas-visual-text-analytics.md), [SAS Retrieval Agent Manager](../sas/sas-retrieval-agent-manager.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Knowledge Banks](../dataiku/dataiku-knowledge-banks.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Docling](../open-source/docling.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [LlamaParse](../independent/llamaparse.md), [Unstructured.io](../independent/unstructured.md), [MuleSoft Anypoint Platform](../independent/mulesoft-anypoint-platform.md) | [Document processing](../../capabilities/processing/document-processing.md) |
