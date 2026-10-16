---
type: Technology
id: fabric-onelake-shortcut-transformations
title: OneLake shortcut transformations
description: Converts CSV, Parquet, JSON or Excel files behind a shortcut into a managed Delta table and keeps it in step as files are added, changed or deleted.
platform: platform-microsoft
kind: feature
availability: ga
realises: [file-ingestion, incremental-processing]
resource: https://learn.microsoft.com/en-us/fabric/onelake/shortcuts-file-transformations/transformations
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

CSV, Parquet and JSON transformations are GA; Excel transformations are in preview. Fabric polls the source every two minutes and runs the conversion on Fabric Spark, so no pipeline is needed for simple landing-to-bronze loads.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) (Ingestion and integration) (primary): Detect and load files arriving in landing storage, processing each file exactly once.
- [Incremental processing](../../capabilities/processing/incremental-processing.md) (Processing and transformation): Process only new or changed data instead of recomputing everything each run.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** OneLake

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift auto-copy](../aws/aws-redshift-auto-copy.md), [AWS DataSync](../aws/aws-datasync.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Storage Transfer Service](../google-cloud/gcp-storage-transfer-service.md), [BigQuery Data Transfer Service](../google-cloud/gcp-bigquery-data-transfer-service.md), [BigQuery external tables and load jobs](../google-cloud/gcp-bigquery-external-tables.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpipe](../snowflake/snowflake-snowpipe.md), [Snowflake bulk loading (COPY INTO <table>)](../snowflake/snowflake-copy-into.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Auto Loader](../databricks/databricks-auto-loader.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md), [Incremental processing](../../capabilities/processing/incremental-processing.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [S3Queue and AzureQueue table engines](../clickhouse/clickhouse-s3queue.md), [ClickPipes](../clickhouse/clickhouse-clickpipes.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica File Ingestion and Replication](../informatica/informatica-file-ingestion-and-replication.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache NiFi](../open-source/apache-nifi.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
