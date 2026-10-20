---
type: Technology
id: fabric-capacities
title: Microsoft Fabric capacities (F SKUs)
description: Pools of capacity units, bought through Azure in sizes from F2 upwards, that all Fabric workloads in assigned workspaces share.
aliases: [F SKUs, Fabric capacity]
platform: platform-microsoft
kind: managed-service
availability: ga
realises: [provisioned-compute, workload-isolation, spend-controls, reserved-capacity]
resource: https://learn.microsoft.com/en-us/fabric/enterprise/licenses
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Pay-as-you-go per second or reserved yearly; can be paused. Smoothing and bursting let short spikes exceed the SKU, with throttling if sustained; surge protection limits background jobs. Separate capacities are the main way to isolate workloads and budgets. Power BI Premium P SKUs are being retired in favour of F SKUs; F64 or larger lets free-licence users view Power BI content.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Provisioned compute](../../capabilities/compute/provisioned-compute.md) (Query and compute) (primary): Run workloads on clusters or warehouses you size and control, for predictable performance and cost.
- [Workload isolation](../../capabilities/compute/workload-isolation.md) (Query and compute): Run different workloads on separate compute so one cannot slow or starve another.
- [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) (Platform operations): Set budgets, quotas and alerts, and stop runaway spend automatically.
- [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) (Query and compute): Reserve compute, query, training or inference capacity in advance for guaranteed availability and lower unit cost.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift](../aws/aws-redshift.md), [Amazon EMR on EC2](../aws/aws-emr-on-ec2.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery editions](../google-cloud/gcp-bigquery-editions.md), [Google Cloud Managed Service for Apache Spark on clusters](../google-cloud/gcp-managed-spark-clusters.md), [BigQuery workload management](../google-cloud/gcp-bigquery-workload-management.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md), [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Workload isolation](../../capabilities/compute/workload-isolation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake virtual warehouses](../snowflake/snowflake-virtual-warehouses.md), [Snowflake generation 2 standard warehouses](../snowflake/snowflake-gen2-warehouses.md), [Snowpark-optimized warehouses](../snowflake/snowflake-snowpark-optimized-warehouses.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [Workload isolation](../../capabilities/compute/workload-isolation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md), [Cloudera on cloud](../cloudera/cloudera-on-cloud.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Exadata](../oracle/oracle-exadata.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Cloud](../teradata/teradata-cloud.md), [Teradata Factory](../teradata/teradata-factory.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [Workload isolation](../../capabilities/compute/workload-isolation.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Netezza Performance Server](../ibm/ibm-netezza.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Managed Cloud Services](../sas/sas-managed-cloud-services.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Hadoop (HDFS and YARN)](../open-source/apache-hadoop.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
