---
type: Capability
id: low-latency-serving
title: Low-latency serving
description: Serve individual records or small result sets to applications in milliseconds.
aliases: [key-value serving, point lookups, online store]
broader: [serving]
related: [real-time-analytics, data-apis, real-time-inference, operational-data-store]
tags: [serving]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A typical request asks for one record or a small set, such as "this customer's current segment and recommended offers", and must be answered in single-digit or tens of milliseconds, often thousands of times a second. The data is computed on the analytical platform and loaded into a store built for key lookups: a key-value store, document database, in-memory cache, or a real-time analytical database for small aggregates. The application queries that store through an API or client library and never scans the warehouse directly.

Analytical engines are built to scan large volumes. Even small queries usually take hundreds of milliseconds or more, and concurrency is limited. Personalisation, pricing, fraud checks and customer portals need fast, predictable answers at high request rates, so a separate serving tier is needed. Data reaches it either by push, with pipelines writing results on a schedule or from a stream, or through a read-through cache in front of a slower store. Online feature stores are a specialised form for model features.

# Key considerations

- Design keys and records around the exact lookup the application makes. Secondary queries on serving stores often perform poorly.
- Define freshness and how updates reach the store, including how deletes and corrections propagate.
- Plan availability and capacity across zones or regions. Applications fail visibly when the serving tier is down.
- Measure tail latency, such as the 99th percentile, not only averages. Slow outliers are what users notice.

# Questions to ask

- What response time and request rate does the application need, including at peak?
- What is the lookup key, and how many records and attributes are served?
- How stale can a served value be before it leads to a wrong decision?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Serving and activation](serving.md) |
| Broader | [Serving and activation](serving.md) |
| Narrower | [Online feature store](../machine-learning/online-feature-store.md) |
| Related | [Agent memory](../generative-ai/agent-memory.md), [Data APIs](data-apis.md), [Feature store](../machine-learning/feature-store.md), [Graph data](../specialised-data/graph-data.md), [Indexes and data skipping](../compute/data-skipping-indexes.md), [Operational data store](operational-data-store.md), [Operational database integration](operational-database.md), [Real-time analytical database](../compute/real-time-analytics.md), [Real-time inference](../mlops/real-time-inference.md) |

# Where it appears

- **Use cases:** [Customer 360](../../use-cases/usecase-customer-360.md) (requires, level 3) · [Personalised recommendations](../../use-cases/usecase-recommendations.md) (requires, level 3)
- **Patterns:** [Separate read models](../../patterns/cqrs-read-models.md) · [Lambda architecture](../../patterns/lambda-architecture.md)
- **Personas:** [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Data serving](../../maturity/track-serving.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon DynamoDB](../../technologies/aws/aws-dynamodb.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Cosmos DB](../../technologies/microsoft/azure-cosmos-db.md), [Cosmos DB in Microsoft Fabric](../../technologies/microsoft/fabric-cosmos-db.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Bigtable](../../technologies/google-cloud/gcp-bigtable.md), [Firestore](../../technologies/google-cloud/gcp-firestore.md), [Memorystore](../../technologies/google-cloud/gcp-memorystore.md), [Spanner](../../technologies/google-cloud/gcp-spanner.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake hybrid tables (Unistore)](../../technologies/snowflake/snowflake-hybrid-tables.md), [Snowflake interactive tables and interactive warehouses](../../technologies/snowflake/snowflake-interactive-tables.md), [Snowflake Postgres](../../technologies/snowflake/snowflake-postgres.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Lakehouse Real-Time](../../technologies/databricks/databricks-lakehouse-real-time.md) (preview), [Lakebase](../../technologies/databricks/databricks-lakebase.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse Cloud Query API Endpoints](../../technologies/clickhouse/clickhouse-query-api-endpoints.md), [ClickHouse dictionaries](../../technologies/clickhouse/clickhouse-dictionaries.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Operational Database](../../technologies/cloudera/cloudera-operational-database.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM Astra DB (DataStax)](../../technologies/ibm/ibm-astra-db.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Ontology](../../technologies/palantir/palantir-ontology.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [K2view Data Product Platform](../../technologies/independent/k2view-data-product-platform.md), [Redis Cloud](../../technologies/independent/redis-cloud.md), [Reltio Multidomain MDM](../../technologies/independent/reltio-multidomain-mdm.md), [StarTree Cloud](../../technologies/independent/startree-cloud.md) |

Narrower capabilities are realised by a further 9 technologies; see their pages.
