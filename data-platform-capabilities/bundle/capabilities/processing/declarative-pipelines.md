---
type: Capability
id: declarative-pipelines
title: Declarative pipelines
description: Declare target tables and their logic, and let the platform work out execution order, incremental refresh and retries.
aliases: [dynamic tables, materialised pipelines]
broader: [processing]
related:
- transformation-as-code
- materialised-views
- asset-based-orchestration
- data-quality-rules
- bad-data-quarantine
depends_on: [incremental-processing]
tags: [processing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The author states what each target table or view should contain, as a query, together with expectations about quality and freshness. The platform builds the dependency graph, decides the order of execution, chooses between full and incremental refresh, provisions compute, retries failures and records lineage and quality metrics. A team might declare a raw table reading new files, a cleaned table built from it and a summary table on top; the platform keeps all three current, in batch or streaming mode, with no hand-written schedule of tasks.

This reduces orchestration code and makes incremental and streaming logic easier to get right, because the engine tracks what changed. The cost is control: the platform makes execution decisions, debugging happens through its interface, and pipeline definitions are often tied to one engine. Dynamic tables, chains of materialised views and framework-managed pipelines are variants of the idea. Transformation as code also declares models, but usually depends on an external scheduler and leaves incremental logic to the author.

# Key considerations

- Check which operations refresh incrementally. Unsupported ones may silently fall back to full recomputation and cost more.
- Understand how refresh frequency or target lag is set and how it is billed.
- Keep pipeline definitions in version control and deploy them through CI, not only through a user interface.
- Confirm what a failed quality expectation does: warn, drop rows, quarantine them or stop the pipeline.

# Questions to ask

- How much effort goes into schedules, retries and incremental logic today?
- Is tying this layer to one engine acceptable, or must the logic be portable?
- Does the same pipeline need to run in both batch and streaming modes?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Processing and transformation](processing.md) |
| Broader | [Processing and transformation](processing.md) |
| Related | [Orchestration](../orchestration/orchestration.md), [Bad-data quarantine](../data-quality/bad-data-quarantine.md), [Data quality rules](../data-quality/data-quality-rules.md), [Data-aware orchestration](../orchestration/asset-based-orchestration.md), [Materialised views](../compute/materialised-views.md), [Streaming SQL](streaming-sql.md), [Transformation as code](transformation-as-code.md), [Workflow orchestration](../orchestration/workflow-orchestration.md) |
| Depends on | [Incremental processing](incremental-processing.md) |

# Where it appears

- **Patterns:** [Medallion architecture](../../patterns/medallion-architecture.md)
- **Maturity tracks:** [Transformation engineering](../../maturity/track-transformation.md) (from level 3, Defined)
- **Frameworks:** [Data mesh principles](../../frameworks/framework-data-mesh.md): Self-serve platform – data product developer experience plane

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Materialized lake views | [Fabric materialized lake views](../../technologies/microsoft/fabric-materialized-lake-views.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Dataform](../../technologies/google-cloud/gcp-dataform.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | Dynamic Tables | [Snowflake Dynamic Tables](../../technologies/snowflake/snowflake-dynamic-tables.md) |
| [Databricks](../../platforms/platform-databricks.md) | Lakeflow pipelines (Spark Declarative Pipelines) | [Lakeflow pipelines](../../technologies/databricks/databricks-lakeflow-pipelines.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Pipeline Builder](../../technologies/palantir/palantir-pipeline-builder.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Flink](../../technologies/open-source/apache-flink.md), [Spark Declarative Pipelines](../../technologies/open-source/apache-spark-declarative-pipelines.md) |
