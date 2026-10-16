---
type: Technology
id: aws-bedrock-data-automation
title: Amazon Bedrock Data Automation
description: Generative AI service that turns documents, images, audio and video into structured fields, summaries and classifications through one API.
aliases: [BDA]
platform: platform-aws
kind: feature
availability: ga
realises: [document-processing, unstructured-ingestion, audio-video-processing]
resource: https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Blueprints define the output schema per document type; confidence scores and visual grounding help review. Can act as the parser for Bedrock Knowledge Bases. Overlaps with Textract for simpler OCR and form extraction.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Document processing](../../capabilities/processing/document-processing.md) (Processing and transformation) (primary): Extract text, tables and fields from documents such as PDFs, scans and images.
- [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) (Ingestion and integration): Bring documents, images, audio and other unstructured content into the platform together with their metadata.
- [Audio and video processing](../../capabilities/specialised-data/audio-video-processing.md) (Specialised data types): Transcribe and extract content from audio and video at scale for analysis and retrieval.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon Bedrock

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Content Understanding in Foundry Tools](../microsoft/azure-content-understanding.md), [Azure Document Intelligence in Foundry Tools](../microsoft/azure-document-intelligence.md) | [Audio and video processing](../../capabilities/specialised-data/audio-video-processing.md), [Document processing](../../capabilities/processing/document-processing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Document AI](../google-cloud/gcp-document-ai.md) | [Document processing](../../capabilities/processing/document-processing.md), [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Functions for documents (AI_PARSE_DOCUMENT, AI_EXTRACT)](../snowflake/snowflake-cortex-document-functions.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks ai_parse_document](../databricks/databricks-ai-parse-document.md) | [Document processing](../../capabilities/processing/document-processing.md), [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) |
| [IBM](../../platforms/platform-ibm.md) | [OpenSearch and OpenRAG in IBM watsonx.data](../ibm/ibm-watsonx-data-opensearch-openrag.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir media sets and AIP Document Intelligence](../palantir/palantir-media-sets.md) | [Audio and video processing](../../capabilities/specialised-data/audio-video-processing.md), [Document processing](../../capabilities/processing/document-processing.md), [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Docling](../open-source/docling.md) | [Document processing](../../capabilities/processing/document-processing.md), [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Unstructured.io](../independent/unstructured.md), [LlamaParse](../independent/llamaparse.md), [MuleSoft Anypoint Platform](../independent/mulesoft-anypoint-platform.md) | [Document processing](../../capabilities/processing/document-processing.md), [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) |
