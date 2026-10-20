---
type: Technology
id: azure-cosmos-db
title: Azure Cosmos DB
description: A globally distributed NoSQL database with single-digit millisecond reads, multi-region writes, a change feed and vector search.
platform: platform-microsoft
kind: managed-service
availability: ga
realises:
- operational-database
- low-latency-serving
- change-feeds
- vector-search
- cross-region-failover
- full-text-search
resource: https://learn.microsoft.com/en-us/azure/cosmos-db/introduction
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Analytics through Fabric mirroring; Synapse Link is deprecated. Also offers MongoDB, Cassandra, PostgreSQL and other APIs.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Operational database integration](../../capabilities/serving/operational-database.md) (Serving and activation) (primary): Run transactional databases as part of the platform, with data flowing to and from analytical storage without separate pipelines.
- [Low-latency serving](../../capabilities/serving/low-latency-serving.md) (Serving and activation): Serve individual records or small result sets to applications in milliseconds.
- [Change feeds](../../capabilities/serving/change-feeds.md) (Serving and activation): Expose row-level changes to tables as a stream that downstream consumers can process incrementally.
- [Vector search](../../capabilities/generative-ai/vector-search.md) (Generative AI): Store embeddings and find the most similar items quickly.
- [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) (Platform operations): Replicate data and configuration to another region and fail over when needed.
- [Full-text search](../../capabilities/specialised-data/full-text-search.md) (Specialised data types): Index text for full-text search, relevance ranking and fast filtering.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Aurora](../aws/aws-aurora.md), [Amazon DynamoDB](../aws/aws-dynamodb.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md), [Operational database integration](../../capabilities/serving/operational-database.md), [Vector search](../../capabilities/generative-ai/vector-search.md), [Change feeds](../../capabilities/serving/change-feeds.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Spanner](../google-cloud/gcp-spanner.md), [Firestore](../google-cloud/gcp-firestore.md), [AlloyDB for PostgreSQL](../google-cloud/gcp-alloydb.md) | [Change feeds](../../capabilities/serving/change-feeds.md), [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Postgres](../snowflake/snowflake-postgres.md), [Snowflake hybrid tables (Unistore)](../snowflake/snowflake-hybrid-tables.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakebase](../databricks/databricks-lakebase.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Managed Postgres](../clickhouse/clickhouse-managed-postgres.md) (preview) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Operational Database](../cloudera/cloudera-operational-database.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md), [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../oracle/oracle-database-multicloud.md), [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Operational database integration](../../capabilities/serving/operational-database.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Astra DB (DataStax)](../ibm/ibm-astra-db.md), [IBM Db2](../ibm/ibm-db2.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Operational database integration](../../capabilities/serving/operational-database.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS SpeedyStore](../sas/sas-speedystore.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [PostgreSQL](../open-source/postgresql.md) | [Operational database integration](../../capabilities/serving/operational-database.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [MongoDB Atlas](../independent/mongodb-atlas.md), [Redis Cloud](../independent/redis-cloud.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Operational database integration](../../capabilities/serving/operational-database.md), [Vector search](../../capabilities/generative-ai/vector-search.md), [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) |
