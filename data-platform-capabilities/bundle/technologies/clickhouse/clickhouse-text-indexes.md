---
type: Technology
id: clickhouse-text-indexes
title: ClickHouse text indexes (full-text search)
description: Inverted indexes on string, array and map columns with configurable tokenisers that answer token, phrase and pattern searches without scanning.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [full-text-search, data-skipping-indexes]
resource: https://clickhouse.com/docs/engines/table-engines/mergetree-family/textindexes
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA from ClickHouse 26.2 with tokenisers including n-grams, sparse grams, ICU and Chinese; phrase search is still experimental. Central to ClickStack log search and a common reason teams consider ClickHouse instead of Elasticsearch-style engines.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Full-text search](../../capabilities/specialised-data/full-text-search.md) (Specialised data types) (primary): Index text for full-text search, relevance ranking and fast filtering.
- [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) (Query and compute): Use indexes, statistics and filters to avoid scanning data that cannot match a query.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon OpenSearch Service](../aws/aws-opensearch-service.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure AI Search](../microsoft/azure-ai-search.md), [Cosmos DB in Microsoft Fabric](../microsoft/fabric-cosmos-db.md), [Azure Cosmos DB](../microsoft/azure-cosmos-db.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery search indexes](../google-cloud/gcp-bigquery-search-indexes.md), [Google Cloud Agent Search](../google-cloud/gcp-agent-search.md), [Spanner](../google-cloud/gcp-spanner.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Search Optimization Service](../snowflake/snowflake-search-optimization-service.md), [Snowflake Cortex Search](../snowflake/snowflake-cortex-search.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Search](../databricks/databricks-ai-search.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [IBM](../../platforms/platform-ibm.md) | [OpenSearch and OpenRAG in IBM watsonx.data](../ibm/ibm-watsonx-data-opensearch-openrag.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenSearch](../open-source/opensearch.md), [Milvus](../open-source/milvus.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Elastic Cloud](../independent/elastic-cloud.md), [Weaviate Cloud](../independent/weaviate-cloud.md), [MongoDB Atlas](../independent/mongodb-atlas.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
