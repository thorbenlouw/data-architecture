---
type: Technology
id: risingwave
title: RisingWave
description: Streaming database that keeps SQL materialised views continuously up to date over streams and CDC sources, with a PostgreSQL-compatible interface.
platform: platform-open-source
kind: open-source
availability: ga
realises: [streaming-sql, materialised-views, change-data-capture]
resource: https://docs.risingwave.com/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, company-led by RisingWave Labs. Stores state in object storage and can write results to Iceberg. An alternative to Flink SQL for teams who prefer a database interface.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Streaming SQL](../../capabilities/processing/streaming-sql.md) (Processing and transformation) (primary): Express continuous transformations and incrementally maintained views over streams in SQL.
- [Materialised views](../../capabilities/compute/materialised-views.md) (Query and compute): Have the query engine store a query's result, refresh it as sources change and optionally use it to answer other queries.
- [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) (Ingestion and integration): Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Service for Apache Flink](../aws/aws-managed-flink.md) | [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Eventstream](../microsoft/fabric-eventstream.md), [Azure Stream Analytics](../microsoft/azure-stream-analytics.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery continuous queries](../google-cloud/gcp-bigquery-continuous-queries.md) | [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow pipelines](../databricks/databricks-lakeflow-pipelines.md) | [Materialised views](../../capabilities/compute/materialised-views.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Streaming Analytics](../cloudera/cloudera-streaming-analytics.md) | [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud for Apache Flink](../ibm/confluent-cloud-flink.md) | [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Materialize](../independent/materialize.md), [Striim Cloud](../independent/striim-cloud.md) | [Materialised views](../../capabilities/compute/materialised-views.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md), [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) |
