---
type: Technology
id: cloudera-data-warehouse
title: Cloudera Data Warehouse
description: Containerised SQL service in which teams create isolated, autoscaling Virtual Warehouses running Impala, Hive LLAP or Trino over shared data lake tables.
aliases: [CDW, Cloudera Data Explorer]
platform: platform-cloudera
kind: managed-service
availability: ga
realises:
- sql-query-engine
- workload-isolation
- elastic-scaling
- query-federation
- result-caching
- approximate-query-processing
- materialised-views
- ad-hoc-analysis
resource: https://docs.cloudera.com/data-warehouse/cloud/release-notes/topics/dw-whats-new-r46.html
tags: [cloudera]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Trino Virtual Warehouses provide federation connectors (Oracle, Kudu, Hive, Impala and others) and, from September 2026, query-level fault tolerance. Hive Virtual Warehouses support materialised views with automatic query rewriting, and Impala has an intermediate results cache. It bundles Cloudera Data Visualization and Cloudera Data Explorer (Hue), an SQL editor whose AI assistant turns natural-language questions into SQL.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SQL query engine](../../capabilities/compute/sql-query-engine.md) (Query and compute) (primary): Run analytical SQL over large datasets with parallel, optimised execution.
- [Workload isolation](../../capabilities/compute/workload-isolation.md) (Query and compute): Run different workloads on separate compute so one cannot slow or starve another.
- [Elastic scaling](../../capabilities/compute/elastic-scaling.md) (Query and compute): Add and remove compute automatically as load changes, including for bursts of concurrent users.
- [Query federation](../../capabilities/compute/query-federation.md) (Query and compute): Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.
- [Result caching](../../capabilities/compute/result-caching.md) (Query and compute): Return results of repeated queries from a cache without recomputing them.
- [Approximate query processing](../../capabilities/compute/approximate-query-processing.md) (Query and compute): Answer aggregate queries faster and with less memory using sampling and probabilistic sketches.
- [Materialised views](../../capabilities/compute/materialised-views.md) (Query and compute): Have the query engine store a query's result, refresh it as sources change and optionally use it to answer other queries.
- [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) (Analytics and BI): Explore data freely with SQL editors, pivots and visual exploration to answer one-off questions.

**Platform:** [Cloudera](../../platforms/platform-cloudera.md)  
**Availability:** ga  
**Product family:** Cloudera Open Data Lakehouse

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Athena](../aws/aws-athena.md), [Amazon Redshift](../aws/aws-redshift.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Query federation](../../capabilities/compute/query-federation.md), [Result caching](../../capabilities/compute/result-caching.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md), [Fabric Data Warehouse](../microsoft/fabric-data-warehouse.md), [Fabric SQL analytics endpoint](../microsoft/fabric-sql-analytics-endpoint.md) | [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Elastic scaling](../../capabilities/compute/elastic-scaling.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery](../google-cloud/gcp-bigquery.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake virtual warehouses](../snowflake/snowflake-virtual-warehouses.md), [Snowflake generation 2 standard warehouses](../snowflake/snowflake-gen2-warehouses.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Workload isolation](../../capabilities/compute/workload-isolation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL](../databricks/databricks-sql.md), [Databricks Photon](../databricks/databricks-photon.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md), [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Approximate query processing](../../capabilities/compute/approximate-query-processing.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md), [SAP HANA Cloud](../sap/sap-hana-cloud.md), [SAP HANA Cloud, data lake](../sap/sap-hana-cloud-data-lake.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database](../teradata/teradata-database.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [IBM](../../platforms/platform-ibm.md) | [Presto (C++) engine in IBM watsonx.data](../ibm/ibm-watsonx-data-presto.md), [IBM Netezza Performance Server](../ibm/ibm-netezza.md), [IBM Db2](../ibm/ibm-db2.md) | [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Presto](../open-source/presto.md), [Trino](../open-source/trino.md), [Apache Doris](../open-source/apache-doris.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Starburst Enterprise](../independent/starburst-enterprise.md), [Starburst Galaxy](../independent/starburst-galaxy.md) | [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
