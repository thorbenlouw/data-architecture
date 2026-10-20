---
type: Technology
id: presto
title: Presto
description: Distributed SQL query engine for interactive analytics over data lakes and federated sources, originally developed at Meta.
aliases: [PrestoDB, Presto C++]
platform: platform-open-source
kind: open-source
availability: ga
realises:
- sql-query-engine
- query-federation
- decoupled-storage-compute
- native-execution-acceleration
- approximate-query-processing
resource: https://prestodb.io/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, governed by the Presto Foundation under the Linux Foundation; IBM (watsonx.data) and Meta are major contributors. Presto C++ (native workers built on Velox) replaces the Java workers for better performance. Not to be confused with Trino, the 2019 fork.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SQL query engine](../../capabilities/compute/sql-query-engine.md) (Query and compute) (primary): Run analytical SQL over large datasets with parallel, optimised execution.
- [Query federation](../../capabilities/compute/query-federation.md) (Query and compute): Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.
- [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) (Query and compute): Scale storage and compute independently and let several compute clusters work on the same data.
- [Vectorised native execution](../../capabilities/compute/native-execution-acceleration.md) (Query and compute): Speed up engines by running operators in native, vectorised code without changing user code.
- [Approximate query processing](../../capabilities/compute/approximate-query-processing.md) (Query and compute): Answer aggregate queries faster and with less memory using sampling and probabilistic sketches.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Athena](../aws/aws-athena.md), [Amazon Redshift](../aws/aws-redshift.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md), [Fabric Data Warehouse](../microsoft/fabric-data-warehouse.md), [Fabric SQL analytics endpoint](../microsoft/fabric-sql-analytics-endpoint.md) | [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery](../google-cloud/gcp-bigquery.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake virtual warehouses](../snowflake/snowflake-virtual-warehouses.md), [Snowflake generation 2 standard warehouses](../snowflake/snowflake-gen2-warehouses.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Photon](../databricks/databricks-photon.md), [Databricks SQL](../databricks/databricks-sql.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Vectorised native execution](../../capabilities/compute/native-execution-acceleration.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md), [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md), [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Approximate query processing](../../capabilities/compute/approximate-query-processing.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md), [SAP HANA Cloud](../sap/sap-hana-cloud.md), [SAP HANA Cloud, data lake](../sap/sap-hana-cloud-data-lake.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database](../teradata/teradata-database.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [IBM](../../platforms/platform-ibm.md) | [Presto (C++) engine in IBM watsonx.data](../ibm/ibm-watsonx-data-presto.md), [IBM Netezza Performance Server](../ibm/ibm-netezza.md), [IBM Db2](../ibm/ibm-db2.md) | [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Vectorised native execution](../../capabilities/compute/native-execution-acceleration.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Cloud Analytic Services (CAS)](../sas/sas-cloud-analytic-services.md), [SAS SpeedyStore](../sas/sas-speedystore.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Starburst Enterprise](../independent/starburst-enterprise.md), [Starburst Galaxy](../independent/starburst-galaxy.md) | [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
