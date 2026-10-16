---
type: Capability
id: semi-structured-data
title: Semi-structured data
description: Store and query nested data such as JSON without flattening it first.
aliases: [VARIANT, JSON columns]
broader: [storage, specialised-data]
related: [schema-evolution, file-formats, columnar-storage, document-processing, data-classification]
tags: [storage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Semi-structured data has structure, but not a fixed one: JSON documents, records with nested arrays, or event payloads whose fields differ by event type. Platforms store it in a native type, such as a variant, JSON or struct column, and let SQL reach inside with path expressions like `payload.device.battery` or with functions that turn arrays into rows. Newer implementations split frequently used paths into hidden typed columns with their own statistics, so queries on them run almost as fast as on ordinary columns. Parquet and Iceberg have added a variant type to make this portable between engines.

It lets teams load data as it arrives and decide later which fields matter, without writing a parser first or failing loads when a new field appears. It suits event, API and log data. Trouble starts when nested data is never modelled: each consumer writes its own paths and casts, and type mistakes surface late. A common approach is to keep raw payloads semi-structured and extract stable, widely used fields into typed columns.

# Key considerations

- Path queries over JSON stored as text are slow and costly at scale. Prefer a native variant or struct type.
- Engines infer types differently, and one field can be a number in one record and text in another. Decide how failed casts are handled.
- Masking and access rules on nested fields are harder than on columns. Check whether sensitive values inside documents can be protected.
- Support for variant types across engines is still uneven. Check before relying on them in tables that several engines share.

# Questions to ask

- Which sources deliver nested or changing structures, and how often do they change?
- Which nested fields are queried often enough to deserve their own typed columns?
- Do nested payloads contain personal or sensitive data that needs masking?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Storage and table management](storage.md) |
| Broader | [Storage and table management](storage.md), [Specialised data types](../specialised-data/specialised-data.md) |
| Related | [Columnar storage](columnar-storage.md), [Data classification](../governance/data-classification.md), [Document processing](../processing/document-processing.md), [Open file formats](file-formats.md), [Schema enforcement and evolution](schema-evolution.md) |

# Where it appears

- **Use cases:** [Security and log analytics](../../use-cases/usecase-security-log-analytics.md) (requires, level 3)
- **Patterns:** [Data lake](../../patterns/data-lake.md) · [One big table](../../patterns/one-big-table.md)
- **Maturity tracks:** [Storage and table management](../../maturity/track-storage.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Redshift SUPER data type | [Amazon Redshift](../../technologies/aws/aws-redshift.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Data Explorer](../../technologies/microsoft/azure-data-explorer.md), [Cosmos DB in Microsoft Fabric](../../technologies/microsoft/fabric-cosmos-db.md), [Eventhouse and KQL database](../../technologies/microsoft/fabric-eventhouse.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery](../../technologies/google-cloud/gcp-bigquery.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake semi-structured data types (VARIANT, OBJECT, ARRAY)](../../technologies/snowflake/snowflake-semi-structured-data.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks VARIANT data type](../../technologies/databricks/databricks-variant.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | JSON, Dynamic and Variant types | [ClickHouse JSON, Dynamic and Variant data types](../../technologies/clickhouse/clickhouse-json-types.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Cloud Data Integration advanced mode](../../technologies/informatica/informatica-cdi-advanced-mode.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle AI Database 26ai](../../technologies/oracle/oracle-ai-database-26ai.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP HANA Cloud](../../technologies/sap/sap-hana-cloud.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Database](../../technologies/teradata/teradata-database.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Spark](../../technologies/open-source/apache-spark.md), [DuckDB](../../technologies/open-source/duckdb.md), [PostgreSQL](../../technologies/open-source/postgresql.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [MongoDB Atlas](../../technologies/independent/mongodb-atlas.md) |
