---
type: Technology
id: azure-data-lake-storage
title: Azure Data Lake Storage
description: Blob Storage with a hierarchical namespace, POSIX-style ACLs and hot, cool, cold and archive tiers, used as the lake for most Azure analytics.
aliases: [ADLS, ADLS Gen2, Azure Data Lake Storage Gen2]
platform: platform-microsoft
kind: managed-service
availability: ga
realises: [object-storage, storage-tiering, object-file-access]
resource: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Lifecycle management policies move or delete blobs by age. Supports SFTP endpoints for simple partner file drops. OneLake is built on the same technology.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Object storage](../../capabilities/storage/object-storage.md) (Storage and table management) (primary): Store any volume of files cheaply and durably as the foundation of a data lake or lakehouse.
- [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) (Storage and table management): Move data between hot, cool and archive tiers automatically based on age or access patterns.
- [File-system access to object storage](../../capabilities/storage/object-file-access.md) (Storage and table management): Mount object storage as a file system so file-based tools, ML jobs and agents can work on lake data without copies.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3](../aws/aws-s3.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Storage](../google-cloud/gcp-cloud-storage.md) | [File-system access to object storage](../../capabilities/storage/object-file-access.md), [Object storage](../../capabilities/storage/object-storage.md), [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake stages and directory tables](../snowflake/snowflake-stages-directory-tables.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Apache Ozone in Cloudera](../cloudera/cloudera-ozone.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud, data lake](../sap/sap-hana-cloud-data-lake.md) | [Object storage](../../capabilities/storage/object-storage.md), [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Hadoop (HDFS and YARN)](../open-source/apache-hadoop.md) | [Object storage](../../capabilities/storage/object-storage.md) |
