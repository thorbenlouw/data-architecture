---
type: Capability
id: asset-based-orchestration
title: Data-aware orchestration
description: Schedule work based on the freshness and dependencies of data assets rather than fixed times.
aliases: [asset-based scheduling, data-aware scheduling]
broader: [orchestration]
related: [declarative-pipelines, freshness-monitoring, table-lineage, data-slas, incremental-processing]
tags: [orchestration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data-aware orchestration models the assets a pipeline produces, such as tables, files, models and reports, and the dependencies between them, rather than a sequence of tasks. Each asset declares what it is built from and how fresh it must be. When an upstream table is updated, the orchestrator knows which downstream assets are now stale and runs only the work needed to refresh them. If a daily report must be no more than two hours old at 08:00, it works backwards to decide when upstream work must start.

This matches orchestration to what consumers care about: is this dataset current and correct? It also gives a built-in view of dependencies and of which assets are stale, which task-based workflows lack. It suits platforms with many interdependent datasets owned by different teams, where hand-wired dependencies between workflows break easily. Dagster's assets and Airflow's asset scheduling are open-source examples. Declarative pipelines apply a similar idea inside one engine; data-aware orchestration applies it across tools.

# Key considerations

- Define assets consistently across teams, ideally with the same identifiers used in the catalogue and lineage.
- Freshness targets need owners and realistic values. Targets tighter than consumers need cause constant reruns and cost.
- Model partitions explicitly, such as one per day. Partitioned assets make backfills and incremental refresh much simpler.
- Moving from task-based workflows takes time. Expect both models to run side by side for a while.

# Questions to ask

- Do consumers care about when jobs run, or about how fresh particular datasets are?
- How many dependencies cross team or tool boundaries today, and how are they wired?
- Is there a shared naming scheme for datasets across the catalogue, lineage and pipelines?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Orchestration](orchestration.md) |
| Broader | [Orchestration](orchestration.md) |
| Related | [Continuous training](../mlops/continuous-training.md), [Data service levels](../data-products/data-slas.md), [Declarative pipelines](../processing/declarative-pipelines.md), [Freshness monitoring](../data-quality/freshness-monitoring.md), [Incremental processing](../processing/incremental-processing.md), [ML pipelines](../machine-learning/ml-pipelines.md), [Table-level lineage](../metadata/table-lineage.md) |

# Where it appears

- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md)
- **Maturity tracks:** [Orchestration](../../maturity/track-orchestration.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Managed Workflows for Apache Airflow](../../technologies/aws/aws-mwaa.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Managed Service for Apache Airflow](../../technologies/google-cloud/gcp-managed-airflow.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Dynamic Tables](../../technologies/snowflake/snowflake-dynamic-tables.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Lakeflow Jobs](../../technologies/databricks/databricks-lakeflow-jobs.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Airflow](../../technologies/open-source/apache-airflow.md), [Dagster](../../technologies/open-source/dagster.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Astronomer Astro](../../technologies/independent/astronomer-astro.md), [Dagster+](../../technologies/independent/dagster-plus.md) |
