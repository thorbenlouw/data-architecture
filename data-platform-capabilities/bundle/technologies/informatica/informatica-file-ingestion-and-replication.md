---
type: Technology
id: informatica-file-ingestion-and-replication
title: Informatica File Ingestion and Replication
description: Moves large numbers of files of any type between on-premises and cloud repositories, and tracks and monitors each transfer.
formerly: [Cloud Mass Ingestion Files, Mass Ingestion Files]
platform: platform-informatica
kind: managed-service
availability: ga
realises: [file-ingestion]
resource: https://onlinehelp.informatica.com/IICS/prod/CDI/en/cc-cloud-dbi_intro/Introducing_Data_Ingestion_and_Replication.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

This is an internal file mover. For trading-partner exchange over AS2 or EDI, use B2B Gateway.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) (Ingestion and integration) (primary): Detect and load files arriving in landing storage, processing each file exactly once.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud, Data Ingestion and Replication

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift auto-copy](../aws/aws-redshift-auto-copy.md), [AWS DataSync](../aws/aws-datasync.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake shortcut transformations](../microsoft/fabric-onelake-shortcut-transformations.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Storage Transfer Service](../google-cloud/gcp-storage-transfer-service.md), [BigQuery Data Transfer Service](../google-cloud/gcp-bigquery-data-transfer-service.md), [BigQuery external tables and load jobs](../google-cloud/gcp-bigquery-external-tables.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpipe](../snowflake/snowflake-snowpipe.md), [Snowflake bulk loading (COPY INTO <table>)](../snowflake/snowflake-copy-into.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Auto Loader](../databricks/databricks-auto-loader.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [S3Queue and AzureQueue table engines](../clickhouse/clickhouse-s3queue.md), [ClickPipes](../clickhouse/clickhouse-clickpipes.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache NiFi](../open-source/apache-nifi.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
