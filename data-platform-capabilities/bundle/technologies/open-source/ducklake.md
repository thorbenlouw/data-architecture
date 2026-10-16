---
type: Technology
id: ducklake
title: DuckLake
description: Lakehouse table format that keeps data in Parquet files on object storage and all table metadata in an ordinary SQL database.
platform: platform-open-source
kind: open-standard
availability: ga
realises: [open-table-formats, acid-transactions, time-travel, table-catalogue, schema-evolution]
resource: https://duckdb.org/2026/04/13/ducklake-10
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

MIT licence, from the DuckDB team. DuckLake 1.0 was released in April 2026. The catalogue can be DuckDB, PostgreSQL, SQLite or MySQL, which removes the separate catalogue service that Iceberg and Delta need. Support outside DuckDB is still limited.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Open table formats](../../capabilities/storage/open-table-formats.md) (Storage and table management) (primary): Manage collections of files as transactional tables with a defined schema, history and metadata.
- [ACID transactions](../../capabilities/storage/acid-transactions.md) (Storage and table management): Commit concurrent writes atomically so readers never see partial or conflicting results.
- [Time travel](../../capabilities/storage/time-travel.md) (Storage and table management): Query or restore a table as it was at an earlier point in time or version.
- [Table catalogue](../../capabilities/storage/table-catalogue.md) (Storage and table management): Register tables, their schemas and storage locations so engines can find, govern and share them.
- [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md) (Storage and table management): Reject data that does not match a table's schema, and change schemas safely over time.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 Tables](../aws/aws-s3-tables.md) | [ACID transactions](../../capabilities/storage/acid-transactions.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md), [Time travel](../../capabilities/storage/time-travel.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Lakehouse](../microsoft/fabric-lakehouse.md), [OneLake](../microsoft/fabric-onelake.md) | [ACID transactions](../../capabilities/storage/acid-transactions.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery tables for Apache Iceberg](../google-cloud/gcp-bigquery-iceberg-managed-tables.md) | [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Apache Iceberg tables in Snowflake](../snowflake/snowflake-iceberg-tables.md), [pg_lake](../snowflake/snowflake-pg-lake.md) (preview) | [ACID transactions](../../capabilities/storage/acid-transactions.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Delta Lake on Databricks](../databricks/databricks-delta-lake.md), [Unity Catalog managed Iceberg tables](../databricks/databricks-managed-iceberg-tables.md) | [ACID transactions](../../capabilities/storage/acid-transactions.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md), [Time travel](../../capabilities/storage/time-travel.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../clickhouse/clickhouse-data-lake.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Time travel](../../capabilities/storage/time-travel.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Apache Iceberg in Cloudera](../cloudera/cloudera-lakehouse-iceberg.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md), [Time travel](../../capabilities/storage/time-travel.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md) | [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data](../ibm/ibm-watsonx-data.md), [IBM Netezza Performance Server](../ibm/ibm-netezza.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Iceberg tables in Palantir Foundry](../palantir/palantir-iceberg-tables.md) (preview) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran Managed Data Lake Service](../independent/fivetran-managed-data-lake-service.md), [Qlik Open Lakehouse](../independent/qlik-open-lakehouse.md), [Redpanda Cloud](../independent/redpanda-cloud.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
