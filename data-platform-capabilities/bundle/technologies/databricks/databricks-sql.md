---
type: Technology
id: databricks-sql
title: Databricks SQL
description: The data warehousing product on the lakehouse. It includes the SQL editor, queries, ANSI SQL engine, SQL transformations, materialised views and BI connectivity, running on SQL warehouses.
aliases: [DBSQL]
platform: platform-databricks
kind: managed-service
availability: ga
realises: [sql-query-engine, ad-hoc-analysis, sql-transformation, query-performance-analysis]
resource: https://docs.databricks.com/aws/en/compute/sql-warehouse/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

In May 2026 the "SQL" section of the workspace sidebar was renamed "Lakehouse", and dashboards, Genie Agents and alerts moved to a new "Analytics" section. The product is still called Databricks SQL. Query history, query profiles and system.query.history (GA September 2026) support tuning, and query tags (GA September 2026) support cost attribution.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SQL query engine](../../capabilities/compute/sql-query-engine.md) (Query and compute) (primary): Run analytical SQL over large datasets with parallel, optimised execution.
- [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) (Analytics and BI): Explore data freely with SQL editors, pivots and visual exploration to answer one-off questions.
- [SQL transformation](../../capabilities/processing/sql-transformation.md) (Processing and transformation): Transform data inside the platform using SQL, typically after it has been loaded.
- [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) (Platform operations): Inspect query plans, job stages, run history and bottlenecks to tune performance and cost.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Databricks SQL

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift](../aws/aws-redshift.md), [Amazon Athena](../aws/aws-athena.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md), [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Data Warehouse](../microsoft/fabric-data-warehouse.md), [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md), [Fabric SQL analytics endpoint](../microsoft/fabric-sql-analytics-endpoint.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md), [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery](../google-cloud/gcp-bigquery.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake generation 2 standard warehouses](../snowflake/snowflake-gen2-warehouses.md), [Snowflake virtual warehouses](../snowflake/snowflake-virtual-warehouses.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md), [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md), [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md), [SAP HANA Cloud, data lake](../sap/sap-hana-cloud-data-lake.md), [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database](../teradata/teradata-database.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Netezza Performance Server](../ibm/ibm-netezza.md), [Presto (C++) engine in IBM watsonx.data](../ibm/ibm-watsonx-data-presto.md), [IBM Db2](../ibm/ibm-db2.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Cloud Analytic Services (CAS)](../sas/sas-cloud-analytic-services.md), [SAS SpeedyStore](../sas/sas-speedystore.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Presto](../open-source/presto.md), [Trino](../open-source/trino.md), [Apache DataFusion](../open-source/apache-datafusion.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Starburst Enterprise](../independent/starburst-enterprise.md), [Starburst Galaxy](../independent/starburst-galaxy.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
