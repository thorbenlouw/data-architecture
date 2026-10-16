---
type: Capability
id: streaming-sql
title: Streaming SQL
description: Express continuous transformations and incrementally maintained views over streams in SQL.
broader: [stream-processing]
related: [materialised-views, change-data-capture, change-feeds, declarative-pipelines, schema-registry]
depends_on: [event-streaming]
tags: [processing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A SQL query over a stream or changing table is compiled into a job that never finishes: it updates its result as each event arrives. A `GROUP BY` keeps running aggregates, and a join holds state for both inputs so new rows on either side can find their match. Some systems expose the result as an incrementally maintained view that other queries read like a table, current to within seconds of the source changing.

It brings stream processing within reach of people who know SQL but not streaming APIs, and lets batch and streaming logic share one language. The meaning differs from batch SQL: results change over time, output can include updates and retractions as well as new rows, and unbounded joins can keep state forever unless limited by time. Some products build on general stream processors such as Flink; others are databases designed around incremental view maintenance. Warehouse materialised views are usually refreshed on a schedule, whereas streaming SQL updates continuously.

# Key considerations

- Unbounded joins and aggregations grow state without limit. Require time bounds or state expiry.
- Check how results are emitted (append, upsert or retraction) and whether downstream systems can consume that form.
- Not all SQL works on streams. Sorting, some window functions and subqueries are often restricted.
- Source schema changes can break running queries. Plan how queries are versioned and restarted.

# Questions to ask

- Do the people building real-time logic know SQL better than streaming APIs?
- Do consumers need a stream of changes, or a view they can query that is always current?
- How much state will the joins and aggregations need to hold?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Processing and transformation](processing.md) |
| Broader | [Stream processing](stream-processing.md) |
| Related | [Change data capture](../ingestion-integration/change-data-capture.md), [Change feeds](../serving/change-feeds.md), [Declarative pipelines](declarative-pipelines.md), [Materialised views](../compute/materialised-views.md), [Schema registry](../metadata/schema-registry.md) |
| Depends on | [Event streaming](../ingestion-integration/event-streaming.md) |

# Where it appears

- **Use cases:** [Operational reporting](../../use-cases/usecase-operational-reporting.md) (benefits from) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (benefits from)
- **Patterns:** [Kappa architecture](../../patterns/kappa-architecture.md)
- **Maturity tracks:** [Real-time and streaming](../../maturity/track-real-time.md) (from level 3, Defined) · [Transformation engineering](../../maturity/track-transformation.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Managed Service for Apache Flink](../../technologies/aws/aws-managed-flink.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Stream Analytics](../../technologies/microsoft/azure-stream-analytics.md), [Fabric Eventstream](../../technologies/microsoft/fabric-eventstream.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | BigQuery continuous queries | [BigQuery continuous queries](../../technologies/google-cloud/gcp-bigquery-continuous-queries.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Lakeflow pipelines](../../technologies/databricks/databricks-lakeflow-pipelines.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | SQL Stream Builder | [Cloudera Streaming Analytics](../../technologies/cloudera/cloudera-streaming-analytics.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Confluent Cloud for Apache Flink](../../technologies/ibm/confluent-cloud-flink.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Flink](../../technologies/open-source/apache-flink.md), [RisingWave](../../technologies/open-source/risingwave.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Materialize](../../technologies/independent/materialize.md), [Striim Cloud](../../technologies/independent/striim-cloud.md) |
