---
type: Technology
id: snowflake-semi-structured-data
title: Snowflake semi-structured data types (VARIANT, OBJECT, ARRAY)
description: Stores JSON, Avro, ORC, Parquet and XML in VARIANT, OBJECT and ARRAY columns, extracting columns for pruning, and queries them with path notation and FLATTEN.
platform: platform-snowflake
kind: feature
availability: ga
realises: [semi-structured-data, file-formats]
resource: https://docs.snowflake.com/en/user-guide/semistructured-intro
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Structured OBJECT and ARRAY types with declared schemas are also available, and Iceberg tables need them.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Semi-structured data](../../capabilities/storage/semi-structured-data.md) (Storage and table management) (primary): Store and query nested data such as JSON without flattening it first.
- [Open file formats](../../capabilities/storage/file-formats.md) (Storage and table management): Store data in open, well-specified file formats such as Parquet, ORC, Avro and JSON.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift](../aws/aws-redshift.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Explorer](../microsoft/azure-data-explorer.md), [Cosmos DB in Microsoft Fabric](../microsoft/fabric-cosmos-db.md), [Eventhouse and KQL database](../microsoft/fabric-eventhouse.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery](../google-cloud/gcp-bigquery.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks VARIANT data type](../databricks/databricks-variant.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse JSON, Dynamic and Variant data types](../clickhouse/clickhouse-json-types.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Integration advanced mode](../informatica/informatica-cdi-advanced-mode.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database](../teradata/teradata-database.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [DuckDB](../open-source/duckdb.md), [PostgreSQL](../open-source/postgresql.md), [Apache Spark](../open-source/apache-spark.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [MongoDB Atlas](../independent/mongodb-atlas.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
