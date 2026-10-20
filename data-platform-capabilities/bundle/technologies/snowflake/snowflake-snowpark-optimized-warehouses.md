---
type: Technology
id: snowflake-snowpark-optimized-warehouses
title: Snowpark-optimized warehouses
description: Warehouses with much more memory per node, and configurable CPU architecture, for memory-intensive Snowpark, UDF and single-node ML training work.
platform: platform-snowflake
kind: feature
availability: ga
realises: [provisioned-compute, model-training]
resource: https://docs.snowflake.com/en/user-guide/warehouses-snowpark-optimized
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Use these for in-warehouse ML training or large UDF state. For GPU or distributed training, use the Container Runtime on Snowpark Container Services compute pools instead.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Provisioned compute](../../capabilities/compute/provisioned-compute.md) (Query and compute) (primary): Run workloads on clusters or warehouses you size and control, for predictable performance and cost.
- [Model training](../../capabilities/machine-learning/model-training.md) (Machine learning development): Train models on platform data at the scale required, from single machines to GPU clusters.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowpark, Snowflake warehouses

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon EMR on EC2](../aws/aws-emr-on-ec2.md), [Amazon Redshift](../aws/aws-redshift.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Fabric capacities (F SKUs)](../microsoft/fabric-capacities.md), [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery editions](../google-cloud/gcp-bigquery-editions.md), [Google Cloud Managed Service for Apache Spark on clusters](../google-cloud/gcp-managed-spark-clusters.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md), [Cloudera on cloud](../cloudera/cloudera-on-cloud.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Exadata](../oracle/oracle-exadata.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Cloud](../teradata/teradata-cloud.md), [Teradata Factory](../teradata/teradata-factory.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Netezza Performance Server](../ibm/ibm-netezza.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Managed Cloud Services](../sas/sas-managed-cloud-services.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Hadoop (HDFS and YARN)](../open-source/apache-hadoop.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
