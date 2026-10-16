---
type: Technology
id: aws-textract
title: Amazon Textract
description: Extracts printed and handwritten text, tables, form fields and specific document types from scanned documents and images.
platform: platform-aws
kind: managed-service
availability: ga
realises: [document-processing]
resource: https://docs.aws.amazon.com/textract/latest/dg/what-is.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Pretrained APIs for invoices, receipts, identity documents and lending packs; queries pull named values. Bedrock Data Automation covers wider multimodal extraction.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Document processing](../../capabilities/processing/document-processing.md) (Processing and transformation) (primary): Extract text, tables and fields from documents such as PDFs, scans and images.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Document Intelligence in Foundry Tools](../microsoft/azure-document-intelligence.md), [Azure Content Understanding in Foundry Tools](../microsoft/azure-content-understanding.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Document AI](../google-cloud/gcp-document-ai.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Functions for documents (AI_PARSE_DOCUMENT, AI_EXTRACT)](../snowflake/snowflake-cortex-document-functions.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks ai_parse_document](../databricks/databricks-ai-parse-document.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [IBM](../../platforms/platform-ibm.md) | [OpenSearch and OpenRAG in IBM watsonx.data](../ibm/ibm-watsonx-data-opensearch-openrag.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir media sets and AIP Document Intelligence](../palantir/palantir-media-sets.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Docling](../open-source/docling.md) | [Document processing](../../capabilities/processing/document-processing.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [LlamaParse](../independent/llamaparse.md), [Unstructured.io](../independent/unstructured.md), [MuleSoft Anypoint Platform](../independent/mulesoft-anypoint-platform.md) | [Document processing](../../capabilities/processing/document-processing.md) |
