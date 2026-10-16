---
type: Capability
id: unstructured-ingestion
title: Unstructured data ingestion
description: Bring documents, images, audio and other unstructured content into the platform together with their metadata.
aliases: [document ingestion]
broader: [ingestion-integration]
related:
- document-processing
- retrieval-pipelines
- permission-aware-retrieval
- unstructured-lineage
- unstructured-data-quality
depends_on: [object-storage]
tags: [ingestion-integration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Connectors collect files such as PDFs, office documents, emails, images, audio and video from shared drives, document management systems, collaboration tools and object stores. Each file lands with its metadata: source path, author, created and modified times, access permissions and any labels. A connector to a document library might copy new and changed files every hour, record each file's permission list, and note deletions so the copies, and anything derived from them, can be removed.

Retrieval-augmented generation, document processing and model training all start here, and they depend on the metadata as much as the content. Without source permissions, AI answers can expose documents a user could not open; without deletion tracking, indexes keep content that should be gone. Approaches range from periodic full crawls to change notifications from the source. Ingestion brings content in; document processing extracts text and fields, and retrieval pipelines prepare it for search.

# Key considerations

- Capture source permissions and keep them current. Permission changes need to reach the platform as quickly as content changes.
- Track deletions and moves as well as new files, so derived chunks, embeddings and extracts can be removed.
- Deduplicate by content hash. Shared drives often hold many copies of the same document.
- File sizes vary by orders of magnitude. Plan throughput and storage tiers for large media separately from documents.

# Questions to ask

- Which repositories hold the content that matters, and how are permissions managed in each?
- How quickly must changes and deletions in the source show up in search and AI answers?
- Which file types and languages must be handled?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Ingestion and integration](ingestion-integration.md) |
| Broader | [Ingestion and integration](ingestion-integration.md) |
| Related | [Audio and video processing](../specialised-data/audio-video-processing.md), [Document and unstructured lineage](../metadata/unstructured-lineage.md), [Document processing](../processing/document-processing.md), [Permission-aware retrieval](../generative-ai/permission-aware-retrieval.md), [Retrieval pipelines](../generative-ai/retrieval-pipelines.md), [Unstructured data management](../specialised-data/unstructured-data.md), [Unstructured data quality](../data-quality/unstructured-data-quality.md) |
| Depends on | [Object storage](../storage/object-storage.md) |

# Where it appears

- **Use cases:** [Document data extraction](../../use-cases/usecase-document-extraction.md) (requires, level 3) · [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (requires, level 3)
- **Maturity tracks:** [Ingestion and integration](../../maturity/track-ingestion.md) (from level 3, Defined)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Document and Content Management

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Bedrock Data Automation](../../technologies/aws/aws-bedrock-data-automation.md), [Amazon Bedrock Knowledge Bases](../../technologies/aws/aws-bedrock-knowledge-bases.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery object tables and ObjectRef](../../technologies/google-cloud/gcp-bigquery-object-tables.md), [Google Cloud Document AI](../../technologies/google-cloud/gcp-document-ai.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Openflow](../../technologies/snowflake/snowflake-openflow.md), [Snowflake stages and directory tables](../../technologies/snowflake/snowflake-stages-directory-tables.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks ai_parse_document](../../technologies/databricks/databricks-ai-parse-document.md), [Lakeflow Connect](../../technologies/databricks/databricks-lakeflow-connect.md), [Unity Catalog volumes](../../technologies/databricks/databricks-volumes.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.data integration](../../technologies/ibm/ibm-watsonx-data-integration.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir media sets and AIP Document Intelligence](../../technologies/palantir/palantir-media-sets.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache NiFi](../../technologies/open-source/apache-nifi.md), [Docling](../../technologies/open-source/docling.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Unstructured.io](../../technologies/independent/unstructured.md) |
