---
type: Technology
id: fabric-ai-functions
title: AI functions in Fabric
description: One-line LLM calls on pandas and PySpark DataFrames, and in T-SQL, to classify, extract, summarise, translate, embed or analyse sentiment.
platform: platform-microsoft
kind: feature
availability: ga
realises: [ai-functions, embedding-generation]
resource: https://learn.microsoft.com/en-us/fabric/data-science/ai-functions/overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Default model is a Microsoft-hosted GPT model billed as capacity units. T-SQL AI functions in the warehouse were announced in preview in March 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI functions in SQL](../../capabilities/processing/ai-functions.md) (Processing and transformation) (primary): Call language models from SQL or DataFrame code to classify, extract, summarise or translate data at scale.
- [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) (Generative AI): Turn text, images or other content into vector embeddings for search and retrieval.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift ML](../aws/aws-redshift-ml.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery generative AI functions](../google-cloud/gcp-bigquery-ai-functions.md), [BigQuery DataFrames](../google-cloud/gcp-bigquery-dataframes.md), [AlloyDB for PostgreSQL](../google-cloud/gcp-alloydb.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Functions](../snowflake/snowflake-cortex-ai-functions.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Functions](../databricks/databricks-ai-functions.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse AI functions](../clickhouse/clickhouse-ai-functions.md) (preview) | [AI functions in SQL](../../capabilities/processing/ai-functions.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud AI Assistant, AI Data Agents and MCP Server](../oracle/oracle-analytics-cloud-ai.md), [Oracle Select AI](../oracle/oracle-select-ai.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Intelligence](../ibm/confluent-intelligence.md) (preview) | [AI functions in SQL](../../capabilities/processing/ai-functions.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md), [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Prompt Studios](../dataiku/dataiku-prompt-studios.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
