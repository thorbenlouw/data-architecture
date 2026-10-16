---
type: Capability
id: schema-evolution
title: Schema enforcement and evolution
description: Reject data that does not match a table's schema, and change schemas safely over time.
aliases: [schema drift handling]
broader: [open-table-formats]
related: [schema-registry, data-contracts, schema-change-management, bad-data-quarantine, impact-analysis]
tags: [storage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Enforcement means a write is rejected, or its bad rows set aside, when the data does not match the table's declared columns and types: text arriving in a numeric `quantity` column fails instead of quietly becoming null. Evolution means the schema can change through explicit operations, such as adding a column, widening an integer type, or renaming and reordering columns, without rewriting existing files. Formats such as Iceberg track columns by internal id rather than by name or position, so a rename does not break old files and a dropped column's data is never read as another column.

Together they stop silent corruption while letting tables keep up with changing sources. Teams choose between strict enforcement, where every change is a deliberate migration, and automatic evolution, where new source columns are added on write. Automatic evolution suits raw ingestion layers; curated tables usually need control. Schema registries do the same job for event streams, and data contracts add the agreement about who may change what, with how much notice.

# Key considerations

- Decide per layer whether new columns are added automatically or rejected. Automatic evolution in curated tables can push unexpected columns into reports.
- Not every allowed change is safe. Narrowing types, changing a column's meaning or reusing a dropped name breaks consumers even when the format permits it.
- Engines differ in which changes they support and how they read older files. Test renames and type changes with every reader.
- Record schema changes with time and author so downstream teams can see what changed and when.

# Questions to ask

- How often do source schemas change, and who is told when they do?
- Which tables have consumers that would break if a column changed type or disappeared?
- Should bad records stop a load, or be set aside while good records continue?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Storage and table management](storage.md) |
| Broader | [Open table formats](open-table-formats.md) |
| Related | [Bad-data quarantine](../data-quality/bad-data-quarantine.md), [Data contracts](../data-products/data-contracts.md), [File ingestion](../ingestion-integration/file-ingestion.md), [Impact analysis](../metadata/impact-analysis.md), [Schema change management](../development-lifecycle/schema-change-management.md), [Schema registry](../metadata/schema-registry.md), [Semi-structured data](semi-structured-data.md), [Stream-to-table materialisation](../ingestion-integration/stream-to-table.md) |

# Where it appears

- **Patterns:** [Metadata-driven pipelines](../../patterns/metadata-driven-pipelines.md)
- **Personas:** [Data architect](../../personas/persona-data-architect.md) · [Data engineer](../../personas/persona-data-engineer.md)
- **Maturity tracks:** [Storage and table management](../../maturity/track-storage.md) (from level 3, Defined)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Modelling and Design · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Schema

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon S3 Tables](../../technologies/aws/aws-s3-tables.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric Lakehouse](../../technologies/microsoft/fabric-lakehouse.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery managed storage](../../technologies/google-cloud/gcp-bigquery-managed-storage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Apache Iceberg tables in Snowflake](../../technologies/snowflake/snowflake-iceberg-tables.md), [Snowflake micro-partitioned table storage](../../technologies/snowflake/snowflake-managed-storage.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Auto Loader](../../technologies/databricks/databricks-auto-loader.md), [Delta Lake on Databricks](../../technologies/databricks/databricks-delta-lake.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse JSON, Dynamic and Variant data types](../../technologies/clickhouse/clickhouse-json-types.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Apache Iceberg in Cloudera](../../technologies/cloudera/cloudera-lakehouse-iceberg.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM StreamSets](../../technologies/ibm/ibm-streamsets.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Avro](../../technologies/open-source/apache-avro.md), [Apache Iceberg](../../technologies/open-source/apache-iceberg.md), [dlt (data load tool)](../../technologies/open-source/dlt.md), [DuckLake](../../technologies/open-source/ducklake.md), [Flink CDC](../../technologies/open-source/apache-flink-cdc.md) |
