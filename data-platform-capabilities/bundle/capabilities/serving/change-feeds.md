---
type: Capability
id: change-feeds
title: Change feeds
description: Expose row-level changes to tables as a stream that downstream consumers can process incrementally.
aliases: [change data feed, table streams]
broader: [serving]
related: [change-data-capture, incremental-processing, time-travel, event-streaming, reverse-etl]
tags: [serving]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A change feed lists every insert, update and delete committed to a table, with its commit version or timestamp, so consumers can read only what changed since their last read. A downstream job processing a customer table asks for changes since version 1,042, receives the 300 rows altered in later commits with their operation type and, where available, before and after values, and updates its own table or cache. Table formats and warehouses offer this as change data feeds, table streams or incremental read APIs.

Change feeds let data flow through the platform's layers incrementally, without rescanning whole tables or relying on timestamp columns. They also make the platform a source for other systems, such as caches, search indexes and applications. Change data capture brings changes from operational databases into the platform; change feeds publish changes from platform tables outwards. Consumers must track their own position, and changes are available only as far back as table history is kept.

# Key considerations

- Feed retention follows table history and maintenance. A consumer that falls behind beyond retention must reload in full.
- Rewrites and compaction can appear as deletes followed by inserts. Check how the feed represents them, or consumers will see changes that did not happen.
- Consumers must store their read position durably and resume after restarts without gaps or duplicates.
- Change tracking adds storage and write overhead. Enable it only on tables that have incremental consumers.

# Questions to ask

- Which downstream jobs or systems reprocess whole tables today that could read only changes?
- How far behind may consumers fall, and how long must change history be kept?
- Do consumers need before and after values, or only the new state?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Serving and activation](serving.md) |
| Broader | [Serving and activation](serving.md) |
| Related | [Change data capture](../ingestion-integration/change-data-capture.md), [Event streaming](../ingestion-integration/event-streaming.md), [Event-driven triggering](../orchestration/event-driven-triggering.md), [Incremental processing](../processing/incremental-processing.md), [Open table formats](../storage/open-table-formats.md), [Retrieval pipelines](../generative-ai/retrieval-pipelines.md), [Reverse ETL](reverse-etl.md), [Row-level updates and deletes](../storage/row-level-updates.md), [Stream processing](../processing/stream-processing.md), [Streaming SQL](../processing/streaming-sql.md), [Time travel](../storage/time-travel.md) |

# Where it appears

- **Use cases:** [Customer 360](../../use-cases/usecase-customer-360.md) (benefits from) · [Marketing audience activation](../../use-cases/usecase-marketing-activation.md) (benefits from) · [Privacy rights handling](../../use-cases/usecase-privacy-rights.md) (benefits from)
- **Patterns:** [Separate read models](../../patterns/cqrs-read-models.md)
- **Personas:** [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Data serving](../../maturity/track-serving.md) (from level 3, Defined) · [Real-time and streaming](../../maturity/track-real-time.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | DynamoDB Streams | [Amazon DynamoDB](../../technologies/aws/aws-dynamodb.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Cosmos DB](../../technologies/microsoft/azure-cosmos-db.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Spanner and Bigtable change streams; BigQuery CHANGES function | [BigQuery change history (APPENDS and CHANGES)](../../technologies/google-cloud/gcp-bigquery-change-history.md), [Bigtable](../../technologies/google-cloud/gcp-bigtable.md), [Spanner](../../technologies/google-cloud/gcp-spanner.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | streams | [Snowflake streams](../../technologies/snowflake/snowflake-streams.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks change data feed](../../technologies/databricks/databricks-change-data-feed.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Business Data Cloud data products](../../technologies/sap/sap-bdc-data-products.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Hudi](../../technologies/open-source/apache-hudi.md), [Apache Paimon](../../technologies/open-source/apache-paimon.md), [Debezium](../../technologies/open-source/debezium.md), [Delta Lake](../../technologies/open-source/delta-lake.md) |
