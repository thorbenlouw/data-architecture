---
type: Technology
id: gcp-cloud-storage
title: Google Cloud Storage
description: Object storage with regional, dual-region and multi-region buckets and Standard, Nearline, Coldline and Archive storage classes.
aliases: [GCS]
platform: platform-google-cloud
kind: managed-service
availability: ga
realises:
- object-storage
- storage-tiering
- data-retention
- cross-region-failover
- object-file-access
- immutable-backups
resource: https://docs.cloud.google.com/storage/docs/introduction
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Lifecycle rules, retention policies, object holds and Bucket Lock support retention and legal hold; dual-region buckets with turbo replication give a 15-minute RPO. Hierarchical namespace buckets and Anywhere Cache target analytics and AI workloads. Storage Intelligence adds Storage Insights datasets in BigQuery and batch operations across buckets.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Object storage](../../capabilities/storage/object-storage.md) (Storage and table management) (primary): Store any volume of files cheaply and durably as the foundation of a data lake or lakehouse.
- [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) (Storage and table management): Move data between hot, cool and archive tiers automatically based on age or access patterns.
- [Retention and disposal](../../capabilities/governance/data-retention.md) (Governance and compliance): Keep data for as long as required, then delete it reliably, including from history, snapshots and backups, with legal holds when needed.
- [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) (Platform operations): Replicate data and configuration to another region and fail over when needed.
- [File-system access to object storage](../../capabilities/storage/object-file-access.md) (Storage and table management): Mount object storage as a file system so file-based tools, ML jobs and agents can work on lake data without copies.
- [Immutable backups](../../capabilities/platform-operations/immutable-backups.md) (Platform operations): Keep backups that nobody can delete or change before they expire, with legal holds, to protect against ransomware.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3](../aws/aws-s3.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md), [Immutable backups](../../capabilities/platform-operations/immutable-backups.md), [Object storage](../../capabilities/storage/object-storage.md), [Retention and disposal](../../capabilities/governance/data-retention.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Lake Storage](../microsoft/azure-data-lake-storage.md), [OneLake](../microsoft/fabric-onelake.md) | [File-system access to object storage](../../capabilities/storage/object-file-access.md), [Object storage](../../capabilities/storage/object-storage.md), [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake stages and directory tables](../snowflake/snowflake-stages-directory-tables.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Apache Ozone in Cloudera](../cloudera/cloudera-ozone.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud, data lake](../sap/sap-hana-cloud-data-lake.md) | [Object storage](../../capabilities/storage/object-storage.md), [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Hadoop (HDFS and YARN)](../open-source/apache-hadoop.md) | [Object storage](../../capabilities/storage/object-storage.md) |
