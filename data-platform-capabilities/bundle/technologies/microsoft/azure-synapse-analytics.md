---
type: Technology
id: azure-synapse-analytics
title: Azure Synapse Analytics
description: Analytics workspace combining dedicated SQL pools (MPP warehouse), serverless SQL over the lake, Apache Spark pools and pipelines.
aliases: [Azure Synapse]
formerly: [Azure SQL Data Warehouse]
platform: platform-microsoft
kind: managed-service
availability: ga
realises: [sql-query-engine, distributed-processing, provisioned-compute, query-federation]
resource: https://learn.microsoft.com/en-us/azure/synapse-analytics/overview-what-is
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

No retirement announced, but little new development; Spark is held at 3.4. Synapse Data Explorer was retired on 7 October 2025 and the storage trusted-services exception ended on 1 August 2026. Microsoft steers new and migrating workloads to Fabric Data Warehouse, Spark and Data Factory.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SQL query engine](../../capabilities/compute/sql-query-engine.md) (Query and compute) (primary): Run analytical SQL over large datasets with parallel, optimised execution.
- [Distributed processing](../../capabilities/processing/distributed-processing.md) (Processing and transformation): Process large datasets in parallel across a cluster of machines.
- [Provisioned compute](../../capabilities/compute/provisioned-compute.md) (Query and compute): Run workloads on clusters or warehouses you size and control, for predictable performance and cost.
- [Query federation](../../capabilities/compute/query-federation.md) (Query and compute): Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Athena](../aws/aws-athena.md), [Amazon Redshift](../aws/aws-redshift.md) | [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery](../google-cloud/gcp-bigquery.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake generation 2 standard warehouses](../snowflake/snowflake-gen2-warehouses.md), [Snowflake virtual warehouses](../snowflake/snowflake-virtual-warehouses.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Photon](../databricks/databricks-photon.md), [Databricks SQL](../databricks/databricks-sql.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md), [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md), [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md), [SAP HANA Cloud](../sap/sap-hana-cloud.md), [SAP HANA Cloud, data lake](../sap/sap-hana-cloud-data-lake.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database](../teradata/teradata-database.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Netezza Performance Server](../ibm/ibm-netezza.md), [Presto (C++) engine in IBM watsonx.data](../ibm/ibm-watsonx-data-presto.md), [IBM Db2](../ibm/ibm-db2.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Presto](../open-source/presto.md), [Trino](../open-source/trino.md), [DuckDB](../open-source/duckdb.md) | [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Starburst Enterprise](../independent/starburst-enterprise.md), [Starburst Galaxy](../independent/starburst-galaxy.md) | [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
