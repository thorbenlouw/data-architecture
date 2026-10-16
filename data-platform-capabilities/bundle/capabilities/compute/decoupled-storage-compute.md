---
type: Capability
id: decoupled-storage-compute
title: Decoupled storage and compute
description: Scale storage and compute independently and let several compute clusters work on the same data.
broader: [compute]
related: [engine-interoperability, managed-storage, open-table-formats, multi-tenancy, workload-isolation]
depends_on: [object-storage]
tags: [compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

In a coupled system, such as a traditional MPP database or an HDFS cluster, each node keeps a slice of the data on its own disks, so adding storage means adding compute and the reverse. Decoupled systems keep data in shared storage, usually object storage, and treat compute nodes as stateless workers that read what they need and cache hot data locally. A finance cluster and a data science cluster can then query the same tables at the same time, each sized and billed separately, and either can be stopped without affecting the data.

This separation underpins elastic scaling, serverless compute, workload isolation and multi-engine access to one copy of data. The cost is that reads cross the network to slower storage, which engines offset with local caches, columnar formats and data skipping. Some real-time databases still couple storage and compute for the lowest latency, or keep a local disk tier in front of object storage.

# Key considerations

- Caching largely decides performance. Check cache size, warm-up time after scaling and how caches stay consistent with storage.
- Many clusters reading the same storage raise request rates and costs. Watch per-request charges and throttling limits.
- Shared storage needs consistent access control for all compute. Govern access in the catalogue or storage layer, not only in each cluster.
- Writes from several clusters still need transactional coordination through the table format or the platform.

# Questions to ask

- How many teams or workloads need to work on the same data at once?
- Do storage and compute needs grow at different rates in your estate?
- Do any latency targets require data to be held close to compute?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Query and compute](compute.md) |
| Broader | [Query and compute](compute.md) |
| Related | [Storage and table management](../storage/storage.md), [Multi-engine interoperability](engine-interoperability.md), [Multi-tenancy and workspace isolation](../platform-operations/multi-tenancy.md), [Object storage](../storage/object-storage.md), [Open table formats](../storage/open-table-formats.md), [Platform-managed storage](../storage/managed-storage.md), [Workload isolation](workload-isolation.md) |
| Depends on | [Object storage](../storage/object-storage.md) |
| Needed by | [Elastic scaling](elastic-scaling.md), [Serverless compute](serverless-compute.md), [Workload isolation](workload-isolation.md) |

# Where it appears

- **Use cases:** [Security and log analytics](../../use-cases/usecase-security-log-analytics.md) (benefits from)
- **Patterns:** [Lakehouse](../../patterns/lakehouse.md)
- **Personas:** [Data architect](../../personas/persona-data-architect.md)
- **Maturity tracks:** [Compute and workload management](../../maturity/track-compute.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Lakehouse architecture of Amazon SageMaker; Redshift RA3 | [Amazon Redshift Spectrum](../../technologies/aws/aws-redshift-spectrum.md), [Lakehouse architecture of Amazon SageMaker](../../technologies/aws/aws-sagemaker-lakehouse.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [OneLake](../../technologies/microsoft/fabric-onelake.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery](../../technologies/google-cloud/gcp-bigquery.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake virtual warehouses](../../technologies/snowflake/snowflake-virtual-warehouses.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks serverless compute](../../technologies/databricks/databricks-serverless-compute.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | SharedMergeTree | [ClickHouse Cloud Warehouses (compute-compute separation)](../../technologies/clickhouse/clickhouse-warehouses.md), [SharedMergeTree](../../technologies/clickhouse/clickhouse-sharedmergetree.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Apache Ozone in Cloudera](../../technologies/cloudera/cloudera-ozone.md), [Cloudera on cloud](../../technologies/cloudera/cloudera-on-cloud.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Cloud](../../technologies/teradata/teradata-cloud.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.data](../../technologies/ibm/ibm-watsonx-data.md), [WarpStream](../../technologies/ibm/warpstream.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Foundry](../../technologies/palantir/palantir-foundry.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Presto](../../technologies/open-source/presto.md), [StarRocks](../../technologies/open-source/starrocks.md), [Trino](../../technologies/open-source/trino.md) |
