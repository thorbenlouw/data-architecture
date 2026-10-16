---
type: Capability
id: document-processing
title: Document processing
description: Extract text, tables and fields from documents such as PDFs, scans and images.
aliases: [OCR, intelligent document processing, document parsing]
broader: [processing, specialised-data]
related: [unstructured-ingestion, unstructured-data, retrieval-pipelines, ai-functions, data-labelling]
tags: [processing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Several steps turn files such as PDFs, scanned forms, invoices and photographs into text and structured fields. Optical character recognition (OCR) reads text from images; layout analysis finds headings, paragraphs, columns and reading order; table extraction rebuilds rows and cells; field extraction maps content to a schema, for example invoice number, supplier, line items and total. Vision-language models increasingly work alongside, or replace, extraction based on fixed templates.

Much business information sits in documents: claims, contracts, delivery notes, clinical letters. Extracted content feeds analytics, process automation and retrieval-augmented generation, where faithful parsing of tables and layout has a large effect on answer quality. Templates are accurate for fixed forms but break when layouts change; model-based extraction copes with variety but needs confidence scores and human review of doubtful fields. AI functions work on text already in a table, and unstructured data management stores and governs the files; document processing is the step that gets content out of them.

# Key considerations

- Link every extracted field to its page and position in the source so people can check it.
- Send low-confidence fields to human review, and use the corrections to measure and improve accuracy.
- Handwriting, poor scans, multi-column layouts and complex tables are where accuracy drops. Test on your own documents.
- Documents often contain personal data. Classify and protect the extracted output as carefully as the originals.

# Questions to ask

- Which document types matter most, and how varied are their layouts?
- What accuracy is needed for each field, and who reviews exceptions?
- Is the output for analytics, process automation, retrieval or all three?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Processing and transformation](processing.md) |
| Broader | [Processing and transformation](processing.md), [Specialised data types](../specialised-data/specialised-data.md) |
| Related | [AI functions in SQL](ai-functions.md), [Audio and video processing](../specialised-data/audio-video-processing.md), [Data labelling](../machine-learning/data-labelling.md), [Retrieval pipelines](../generative-ai/retrieval-pipelines.md), [Semi-structured data](../storage/semi-structured-data.md), [Unstructured data ingestion](../ingestion-integration/unstructured-ingestion.md), [Unstructured data management](../specialised-data/unstructured-data.md) |

# Where it appears

- **Use cases:** [Agentic process automation](../../use-cases/usecase-agentic-automation.md) (benefits from) · [Document data extraction](../../use-cases/usecase-document-extraction.md) (requires, level 3) · [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (requires, level 3)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md)
- **Maturity tracks:** [Specialised data](../../maturity/track-specialised-data.md) (from level 4, Measured) · [Transformation engineering](../../maturity/track-transformation.md) (from level 4, Measured)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Document and Content Management

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Amazon Textract; Bedrock Data Automation | [Amazon Bedrock Data Automation](../../technologies/aws/aws-bedrock-data-automation.md), [Amazon Textract](../../technologies/aws/aws-textract.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Content Understanding in Foundry Tools](../../technologies/microsoft/azure-content-understanding.md), [Azure Document Intelligence in Foundry Tools](../../technologies/microsoft/azure-document-intelligence.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Document AI](../../technologies/google-cloud/gcp-document-ai.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | AI_PARSE_DOCUMENT and AI_EXTRACT (formerly Document AI) | [Snowflake Cortex AI Functions for documents (AI_PARSE_DOCUMENT, AI_EXTRACT)](../../technologies/snowflake/snowflake-cortex-document-functions.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks ai_parse_document](../../technologies/databricks/databricks-ai-parse-document.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [OpenSearch and OpenRAG in IBM watsonx.data](../../technologies/ibm/ibm-watsonx-data-opensearch-openrag.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir media sets and AIP Document Intelligence](../../technologies/palantir/palantir-media-sets.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Docling](../../technologies/open-source/docling.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [LlamaParse](../../technologies/independent/llamaparse.md), [MuleSoft Anypoint Platform](../../technologies/independent/mulesoft-anypoint-platform.md), [Unstructured.io](../../technologies/independent/unstructured.md) |
