---
type: Technology
id: apache-hadoop
title: Apache Hadoop (HDFS and YARN)
description: Distributed file system (HDFS) and cluster resource manager (YARN) that formed the first generation of on-premises data lakes.
aliases: [Hadoop, HDFS, YARN]
platform: platform-open-source
kind: open-source
availability: ga
realises: [object-storage, provisioned-compute, distributed-processing]
resource: https://hadoop.apache.org/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ASF top-level project, Apache 2.0. Still common in regulated and on-premises estates, often with Hive, Ranger and Atlas. Most new designs use S3-compatible object storage and Kubernetes instead. HDFS is a file system rather than object storage, but fills the same role.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Object storage](../../capabilities/storage/object-storage.md) (Storage and table management) (primary): Store any volume of files cheaply and durably as the foundation of a data lake or lakehouse.
- [Provisioned compute](../../capabilities/compute/provisioned-compute.md) (Query and compute): Run workloads on clusters or warehouses you size and control, for predictable performance and cost.
- [Distributed processing](../../capabilities/processing/distributed-processing.md) (Processing and transformation): Process large datasets in parallel across a cluster of machines.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3](../aws/aws-s3.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Lake Storage](../microsoft/azure-data-lake-storage.md), [OneLake](../microsoft/fabric-onelake.md), [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md) | [Object storage](../../capabilities/storage/object-storage.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Storage](../google-cloud/gcp-cloud-storage.md), [Google Cloud Managed Service for Apache Spark on clusters](../google-cloud/gcp-managed-spark-clusters.md) | [Object storage](../../capabilities/storage/object-storage.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake stages and directory tables](../snowflake/snowflake-stages-directory-tables.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Apache Ozone in Cloudera](../cloudera/cloudera-ozone.md), [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md) | [Object storage](../../capabilities/storage/object-storage.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud, data lake](../sap/sap-hana-cloud-data-lake.md) | [Object storage](../../capabilities/storage/object-storage.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Object storage](../../capabilities/storage/object-storage.md) |
