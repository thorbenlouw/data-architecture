---
type: Technology
id: oracle-ai-database-26ai
title: Oracle AI Database 26ai
description: Oracle's converged database release that supports relational, JSON, graph, spatial, text and vector data in one engine for transactional and analytical work.
aliases: [Oracle Database, Oracle AI Database, Oracle Machine Learning]
formerly: [Oracle Database 23ai, Oracle Database 23c]
platform: platform-oracle
kind: software
availability: ga
realises:
- sql-query-engine
- semi-structured-data
- graph-data
- geospatial-data
- operational-database
- temporal-data
- approximate-query-processing
- full-text-search
- in-database-ml
resource: https://www.oracle.com/database/ai-native-database-26ai/
tags: [oracle]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A long-term-support release that replaces 23ai; existing 23ai databases move to it by applying the October 2025 release update rather than a full upgrade. JSON Relational Duality views, property graphs (SQL/PGQ), AI Vector Search and Oracle Machine Learning, which trains and scores models with SQL, Python and R inside the database, are included at no extra charge. Real Application Clusters and Data Guard remain the standard high-availability and disaster-recovery options.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SQL query engine](../../capabilities/compute/sql-query-engine.md) (Query and compute) (primary): Run analytical SQL over large datasets with parallel, optimised execution.
- [Semi-structured data](../../capabilities/storage/semi-structured-data.md) (Storage and table management): Store and query nested data such as JSON without flattening it first.
- [Graph data](../../capabilities/specialised-data/graph-data.md) (Specialised data types): Model and query connected data as nodes and relationships.
- [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) (Specialised data types): Store, index and analyse location and shape data with spatial types and functions.
- [Operational database integration](../../capabilities/serving/operational-database.md) (Serving and activation): Run transactional databases as part of the platform, with data flowing to and from analytical storage without separate pipelines.
- [Bitemporal data](../../capabilities/specialised-data/temporal-data.md) (Specialised data types): Store and query data as it was true in the real world and as it was recorded in the system.
- [Approximate query processing](../../capabilities/compute/approximate-query-processing.md) (Query and compute): Answer aggregate queries faster and with less memory using sampling and probabilistic sketches.
- [Full-text search](../../capabilities/specialised-data/full-text-search.md) (Specialised data types): Index text for full-text search, relevance ranking and fast filtering.
- [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) (Machine learning development): Train and run models using SQL inside the data platform.

**Platform:** [Oracle](../../platforms/platform-oracle.md)  
**Availability:** ga  
**Product family:** Oracle AI Database

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift](../aws/aws-redshift.md), [Amazon Athena](../aws/aws-athena.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md), [Fabric Data Warehouse](../microsoft/fabric-data-warehouse.md), [Fabric SQL analytics endpoint](../microsoft/fabric-sql-analytics-endpoint.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery](../google-cloud/gcp-bigquery.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake generation 2 standard warehouses](../snowflake/snowflake-gen2-warehouses.md), [Snowflake virtual warehouses](../snowflake/snowflake-virtual-warehouses.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Photon](../databricks/databricks-photon.md), [Databricks SQL](../databricks/databricks-sql.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md), [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md), [Dremio Cloud](../sap/dremio-cloud.md), [SAP HANA Cloud, data lake](../sap/sap-hana-cloud-data-lake.md) | [Bitemporal data](../../capabilities/specialised-data/temporal-data.md), [Geospatial data](../../capabilities/specialised-data/geospatial-data.md), [Graph data](../../capabilities/specialised-data/graph-data.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database](../teradata/teradata-database.md) | [Bitemporal data](../../capabilities/specialised-data/temporal-data.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Netezza Performance Server](../ibm/ibm-netezza.md), [Presto (C++) engine in IBM watsonx.data](../ibm/ibm-watsonx-data-presto.md), [IBM Db2](../ibm/ibm-db2.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Bitemporal data](../../capabilities/specialised-data/temporal-data.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Presto](../open-source/presto.md), [Trino](../open-source/trino.md), [DuckDB](../open-source/duckdb.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Starburst Enterprise](../independent/starburst-enterprise.md), [Starburst Galaxy](../independent/starburst-galaxy.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
