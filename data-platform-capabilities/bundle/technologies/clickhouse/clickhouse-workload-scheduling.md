---
type: Technology
id: clickhouse-workload-scheduling
title: ClickHouse workload scheduling
description: Divides CPU, disk I/O, memory and query slots between a hierarchy of SQL-defined workloads using priorities, weights and limits.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [workload-management]
resource: https://clickhouse.com/docs/operations/workload-scheduling
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Off until at least one RESOURCE and one WORKLOAD are created; queries join a workload through a setting. Memory reservations are experimental, and merges and mutations are not yet covered by CPU or memory scheduling.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Workload management](../../capabilities/compute/workload-management.md) (Query and compute) (primary): Prioritise, queue and limit queries and jobs so the most important work meets its service levels.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift concurrency scaling](../aws/aws-redshift-concurrency-scaling.md), [Amazon Redshift](../aws/aws-redshift.md) | [Workload management](../../capabilities/compute/workload-management.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Data Warehouse](../microsoft/fabric-data-warehouse.md) | [Workload management](../../capabilities/compute/workload-management.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery workload management](../google-cloud/gcp-bigquery-workload-management.md) | [Workload management](../../capabilities/compute/workload-management.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake multi-cluster warehouses](../snowflake/snowflake-multi-cluster-warehouses.md), [Snowflake Adaptive Compute](../snowflake/snowflake-adaptive-compute.md) | [Workload management](../../capabilities/compute/workload-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL warehouses (serverless, pro and classic)](../databricks/databricks-sql-warehouses.md) | [Workload management](../../capabilities/compute/workload-management.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Viewpoint](../teradata/teradata-viewpoint.md), [Teradata Database](../teradata/teradata-database.md) | [Workload management](../../capabilities/compute/workload-management.md) |
