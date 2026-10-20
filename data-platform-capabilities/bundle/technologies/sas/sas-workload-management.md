---
type: Technology
id: sas-workload-management
title: SAS Workload Management
description: Scheduler for SAS Viya compute sessions and jobs on Kubernetes that routes work through rule-based queues and priorities, balances it across nodes by capacity and restarts pre-empted jobs.
aliases: [SAS Workload Orchestrator, SWO]
platform: platform-sas
kind: feature
availability: ga
realises: [workload-management]
resource: https://www.sas.com/en_us/software/workload-management.html
tags: [sas]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:10:17Z'}
---

Its core component is SAS Workload Orchestrator, with a manager and a daemon on each compute node, administered through a web interface or the SAS Viya command-line interface. It brings the queues, priorities and restart features of SAS Grid Manager from SAS 9 to SAS Viya.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Workload management](../../capabilities/compute/workload-management.md) (Query and compute) (primary): Prioritise, queue and limit queries and jobs so the most important work meets its service levels.

**Platform:** [SAS](../../platforms/platform-sas.md)  
**Availability:** ga  
**Product family:** SAS Viya

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift concurrency scaling](../aws/aws-redshift-concurrency-scaling.md), [Amazon Redshift](../aws/aws-redshift.md) | [Workload management](../../capabilities/compute/workload-management.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Data Warehouse](../microsoft/fabric-data-warehouse.md) | [Workload management](../../capabilities/compute/workload-management.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery workload management](../google-cloud/gcp-bigquery-workload-management.md) | [Workload management](../../capabilities/compute/workload-management.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake multi-cluster warehouses](../snowflake/snowflake-multi-cluster-warehouses.md), [Snowflake Adaptive Compute](../snowflake/snowflake-adaptive-compute.md) | [Workload management](../../capabilities/compute/workload-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL warehouses (serverless, pro and classic)](../databricks/databricks-sql-warehouses.md) | [Workload management](../../capabilities/compute/workload-management.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse workload scheduling](../clickhouse/clickhouse-workload-scheduling.md), [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../clickhouse/clickhouse-access-control.md) | [Workload management](../../capabilities/compute/workload-management.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Viewpoint](../teradata/teradata-viewpoint.md), [Teradata Database](../teradata/teradata-database.md) | [Workload management](../../capabilities/compute/workload-management.md) |
