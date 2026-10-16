---
type: Technology
id: aws-kendra
title: Amazon Kendra
description: Enterprise search service that indexes documents from many connectors and returns ranked, permission-filtered results.
platform: platform-aws
kind: managed-service
availability: deprecated
realises: [full-text-search, permission-aware-retrieval]
resource: https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html
tags: [aws]
status: deprecated
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

In maintenance since 30 June 2026 and closed to new customers from 30 July 2026. The replacement is Bedrock Managed Knowledge Base, which has fewer connectors and lacks facets, synonyms and query suggestions.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Full-text search](../../capabilities/specialised-data/full-text-search.md) (Specialised data types) (primary): Index text for full-text search, relevance ranking and fast filtering.
- [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md) (Generative AI): Filter retrieved content by each user's permissions in the source systems so AI answers never reveal what the user could not open.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** deprecated  
Not counted in platform coverage because it is deprecated.

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure AI Search](../microsoft/azure-ai-search.md), [Cosmos DB in Microsoft Fabric](../microsoft/fabric-cosmos-db.md), [Azure Cosmos DB](../microsoft/azure-cosmos-db.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Search](../google-cloud/gcp-agent-search.md), [BigQuery search indexes](../google-cloud/gcp-bigquery-search-indexes.md), [Spanner](../google-cloud/gcp-spanner.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Search Optimization Service](../snowflake/snowflake-search-optimization-service.md), [Snowflake Cortex Search](../snowflake/snowflake-cortex-search.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Search](../databricks/databricks-ai-search.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse text indexes (full-text search)](../clickhouse/clickhouse-text-indexes.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [IBM](../../platforms/platform-ibm.md) | [OpenSearch and OpenRAG in IBM watsonx.data](../ibm/ibm-watsonx-data-opensearch-openrag.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenSearch](../open-source/opensearch.md), [Milvus](../open-source/milvus.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Elastic Cloud](../independent/elastic-cloud.md), [Weaviate Cloud](../independent/weaviate-cloud.md), [MongoDB Atlas](../independent/mongodb-atlas.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md) |
