---
type: Technology
id: gcp-bigquery-object-tables
title: BigQuery object tables and ObjectRef
description: Exposes files in Cloud Storage as rows of metadata (object tables) or as ObjectRef values inside ordinary tables so images, documents and audio can be governed and processed with SQL.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [unstructured-data, unstructured-ingestion]
resource: https://docs.cloud.google.com/bigquery/docs/object-table-introduction
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ObjectRef functions went GA in March 2026 and let multimodal tables mix structured columns with object references passed to AI functions. Access uses connections, so fine-grained security is applied without granting bucket access.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) (Specialised data types) (primary): Store, catalogue, govern and process documents, images, audio and video alongside structured data.
- [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) (Ingestion and integration): Bring documents, images, audio and other unstructured content into the platform together with their metadata.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 Files](../aws/aws-s3-files.md), [Amazon Comprehend](../aws/aws-comprehend.md), [Amazon S3 Metadata](../aws/aws-s3-metadata.md) | [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake stages and directory tables](../snowflake/snowflake-stages-directory-tables.md) | [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md), [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog volumes](../databricks/databricks-volumes.md) | [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md), [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Unstructured Data Governance](../informatica/informatica-unstructured-data-governance.md) (preview) | [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir media sets and AIP Document Intelligence](../palantir/palantir-media-sets.md) | [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md), [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Unity Catalog (open source)](../open-source/unity-catalog.md) | [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Tonic Textual](../independent/tonic-textual.md), [Anomalo](../independent/anomalo.md) | [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
