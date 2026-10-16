---
type: Technology
id: snowflake-streams
title: Snowflake streams
description: Track inserts, updates and deletes on tables, views and other objects since an offset, so downstream jobs process only the changes.
platform: platform-snowflake
kind: feature
availability: ga
realises: [change-feeds, incremental-processing]
resource: https://docs.snowflake.com/en/user-guide/streams-intro
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Stream types are standard, append-only and insert-only (for external and externally managed Iceberg tables). A stream goes stale if it is not consumed within the source's retention period.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Change feeds](../../capabilities/serving/change-feeds.md) (Serving and activation) (primary): Expose row-level changes to tables as a stream that downstream consumers can process incrementally.
- [Incremental processing](../../capabilities/processing/incremental-processing.md) (Processing and transformation): Process only new or changed data instead of recomputing everything each run.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon DynamoDB](../aws/aws-dynamodb.md) | [Change feeds](../../capabilities/serving/change-feeds.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Cosmos DB](../microsoft/azure-cosmos-db.md) | [Change feeds](../../capabilities/serving/change-feeds.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery change history (APPENDS and CHANGES)](../google-cloud/gcp-bigquery-change-history.md), [Bigtable](../google-cloud/gcp-bigtable.md), [Spanner](../google-cloud/gcp-spanner.md) | [Change feeds](../../capabilities/serving/change-feeds.md), [Incremental processing](../../capabilities/processing/incremental-processing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks change data feed](../databricks/databricks-change-data-feed.md) | [Change feeds](../../capabilities/serving/change-feeds.md), [Incremental processing](../../capabilities/processing/incremental-processing.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud data products](../sap/sap-bdc-data-products.md) | [Change feeds](../../capabilities/serving/change-feeds.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Hudi](../open-source/apache-hudi.md), [Debezium](../open-source/debezium.md), [Apache Paimon](../open-source/apache-paimon.md) | [Change feeds](../../capabilities/serving/change-feeds.md), [Incremental processing](../../capabilities/processing/incremental-processing.md) |
