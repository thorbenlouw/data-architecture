---
type: Technology
id: gcp-bigquery-iceberg-managed-tables
title: BigQuery tables for Apache Iceberg
description: BigQuery-managed tables stored as Apache Iceberg files in your Cloud Storage bucket, with BigQuery handling writes, clustering, compaction and garbage collection.
aliases: [Iceberg managed tables, BigQuery Iceberg tables]
formerly: [BigLake tables for Apache Iceberg in BigQuery, BigLake managed tables]
platform: platform-google-cloud
kind: feature
availability: ga
realises: [open-table-formats, engine-interoperability, table-maintenance, row-level-updates]
resource: https://docs.cloud.google.com/biglake/docs/biglake-iceberg-tables
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Only BigQuery writes them directly; other engines read them through the [Lakehouse runtime catalog](../google-cloud/gcp-lakehouse-runtime-catalog.md). They support DML, streaming through the Storage Write API and continuous query output (September 2026). Iceberg V3 deletion vectors are in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Open table formats](../../capabilities/storage/open-table-formats.md) (Storage and table management) (primary): Manage collections of files as transactional tables with a defined schema, history and metadata.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.
- [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) (Storage and table management): Compact small files, remove obsolete files and reorganise data so tables stay fast and cheap.
- [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md) (Storage and table management): Update, delete and merge individual rows in large tables efficiently.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery, Google Cloud Lakehouse

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 Tables](../aws/aws-s3-tables.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md), [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Lakehouse](../microsoft/fabric-lakehouse.md), [OneLake](../microsoft/fabric-onelake.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Apache Iceberg tables in Snowflake](../snowflake/snowflake-iceberg-tables.md), [pg_lake](../snowflake/snowflake-pg-lake.md) (preview) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog managed Iceberg tables](../databricks/databricks-managed-iceberg-tables.md), [Delta Lake on Databricks](../databricks/databricks-delta-lake.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../clickhouse/clickhouse-data-lake.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Apache Iceberg in Cloudera](../cloudera/cloudera-lakehouse-iceberg.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data](../ibm/ibm-watsonx-data.md), [IBM Netezza Performance Server](../ibm/ibm-netezza.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Iceberg tables in Palantir Foundry](../palantir/palantir-iceberg-tables.md) (preview) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Hudi](../open-source/apache-hudi.md), [Apache Paimon](../open-source/apache-paimon.md), [Delta Lake](../open-source/delta-lake.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md), [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran Managed Data Lake Service](../independent/fivetran-managed-data-lake-service.md), [Qlik Open Lakehouse](../independent/qlik-open-lakehouse.md), [Redpanda Cloud](../independent/redpanda-cloud.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
