---
type: Technology
id: delta-lake
title: Delta Lake
description: Open table format and libraries that add ACID transactions, schema enforcement, time travel and row-level updates to Parquet files.
platform: platform-open-source
kind: open-standard
availability: ga
realises:
- open-table-formats
- acid-transactions
- row-level-updates
- time-travel
- change-feeds
- table-format-conversion
resource: https://delta.io/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Linux Foundation project, Apache 2.0, with Databricks as main contributor. Delta Lake 4.4.0 runs on Spark 4.2. UniForm writes Iceberg (and Hudi) metadata so other clients can read Delta tables; Delta Kernel libraries (Java, Rust) let other engines implement the protocol. The Change Data Feed exposes row-level changes.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Open table formats](../../capabilities/storage/open-table-formats.md) (Storage and table management) (primary): Manage collections of files as transactional tables with a defined schema, history and metadata.
- [ACID transactions](../../capabilities/storage/acid-transactions.md) (Storage and table management): Commit concurrent writes atomically so readers never see partial or conflicting results.
- [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md) (Storage and table management): Update, delete and merge individual rows in large tables efficiently.
- [Time travel](../../capabilities/storage/time-travel.md) (Storage and table management): Query or restore a table as it was at an earlier point in time or version.
- [Change feeds](../../capabilities/serving/change-feeds.md) (Serving and activation): Expose row-level changes to tables as a stream that downstream consumers can process incrementally.
- [Table format conversion](../../capabilities/storage/table-format-conversion.md) (Storage and table management): Expose one copy of table data in several table formats by generating or translating metadata.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 Tables](../aws/aws-s3-tables.md) | [ACID transactions](../../capabilities/storage/acid-transactions.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md), [Time travel](../../capabilities/storage/time-travel.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Lakehouse](../microsoft/fabric-lakehouse.md), [OneLake](../microsoft/fabric-onelake.md) | [ACID transactions](../../capabilities/storage/acid-transactions.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery tables for Apache Iceberg](../google-cloud/gcp-bigquery-iceberg-managed-tables.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Apache Iceberg tables in Snowflake](../snowflake/snowflake-iceberg-tables.md), [pg_lake](../snowflake/snowflake-pg-lake.md) (preview) | [ACID transactions](../../capabilities/storage/acid-transactions.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md), [Table format conversion](../../capabilities/storage/table-format-conversion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Delta Lake on Databricks](../databricks/databricks-delta-lake.md), [Unity Catalog managed Iceberg tables](../databricks/databricks-managed-iceberg-tables.md) | [ACID transactions](../../capabilities/storage/acid-transactions.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md), [Time travel](../../capabilities/storage/time-travel.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../clickhouse/clickhouse-data-lake.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Time travel](../../capabilities/storage/time-travel.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Apache Iceberg in Cloudera](../cloudera/cloudera-lakehouse-iceberg.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md), [Time travel](../../capabilities/storage/time-travel.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md) | [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Netezza Performance Server](../ibm/ibm-netezza.md), [IBM watsonx.data](../ibm/ibm-watsonx-data.md) | [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Iceberg tables in Palantir Foundry](../palantir/palantir-iceberg-tables.md) (preview) | [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran Managed Data Lake Service](../independent/fivetran-managed-data-lake-service.md), [Qlik Open Lakehouse](../independent/qlik-open-lakehouse.md), [Redpanda Cloud](../independent/redpanda-cloud.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Table format conversion](../../capabilities/storage/table-format-conversion.md) |
