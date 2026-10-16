---
type: Technology
id: gcp-bigtable
title: Bigtable
description: Wide-column NoSQL database for very high-throughput, low-latency reads and writes, often used for time series, events and feature serving.
formerly: [Cloud Bigtable]
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [low-latency-serving, time-series-data, online-feature-store, change-feeds]
resource: https://docs.cloud.google.com/bigtable/docs/overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Supports GoogleSQL queries, continuous materialised views, change streams and Data Boost for isolated batch reads; tiered storage for infrequently read data is in preview. It is the storage behind Agent Platform Feature Store's Bigtable online serving.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Low-latency serving](../../capabilities/serving/low-latency-serving.md) (Serving and activation) (primary): Serve individual records or small result sets to applications in milliseconds.
- [Time-series data](../../capabilities/specialised-data/time-series-data.md) (Specialised data types): Store and query time-stamped measurements efficiently, with time-based functions and retention.
- [Online feature store](../../capabilities/machine-learning/online-feature-store.md) (Machine learning development): Serve the latest feature values to models in milliseconds.
- [Change feeds](../../capabilities/serving/change-feeds.md) (Serving and activation): Expose row-level changes to tables as a stream that downstream consumers can process incrementally.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon DynamoDB](../aws/aws-dynamodb.md) | [Change feeds](../../capabilities/serving/change-feeds.md), [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Online feature store](../../capabilities/machine-learning/online-feature-store.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Cosmos DB](../microsoft/azure-cosmos-db.md), [Cosmos DB in Microsoft Fabric](../microsoft/fabric-cosmos-db.md) | [Change feeds](../../capabilities/serving/change-feeds.md), [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Postgres](../snowflake/snowflake-postgres.md), [Snowflake hybrid tables (Unistore)](../snowflake/snowflake-hybrid-tables.md), [Snowflake interactive tables and interactive warehouses](../snowflake/snowflake-interactive-tables.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Lakehouse Real-Time](../databricks/databricks-lakehouse-real-time.md) (preview), [Lakebase](../databricks/databricks-lakebase.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud Query API Endpoints](../clickhouse/clickhouse-query-api-endpoints.md), [ClickHouse dictionaries](../clickhouse/clickhouse-dictionaries.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Operational Database](../cloudera/cloudera-operational-database.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Astra DB (DataStax)](../ibm/ibm-astra-db.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Ontology](../palantir/palantir-ontology.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redis Cloud](../independent/redis-cloud.md), [K2view Data Product Platform](../independent/k2view-data-product-platform.md), [StarTree Cloud](../independent/startree-cloud.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Online feature store](../../capabilities/machine-learning/online-feature-store.md) |
