---
type: Capability
id: object-storage
title: Object storage
description: Store any volume of files cheaply and durably as the foundation of a data lake or lakehouse.
aliases: [data lake storage, blob storage]
broader: [storage]
related: [decoupled-storage-compute, data-residency, encryption, network-security, backup-restore]
tags: [storage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Object storage keeps data as objects: a block of bytes, a key that looks like a path (`sales/2026/10/part-0001.parquet`) and some metadata. It is reached through HTTP APIs rather than a file system, so there is no real directory tree, no editing in place and no file locking; an object is written whole and replaced whole. Cloud services spread redundant copies or erasure-coded fragments of each object across devices and zones, giving very high durability at a low price per gigabyte, and capacity grows without planning. The S3 API has become the common interface, and many on-premises and open-source stores implement it.

It is the foundation of the data lake and lakehouse because any engine can read the same files and storage grows separately from compute. The trade-offs are higher latency per request than local disk, charges per request, and listings that slow down when a prefix holds millions of objects. On its own it offers no tables or transactions; open table formats add those on top.

# Key considerations

- Many small objects hurt cost and speed, because each read is a separate request. Aim for analytical files in the tens to hundreds of megabytes.
- Check the consistency model and whether conditional writes such as put-if-absent are supported. Table formats rely on them for safe concurrent commits.
- Egress and cross-region transfer can cost more than the storage itself. Keep compute in the same region as the data it reads most.
- Object versioning, object lock and replication protect against deletion and ransomware but multiply the stored volume. Turn them on deliberately.
- Lay out buckets and prefixes around access-control and lifecycle boundaries, not only around team names.

# Questions to ask

- Which regions and jurisdictions must the data stay in?
- What durability, availability and recovery objectives apply to the data?
- How many files are written each day, and how small are they?
- Do on-premises or edge sites also need an S3-compatible store?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Storage and table management](storage.md) |
| Broader | [Storage and table management](storage.md) |
| Narrower | [File-system access to object storage](object-file-access.md), [Storage tiering and lifecycle](storage-tiering.md) |
| Related | [Backup and restore](../platform-operations/backup-restore.md), [Data residency and sovereignty](../governance/data-residency.md), [Decoupled storage and compute](../compute/decoupled-storage-compute.md), [Encryption](../security/encryption.md), [Network security](../security/network-security.md), [Storage credential vending](credential-vending.md) |
| Needed by | [Backup and restore](../platform-operations/backup-restore.md), [Bulk and offline transfer](../ingestion-integration/bulk-data-transfer.md), [Decoupled storage and compute](../compute/decoupled-storage-compute.md), [File ingestion](../ingestion-integration/file-ingestion.md), [Immutable backups](../platform-operations/immutable-backups.md), [Multimodal data formats](multimodal-data-formats.md), [Open table formats](open-table-formats.md), [Unstructured data ingestion](../ingestion-integration/unstructured-ingestion.md), [Unstructured data management](../specialised-data/unstructured-data.md) |

# Where it appears

- **Use cases:** [Security and log analytics](../../use-cases/usecase-security-log-analytics.md) (requires, level 3)
- **Patterns:** [Data lake](../../patterns/data-lake.md) · [Lakehouse](../../patterns/lakehouse.md)
- **Maturity tracks:** [Storage and table management](../../maturity/track-storage.md) (from level 1, Initial)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Big Data and Data Science

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Amazon S3 general purpose buckets | [Amazon S3](../../technologies/aws/aws-s3.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Data Lake Storage](../../technologies/microsoft/azure-data-lake-storage.md), [OneLake](../../technologies/microsoft/fabric-onelake.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Storage](../../technologies/google-cloud/gcp-cloud-storage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake stages and directory tables](../../technologies/snowflake/snowflake-stages-directory-tables.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Apache Ozone in Cloudera](../../technologies/cloudera/cloudera-ozone.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP HANA Cloud, data lake](../../technologies/sap/sap-hana-cloud-data-lake.md) |
| [Teradata](../../platforms/platform-teradata.md) | Native Object Store | [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../../technologies/teradata/teradata-open-table-format.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Hadoop (HDFS and YARN)](../../technologies/open-source/apache-hadoop.md), [MinIO (community edition)](../../technologies/open-source/minio.md) (deprecated) |

Narrower capabilities are realised by a further 13 technologies; see their pages.
