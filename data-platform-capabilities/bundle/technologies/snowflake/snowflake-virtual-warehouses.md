---
type: Technology
id: snowflake-virtual-warehouses
title: Snowflake virtual warehouses
description: Named clusters of compute, sized from X-Small to 6X-Large, that run SQL and Snowpark workloads against shared storage and suspend and resume automatically.
platform: platform-snowflake
kind: feature
availability: ga
realises: [provisioned-compute, sql-query-engine, decoupled-storage-compute, workload-isolation]
resource: https://docs.snowflake.com/en/user-guide/warehouses-overview
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Several warehouses can work on the same data at once, so giving each workload its own warehouse is the standard isolation pattern. Billing is per second with a 60-second minimum each time a warehouse resumes.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Provisioned compute](../../capabilities/compute/provisioned-compute.md) (Query and compute) (primary): Run workloads on clusters or warehouses you size and control, for predictable performance and cost.
- [SQL query engine](../../capabilities/compute/sql-query-engine.md) (Query and compute): Run analytical SQL over large datasets with parallel, optimised execution.
- [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) (Query and compute): Scale storage and compute independently and let several compute clusters work on the same data.
- [Workload isolation](../../capabilities/compute/workload-isolation.md) (Query and compute): Run different workloads on separate compute so one cannot slow or starve another.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake warehouses

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift](../aws/aws-redshift.md), [Amazon EMR on EC2](../aws/aws-emr-on-ec2.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Fabric capacities (F SKUs)](../microsoft/fabric-capacities.md), [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [Workload isolation](../../capabilities/compute/workload-isolation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery editions](../google-cloud/gcp-bigquery-editions.md), [Google Cloud Managed Service for Apache Spark on clusters](../google-cloud/gcp-managed-spark-clusters.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud Warehouses (compute-compute separation)](../clickhouse/clickhouse-warehouses.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [Workload isolation](../../capabilities/compute/workload-isolation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md), [Cloudera on cloud](../cloudera/cloudera-on-cloud.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Exadata](../oracle/oracle-exadata.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Cloud](../teradata/teradata-cloud.md), [Teradata Factory](../teradata/teradata-factory.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [Workload isolation](../../capabilities/compute/workload-isolation.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Netezza Performance Server](../ibm/ibm-netezza.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Managed Cloud Services](../sas/sas-managed-cloud-services.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Hadoop (HDFS and YARN)](../open-source/apache-hadoop.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
