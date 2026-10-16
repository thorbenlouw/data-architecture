---
type: Technology
id: fabric-onelake
title: OneLake
description: A single logical data lake per Fabric tenant, built on ADLS Gen2, in which every Fabric item stores its data, with tables held as Delta Parquet.
platform: platform-microsoft
kind: managed-service
availability: ga
realises:
- object-storage
- decoupled-storage-compute
- engine-interoperability
- open-table-formats
- object-file-access
resource: https://learn.microsoft.com/en-us/fabric/onelake/onelake-overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Exposed through ADLS Gen2-compatible APIs and the OneLake file explorer, so external engines (Azure Databricks, Snowflake, Spark) can read and write it. Storage is billed separately from capacity compute. Organised by workspace and item rather than by storage account.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Object storage](../../capabilities/storage/object-storage.md) (Storage and table management) (primary): Store any volume of files cheaply and durably as the foundation of a data lake or lakehouse.
- [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) (Query and compute): Scale storage and compute independently and let several compute clusters work on the same data.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.
- [Open table formats](../../capabilities/storage/open-table-formats.md) (Storage and table management): Manage collections of files as transactional tables with a defined schema, history and metadata.
- [File-system access to object storage](../../capabilities/storage/object-file-access.md) (Storage and table management): Mount object storage as a file system so file-based tools, ML jobs and agents can work on lake data without copies.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** OneLake

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3](../aws/aws-s3.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Storage](../google-cloud/gcp-cloud-storage.md) | [File-system access to object storage](../../capabilities/storage/object-file-access.md), [Object storage](../../capabilities/storage/object-storage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake stages and directory tables](../snowflake/snowflake-stages-directory-tables.md), [pg_lake](../snowflake/snowflake-pg-lake.md) (preview) | [Object storage](../../capabilities/storage/object-storage.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Apache Ozone in Cloudera](../cloudera/cloudera-ozone.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [Object storage](../../capabilities/storage/object-storage.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud, data lake](../sap/sap-hana-cloud-data-lake.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Object storage](../../capabilities/storage/object-storage.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data](../ibm/ibm-watsonx-data.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Hadoop (HDFS and YARN)](../open-source/apache-hadoop.md) | [Object storage](../../capabilities/storage/object-storage.md) |
