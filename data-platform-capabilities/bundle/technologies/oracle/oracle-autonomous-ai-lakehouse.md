---
type: Technology
id: oracle-autonomous-ai-lakehouse
title: Oracle Autonomous AI Lakehouse
description: The analytics workload type of Autonomous AI Database, which runs Oracle SQL over its own tables and over Apache Iceberg tables in object storage registered in external catalogues.
formerly: [Oracle Autonomous Data Warehouse, ADW]
platform: platform-oracle
kind: managed-service
availability: ga
realises: [sql-query-engine, open-table-formats, engine-interoperability, query-federation, elastic-scaling]
resource: https://www.oracle.com/news/announcement/ai-world-oracle-introduces-autonomous-ai-lakehouse-2025-10-14/
tags: [oracle]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Announced in October 2025, when Autonomous Data Warehouse instances were converted automatically. It reads Iceberg tables through AWS Glue, Databricks Unity Catalog and Polaris-based catalogues, and the Data Lake Accelerator adds pay-per-use network and compute for large Iceberg scans. Runs on OCI, AWS, Azure, Google Cloud and Exadata Cloud@Customer.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SQL query engine](../../capabilities/compute/sql-query-engine.md) (Query and compute) (primary): Run analytical SQL over large datasets with parallel, optimised execution.
- [Open table formats](../../capabilities/storage/open-table-formats.md) (Storage and table management): Manage collections of files as transactional tables with a defined schema, history and metadata.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.
- [Query federation](../../capabilities/compute/query-federation.md) (Query and compute): Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.
- [Elastic scaling](../../capabilities/compute/elastic-scaling.md) (Query and compute): Add and remove compute automatically as load changes, including for bursts of concurrent users.

**Platform:** [Oracle](../../platforms/platform-oracle.md)  
**Availability:** ga  
**Product family:** Oracle Autonomous AI Database

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Athena](../aws/aws-athena.md), [Amazon Redshift](../aws/aws-redshift.md) | [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md), [Fabric Data Warehouse](../microsoft/fabric-data-warehouse.md), [Fabric SQL analytics endpoint](../microsoft/fabric-sql-analytics-endpoint.md) | [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Elastic scaling](../../capabilities/compute/elastic-scaling.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery](../google-cloud/gcp-bigquery.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake generation 2 standard warehouses](../snowflake/snowflake-gen2-warehouses.md), [Snowflake virtual warehouses](../snowflake/snowflake-virtual-warehouses.md), [pg_lake](../snowflake/snowflake-pg-lake.md) (preview) | [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Photon](../databricks/databricks-photon.md), [Databricks SQL](../databricks/databricks-sql.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md), [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../clickhouse/clickhouse-data-lake.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md), [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md), [SAP HANA Cloud](../sap/sap-hana-cloud.md), [SAP HANA Cloud, data lake](../sap/sap-hana-cloud-data-lake.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database](../teradata/teradata-database.md), [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Netezza Performance Server](../ibm/ibm-netezza.md), [Presto (C++) engine in IBM watsonx.data](../ibm/ibm-watsonx-data-presto.md), [IBM Db2](../ibm/ibm-db2.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Cloud Analytic Services (CAS)](../sas/sas-cloud-analytic-services.md), [SAS SpeedyStore](../sas/sas-speedystore.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Trino](../open-source/trino.md), [Presto](../open-source/presto.md), [DuckDB](../open-source/duckdb.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Starburst Galaxy](../independent/starburst-galaxy.md), [Starburst Enterprise](../independent/starburst-enterprise.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
