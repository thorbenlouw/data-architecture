---
type: Technology
id: aws-s3
title: Amazon S3
description: Object storage service that holds files of any size in buckets and is the usual foundation for data lakes on AWS.
aliases: [Amazon Simple Storage Service, S3 Object Lock, S3 Access Grants]
platform: platform-aws
kind: managed-service
availability: ga
realises:
- object-storage
- unstructured-data
- cross-region-failover
- data-retention
- access-control
- immutable-backups
resource: https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Same-Region and Cross-Region Replication, Versioning and Object Lock (WORM retention and legal holds) cover resilience and retention; S3 Access Grants map corporate identities to prefixes. S3 Select, S3 Glacier Select and S3 Object Lambda are in maintenance and closed to new customers.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Object storage](../../capabilities/storage/object-storage.md) (Storage and table management) (primary): Store any volume of files cheaply and durably as the foundation of a data lake or lakehouse.
- [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) (Specialised data types): Store, catalogue, govern and process documents, images, audio and video alongside structured data.
- [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) (Platform operations): Replicate data and configuration to another region and fail over when needed.
- [Retention and disposal](../../capabilities/governance/data-retention.md) (Governance and compliance): Keep data for as long as required, then delete it reliably, including from history, snapshots and backups, with legal holds when needed.
- [Access control](../../capabilities/security/access-control.md) (Security and access): Decide who can see and change which data, at every level from account down to individual values.
- [Immutable backups](../../capabilities/platform-operations/immutable-backups.md) (Platform operations): Keep backups that nobody can delete or change before they expire, with legal holds, to protect against ransomware.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon S3

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Lake Storage](../microsoft/azure-data-lake-storage.md), [OneLake](../microsoft/fabric-onelake.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Storage](../google-cloud/gcp-cloud-storage.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md), [Immutable backups](../../capabilities/platform-operations/immutable-backups.md), [Object storage](../../capabilities/storage/object-storage.md), [Retention and disposal](../../capabilities/governance/data-retention.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake stages and directory tables](../snowflake/snowflake-stages-directory-tables.md) | [Object storage](../../capabilities/storage/object-storage.md), [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Apache Ozone in Cloudera](../cloudera/cloudera-ozone.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud, data lake](../sap/sap-hana-cloud-data-lake.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Hadoop (HDFS and YARN)](../open-source/apache-hadoop.md) | [Object storage](../../capabilities/storage/object-storage.md) |
