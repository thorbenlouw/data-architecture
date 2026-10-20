---
type: Technology
id: clickhouse-integration-engines
title: ClickHouse integration table engines and table functions
description: Engines and functions such as postgresql, mysql, mongodb, s3, url, jdbc, odbc and arrowflight that read from and write to external databases and storage directly in SQL.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [query-federation, database-extraction, data-export, file-formats]
resource: https://clickhouse.com/docs/engines/table-engines/integrations
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Used for one-off loads (INSERT INTO ... SELECT FROM postgresql(...)), live federated lookups and exports to files in S3, GCS or Azure in formats such as Parquet. Over 70 input and output formats are supported. JDBC/ODBC bridges are self-managed only.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Query federation](../../capabilities/compute/query-federation.md) (Query and compute) (primary): Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.
- [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) (Ingestion and integration): Extract full or incremental snapshots from relational and NoSQL databases using queries or bulk export.
- [Data export](../../capabilities/serving/data-export.md) (Serving and activation): Unload query results or tables to files and external systems in bulk.
- [Open file formats](../../capabilities/storage/file-formats.md) (Storage and table management): Store data in open, well-specified file formats such as Parquet, ORC, Avro and JSON.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga  
**Product family:** ClickHouse table engines

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift federated query](../aws/aws-redshift-federated-query.md), [Amazon Athena](../aws/aws-athena.md), [Amazon Redshift Spectrum](../aws/aws-redshift-spectrum.md) | [Query federation](../../capabilities/compute/query-federation.md), [Data export](../../capabilities/serving/data-export.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake shortcuts](../microsoft/fabric-onelake-shortcuts.md), [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery federated queries](../google-cloud/gcp-bigquery-federated-queries.md), [BigQuery external tables and load jobs](../google-cloud/gcp-bigquery-external-tables.md), [BigQuery Omni](../google-cloud/gcp-bigquery-omni.md) | [Query federation](../../capabilities/compute/query-federation.md), [Open file formats](../../capabilities/storage/file-formats.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake external tables](../snowflake/snowflake-external-tables.md) | [Open file formats](../../capabilities/storage/file-formats.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakehouse Federation (query federation)](../databricks/databricks-lakehouse-federation.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md), [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md), [SAP Datasphere](../sap/sap-datasphere.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Fabric](../teradata/teradata-fabric.md), [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [IBM](../../platforms/platform-ibm.md) | [Presto (C++) engine in IBM watsonx.data](../ibm/ibm-watsonx-data-presto.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Data export](../../capabilities/serving/data-export.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Hub](../sas/sas-data-hub.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [DuckDB](../open-source/duckdb.md), [Presto](../open-source/presto.md), [Trino](../open-source/trino.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Denodo Platform](../independent/denodo-platform.md), [Starburst Enterprise](../independent/starburst-enterprise.md), [StarTree Cloud](../independent/startree-cloud.md) | [Query federation](../../capabilities/compute/query-federation.md) |
