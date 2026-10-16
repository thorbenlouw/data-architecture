---
type: Technology
id: sap-hana-cloud-data-lake
title: SAP HANA Cloud, data lake
description: Low-cost storage tier of SAP HANA Cloud with data lake Files for object storage and a data lake Relational Engine for SQL over large, colder datasets.
platform: platform-sap
kind: feature
availability: ga
realises: [object-storage, storage-tiering, sql-query-engine]
resource: https://www.sap.com/products/data-cloud/hana.html
tags: [sap]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The Relational Engine derives from SAP IQ. BDC keeps its data products in its own object store, which is separate from the HANA Cloud data lake.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Object storage](../../capabilities/storage/object-storage.md) (Storage and table management) (primary): Store any volume of files cheaply and durably as the foundation of a data lake or lakehouse.
- [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) (Storage and table management): Move data between hot, cool and archive tiers automatically based on age or access patterns.
- [SQL query engine](../../capabilities/compute/sql-query-engine.md) (Query and compute): Run analytical SQL over large datasets with parallel, optimised execution.

**Platform:** [SAP](../../platforms/platform-sap.md)  
**Availability:** ga  
**Product family:** SAP HANA Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3](../aws/aws-s3.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Lake Storage](../microsoft/azure-data-lake-storage.md), [OneLake](../microsoft/fabric-onelake.md) | [Object storage](../../capabilities/storage/object-storage.md), [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Storage](../google-cloud/gcp-cloud-storage.md) | [Object storage](../../capabilities/storage/object-storage.md), [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake stages and directory tables](../snowflake/snowflake-stages-directory-tables.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Apache Ozone in Cloudera](../cloudera/cloudera-ozone.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Hadoop (HDFS and YARN)](../open-source/apache-hadoop.md) | [Object storage](../../capabilities/storage/object-storage.md) |
