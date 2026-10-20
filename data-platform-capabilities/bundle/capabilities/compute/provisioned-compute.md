---
type: Capability
id: provisioned-compute
title: Provisioned compute
description: Run workloads on clusters or warehouses you size and control, for predictable performance and cost.
aliases: [clusters, virtual warehouses, dedicated capacity, job clusters]
broader: [compute-options]
related: [reserved-capacity, workload-isolation, cost-optimisation, infrastructure-as-code, elastic-scaling]
tags: [compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

You choose the size and number of nodes, or a warehouse size such as small, medium or large, and the platform runs that capacity, starting and stopping it on a schedule or when idle. You decide engine settings, libraries, instance types and autoscaling limits. A transformation cluster sized for the nightly load can start at 01:00, run at full use for two hours and shut down, giving known cost and performance.

It suits steady, heavy or performance-sensitive work, jobs that need special settings or libraries, and organisations that must forecast spend closely. The drawback is that you pay for capacity while it runs, used or not, and someone has to size and tune it. Auto-suspend, auto-resume and autoscaling within limits now blur the line with serverless; the remaining difference is who owns the sizing decision and whether idle time is charged.

# Key considerations

- Auto-suspend settings drive cost. Short idle timeouts save money but make the next user wait for start-up.
- Right-size from measured utilisation and review it regularly. Clusters sized for last year's peak are a common source of waste.
- One large shared cluster lowers cost but weakens isolation. Decide how workloads map to clusters.
- Define clusters in code with approved sizes and policies, so teams cannot create oversized or unmanaged ones.

# Questions to ask

- How steady and predictable is the workload's demand?
- Does the workload need custom libraries, instance types or engine settings?
- Who will size, tune and review the clusters over time?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Query and compute](compute.md) |
| Broader | [Compute provisioning options](compute-options.md) |
| Related | [Cost optimisation](../platform-operations/cost-optimisation.md), [Elastic scaling](elastic-scaling.md), [Infrastructure as code](../platform-operations/infrastructure-as-code.md), [Reserved and committed capacity](reserved-capacity.md), [Workload isolation](workload-isolation.md) |

# Where it appears

- **Personas:** [FinOps practitioner](../../personas/persona-finops-practitioner.md)
- **Maturity tracks:** [Compute and workload management](../../maturity/track-compute.md) (from level 1, Initial)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon EMR on EC2](../../technologies/aws/aws-emr-on-ec2.md), [Amazon Redshift](../../technologies/aws/aws-redshift.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Capacity (F SKU) | [Azure Synapse Analytics](../../technologies/microsoft/azure-synapse-analytics.md), [Microsoft Fabric capacities (F SKUs)](../../technologies/microsoft/fabric-capacities.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | BigQuery editions reservations (slots) | [BigQuery editions](../../technologies/google-cloud/gcp-bigquery-editions.md), [Google Cloud Managed Service for Apache Spark on clusters](../../technologies/google-cloud/gcp-managed-spark-clusters.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | virtual warehouses | [Snowflake generation 2 standard warehouses](../../technologies/snowflake/snowflake-gen2-warehouses.md), [Snowflake virtual warehouses](../../technologies/snowflake/snowflake-virtual-warehouses.md), [Snowpark-optimized warehouses](../../technologies/snowflake/snowflake-snowpark-optimized-warehouses.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks classic compute (Databricks Runtime clusters)](../../technologies/databricks/databricks-classic-compute.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | Data Hub clusters | [Cloudera Base on premises](../../technologies/cloudera/cloudera-base-on-premises.md), [Cloudera on cloud](../../technologies/cloudera/cloudera-on-cloud.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Exadata](../../technologies/oracle/oracle-exadata.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Cloud](../../technologies/teradata/teradata-cloud.md), [Teradata Factory](../../technologies/teradata/teradata-factory.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM Netezza Performance Server](../../technologies/ibm/ibm-netezza.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS Managed Cloud Services](../../technologies/sas/sas-managed-cloud-services.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Hadoop (HDFS and YARN)](../../technologies/open-source/apache-hadoop.md) |
