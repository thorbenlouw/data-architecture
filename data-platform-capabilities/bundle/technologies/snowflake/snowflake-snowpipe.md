---
type: Technology
id: snowflake-snowpipe
title: Snowpipe
description: A serverless pipe that loads files continuously from stages as they arrive, triggered by cloud storage event notifications or REST calls.
platform: platform-snowflake
kind: feature
availability: ga
realises: [file-ingestion, event-driven-triggering]
resource: https://docs.snowflake.com/en/user-guide/data-load-snowpipe-intro
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Snowpipe is billed per GB loaded. It remembers loaded files for 14 days, so re-staging a file after that can duplicate data, and it does not guarantee order or latency. Auto-ingest from internal stages is in preview on AWS.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) (Ingestion and integration) (primary): Detect and load files arriving in landing storage, processing each file exactly once.
- [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) (Orchestration): Start pipelines when something happens, such as a file arriving, a table changing or a message being published.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowpipe

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift auto-copy](../aws/aws-redshift-auto-copy.md), [AWS DataSync](../aws/aws-datasync.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake shortcut transformations](../microsoft/fabric-onelake-shortcut-transformations.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Storage Transfer Service](../google-cloud/gcp-storage-transfer-service.md), [BigQuery Data Transfer Service](../google-cloud/gcp-bigquery-data-transfer-service.md), [BigQuery external tables and load jobs](../google-cloud/gcp-bigquery-external-tables.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Auto Loader](../databricks/databricks-auto-loader.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [S3Queue and AzureQueue table engines](../clickhouse/clickhouse-s3queue.md), [ClickPipes](../clickhouse/clickhouse-clickpipes.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica File Ingestion and Replication](../informatica/informatica-file-ingestion-and-replication.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache NiFi](../open-source/apache-nifi.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
