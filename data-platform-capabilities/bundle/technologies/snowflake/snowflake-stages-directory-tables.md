---
type: Technology
id: snowflake-stages-directory-tables
title: Snowflake stages and directory tables
description: Internal and external stages hold files in object storage, and directory tables catalogue the staged files with metadata so unstructured content can be listed, governed and processed with SQL.
platform: platform-snowflake
kind: feature
availability: ga
realises: [object-storage, unstructured-data, unstructured-ingestion]
resource: https://docs.snowflake.com/en/user-guide/data-load-dirtables
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The FILE data type and scoped or pre-signed URLs let functions such as AI_PARSE_DOCUMENT and AI_TRANSCRIBE work on staged files. Directory tables can refresh automatically from cloud event notifications.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Object storage](../../capabilities/storage/object-storage.md) (Storage and table management) (primary): Store any volume of files cheaply and durably as the foundation of a data lake or lakehouse.
- [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) (Specialised data types): Store, catalogue, govern and process documents, images, audio and video alongside structured data.
- [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) (Ingestion and integration): Bring documents, images, audio and other unstructured content into the platform together with their metadata.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3](../aws/aws-s3.md) | [Object storage](../../capabilities/storage/object-storage.md), [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Lake Storage](../microsoft/azure-data-lake-storage.md), [OneLake](../microsoft/fabric-onelake.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Storage](../google-cloud/gcp-cloud-storage.md), [BigQuery object tables and ObjectRef](../google-cloud/gcp-bigquery-object-tables.md) | [Object storage](../../capabilities/storage/object-storage.md), [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md), [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog volumes](../databricks/databricks-volumes.md) | [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md), [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Apache Ozone in Cloudera](../cloudera/cloudera-ozone.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud, data lake](../sap/sap-hana-cloud-data-lake.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir media sets and AIP Document Intelligence](../palantir/palantir-media-sets.md) | [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md), [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Hadoop (HDFS and YARN)](../open-source/apache-hadoop.md) | [Object storage](../../capabilities/storage/object-storage.md) |
