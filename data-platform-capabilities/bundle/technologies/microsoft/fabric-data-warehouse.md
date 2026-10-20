---
type: Technology
id: fabric-data-warehouse
title: Fabric Data Warehouse
description: A T-SQL warehouse with multi-table transactions that stores its tables as Delta Parquet in OneLake and scales compute automatically.
aliases: [Fabric Warehouse]
formerly: [Synapse Data Warehouse]
platform: platform-microsoft
kind: feature
availability: ga
realises:
- sql-query-engine
- sql-transformation
- acid-transactions
- managed-storage
- workload-management
- code-translation
- elastic-scaling
resource: https://learn.microsoft.com/en-us/fabric/data-warehouse/data-warehousing
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Target for Synapse dedicated SQL pool migrations, helped by the Migration Assistant (Synapse, SQL Server, Teradata in preview). Custom SQL pools for workload isolation and GPU acceleration are in preview; outbound access protection and SQL audit logs became GA in March 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SQL query engine](../../capabilities/compute/sql-query-engine.md) (Query and compute) (primary): Run analytical SQL over large datasets with parallel, optimised execution.
- [SQL transformation](../../capabilities/processing/sql-transformation.md) (Processing and transformation): Transform data inside the platform using SQL, typically after it has been loaded.
- [ACID transactions](../../capabilities/storage/acid-transactions.md) (Storage and table management): Commit concurrent writes atomically so readers never see partial or conflicting results.
- [Platform-managed storage](../../capabilities/storage/managed-storage.md) (Storage and table management): Let the platform manage table storage layout, compression and durability internally.
- [Workload management](../../capabilities/compute/workload-management.md) (Query and compute): Prioritise, queue and limit queries and jobs so the most important work meets its service levels.
- [Code and SQL translation](../../capabilities/platform-operations/code-translation.md) (Platform operations): Convert SQL dialects, stored procedures and ETL jobs automatically to run on a target platform.
- [Elastic scaling](../../capabilities/compute/elastic-scaling.md) (Query and compute): Add and remove compute automatically as load changes, including for bursts of concurrent users.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Fabric Data Warehouse

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift](../aws/aws-redshift.md), [Amazon Athena](../aws/aws-athena.md) | [Platform-managed storage](../../capabilities/storage/managed-storage.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md), [SQL transformation](../../capabilities/processing/sql-transformation.md), [Workload management](../../capabilities/compute/workload-management.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery](../google-cloud/gcp-bigquery.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake generation 2 standard warehouses](../snowflake/snowflake-gen2-warehouses.md), [Snowflake virtual warehouses](../snowflake/snowflake-virtual-warehouses.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL](../databricks/databricks-sql.md), [Databricks Photon](../databricks/databricks-photon.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md), [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md), [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md), [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md), [SAP HANA Cloud, data lake](../sap/sap-hana-cloud-data-lake.md), [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database](../teradata/teradata-database.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Workload management](../../capabilities/compute/workload-management.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Netezza Performance Server](../ibm/ibm-netezza.md), [Presto (C++) engine in IBM watsonx.data](../ibm/ibm-watsonx-data-presto.md), [IBM Db2](../ibm/ibm-db2.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Cloud Analytic Services (CAS)](../sas/sas-cloud-analytic-services.md), [SAS SpeedyStore](../sas/sas-speedystore.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Presto](../open-source/presto.md), [Trino](../open-source/trino.md), [Apache DataFusion](../open-source/apache-datafusion.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Starburst Enterprise](../independent/starburst-enterprise.md), [Starburst Galaxy](../independent/starburst-galaxy.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
