---
type: Capability
id: file-ingestion
title: File ingestion
description: Detect and load files arriving in landing storage, processing each file exactly once.
aliases: [auto loader, landing zone ingestion, incremental file loading, Snowpipe]
broader: [batch-ingestion]
related:
- managed-file-transfer
- idempotent-loading
- bad-data-quarantine
- event-driven-triggering
- schema-evolution
depends_on: [object-storage]
tags: [ingestion-integration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Files land in a location such as an object storage prefix or an SFTP folder. The platform finds new ones by listing the location or by receiving storage notifications, parses them and loads them into tables. A retailer's stores might drop CSV sales files every hour; the loader picks up each new file, applies a declared schema, writes the rows and records the file path and checksum so the same file is never loaded twice, even if it is resent or the job restarts.

Files remain the most common way to exchange data with partners and legacy systems, so nearly every platform needs this. Listing is simple but slows as folders grow to millions of files; notifications scale better but need a fallback for missed events. Formats range from CSV, JSON and fixed-width text to Parquet and Avro, each with its own parsing problems. Managed file transfer moves files securely between organisations; file ingestion starts once they have arrived.

# Key considerations

- Track processed files in a durable manifest or checkpoint keyed by path and checksum, so restarts and resends do not create duplicates.
- Decide how malformed rows are handled: fail the file, skip and log, or quarantine them. Silently dropping rows hides problems.
- Infer schemas only for exploration. Declare them for production feeds so a changed layout is caught rather than loaded wrongly.
- Agree a completion signal with producers, such as a marker file or an atomic rename, so partly written files are never read.
- Keep original files for a set period so loads can be replayed after a parsing or logic fix.

# Questions to ask

- Which file formats, sizes and arrival frequencies must be supported?
- How do producers signal that a file is complete, and can they resend or correct one?
- How many files will accumulate in each landing location over a year?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Ingestion and integration](ingestion-integration.md) |
| Broader | [Batch ingestion](batch-ingestion.md) |
| Related | [Bad-data quarantine](../data-quality/bad-data-quarantine.md), [Deduplication and idempotent loading](idempotent-loading.md), [Event-driven triggering](../orchestration/event-driven-triggering.md), [Managed file transfer](managed-file-transfer.md), [Open file formats](../storage/file-formats.md), [Schema enforcement and evolution](../storage/schema-evolution.md) |
| Depends on | [Object storage](../storage/object-storage.md) |

# Where it appears

- **Patterns:** [Data lake](../../patterns/data-lake.md) · [Metadata-driven pipelines](../../patterns/metadata-driven-pipelines.md)
- **Maturity tracks:** [Ingestion and integration](../../maturity/track-ingestion.md) (from level 1, Initial)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Redshift auto-copy (S3 event integration) | [Amazon Redshift auto-copy](../../technologies/aws/aws-redshift-auto-copy.md), [AWS DataSync](../../technologies/aws/aws-datasync.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [OneLake shortcut transformations](../../technologies/microsoft/fabric-onelake-shortcut-transformations.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery Data Transfer Service](../../technologies/google-cloud/gcp-bigquery-data-transfer-service.md), [BigQuery external tables and load jobs](../../technologies/google-cloud/gcp-bigquery-external-tables.md), [Google Cloud Storage Transfer Service](../../technologies/google-cloud/gcp-storage-transfer-service.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | Snowpipe (continuous) and COPY INTO (bulk) | [Snowflake bulk loading (COPY INTO <table>)](../../technologies/snowflake/snowflake-copy-into.md), [Snowpipe](../../technologies/snowflake/snowflake-snowpipe.md) |
| [Databricks](../../platforms/platform-databricks.md) | Auto Loader | [Databricks Auto Loader](../../technologies/databricks/databricks-auto-loader.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | S3Queue and ClickPipes object storage pipes | [ClickPipes](../../technologies/clickhouse/clickhouse-clickpipes.md), [S3Queue and AzureQueue table engines](../../technologies/clickhouse/clickhouse-s3queue.md) |
| [Informatica](../../platforms/platform-informatica.md) | File Ingestion and Replication | [Informatica File Ingestion and Replication](../../technologies/informatica/informatica-file-ingestion-and-replication.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Flow](../../technologies/cloudera/cloudera-data-flow.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache NiFi](../../technologies/open-source/apache-nifi.md) |
