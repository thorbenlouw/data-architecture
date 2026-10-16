---
type: Technology
id: palantir-media-sets
title: Palantir media sets and AIP Document Intelligence
description: Foundry storage and pipelines for unstructured files such as PDFs, images, audio and video, with AIP Document Intelligence strategies for extracting text, tables and fields.
platform: platform-palantir
kind: feature
availability: ga
realises: [unstructured-data, unstructured-ingestion, document-processing, audio-video-processing]
resource: https://www.palantir.com/docs/foundry/aip/overview/
tags: [palantir]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Media sets can be synced from sources and processed in Pipeline Builder or Python transforms; extraction strategies can be deployed to transforms and functions.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) (Specialised data types) (primary): Store, catalogue, govern and process documents, images, audio and video alongside structured data.
- [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) (Ingestion and integration): Bring documents, images, audio and other unstructured content into the platform together with their metadata.
- [Document processing](../../capabilities/processing/document-processing.md) (Processing and transformation): Extract text, tables and fields from documents such as PDFs, scans and images.
- [Audio and video processing](../../capabilities/specialised-data/audio-video-processing.md) (Specialised data types): Transcribe and extract content from audio and video at scale for analysis and retrieval.

**Platform:** [Palantir](../../platforms/platform-palantir.md)  
**Availability:** ga  
**Product family:** Palantir Foundry, Palantir AIP

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock Data Automation](../aws/aws-bedrock-data-automation.md), [Amazon S3 Files](../aws/aws-s3-files.md), [Amazon Comprehend](../aws/aws-comprehend.md) | [Audio and video processing](../../capabilities/specialised-data/audio-video-processing.md), [Document processing](../../capabilities/processing/document-processing.md), [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md), [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Content Understanding in Foundry Tools](../microsoft/azure-content-understanding.md) | [Audio and video processing](../../capabilities/specialised-data/audio-video-processing.md), [Document processing](../../capabilities/processing/document-processing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery object tables and ObjectRef](../google-cloud/gcp-bigquery-object-tables.md), [Google Cloud Document AI](../google-cloud/gcp-document-ai.md) | [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md), [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md), [Document processing](../../capabilities/processing/document-processing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake stages and directory tables](../snowflake/snowflake-stages-directory-tables.md) | [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md), [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog volumes](../databricks/databricks-volumes.md), [Databricks ai_parse_document](../databricks/databricks-ai-parse-document.md) | [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md), [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md), [Document processing](../../capabilities/processing/document-processing.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Unstructured Data Governance](../informatica/informatica-unstructured-data-governance.md) (preview) | [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Unity Catalog (open source)](../open-source/unity-catalog.md), [Docling](../open-source/docling.md) | [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md), [Document processing](../../capabilities/processing/document-processing.md), [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Tonic Textual](../independent/tonic-textual.md), [Anomalo](../independent/anomalo.md) | [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
