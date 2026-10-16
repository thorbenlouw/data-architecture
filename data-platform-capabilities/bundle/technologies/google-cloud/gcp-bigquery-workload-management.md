---
type: Technology
id: gcp-bigquery-workload-management
title: BigQuery workload management
description: Reservations, assignments, idle-slot sharing, target concurrency, query queues and reservation groups that divide slot capacity between projects and workload types.
aliases: [BigQuery reservations]
formerly: [BigQuery capacity management]
platform: platform-google-cloud
kind: feature
availability: ga
realises: [workload-management, workload-isolation, spend-controls]
resource: https://docs.cloud.google.com/bigquery/docs/reservations-intro
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Renamed from capacity management in June 2026. Assignment types (QUERY, PIPELINE, CONTINUOUS, BACKGROUND, ML) isolate workload classes; reservation groups went GA in May 2026 and project-level caps entered preview in July 2026. BI Engine memory is reserved separately.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Workload management](../../capabilities/compute/workload-management.md) (Query and compute) (primary): Prioritise, queue and limit queries and jobs so the most important work meets its service levels.
- [Workload isolation](../../capabilities/compute/workload-isolation.md) (Query and compute): Run different workloads on separate compute so one cannot slow or starve another.
- [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) (Platform operations): Set budgets, quotas and alerts, and stop runaway spend automatically.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift concurrency scaling](../aws/aws-redshift-concurrency-scaling.md), [Amazon Redshift](../aws/aws-redshift.md) | [Workload management](../../capabilities/compute/workload-management.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Data Warehouse](../microsoft/fabric-data-warehouse.md), [Microsoft Fabric capacities (F SKUs)](../microsoft/fabric-capacities.md) | [Workload management](../../capabilities/compute/workload-management.md), [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Workload isolation](../../capabilities/compute/workload-isolation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake multi-cluster warehouses](../snowflake/snowflake-multi-cluster-warehouses.md), [Snowflake Adaptive Compute](../snowflake/snowflake-adaptive-compute.md) | [Workload management](../../capabilities/compute/workload-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL warehouses (serverless, pro and classic)](../databricks/databricks-sql-warehouses.md) | [Workload isolation](../../capabilities/compute/workload-isolation.md), [Workload management](../../capabilities/compute/workload-management.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse workload scheduling](../clickhouse/clickhouse-workload-scheduling.md), [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../clickhouse/clickhouse-access-control.md) | [Workload management](../../capabilities/compute/workload-management.md), [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Viewpoint](../teradata/teradata-viewpoint.md), [Teradata Database](../teradata/teradata-database.md) | [Workload management](../../capabilities/compute/workload-management.md) |
