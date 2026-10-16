---
type: Technology
id: teradata-database
title: Teradata Database
description: Shared-nothing MPP SQL database engine that underlies all Teradata deployments, with mixed-workload management, temporal tables and support for semi-structured data.
formerly: [Vantage Advanced SQL Engine]
platform: platform-teradata
kind: software
availability: ga
realises:
- sql-query-engine
- workload-management
- columnar-storage
- semi-structured-data
- time-series-data
- temporal-data
resource: https://www.teradata.com/platform
tags: [teradata]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Supports JSON and XML types, the DATASET type with Avro and CSV storage formats, reading and writing Parquet files in object storage through Native Object Store, temporal (period) tables, and time-series and geospatial functions. Teradata Active System Management (TASM) priorities and throttles let one system run tactical and strategic workloads together; this is often the main reason customers stay on Teradata.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SQL query engine](../../capabilities/compute/sql-query-engine.md) (Query and compute) (primary): Run analytical SQL over large datasets with parallel, optimised execution.
- [Workload management](../../capabilities/compute/workload-management.md) (Query and compute): Prioritise, queue and limit queries and jobs so the most important work meets its service levels.
- [Columnar storage](../../capabilities/storage/columnar-storage.md) (Storage and table management): Store data column by column with compression and statistics so analytical queries read only what they need.
- [Semi-structured data](../../capabilities/storage/semi-structured-data.md) (Storage and table management): Store and query nested data such as JSON without flattening it first.
- [Time-series data](../../capabilities/specialised-data/time-series-data.md) (Specialised data types): Store and query time-stamped measurements efficiently, with time-based functions and retention.
- [Bitemporal data](../../capabilities/specialised-data/temporal-data.md) (Specialised data types): Store and query data as it was true in the real world and as it was recorded in the system.

**Platform:** [Teradata](../../platforms/platform-teradata.md)  
**Availability:** ga  
**Product family:** Teradata Autonomous Knowledge Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift](../aws/aws-redshift.md), [Amazon Athena](../aws/aws-athena.md) | [Columnar storage](../../capabilities/storage/columnar-storage.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Workload management](../../capabilities/compute/workload-management.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Data Warehouse](../microsoft/fabric-data-warehouse.md), [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md), [Fabric SQL analytics endpoint](../microsoft/fabric-sql-analytics-endpoint.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Workload management](../../capabilities/compute/workload-management.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery](../google-cloud/gcp-bigquery.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake generation 2 standard warehouses](../snowflake/snowflake-gen2-warehouses.md), [Snowflake virtual warehouses](../snowflake/snowflake-virtual-warehouses.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Photon](../databricks/databricks-photon.md), [Databricks SQL](../databricks/databricks-sql.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md), [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md), [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md) | [Bitemporal data](../../capabilities/specialised-data/temporal-data.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md), [Dremio Cloud](../sap/dremio-cloud.md), [SAP HANA Cloud, data lake](../sap/sap-hana-cloud-data-lake.md) | [Bitemporal data](../../capabilities/specialised-data/temporal-data.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Db2](../ibm/ibm-db2.md), [IBM Netezza Performance Server](../ibm/ibm-netezza.md), [Presto (C++) engine in IBM watsonx.data](../ibm/ibm-watsonx-data-presto.md) | [Bitemporal data](../../capabilities/specialised-data/temporal-data.md), [Columnar storage](../../capabilities/storage/columnar-storage.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Presto](../open-source/presto.md), [Trino](../open-source/trino.md), [DuckDB](../open-source/duckdb.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Starburst Enterprise](../independent/starburst-enterprise.md), [Starburst Galaxy](../independent/starburst-galaxy.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
