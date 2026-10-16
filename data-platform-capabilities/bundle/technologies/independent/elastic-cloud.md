---
type: Technology
id: elastic-cloud
title: Elastic Cloud
description: Managed Elasticsearch, offered serverless or as hosted clusters, for full-text, log and vector search, with observability and security solutions and an agent builder.
aliases: [Elasticsearch, Elastic Cloud Serverless, Elastic Cloud Hosted]
platform: platform-independent
vendor: Elastic
kind: managed-service
availability: ga
realises:
- full-text-search
- vector-search
- serverless-compute
- ai-agents
- observability-analytics
- permission-aware-retrieval
resource: https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud/serverless
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Serverless project types are Elasticsearch, Vector Database, Observability and Security, with separate storage and compute. Elastic Cloud Hosted keeps node and version control. Agent Builder defines agents with ES|QL, search, workflow and MCP tools.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Full-text search](../../capabilities/specialised-data/full-text-search.md) (Specialised data types) (primary): Index text for full-text search, relevance ranking and fast filtering.
- [Vector search](../../capabilities/generative-ai/vector-search.md) (Generative AI): Store embeddings and find the most similar items quickly.
- [Serverless compute](../../capabilities/compute/serverless-compute.md) (Query and compute): Run workloads without managing servers, with capacity allocated on demand and billed by use.
- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI): Build systems in which models plan, call tools and act over several steps to complete a task.
- [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md) (Specialised data types): Store and analyse logs, metrics and traces from applications and infrastructure at scale, with search, dashboards and alerts.
- [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md) (Generative AI): Filter retrieved content by each user's permissions in the source systems so AI answers never reveal what the user could not open.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon OpenSearch Service](../aws/aws-opensearch-service.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure AI Search](../microsoft/azure-ai-search.md), [Cosmos DB in Microsoft Fabric](../microsoft/fabric-cosmos-db.md), [Azure Cosmos DB](../microsoft/azure-cosmos-db.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Search](../google-cloud/gcp-agent-search.md), [Spanner](../google-cloud/gcp-spanner.md), [BigQuery search indexes](../google-cloud/gcp-bigquery-search-indexes.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Search](../snowflake/snowflake-cortex-search.md), [Snowflake Search Optimization Service](../snowflake/snowflake-search-optimization-service.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Search](../databricks/databricks-ai-search.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse text indexes (full-text search)](../clickhouse/clickhouse-text-indexes.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [IBM](../../platforms/platform-ibm.md) | [OpenSearch and OpenRAG in IBM watsonx.data](../ibm/ibm-watsonx-data-opensearch-openrag.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenSearch](../open-source/opensearch.md), [Milvus](../open-source/milvus.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
