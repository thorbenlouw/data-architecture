---
type: Technology
id: oracle-exadata
title: Oracle Exadata
description: Engineered database platform with scale-out storage servers that offload SQL filtering and caching, available on premises, as Exadata Database Service on OCI and as Exadata Cloud@Customer.
aliases: [Exadata Cloud@Customer, Exadata Database Service, Exadata Exascale]
platform: platform-oracle
kind: software
availability: ga
realises: [provisioned-compute, query-acceleration, data-skipping-indexes, hybrid-data-plane]
resource: https://www.oracle.com/engineered-systems/exadata/
tags: [oracle]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Exadata Exascale adds a multi-tenant, pay-per-use storage and compute model. Smart Scan and storage indexes reduce data read for analytical queries; Exadata Table Cache was added for lakehouse use. Underpins Autonomous AI Database.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Provisioned compute](../../capabilities/compute/provisioned-compute.md) (Query and compute) (primary): Run workloads on clusters or warehouses you size and control, for predictable performance and cost.
- [Query acceleration](../../capabilities/compute/query-acceleration.md) (Query and compute): Speed up repeated or selective queries using caches, precomputed results and indexes.
- [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) (Query and compute): Use indexes, statistics and filters to avoid scanning data that cannot match a query.
- [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) (Platform operations): Run processing inside your own network or cloud account while the vendor operates the control plane as a service.

**Platform:** [Oracle](../../platforms/platform-oracle.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon EMR on EC2](../aws/aws-emr-on-ec2.md), [Amazon Redshift](../aws/aws-redshift.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Fabric capacities (F SKUs)](../microsoft/fabric-capacities.md), [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery editions](../google-cloud/gcp-bigquery-editions.md), [Google Cloud Managed Service for Apache Spark on clusters](../google-cloud/gcp-managed-spark-clusters.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake generation 2 standard warehouses](../snowflake/snowflake-gen2-warehouses.md), [Snowpark-optimized warehouses](../snowflake/snowflake-snowpark-optimized-warehouses.md), [Snowflake virtual warehouses](../snowflake/snowflake-virtual-warehouses.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse projections](../clickhouse/clickhouse-projections.md) | [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md), [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera on cloud](../cloudera/cloudera-on-cloud.md), [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Cloud](../teradata/teradata-cloud.md), [Teradata Factory](../teradata/teradata-factory.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Netezza Performance Server](../ibm/ibm-netezza.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Managed Cloud Services](../sas/sas-managed-cloud-services.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Hadoop (HDFS and YARN)](../open-source/apache-hadoop.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
