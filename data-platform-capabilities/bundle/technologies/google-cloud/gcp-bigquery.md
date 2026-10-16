---
type: Technology
id: gcp-bigquery
title: BigQuery
description: Serverless analytical database that runs GoogleSQL over managed and open-format tables with storage and compute billed and scaled separately.
aliases: [BQ]
platform: platform-google-cloud
kind: managed-service
availability: ga
realises:
- sql-query-engine
- serverless-compute
- decoupled-storage-compute
- semi-structured-data
- sql-access
- approximate-query-processing
resource: https://docs.cloud.google.com/bigquery/docs/introduction
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Compute is either on-demand (per TiB scanned) or slot-based through [BigQuery editions](../google-cloud/gcp-bigquery-editions.md); storage is billed separately on logical or physical bytes. A native JSON type, the Storage Read API, JDBC and ODBC drivers and a 24-hour cache of query results are built in. Related features include [BigQuery managed storage](../google-cloud/gcp-bigquery-managed-storage.md), [BigQuery ML](../google-cloud/gcp-bigquery-ml.md), [BigQuery sharing](../google-cloud/gcp-bigquery-sharing.md) and [BigQuery workload management](../google-cloud/gcp-bigquery-workload-management.md).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SQL query engine](../../capabilities/compute/sql-query-engine.md) (Query and compute) (primary): Run analytical SQL over large datasets with parallel, optimised execution.
- [Serverless compute](../../capabilities/compute/serverless-compute.md) (Query and compute): Run workloads without managing servers, with capacity allocated on demand and billed by use.
- [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) (Query and compute): Scale storage and compute independently and let several compute clusters work on the same data.
- [Semi-structured data](../../capabilities/storage/semi-structured-data.md) (Storage and table management): Store and query nested data such as JSON without flattening it first.
- [SQL and programmatic access](../../capabilities/serving/sql-access.md) (Serving and activation): Connect tools and code to the platform through standard drivers and protocols.
- [Approximate query processing](../../capabilities/compute/approximate-query-processing.md) (Query and compute): Answer aggregate queries faster and with less memory using sampling and probabilistic sketches.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Athena](../aws/aws-athena.md), [Amazon Redshift](../aws/aws-redshift.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Serverless compute](../../capabilities/compute/serverless-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric SQL analytics endpoint](../microsoft/fabric-sql-analytics-endpoint.md), [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md), [Fabric Data Warehouse](../microsoft/fabric-data-warehouse.md) | [SQL and programmatic access](../../capabilities/serving/sql-access.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake virtual warehouses](../snowflake/snowflake-virtual-warehouses.md), [Snowflake generation 2 standard warehouses](../snowflake/snowflake-gen2-warehouses.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Photon](../databricks/databricks-photon.md), [Databricks SQL](../databricks/databricks-sql.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md), [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md), [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md), [SAP HANA Cloud](../sap/sap-hana-cloud.md), [SAP HANA Cloud, data lake](../sap/sap-hana-cloud-data-lake.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database](../teradata/teradata-database.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Netezza Performance Server](../ibm/ibm-netezza.md), [Presto (C++) engine in IBM watsonx.data](../ibm/ibm-watsonx-data-presto.md), [IBM Db2](../ibm/ibm-db2.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Presto](../open-source/presto.md), [Trino](../open-source/trino.md), [DuckDB](../open-source/duckdb.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Starburst Enterprise](../independent/starburst-enterprise.md), [Starburst Galaxy](../independent/starburst-galaxy.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
