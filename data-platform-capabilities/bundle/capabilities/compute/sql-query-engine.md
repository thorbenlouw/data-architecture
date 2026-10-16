---
type: Capability
id: sql-query-engine
title: SQL query engine
description: Run analytical SQL over large datasets with parallel, optimised execution.
aliases: [MPP, data warehouse engine]
broader: [compute]
related:
- sql-transformation
- distributed-processing
- single-node-processing
- query-performance-analysis
- ad-hoc-analysis
tags: [compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A SQL query engine turns a query into a plan of operators, such as scans, filters, joins and aggregations, and runs that plan in parallel across many cores and machines. In massively parallel processing (MPP), each worker scans and aggregates its share of the data, then workers exchange intermediate results by join or grouping key and combine them. A cost-based optimiser uses table statistics to choose join order and method, for example sending a small dimension table to every worker rather than moving a billion-row fact table across the network. Trino, Spark SQL and, on a single machine, DuckDB are open-source examples.

It is the workhorse for BI, ad hoc analysis and most transformation. Engines differ in latency (sub-second interactive or minutes-long batch), tolerance of node failures in long queries, SQL dialect and handling of many concurrent users. They also differ in what they read: their own managed storage, open table formats, or both. Real-time analytical databases are a specialised kind tuned for millisecond answers on fresh data.

# Key considerations

- Check SQL compatibility in detail. Window functions, MERGE, nested data, time zones and NULL handling vary between dialects.
- Statistics drive good plans. Make sure they are collected and kept fresh on open tables as well as managed ones.
- Large data exchanges between workers and skewed join keys cause most slow or failed queries. Look for spill-to-disk and skew handling.
- Engines built for interactive queries may restart a whole query when one node fails, which hurts two-hour batch jobs.

# Questions to ask

- What mix of interactive, reporting and batch queries will the engine serve?
- How many concurrent users and queries are expected at peak?
- Which SQL dialect do existing code and skills use?
- Which table formats and catalogues must the engine read and write?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Query and compute](compute.md) |
| Broader | [Query and compute](compute.md) |
| Related | [Processing and transformation](../processing/processing.md), [Specialised data types](../specialised-data/specialised-data.md), [Ad hoc analysis](../analytics-bi/ad-hoc-analysis.md), [Columnar storage](../storage/columnar-storage.md), [Distributed processing](../processing/distributed-processing.md), [Query and job performance analysis](../platform-operations/query-performance-analysis.md), [Single-node processing](../processing/single-node-processing.md), [SQL transformation](../processing/sql-transformation.md) |
| Needed by | [Ad hoc analysis](../analytics-bi/ad-hoc-analysis.md), [In-database machine learning](../machine-learning/in-database-ml.md), [Materialised views](materialised-views.md), [Query and job performance analysis](../platform-operations/query-performance-analysis.md), [Query federation](query-federation.md), [Semantic layer](../analytics-bi/semantic-layer.md), [SQL and programmatic access](../serving/sql-access.md), [SQL transformation](../processing/sql-transformation.md) |

# Where it appears

- **Use cases:** [Operational reporting](../../use-cases/usecase-operational-reporting.md) (requires, level 2) · [Self-service BI](../../use-cases/usecase-self-service-bi.md) (requires, level 2)
- **Patterns:** [Data warehouse](../../patterns/data-warehouse.md)
- **Maturity tracks:** [Compute and workload management](../../maturity/track-compute.md) (from level 1, Initial)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Warehousing and Business Intelligence

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Amazon Athena; Amazon Redshift | [Amazon Athena](../../technologies/aws/aws-athena.md), [Amazon Redshift](../../technologies/aws/aws-redshift.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Synapse Analytics](../../technologies/microsoft/azure-synapse-analytics.md), [Fabric Data Warehouse](../../technologies/microsoft/fabric-data-warehouse.md), [Fabric SQL analytics endpoint](../../technologies/microsoft/fabric-sql-analytics-endpoint.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery](../../technologies/google-cloud/gcp-bigquery.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake generation 2 standard warehouses](../../technologies/snowflake/snowflake-gen2-warehouses.md), [Snowflake virtual warehouses](../../technologies/snowflake/snowflake-virtual-warehouses.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Photon](../../technologies/databricks/databricks-photon.md), [Databricks SQL](../../technologies/databricks/databricks-sql.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse server](../../technologies/clickhouse/clickhouse-server.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Base on premises](../../technologies/cloudera/cloudera-base-on-premises.md), [Cloudera Data Warehouse](../../technologies/cloudera/cloudera-data-warehouse.md) |
| [Oracle](../../platforms/platform-oracle.md) | Autonomous AI Lakehouse | [Oracle AI Database 26ai](../../technologies/oracle/oracle-ai-database-26ai.md), [Oracle Autonomous AI Lakehouse](../../technologies/oracle/oracle-autonomous-ai-lakehouse.md) |
| [SAP](../../platforms/platform-sap.md) |  | [Dremio Cloud](../../technologies/sap/dremio-cloud.md), [SAP HANA Cloud](../../technologies/sap/sap-hana-cloud.md), [SAP HANA Cloud, data lake](../../technologies/sap/sap-hana-cloud-data-lake.md), [SAP Snowflake](../../technologies/sap/sap-snowflake.md) (unconfirmed; distribution of Snowflake) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Database](../../technologies/teradata/teradata-database.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM Db2](../../technologies/ibm/ibm-db2.md), [IBM Netezza Performance Server](../../technologies/ibm/ibm-netezza.md), [Presto (C++) engine in IBM watsonx.data](../../technologies/ibm/ibm-watsonx-data-presto.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache DataFusion](../../technologies/open-source/apache-datafusion.md), [Apache Doris](../../technologies/open-source/apache-doris.md), [DuckDB](../../technologies/open-source/duckdb.md), [Presto](../../technologies/open-source/presto.md), [StarRocks](../../technologies/open-source/starrocks.md), [Trino](../../technologies/open-source/trino.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Starburst Enterprise](../../technologies/independent/starburst-enterprise.md), [Starburst Galaxy](../../technologies/independent/starburst-galaxy.md) |
