---
type: Capability
id: unstructured-data
title: Unstructured data management
description: Store, catalogue, govern and process documents, images, audio and video alongside structured data.
aliases: [volumes, object tables]
broader: [specialised-data]
related: [unstructured-ingestion, unstructured-lineage, permission-aware-retrieval, data-classification]
depends_on: [object-storage]
tags: [specialised-data]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Documents, images, audio and video are managed as governed data assets rather than loose files in shared drives. The files sit in object storage, and a table records each one's location, type, size, source, owner, classification and derived content such as extracted text, captions or embeddings. Users can then ask for "all supplier contracts from 2024 that mention a change-of-control clause" by combining metadata filters with extracted content, and apply access controls, retention and lineage as they would for tables.

Most organisational information is unstructured, and generative AI has made it directly usable for search, assistants and model training. The hard parts are scale, duplicate and outdated versions, permissions inherited from document management and collaboration tools, sensitive content buried in free text, and keeping derived content in step when files change. Unstructured ingestion brings files in and document processing extracts their content; this capability covers storing, cataloguing and governing the collection over its whole life.

# Key considerations

- Carry over source permissions and track changes to them, or AI tools will show documents to the wrong people.
- Link derived text and embeddings to the exact file version they came from, and refresh them when files change.
- Scan content for personal and confidential data, not only file names and metadata.
- Duplicate and outdated versions degrade search and AI answers. Plan for detecting them and for retention.

# Questions to ask

- Where do your important documents and media live today, and who controls access to them?
- Is the content for search, analytics, AI assistants or model training?
- What volumes, file types and rates of change must be handled?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Specialised data types](specialised-data.md) |
| Broader | [Specialised data types](specialised-data.md) |
| Narrower | [Audio and video processing](audio-video-processing.md), [Multimodal data formats](../storage/multimodal-data-formats.md), [Unstructured data quality](../data-quality/unstructured-data-quality.md) |
| Related | [Generative AI](../generative-ai/generative-ai.md), [AI functions in SQL](../processing/ai-functions.md), [Data classification](../governance/data-classification.md), [Data labelling](../machine-learning/data-labelling.md), [Document and unstructured lineage](../metadata/unstructured-lineage.md), [Document processing](../processing/document-processing.md), [File-system access to object storage](../storage/object-file-access.md), [Permission-aware retrieval](../generative-ai/permission-aware-retrieval.md), [Product information management](../master-data/product-information-management.md), [Unstructured data ingestion](../ingestion-integration/unstructured-ingestion.md) |
| Depends on | [Object storage](../storage/object-storage.md) |

# Where it appears

- **Patterns:** [Data lake](../../patterns/data-lake.md)
- **Maturity tracks:** [Specialised data](../../maturity/track-specialised-data.md) (from level 3, Defined)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Document and Content Management

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Comprehend](../../technologies/aws/aws-comprehend.md), [Amazon S3](../../technologies/aws/aws-s3.md), [Amazon S3 Files](../../technologies/aws/aws-s3-files.md), [Amazon S3 Metadata](../../technologies/aws/aws-s3-metadata.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery object tables and ObjectRef](../../technologies/google-cloud/gcp-bigquery-object-tables.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake stages and directory tables](../../technologies/snowflake/snowflake-stages-directory-tables.md) |
| [Databricks](../../platforms/platform-databricks.md) | Unity Catalog volumes | [Unity Catalog volumes](../../technologies/databricks/databricks-volumes.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Unstructured Data Governance](../../technologies/informatica/informatica-unstructured-data-governance.md) (preview) |
| [Palantir](../../platforms/platform-palantir.md) | Media sets | [Palantir media sets and AIP Document Intelligence](../../technologies/palantir/palantir-media-sets.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Unity Catalog (open source)](../../technologies/open-source/unity-catalog.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Anomalo](../../technologies/independent/anomalo.md), [Tonic Textual](../../technologies/independent/tonic-textual.md) |

Narrower capabilities are realised by a further 10 technologies; see their pages.
