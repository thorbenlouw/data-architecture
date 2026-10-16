---
type: Technology
id: gcp-bigquery-change-history
title: BigQuery change history (APPENDS and CHANGES)
description: Table-valued functions that return rows appended to, or changed in, a table over a time range so downstream jobs can process only the delta.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [change-feeds, incremental-processing]
resource: https://docs.cloud.google.com/bigquery/docs/change-history
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

APPENDS and CHANGES became GA in July 2026. CHANGES (which includes updates and deletes) needs the table option enable_change_history, the window is bounded by time travel, and CHANGES cannot be combined with stateful continuous query operations.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Change feeds](../../capabilities/serving/change-feeds.md) (Serving and activation) (primary): Expose row-level changes to tables as a stream that downstream consumers can process incrementally.
- [Incremental processing](../../capabilities/processing/incremental-processing.md) (Processing and transformation): Process only new or changed data instead of recomputing everything each run.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon DynamoDB](../aws/aws-dynamodb.md) | [Change feeds](../../capabilities/serving/change-feeds.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Cosmos DB](../microsoft/azure-cosmos-db.md) | [Change feeds](../../capabilities/serving/change-feeds.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake streams](../snowflake/snowflake-streams.md) | [Change feeds](../../capabilities/serving/change-feeds.md), [Incremental processing](../../capabilities/processing/incremental-processing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks change data feed](../databricks/databricks-change-data-feed.md) | [Change feeds](../../capabilities/serving/change-feeds.md), [Incremental processing](../../capabilities/processing/incremental-processing.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud data products](../sap/sap-bdc-data-products.md) | [Change feeds](../../capabilities/serving/change-feeds.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Hudi](../open-source/apache-hudi.md), [Debezium](../open-source/debezium.md), [Apache Paimon](../open-source/apache-paimon.md) | [Change feeds](../../capabilities/serving/change-feeds.md), [Incremental processing](../../capabilities/processing/incremental-processing.md) |
