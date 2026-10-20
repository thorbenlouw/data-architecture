---
type: Technology
id: aws-redshift-concurrency-scaling
title: Amazon Redshift concurrency scaling
description: Adds transient compute automatically when queries queue on a Redshift warehouse and removes it when load drops.
platform: platform-aws
kind: feature
availability: ga
realises: [elastic-scaling, workload-management]
resource: https://docs.aws.amazon.com/redshift/latest/dg/concurrency-scaling.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Free credits accrue daily on provisioned clusters; beyond them it is billed per second. In 2026 it was extended to writes, COPY, auto-copy and zero-ETL ingestion.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Elastic scaling](../../capabilities/compute/elastic-scaling.md) (Query and compute) (primary): Add and remove compute automatically as load changes, including for bursts of concurrent users.
- [Workload management](../../capabilities/compute/workload-management.md) (Query and compute): Prioritise, queue and limit queries and jobs so the most important work meets its service levels.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon Redshift

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Data Warehouse](../microsoft/fabric-data-warehouse.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Workload management](../../capabilities/compute/workload-management.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery editions](../google-cloud/gcp-bigquery-editions.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake multi-cluster warehouses](../snowflake/snowflake-multi-cluster-warehouses.md), [Snowflake Adaptive Compute](../snowflake/snowflake-adaptive-compute.md), [Snowflake Query Acceleration Service](../snowflake/snowflake-query-acceleration-service.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Workload management](../../capabilities/compute/workload-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL warehouses (serverless, pro and classic)](../databricks/databricks-sql-warehouses.md), [Databricks serverless compute](../databricks/databricks-serverless-compute.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Workload management](../../capabilities/compute/workload-management.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud Warehouses (compute-compute separation)](../clickhouse/clickhouse-warehouses.md), [SharedMergeTree](../clickhouse/clickhouse-sharedmergetree.md), [ClickHouse Cloud](../clickhouse/clickhouse-cloud.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md) |
| [Informatica](../../platforms/platform-informatica.md) | [IDMC serverless runtime environment](../informatica/informatica-serverless-runtime-environment.md), [Informatica Cloud Data Integration advanced mode](../informatica/informatica-cdi-advanced-mode.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md), [Oracle Autonomous AI Database](../oracle/oracle-autonomous-ai-database.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Cloud](../teradata/teradata-cloud.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Workload Management](../sas/sas-workload-management.md) | [Workload management](../../capabilities/compute/workload-management.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [KServe](../open-source/kserve.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md) |
