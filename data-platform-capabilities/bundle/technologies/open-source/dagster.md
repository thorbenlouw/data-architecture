---
type: Technology
id: dagster
title: Dagster
description: Data orchestrator built around software-defined assets, where you declare the data assets you want and their dependencies and Dagster schedules and tracks them.
aliases: [Dagster OSS]
platform: platform-open-source
kind: open-source
availability: ga
realises:
- asset-based-orchestration
- workflow-orchestration
- backfill-replay
- data-quality-rules
- table-lineage
resource: https://docs.dagster.io/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, company-led by Dagster Labs, which sells Dagster+ as a managed service. Asset checks attach quality tests to assets; declarative automation materialises assets based on freshness and upstream changes. Integrates closely with dbt and SQLMesh.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md) (Orchestration) (primary): Schedule work based on the freshness and dependencies of data assets rather than fixed times.
- [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) (Orchestration): Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.
- [Backfill and reprocessing](../../capabilities/orchestration/backfill-replay.md) (Orchestration): Rerun pipelines over historical periods or replay events to correct or rebuild data.
- [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) (Data quality and observability): Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency.
- [Table-level lineage](../../capabilities/metadata/table-lineage.md) (Metadata and discovery): Track dependencies between datasets, tables and views.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Workflows for Apache Airflow](../aws/aws-mwaa.md) | [Backfill and reprocessing](../../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Managed Service for Apache Airflow](../google-cloud/gcp-managed-airflow.md) | [Backfill and reprocessing](../../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Dynamic Tables](../snowflake/snowflake-dynamic-tables.md) | [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Jobs](../databricks/databricks-lakeflow-jobs.md) | [Backfill and reprocessing](../../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Dagster+](../independent/dagster-plus.md), [Astronomer Astro](../independent/astronomer-astro.md) | [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
