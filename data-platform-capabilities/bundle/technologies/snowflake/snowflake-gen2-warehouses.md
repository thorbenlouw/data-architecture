---
type: Technology
id: snowflake-gen2-warehouses
title: Snowflake generation 2 standard warehouses
description: The newer generation of standard warehouses, running on faster hardware with optimisations for DELETE, UPDATE, MERGE and table scans.
aliases: [Gen2 warehouses]
platform: platform-snowflake
kind: feature
availability: ga
realises: [provisioned-compute, sql-query-engine]
resource: https://docs.snowflake.com/en/user-guide/warehouses-gen2
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Gen2 is now the default for new standard warehouses where the region supports it. It is not available for X5LARGE or X6LARGE. New Gen2 warehouses have the Query Acceleration Service turned on by default. With account replication, the secondary region must also support Gen2.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Provisioned compute](../../capabilities/compute/provisioned-compute.md) (Query and compute) (primary): Run workloads on clusters or warehouses you size and control, for predictable performance and cost.
- [SQL query engine](../../capabilities/compute/sql-query-engine.md) (Query and compute): Run analytical SQL over large datasets with parallel, optimised execution.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake warehouses

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift](../aws/aws-redshift.md), [Amazon EMR on EC2](../aws/aws-emr-on-ec2.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md), [Microsoft Fabric capacities (F SKUs)](../microsoft/fabric-capacities.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery editions](../google-cloud/gcp-bigquery-editions.md), [Google Cloud Managed Service for Apache Spark on clusters](../google-cloud/gcp-managed-spark-clusters.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md), [Cloudera on cloud](../cloudera/cloudera-on-cloud.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Exadata](../oracle/oracle-exadata.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Cloud](../teradata/teradata-cloud.md), [Teradata Factory](../teradata/teradata-factory.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Netezza Performance Server](../ibm/ibm-netezza.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Managed Cloud Services](../sas/sas-managed-cloud-services.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Hadoop (HDFS and YARN)](../open-source/apache-hadoop.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
