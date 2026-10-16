---
type: Capability
id: backfill-replay
title: Backfill and reprocessing
description: Rerun pipelines over historical periods or replay events to correct or rebuild data.
broader: [orchestration]
related: [data-branching, time-travel, workload-isolation, event-streaming, incremental-processing]
depends_on: [idempotent-loading]
tags: [orchestration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A backfill reruns a pipeline for past periods, for example recomputing two years of daily revenue tables after a currency conversion bug is fixed. The orchestrator creates one run per day or month in the range and executes them with limited parallelism, each processing only its own period. Replay is the streaming equivalent: a consumer resets its position in an event stream to an earlier offset or time and processes events again, for instance to rebuild a table with changed logic or to fill a new consumer.

Every platform has to correct history, because logic changes, late data, source fixes and new derived columns all require it. It is practical only when pipelines are parameterised by period, deterministic and idempotent on write, and when raw inputs have been kept. Approaches range from rerunning partitions in place, to building a corrected copy beside the live table and swapping it in, to replaying from stream retention or an event archive. Large backfills can cost more than months of normal running.

# Key considerations

- Keep raw inputs long enough to rebuild from. Backfill depends on retention in landing storage and in event streams.
- Build corrected data in a separate location or branch and swap it in atomically, so consumers never see half-corrected history.
- Limit parallelism so backfills do not starve production workloads or exceed source and API quotas.
- Tell consumers before history changes. Reports and models built on the old numbers will shift.

# Questions to ask

- How often does historical data need correcting, and how far back?
- Are raw inputs and events kept long enough to rebuild from?
- Can every pipeline run for an arbitrary past period without code changes?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Orchestration](orchestration.md) |
| Broader | [Orchestration](orchestration.md) |
| Related | [Bad-data quarantine](../data-quality/bad-data-quarantine.md), [Data branching and tagging](../storage/data-branching.md), [Deduplication and idempotent loading](../ingestion-integration/idempotent-loading.md), [Event streaming](../ingestion-integration/event-streaming.md), [Event-time windowing](../processing/event-time-windowing.md), [Incremental processing](../processing/incremental-processing.md), [Spot and interruptible compute](../compute/interruptible-compute.md), [Time travel](../storage/time-travel.md), [Workload isolation](../compute/workload-isolation.md) |
| Depends on | [Deduplication and idempotent loading](../ingestion-integration/idempotent-loading.md) |

# Where it appears

- **Use cases:** [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (benefits from)
- **Patterns:** [Separate read models](../../patterns/cqrs-read-models.md) · [Kappa architecture](../../patterns/kappa-architecture.md) · [Medallion architecture](../../patterns/medallion-architecture.md)
- **Personas:** [Data engineer](../../personas/persona-data-engineer.md)
- **Maturity tracks:** [Orchestration](../../maturity/track-orchestration.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Kinesis Data Streams](../../technologies/aws/aws-kinesis-data-streams.md), [Amazon Managed Workflows for Apache Airflow](../../technologies/aws/aws-mwaa.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Managed Service for Apache Airflow](../../technologies/google-cloud/gcp-managed-airflow.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Lakeflow Jobs](../../technologies/databricks/databricks-lakeflow-jobs.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Airflow](../../technologies/open-source/apache-airflow.md), [Dagster](../../technologies/open-source/dagster.md), [Kestra](../../technologies/open-source/kestra.md) |
