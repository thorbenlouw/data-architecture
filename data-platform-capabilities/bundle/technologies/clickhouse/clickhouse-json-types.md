---
type: Technology
id: clickhouse-json-types
title: ClickHouse JSON, Dynamic and Variant data types
description: Column types that store semi-structured JSON as typed sub-columns per path, and values whose type varies from row to row, without flattening them first.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [semi-structured-data, schema-evolution]
resource: https://clickhouse.com/docs/sql-reference/data-types/newjson
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The JSON type was marked production ready in 25.3. Undeclared paths become Dynamic sub-columns, and type hints fix known paths; for stable structures ordinary columns, Tuple or Variant are still recommended.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Semi-structured data](../../capabilities/storage/semi-structured-data.md) (Storage and table management) (primary): Store and query nested data such as JSON without flattening it first.
- [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md) (Storage and table management): Reject data that does not match a table's schema, and change schemas safely over time.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift](../aws/aws-redshift.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Explorer](../microsoft/azure-data-explorer.md), [Cosmos DB in Microsoft Fabric](../microsoft/fabric-cosmos-db.md), [Eventhouse and KQL database](../microsoft/fabric-eventhouse.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery](../google-cloud/gcp-bigquery.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake semi-structured data types (VARIANT, OBJECT, ARRAY)](../snowflake/snowflake-semi-structured-data.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks VARIANT data type](../databricks/databricks-variant.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Integration advanced mode](../informatica/informatica-cdi-advanced-mode.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database](../teradata/teradata-database.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [DuckDB](../open-source/duckdb.md), [PostgreSQL](../open-source/postgresql.md), [Apache Spark](../open-source/apache-spark.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [MongoDB Atlas](../independent/mongodb-atlas.md) | [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
