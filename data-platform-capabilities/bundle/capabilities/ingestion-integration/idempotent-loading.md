---
type: Capability
id: idempotent-loading
title: Deduplication and idempotent loading
description: Make loads safe to retry or replay by removing duplicates on write so nothing is counted twice.
aliases: [exactly-once delivery, deduplication]
broader: [ingestion-integration]
related: [backfill-replay, row-level-updates, data-reconciliation, entity-resolution, streaming-ingestion]
depends_on: [acid-transactions]
tags: [ingestion-integration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A load is idempotent if running it twice gives the same result as running it once. Retries after a timeout, replays from a stream and backfills all resend data the platform may already hold, so the load step must recognise it. Common mechanisms are a MERGE on a business or event key that updates existing rows instead of inserting new ones, atomic replacement of a whole partition, and a record of committed files, batch ids or stream offsets that are skipped on retry.

Without it, every recovery risks double-counted orders, inflated metrics and failed reconciliations, and engineers become reluctant to rerun jobs. It is what makes at-least-once delivery from streams and connectors safe in practice: duplicates are tolerated in transit and removed on write. Deduplicating within one batch is easy; across batches it needs a key index or a lookback window. Entity resolution is a different problem: it links different records that describe the same thing, whereas this removes repeated copies of one record.

# Key considerations

- Pick a stable deduplication key. Producer-generated event ids work; arrival timestamps and ingestion-time ids do not.
- Cross-batch deduplication needs a lookback window or key index. Decide how late duplicates can arrive and size it to match.
- Partition overwrite is simple and safe for batch data, but each run must rewrite the whole partition or rows are lost.
- Make side effects idempotent too, such as notifications or downstream API calls triggered by a load.

# Questions to ask

- Which sources deliver at least once and may resend data?
- Does each record or event have a reliable unique key?
- How are failed loads rerun today, and has double-counting happened before?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Ingestion and integration](ingestion-integration.md) |
| Broader | [Ingestion and integration](ingestion-integration.md) |
| Related | [ACID transactions](../storage/acid-transactions.md), [API ingestion](api-ingestion.md), [Backfill and reprocessing](../orchestration/backfill-replay.md), [Bad-data quarantine](../data-quality/bad-data-quarantine.md), [Batch ingestion](batch-ingestion.md), [Change data capture](change-data-capture.md), [Data reconciliation](../data-quality/data-reconciliation.md), [Entity resolution](../master-data/entity-resolution.md), [File ingestion](file-ingestion.md), [Incremental processing](../processing/incremental-processing.md), [Message queuing](message-queuing.md), [Row-level updates and deletes](../storage/row-level-updates.md), [SQL transformation](../processing/sql-transformation.md), [Streaming ingestion](streaming-ingestion.md) |
| Depends on | [ACID transactions](../storage/acid-transactions.md) |
| Needed by | [Backfill and reprocessing](../orchestration/backfill-replay.md) |

# Where it appears

- **Use cases:** [Application data publishing](../../use-cases/usecase-application-data-publishing.md) (benefits from) · [Operational reporting](../../use-cases/usecase-operational-reporting.md) (requires, level 3)
- **Patterns:** [Data Vault](../../patterns/data-vault.md) · [Kappa architecture](../../patterns/kappa-architecture.md) · [Metadata-driven pipelines](../../patterns/metadata-driven-pipelines.md) · [Transactional outbox](../../patterns/transactional-outbox.md)
- **Personas:** [Data engineer](../../personas/persona-data-engineer.md)
- **Maturity tracks:** [Ingestion and integration](../../maturity/track-ingestion.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery Storage Write API](../../technologies/google-cloud/gcp-bigquery-storage-write-api.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Connector for Kafka](../../technologies/snowflake/snowflake-connector-for-kafka.md), [Snowpipe Streaming](../../technologies/snowflake/snowflake-snowpipe-streaming.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickPipes](../../technologies/clickhouse/clickhouse-clickpipes.md), [MergeTree table engine family](../../technologies/clickhouse/clickhouse-mergetree.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Airbyte](../../technologies/open-source/airbyte.md), [Apache Doris](../../technologies/open-source/apache-doris.md), [Apache Druid](../../technologies/open-source/apache-druid.md), [Apache Flink](../../technologies/open-source/apache-flink.md), [Apache Hudi](../../technologies/open-source/apache-hudi.md), [Apache Kafka](../../technologies/open-source/apache-kafka.md), [Apache Paimon](../../technologies/open-source/apache-paimon.md), [Apache Pinot](../../technologies/open-source/apache-pinot.md), [Apache Pulsar](../../technologies/open-source/apache-pulsar.md), [dlt (data load tool)](../../technologies/open-source/dlt.md), [Spark Structured Streaming](../../technologies/open-source/apache-spark-structured-streaming.md), [StarRocks](../../technologies/open-source/starrocks.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Airbyte Cloud](../../technologies/independent/airbyte-cloud.md), [Estuary](../../technologies/independent/estuary.md), [Fivetran](../../technologies/independent/fivetran.md) |
