---
type: Capability
id: bad-data-quarantine
title: Bad-data quarantine
description: Route records that fail checks to a holding area for inspection and replay instead of failing or loading them.
aliases: [dead-letter queue, quarantine tables]
broader: [data-quality]
related: [idempotent-loading, backfill-replay, message-queuing, data-issue-management, schema-evolution]
depends_on: [data-quality-rules]
tags: [data-quality]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Take a batch of a million orders in which 300 have invalid currency codes. With quarantine, the 999,700 good rows load as normal, and the 300 go to a holding table together with the rule that failed, the source file and a timestamp. Once the source or the rule is fixed, the held records are replayed through the pipeline. Streaming systems call the same pattern a dead-letter queue.

It matters when stopping the pipeline is costly but loading bad records would corrupt results. Good data keeps flowing while failures stay visible and recoverable. For each rule the choice is fail, quarantine or warn. Quarantine suits problems in individual records; problems with a whole table, such as half a file missing, usually call for stopping. Partial loads must be reported, so consumers know totals may be incomplete.

# Key considerations

- Someone must own the quarantine. Unreviewed holding tables grow until the data is too old to replay.
- Partial loads can mislead, because totals look plausible while records are missing. Expose quarantine counts to consumers or in quality status.
- Make replay idempotent, so reprocessing held records does not create duplicates.
- Quarantined data is as sensitive as its source. Apply the same access controls and retention.

# Questions to ask

- For each critical feed, is it worse to stop, to load partial data or to load bad data?
- How are rejected records found, fixed and reprocessed today?
- Who will review quarantined records, and how quickly?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data quality and observability](data-quality.md) |
| Broader | [Data quality and observability](data-quality.md) |
| Related | [Backfill and reprocessing](../orchestration/backfill-replay.md), [Data issue management](data-issue-management.md), [Data quality rules](data-quality-rules.md), [Declarative pipelines](../processing/declarative-pipelines.md), [Deduplication and idempotent loading](../ingestion-integration/idempotent-loading.md), [File ingestion](../ingestion-integration/file-ingestion.md), [Message queuing](../ingestion-integration/message-queuing.md), [Schema enforcement and evolution](../storage/schema-evolution.md) |
| Depends on | [Data quality rules](data-quality-rules.md) |

# Where it appears

- **Use cases:** [Application data publishing](../../use-cases/usecase-application-data-publishing.md) (benefits from)
- **Personas:** [Data engineer](../../personas/persona-data-engineer.md)
- **Maturity tracks:** [Data quality and observability](../../maturity/track-data-quality.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Glue Data Quality](../../technologies/aws/aws-glue-data-quality.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery data preparation](../../technologies/google-cloud/gcp-bigquery-data-preparation.md) (preview) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Lakeflow pipelines expectations](../../technologies/databricks/databricks-pipeline-expectations.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickPipes](../../technologies/clickhouse/clickhouse-clickpipes.md) |
| [Informatica](../../platforms/platform-informatica.md) | exception management | [Informatica Cloud Data Quality (CDQ)](../../technologies/informatica/informatica-cloud-data-quality.md) |
