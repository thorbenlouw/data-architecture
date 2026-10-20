---
type: Technology
id: teradata-cloud
title: Teradata Cloud
description: Teradata-managed deployment of the platform on AWS, Azure and Google Cloud, combining always-on active compute with elastic compute that scales on demand over database and object-storage data.
formerly: [Teradata VantageCloud, VantageCloud Lake, VantageCloud Enterprise]
platform: platform-teradata
kind: managed-service
availability: ga
realises:
- provisioned-compute
- elastic-scaling
- workload-isolation
- serverless-compute
- decoupled-storage-compute
resource: https://www.teradata.com/platform/cloud
tags: [teradata]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Elastic compute, introduced in May 2026, scales on demand next to always-on compute and works directly on Iceberg and Delta Lake tables in object storage. The Connected Data Foundation brings block and object storage under one governed architecture. Contracts and documents still refer to the earlier VantageCloud Lake (object storage first, with compute clusters) and VantageCloud Enterprise (block storage, fixed capacity) editions.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Provisioned compute](../../capabilities/compute/provisioned-compute.md) (Query and compute) (primary): Run workloads on clusters or warehouses you size and control, for predictable performance and cost.
- [Elastic scaling](../../capabilities/compute/elastic-scaling.md) (Query and compute): Add and remove compute automatically as load changes, including for bursts of concurrent users.
- [Workload isolation](../../capabilities/compute/workload-isolation.md) (Query and compute): Run different workloads on separate compute so one cannot slow or starve another.
- [Serverless compute](../../capabilities/compute/serverless-compute.md) (Query and compute): Run workloads without managing servers, with capacity allocated on demand and billed by use.
- [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) (Query and compute): Scale storage and compute independently and let several compute clusters work on the same data.

**Platform:** [Teradata](../../platforms/platform-teradata.md)  
**Availability:** ga  
**Product family:** Teradata Autonomous Knowledge Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon EMR on EC2](../aws/aws-emr-on-ec2.md), [Amazon Redshift Serverless](../aws/aws-redshift-serverless.md), [Amazon Redshift](../aws/aws-redshift.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Serverless compute](../../capabilities/compute/serverless-compute.md), [Workload isolation](../../capabilities/compute/workload-isolation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Fabric capacities (F SKUs)](../microsoft/fabric-capacities.md), [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [Workload isolation](../../capabilities/compute/workload-isolation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery editions](../google-cloud/gcp-bigquery-editions.md), [Google Cloud Managed Service for Apache Spark on clusters](../google-cloud/gcp-managed-spark-clusters.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake virtual warehouses](../snowflake/snowflake-virtual-warehouses.md), [Snowflake generation 2 standard warehouses](../snowflake/snowflake-gen2-warehouses.md), [Snowpark-optimized warehouses](../snowflake/snowflake-snowpark-optimized-warehouses.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [Workload isolation](../../capabilities/compute/workload-isolation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md), [Databricks serverless compute](../databricks/databricks-serverless-compute.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud Warehouses (compute-compute separation)](../clickhouse/clickhouse-warehouses.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Workload isolation](../../capabilities/compute/workload-isolation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera on cloud](../cloudera/cloudera-on-cloud.md), [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Exadata](../oracle/oracle-exadata.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Netezza Performance Server](../ibm/ibm-netezza.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Managed Cloud Services](../sas/sas-managed-cloud-services.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Hadoop (HDFS and YARN)](../open-source/apache-hadoop.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
