---
type: Technology
id: clickhouse-warehouses
title: ClickHouse Cloud Warehouses (compute-compute separation)
description: Groups several Cloud services with their own replicas and endpoints over the same data, so ingestion, reporting and ad hoc workloads can run on separately sized compute.
aliases: [compute-compute separation]
platform: platform-clickhouse
kind: feature
availability: ga
realises: [workload-isolation, decoupled-storage-compute, elastic-scaling]
resource: https://clickhouse.com/docs/cloud/reference/warehouses
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA since January 2025 on Scale and Enterprise. Secondary services can be read-only, which skips background merges; refreshable materialised views run only on read-write services. Isolation is not total because merges and S3Queue inserts on read-write services still affect the shared storage; the default cap is 50 replicas per warehouse. Primary-service idling became GA in May 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Workload isolation](../../capabilities/compute/workload-isolation.md) (Query and compute) (primary): Run different workloads on separate compute so one cannot slow or starve another.
- [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) (Query and compute): Scale storage and compute independently and let several compute clusters work on the same data.
- [Elastic scaling](../../capabilities/compute/elastic-scaling.md) (Query and compute): Add and remove compute automatically as load changes, including for bursts of concurrent users.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga  
**Product family:** ClickHouse Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift Serverless](../aws/aws-redshift-serverless.md), [Amazon Redshift data sharing](../aws/aws-redshift-data-sharing.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Workload isolation](../../capabilities/compute/workload-isolation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Fabric capacities (F SKUs)](../microsoft/fabric-capacities.md) | [Workload isolation](../../capabilities/compute/workload-isolation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery workload management](../google-cloud/gcp-bigquery-workload-management.md) | [Workload isolation](../../capabilities/compute/workload-isolation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake virtual warehouses](../snowflake/snowflake-virtual-warehouses.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [Workload isolation](../../capabilities/compute/workload-isolation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL warehouses (serverless, pro and classic)](../databricks/databricks-sql-warehouses.md), [Databricks serverless compute](../databricks/databricks-serverless-compute.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Workload isolation](../../capabilities/compute/workload-isolation.md), [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md), [Cloudera Data Services on premises](../cloudera/cloudera-data-services-on-premises.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Workload isolation](../../capabilities/compute/workload-isolation.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Cloud](../teradata/teradata-cloud.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Workload isolation](../../capabilities/compute/workload-isolation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Kyuubi](../open-source/apache-kyuubi.md) | [Workload isolation](../../capabilities/compute/workload-isolation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [MotherDuck](../independent/motherduck.md) | [Workload isolation](../../capabilities/compute/workload-isolation.md) |
