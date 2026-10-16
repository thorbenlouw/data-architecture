---
type: Technology
id: cloudera-operational-database
title: Cloudera Operational Database
description: Autoscaling Apache HBase service with Apache Phoenix SQL for low-latency reads and writes on large, sparse operational datasets.
aliases: [COD]
platform: platform-cloudera
kind: managed-service
availability: ga
realises: [low-latency-serving, operational-database, operational-data-store]
resource: https://docs.cloudera.com/
tags: [cloudera]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Offered as a data service on cloud and as HBase/Phoenix in Base on premises. Typical uses are lookups, time-stamped event stores and serving precomputed results to applications.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Low-latency serving](../../capabilities/serving/low-latency-serving.md) (Serving and activation) (primary): Serve individual records or small result sets to applications in milliseconds.
- [Operational database integration](../../capabilities/serving/operational-database.md) (Serving and activation): Run transactional databases as part of the platform, with data flowing to and from analytical storage without separate pipelines.
- [Operational data store](../../capabilities/serving/operational-data-store.md) (Serving and activation): Hold a current, integrated view of data from several operational systems for operational reporting and lookups.

**Platform:** [Cloudera](../../platforms/platform-cloudera.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon DynamoDB](../aws/aws-dynamodb.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Cosmos DB in Microsoft Fabric](../microsoft/fabric-cosmos-db.md), [Azure Cosmos DB](../microsoft/azure-cosmos-db.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Firestore](../google-cloud/gcp-firestore.md), [Memorystore](../google-cloud/gcp-memorystore.md), [Bigtable](../google-cloud/gcp-bigtable.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake hybrid tables (Unistore)](../snowflake/snowflake-hybrid-tables.md), [Snowflake Postgres](../snowflake/snowflake-postgres.md), [Snowflake interactive tables and interactive warehouses](../snowflake/snowflake-interactive-tables.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational data store](../../capabilities/serving/operational-data-store.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakebase](../databricks/databricks-lakebase.md), [Databricks Lakehouse Real-Time](../databricks/databricks-lakehouse-real-time.md) (preview) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud Query API Endpoints](../clickhouse/clickhouse-query-api-endpoints.md), [ClickHouse dictionaries](../clickhouse/clickhouse-dictionaries.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Astra DB (DataStax)](../ibm/ibm-astra-db.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Ontology](../palantir/palantir-ontology.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational data store](../../capabilities/serving/operational-data-store.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redis Cloud](../independent/redis-cloud.md), [K2view Data Product Platform](../independent/k2view-data-product-platform.md), [StarTree Cloud](../independent/startree-cloud.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational data store](../../capabilities/serving/operational-data-store.md) |
