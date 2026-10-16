---
type: Technology
id: opensearch
title: OpenSearch
description: Search and analytics engine for full-text search, log analytics and vector search, with dashboards for visualisation.
aliases: [OpenSearch Dashboards]
platform: platform-open-source
kind: open-source
availability: ga
realises: [full-text-search, vector-search, dashboards-reports, observability-analytics]
resource: https://opensearch.org/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, forked from Elasticsearch in 2021 after Elastic's licence change; governed by the OpenSearch Software Foundation under the Linux Foundation since 2024. Elastic added AGPLv3 as an option for Elasticsearch in 2024, so both are open source again but with different licences.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Full-text search](../../capabilities/specialised-data/full-text-search.md) (Specialised data types) (primary): Index text for full-text search, relevance ranking and fast filtering.
- [Vector search](../../capabilities/generative-ai/vector-search.md) (Generative AI): Store embeddings and find the most similar items quickly.
- [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) (Analytics and BI): Build and share visual, interactive dashboards with filters and drill-down.
- [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md) (Specialised data types): Store and analyse logs, metrics and traces from applications and infrastructure at scale, with search, dashboards and alerts.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon OpenSearch Service](../aws/aws-opensearch-service.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure AI Search](../microsoft/azure-ai-search.md), [Cosmos DB in Microsoft Fabric](../microsoft/fabric-cosmos-db.md), [Azure Cosmos DB](../microsoft/azure-cosmos-db.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Search](../google-cloud/gcp-agent-search.md), [Spanner](../google-cloud/gcp-spanner.md), [BigQuery search indexes](../google-cloud/gcp-bigquery-search-indexes.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Search](../snowflake/snowflake-cortex-search.md), [Snowflake Search Optimization Service](../snowflake/snowflake-search-optimization-service.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Search](../databricks/databricks-ai-search.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse text indexes (full-text search)](../clickhouse/clickhouse-text-indexes.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [IBM](../../platforms/platform-ibm.md) | [OpenSearch and OpenRAG in IBM watsonx.data](../ibm/ibm-watsonx-data-opensearch-openrag.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Elastic Cloud](../independent/elastic-cloud.md), [Weaviate Cloud](../independent/weaviate-cloud.md), [MongoDB Atlas](../independent/mongodb-atlas.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
