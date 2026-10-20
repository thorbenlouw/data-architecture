---
type: Technology
id: sas-managed-cloud-services
title: SAS Managed Cloud Services
description: SAS-operated hosting and management of SAS software on Microsoft Azure or AWS, or in a customer's own cloud, including SAS Viya Essentials, a fixed-price set of SAS Viya products on Azure.
aliases: [SAS Cloud, SAS Managed Services, SAS Viya Essentials, SAS Software as a Service]
platform: platform-sas
kind: managed-service
availability: ga
realises: [provisioned-compute]
resource: https://www.sas.com/en_us/solutions/cloud/sas-managed-cloud-services.html
tags: [sas]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:10:17Z'}
---

Hosted Managed Services run on Azure, Azure Government or AWS; Remote Managed Services monitor and manage SAS software in the customer's own cloud. SAS Viya Essentials, announced in October 2025, deploys SAS Visual Analytics, SAS Visual Statistics and SAS Viya in four predefined architecture profiles with a 99.5% uptime guarantee.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Provisioned compute](../../capabilities/compute/provisioned-compute.md) (Query and compute) (primary): Run workloads on clusters or warehouses you size and control, for predictable performance and cost.

**Platform:** [SAS](../../platforms/platform-sas.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon EMR on EC2](../aws/aws-emr-on-ec2.md), [Amazon Redshift](../aws/aws-redshift.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Fabric capacities (F SKUs)](../microsoft/fabric-capacities.md), [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery editions](../google-cloud/gcp-bigquery-editions.md), [Google Cloud Managed Service for Apache Spark on clusters](../google-cloud/gcp-managed-spark-clusters.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake generation 2 standard warehouses](../snowflake/snowflake-gen2-warehouses.md), [Snowpark-optimized warehouses](../snowflake/snowflake-snowpark-optimized-warehouses.md), [Snowflake virtual warehouses](../snowflake/snowflake-virtual-warehouses.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md), [Cloudera on cloud](../cloudera/cloudera-on-cloud.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Exadata](../oracle/oracle-exadata.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Cloud](../teradata/teradata-cloud.md), [Teradata Factory](../teradata/teradata-factory.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Netezza Performance Server](../ibm/ibm-netezza.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Hadoop (HDFS and YARN)](../open-source/apache-hadoop.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
