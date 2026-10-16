---
type: Technology
id: cloudera-ozone
title: Apache Ozone in Cloudera
description: S3-compatible, scale-out object store for on-premises Cloudera clusters, intended to replace HDFS for very large file counts.
aliases: [Apache Ozone]
platform: platform-cloudera
kind: software
availability: ga
realises: [object-storage, decoupled-storage-compute]
resource: https://docs.cloudera.com/
tags: [cloudera]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Supports both S3 and Hadoop filesystem APIs on the same data. Used as the storage layer for on-premises lakehouses where cloud object storage is not available.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Object storage](../../capabilities/storage/object-storage.md) (Storage and table management) (primary): Store any volume of files cheaply and durably as the foundation of a data lake or lakehouse.
- [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) (Query and compute): Scale storage and compute independently and let several compute clusters work on the same data.

**Platform:** [Cloudera](../../platforms/platform-cloudera.md)  
**Availability:** ga  
**Product family:** Cloudera Open Data Lakehouse

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3](../aws/aws-s3.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake](../microsoft/fabric-onelake.md), [Azure Data Lake Storage](../microsoft/azure-data-lake-storage.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [Object storage](../../capabilities/storage/object-storage.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Storage](../google-cloud/gcp-cloud-storage.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake stages and directory tables](../snowflake/snowflake-stages-directory-tables.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud, data lake](../sap/sap-hana-cloud-data-lake.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Hadoop (HDFS and YARN)](../open-source/apache-hadoop.md) | [Object storage](../../capabilities/storage/object-storage.md) |
