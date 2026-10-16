---
type: Technology
id: databricks-auto-loader
title: Databricks Auto Loader
description: A Structured Streaming source (cloudFiles) that discovers new files in cloud storage and processes each one exactly once, with schema inference, schema evolution and a rescued-data column.
aliases: [cloudFiles]
platform: platform-databricks
kind: feature
availability: ga
realises: [file-ingestion, incremental-processing, schema-evolution]
resource: https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Databricks recommends file notification mode using Unity Catalog file events, which are on by default for new external locations since February 2026, rather than directory listing. Automatic type widening is in Public Preview. It is used inside Lakeflow pipelines, jobs and notebooks.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) (Ingestion and integration) (primary): Detect and load files arriving in landing storage, processing each file exactly once.
- [Incremental processing](../../capabilities/processing/incremental-processing.md) (Processing and transformation): Process only new or changed data instead of recomputing everything each run.
- [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md) (Storage and table management): Reject data that does not match a table's schema, and change schemas safely over time.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift auto-copy](../aws/aws-redshift-auto-copy.md), [AWS DataSync](../aws/aws-datasync.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake shortcut transformations](../microsoft/fabric-onelake-shortcut-transformations.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md), [Incremental processing](../../capabilities/processing/incremental-processing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Storage Transfer Service](../google-cloud/gcp-storage-transfer-service.md), [BigQuery Data Transfer Service](../google-cloud/gcp-bigquery-data-transfer-service.md), [BigQuery external tables and load jobs](../google-cloud/gcp-bigquery-external-tables.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpipe](../snowflake/snowflake-snowpipe.md), [Snowflake bulk loading (COPY INTO <table>)](../snowflake/snowflake-copy-into.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [S3Queue and AzureQueue table engines](../clickhouse/clickhouse-s3queue.md), [ClickPipes](../clickhouse/clickhouse-clickpipes.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica File Ingestion and Replication](../informatica/informatica-file-ingestion-and-replication.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache NiFi](../open-source/apache-nifi.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
