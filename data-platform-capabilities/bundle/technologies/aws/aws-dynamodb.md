---
type: Technology
id: aws-dynamodb
title: Amazon DynamoDB
description: Serverless key-value and document database with single-digit millisecond reads and writes, which partitions data automatically as tables grow.
aliases: [DynamoDB Streams, DynamoDB global tables]
platform: platform-aws
kind: managed-service
availability: ga
realises:
- low-latency-serving
- operational-database
- change-feeds
- cross-region-failover
- online-feature-store
resource: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

DynamoDB Streams and Kinesis integration expose item changes; global tables replicate across Regions; point-in-time recovery and S3 export/import support analytics. Zero-ETL integrations feed Redshift, the SageMaker lakehouse and OpenSearch.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Low-latency serving](../../capabilities/serving/low-latency-serving.md) (Serving and activation) (primary): Serve individual records or small result sets to applications in milliseconds.
- [Operational database integration](../../capabilities/serving/operational-database.md) (Serving and activation): Run transactional databases as part of the platform, with data flowing to and from analytical storage without separate pipelines.
- [Change feeds](../../capabilities/serving/change-feeds.md) (Serving and activation): Expose row-level changes to tables as a stream that downstream consumers can process incrementally.
- [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) (Platform operations): Replicate data and configuration to another region and fail over when needed.
- [Online feature store](../../capabilities/machine-learning/online-feature-store.md) (Machine learning development): Serve the latest feature values to models in milliseconds.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Cosmos DB](../microsoft/azure-cosmos-db.md), [Cosmos DB in Microsoft Fabric](../microsoft/fabric-cosmos-db.md) | [Change feeds](../../capabilities/serving/change-feeds.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md), [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Bigtable](../google-cloud/gcp-bigtable.md), [Spanner](../google-cloud/gcp-spanner.md), [Memorystore](../google-cloud/gcp-memorystore.md) | [Change feeds](../../capabilities/serving/change-feeds.md), [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Online feature store](../../capabilities/machine-learning/online-feature-store.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Postgres](../snowflake/snowflake-postgres.md), [Snowflake hybrid tables (Unistore)](../snowflake/snowflake-hybrid-tables.md), [Snowflake interactive tables and interactive warehouses](../snowflake/snowflake-interactive-tables.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakebase](../databricks/databricks-lakebase.md), [Databricks Lakehouse Real-Time](../databricks/databricks-lakehouse-real-time.md) (preview) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud Query API Endpoints](../clickhouse/clickhouse-query-api-endpoints.md), [ClickHouse dictionaries](../clickhouse/clickhouse-dictionaries.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Operational Database](../cloudera/cloudera-operational-database.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Astra DB (DataStax)](../ibm/ibm-astra-db.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Ontology](../palantir/palantir-ontology.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redis Cloud](../independent/redis-cloud.md), [K2view Data Product Platform](../independent/k2view-data-product-platform.md), [StarTree Cloud](../independent/startree-cloud.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md), [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Online feature store](../../capabilities/machine-learning/online-feature-store.md) |
