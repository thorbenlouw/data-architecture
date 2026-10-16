---
type: Technology
id: aws-redshift-auto-copy
title: Amazon Redshift auto-copy
description: COPY jobs that watch an S3 prefix and load each new file into a Redshift table once, as it arrives.
platform: platform-aws
kind: feature
availability: ga
realises: [file-ingestion]
resource: https://docs.aws.amazon.com/redshift/latest/dg/loading-data-copy-job.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Uses an S3 event integration and tracks loaded files to avoid duplicates. Replaces hand-built Lambda or Glue loaders for simple file drops.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) (Ingestion and integration) (primary): Detect and load files arriving in landing storage, processing each file exactly once.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon Redshift

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake shortcut transformations](../microsoft/fabric-onelake-shortcut-transformations.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Storage Transfer Service](../google-cloud/gcp-storage-transfer-service.md), [BigQuery Data Transfer Service](../google-cloud/gcp-bigquery-data-transfer-service.md), [BigQuery external tables and load jobs](../google-cloud/gcp-bigquery-external-tables.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpipe](../snowflake/snowflake-snowpipe.md), [Snowflake bulk loading (COPY INTO <table>)](../snowflake/snowflake-copy-into.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Auto Loader](../databricks/databricks-auto-loader.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [S3Queue and AzureQueue table engines](../clickhouse/clickhouse-s3queue.md), [ClickPipes](../clickhouse/clickhouse-clickpipes.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica File Ingestion and Replication](../informatica/informatica-file-ingestion-and-replication.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache NiFi](../open-source/apache-nifi.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
