---
type: Technology
id: cloudera-lakehouse-iceberg
title: Apache Iceberg in Cloudera
description: Native Apache Iceberg v2 table support across Spark, Hive, Impala, Trino, Flink and NiFi, including time travel, partition evolution and row-level changes.
platform: platform-cloudera
kind: feature
availability: ga
realises: [open-table-formats, time-travel, schema-evolution, row-level-updates, partitioning-clustering]
resource: https://docs.cloudera.com/
tags: [cloudera]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Iceberg is Cloudera's default open table format and the basis of what Cloudera markets as its open data lakehouse. Tables are registered in the Hive Metastore and governed by Apache Ranger. Hive supports Z-ordering on Iceberg tables from 2026. The open format itself is described under [Apache Iceberg](../open-source/apache-iceberg.md).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Open table formats](../../capabilities/storage/open-table-formats.md) (Storage and table management) (primary): Manage collections of files as transactional tables with a defined schema, history and metadata.
- [Time travel](../../capabilities/storage/time-travel.md) (Storage and table management): Query or restore a table as it was at an earlier point in time or version.
- [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md) (Storage and table management): Reject data that does not match a table's schema, and change schemas safely over time.
- [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md) (Storage and table management): Update, delete and merge individual rows in large tables efficiently.
- [Partitioning and clustering](../../capabilities/storage/partitioning-clustering.md) (Storage and table management): Organise table data by key columns so queries can skip data they do not need.

**Platform:** [Cloudera](../../platforms/platform-cloudera.md)  
**Availability:** ga  
**Product family:** Cloudera Open Data Lakehouse

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 Tables](../aws/aws-s3-tables.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md), [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md), [Time travel](../../capabilities/storage/time-travel.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Lakehouse](../microsoft/fabric-lakehouse.md), [OneLake](../microsoft/fabric-onelake.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md), [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery tables for Apache Iceberg](../google-cloud/gcp-bigquery-iceberg-managed-tables.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Apache Iceberg tables in Snowflake](../snowflake/snowflake-iceberg-tables.md), [pg_lake](../snowflake/snowflake-pg-lake.md) (preview) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md), [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Delta Lake on Databricks](../databricks/databricks-delta-lake.md), [Unity Catalog managed Iceberg tables](../databricks/databricks-managed-iceberg-tables.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md), [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md), [Time travel](../../capabilities/storage/time-travel.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../clickhouse/clickhouse-data-lake.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Time travel](../../capabilities/storage/time-travel.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md) | [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Netezza Performance Server](../ibm/ibm-netezza.md), [IBM watsonx.data](../ibm/ibm-watsonx-data.md) | [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Iceberg tables in Palantir Foundry](../palantir/palantir-iceberg-tables.md) (preview) | [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Iceberg](../open-source/apache-iceberg.md), [DuckLake](../open-source/ducklake.md), [Delta Lake](../open-source/delta-lake.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Partitioning and clustering](../../capabilities/storage/partitioning-clustering.md), [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md), [Time travel](../../capabilities/storage/time-travel.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran Managed Data Lake Service](../independent/fivetran-managed-data-lake-service.md), [Qlik Open Lakehouse](../independent/qlik-open-lakehouse.md), [Redpanda Cloud](../independent/redpanda-cloud.md) | [Open table formats](../../capabilities/storage/open-table-formats.md) |
