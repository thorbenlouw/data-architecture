---
type: Technology
id: databricks-volumes
title: Unity Catalog volumes
description: Governed, path-addressable storage for non-tabular files such as documents, images, libraries and landing data. Volumes can be managed or external.
aliases: [UC volumes]
platform: platform-databricks
kind: feature
availability: ga
realises: [unstructured-data, unstructured-ingestion, object-file-access, analytical-sandboxes]
resource: https://docs.databricks.com/aws/en/volumes/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Unity Catalog fully governs managed volumes. Unity Catalog cannot enforce its permissions on direct access to external volume paths. A FILE type for referencing volume files from tables, and per-user "My Files" volumes, are in Beta.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) (Specialised data types) (primary): Store, catalogue, govern and process documents, images, audio and video alongside structured data.
- [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) (Ingestion and integration): Bring documents, images, audio and other unstructured content into the platform together with their metadata.
- [File-system access to object storage](../../capabilities/storage/object-file-access.md) (Storage and table management): Mount object storage as a file system so file-based tools, ML jobs and agents can work on lake data without copies.
- [Analytical sandboxes](../../capabilities/analytics-bi/analytical-sandboxes.md) (Analytics and BI): Give analysts and teams governed spaces on the platform where they can upload files, create tables and try out analyses, with quotas, expiry and the platform's access controls.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Unity Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 Files](../aws/aws-s3-files.md), [Amazon Comprehend](../aws/aws-comprehend.md), [Amazon S3 Metadata](../aws/aws-s3-metadata.md) | [File-system access to object storage](../../capabilities/storage/object-file-access.md), [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery object tables and ObjectRef](../google-cloud/gcp-bigquery-object-tables.md) | [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md), [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake stages and directory tables](../snowflake/snowflake-stages-directory-tables.md) | [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md), [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Unstructured Data Governance](../informatica/informatica-unstructured-data-governance.md) (preview) | [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir media sets and AIP Document Intelligence](../palantir/palantir-media-sets.md) | [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md), [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Unity Catalog (open source)](../open-source/unity-catalog.md) | [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Tonic Textual](../independent/tonic-textual.md), [Anomalo](../independent/anomalo.md) | [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
