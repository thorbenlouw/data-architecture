---
type: Technology
id: fabric-lakehouse
title: Fabric Lakehouse
description: A Fabric item that stores tables and files in OneLake, with Delta Lake tables, optional schemas and an automatic SQL analytics endpoint.
platform: platform-microsoft
kind: feature
availability: ga
realises: [open-table-formats, table-catalogue, acid-transactions, schema-evolution, row-level-updates]
resource: https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Written mainly by Spark and Data Factory; read by every Fabric engine. Lakehouse schemas allow multi-level namespaces.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Open table formats](../../capabilities/storage/open-table-formats.md) (Storage and table management) (primary): Manage collections of files as transactional tables with a defined schema, history and metadata.
- [Table catalogue](../../capabilities/storage/table-catalogue.md) (Storage and table management): Register tables, their schemas and storage locations so engines can find, govern and share them.
- [ACID transactions](../../capabilities/storage/acid-transactions.md) (Storage and table management): Commit concurrent writes atomically so readers never see partial or conflicting results.
- [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md) (Storage and table management): Reject data that does not match a table's schema, and change schemas safely over time.
- [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md) (Storage and table management): Update, delete and merge individual rows in large tables efficiently.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Fabric Data Engineering

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 Tables](../aws/aws-s3-tables.md) | [ACID transactions](../../capabilities/storage/acid-transactions.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md), [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery tables for Apache Iceberg](../google-cloud/gcp-bigquery-iceberg-managed-tables.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Apache Iceberg tables in Snowflake](../snowflake/snowflake-iceberg-tables.md), [pg_lake](../snowflake/snowflake-pg-lake.md) (preview), [Snowflake micro-partitioned table storage](../snowflake/snowflake-managed-storage.md) | [ACID transactions](../../capabilities/storage/acid-transactions.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md), [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Delta Lake on Databricks](../databricks/databricks-delta-lake.md), [Unity Catalog managed Iceberg tables](../databricks/databricks-managed-iceberg-tables.md) | [ACID transactions](../../capabilities/storage/acid-transactions.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md), [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../clickhouse/clickhouse-data-lake.md) | [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Apache Iceberg in Cloudera](../cloudera/cloudera-lakehouse-iceberg.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md), [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md) | [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data](../ibm/ibm-watsonx-data.md), [IBM Netezza Performance Server](../ibm/ibm-netezza.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Iceberg tables in Palantir Foundry](../palantir/palantir-iceberg-tables.md) (preview) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [DuckLake](../open-source/ducklake.md), [Apache Iceberg](../open-source/apache-iceberg.md), [Delta Lake](../open-source/delta-lake.md) | [ACID transactions](../../capabilities/storage/acid-transactions.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran Managed Data Lake Service](../independent/fivetran-managed-data-lake-service.md), [Qlik Open Lakehouse](../independent/qlik-open-lakehouse.md), [Redpanda Cloud](../independent/redpanda-cloud.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
