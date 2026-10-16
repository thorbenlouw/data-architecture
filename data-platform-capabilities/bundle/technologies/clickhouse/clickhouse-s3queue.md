---
type: Technology
id: clickhouse-s3queue
title: S3Queue and AzureQueue table engines
description: Table engines that watch an S3 or Azure Blob path and load new files in the background through a materialised view, tracking which files have been processed in Keeper.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [file-ingestion, event-driven-triggering]
resource: https://clickhouse.com/docs/engines/table-engines/integrations/s3queue
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Supports ordered, unordered and exclusive modes; it does not promise exactly-once, and duplicates are possible after retries or crashes. Used on self-managed clusters and in Cloud, where ClickPipes object storage pipes are the managed alternative.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) (Ingestion and integration) (primary): Detect and load files arriving in landing storage, processing each file exactly once.
- [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) (Orchestration): Start pipelines when something happens, such as a file arriving, a table changing or a message being published.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga  
**Product family:** ClickHouse table engines

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift auto-copy](../aws/aws-redshift-auto-copy.md), [AWS DataSync](../aws/aws-datasync.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake shortcut transformations](../microsoft/fabric-onelake-shortcut-transformations.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Storage Transfer Service](../google-cloud/gcp-storage-transfer-service.md), [BigQuery Data Transfer Service](../google-cloud/gcp-bigquery-data-transfer-service.md), [BigQuery external tables and load jobs](../google-cloud/gcp-bigquery-external-tables.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpipe](../snowflake/snowflake-snowpipe.md), [Snowflake bulk loading (COPY INTO <table>)](../snowflake/snowflake-copy-into.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Auto Loader](../databricks/databricks-auto-loader.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica File Ingestion and Replication](../informatica/informatica-file-ingestion-and-replication.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache NiFi](../open-source/apache-nifi.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
