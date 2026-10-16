---
type: Technology
id: gcp-bigquery-external-tables
title: BigQuery external tables and load jobs
description: Reads or loads Parquet, ORC, Avro, JSON and CSV files from Cloud Storage, including Hive-partitioned layouts, as queryable external tables or native tables.
aliases: [BigLake tables]
platform: platform-google-cloud
kind: feature
availability: ga
realises: [file-formats, file-ingestion, query-federation]
resource: https://docs.cloud.google.com/bigquery/docs/external-data-sources
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

External tables that use a connection, called BigLake tables in BigQuery documentation, use access delegation, so they get fine-grained security and metadata caching over Cloud Storage, S3 or Azure; plain external tables do not. Load jobs are free on the shared slot pool. Iceberg external tables are read-only from BigQuery.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Open file formats](../../capabilities/storage/file-formats.md) (Storage and table management) (primary): Store data in open, well-specified file formats such as Parquet, ORC, Avro and JSON.
- [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) (Ingestion and integration): Detect and load files arriving in landing storage, processing each file exactly once.
- [Query federation](../../capabilities/compute/query-federation.md) (Query and compute): Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Data Firehose](../aws/aws-data-firehose.md) | [Open file formats](../../capabilities/storage/file-formats.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake external tables](../snowflake/snowflake-external-tables.md), [Snowflake semi-structured data types (VARIANT, OBJECT, ARRAY)](../snowflake/snowflake-semi-structured-data.md) | [Open file formats](../../capabilities/storage/file-formats.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse integration table engines and table functions](../clickhouse/clickhouse-integration-engines.md), [clickhouse-local](../clickhouse/clickhouse-local.md) | [Open file formats](../../capabilities/storage/file-formats.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Avro](../open-source/apache-avro.md), [Apache ORC](../open-source/apache-orc.md), [Apache Parquet](../open-source/apache-parquet.md) | [Open file formats](../../capabilities/storage/file-formats.md) |
