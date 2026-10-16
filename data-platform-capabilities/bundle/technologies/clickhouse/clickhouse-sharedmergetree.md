---
type: Technology
id: clickhouse-sharedmergetree
title: SharedMergeTree
description: Cloud-native counterpart of the MergeTree family that keeps table data and metadata in shared object storage and coordinates replicas through Keeper instead of copying data between them.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [decoupled-storage-compute, managed-storage, elastic-scaling]
resource: https://clickhouse.com/docs/cloud/reference/shared-merge-tree
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Applied automatically in ClickHouse Cloud, where Replacing, Aggregating, Summing, Collapsing and other MergeTree variants are converted to their Shared equivalents without DDL changes. It is what allows replicas to be added quickly and many services to share one dataset; it is not part of the open-source build.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) (Query and compute) (primary): Scale storage and compute independently and let several compute clusters work on the same data.
- [Platform-managed storage](../../capabilities/storage/managed-storage.md) (Storage and table management): Let the platform manage table storage layout, compression and durability internally.
- [Elastic scaling](../../capabilities/compute/elastic-scaling.md) (Query and compute): Add and remove compute automatically as load changes, including for bursts of concurrent users.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga  
**Product family:** ClickHouse Cloud, ClickHouse table engines

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift Spectrum](../aws/aws-redshift-spectrum.md), [Lakehouse architecture of Amazon SageMaker](../aws/aws-sagemaker-lakehouse.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake](../microsoft/fabric-onelake.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery](../google-cloud/gcp-bigquery.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake virtual warehouses](../snowflake/snowflake-virtual-warehouses.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks serverless compute](../databricks/databricks-serverless-compute.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [Elastic scaling](../../capabilities/compute/elastic-scaling.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Apache Ozone in Cloudera](../cloudera/cloudera-ozone.md), [Cloudera on cloud](../cloudera/cloudera-on-cloud.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Cloud](../teradata/teradata-cloud.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [Elastic scaling](../../capabilities/compute/elastic-scaling.md) |
| [IBM](../../platforms/platform-ibm.md) | [WarpStream](../ibm/warpstream.md), [IBM watsonx.data](../ibm/ibm-watsonx-data.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry](../palantir/palantir-foundry.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [Platform-managed storage](../../capabilities/storage/managed-storage.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Presto](../open-source/presto.md), [Trino](../open-source/trino.md), [StarRocks](../open-source/starrocks.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) |
