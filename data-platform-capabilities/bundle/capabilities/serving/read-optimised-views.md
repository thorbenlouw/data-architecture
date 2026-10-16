---
type: Capability
id: read-optimised-views
title: Read-optimised views
description: Precompute tables in the shape consumers read them, such as pre-joined or pre-aggregated tables, and keep them current with pipelines so reads are fast and cheap.
aliases:
- serving tables
- aggregate tables
- summary tables
- denormalised tables
- read models
- precomputed aggregates
broader: [serving]
related: [materialised-views, semantic-layer, operational-data-store, data-modelling, incremental-processing]
tags: [serving]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

These are tables built from detailed data and stored in the exact shape consumers query: pre-joined, pre-aggregated, filtered and sorted. Instead of every dashboard joining billions of order lines with products and stores and summing by day, a pipeline builds a daily sales-by-store table once and dashboards read a few thousand rows from it. The same idea appears as aggregate tables, OLAP cubes, wide denormalised tables and, in application design, the read models of command query responsibility segregation (CQRS).

They trade storage and refresh work for fast, cheap and predictable reads, and they pay off most where many consumers run similar queries or response times must be consistent. Materialised views are one way to build them, with the engine keeping results current. Others are tables refreshed by transformation pipelines, or copies loaded into a separate serving store. The design question is which shapes to precompute: too few and queries stay slow, too many and refresh cost and confusion grow.

# Key considerations

- Choose views from observed query history rather than guesses about what consumers will ask.
- Make refresh frequency and dependencies explicit, and show consumers when each view was last updated.
- Keep business logic in one modelling layer. Views that calculate measures differently from the semantic layer produce conflicting numbers.
- Retire unused views. They go on costing refresh compute long after their last reader has gone.

# Questions to ask

- Which queries run most often, or cost the most, today?
- What response time do dashboards and applications need, and at what concurrency?
- How fresh must the precomputed data be?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Serving and activation](serving.md) |
| Broader | [Serving and activation](serving.md) |
| Related | [Data modelling and design](../development-lifecycle/data-modelling.md), [Incremental processing](../processing/incremental-processing.md), [Materialised views](../compute/materialised-views.md), [Operational data store](operational-data-store.md), [Query acceleration](../compute/query-acceleration.md), [Semantic layer](../analytics-bi/semantic-layer.md) |

# Where it appears

- **Use cases:** [Customer-facing analytics](../../use-cases/usecase-customer-facing-analytics.md) (requires, level 3)
- **Patterns:** [Separate read models](../../patterns/cqrs-read-models.md) · [Lambda architecture](../../patterns/lambda-architecture.md) · [One big table](../../patterns/one-big-table.md)
- **Personas:** [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Data serving](../../maturity/track-serving.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Dynamic Tables](../../technologies/snowflake/snowflake-dynamic-tables.md), [Snowflake interactive tables and interactive warehouses](../../technologies/snowflake/snowflake-interactive-tables.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Lakebase](../../technologies/databricks/databricks-lakebase.md), [Lakeflow pipelines](../../technologies/databricks/databricks-lakeflow-pipelines.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | Materialized views and projections |  |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Druid](../../technologies/open-source/apache-druid.md) |
