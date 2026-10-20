---
type: Technology
id: clickhouse-ai-functions
title: ClickHouse AI functions
description: SQL functions such as aiGenerate, aiClassify, aiExtract, aiTranslate, aiRedact and aiEmbed that call an LLM or embedding endpoint for each row.
platform: platform-clickhouse
kind: feature
availability: preview
realises: [ai-functions, embedding-generation]
resource: https://clickhouse.com/docs/sql-reference/functions/ai-functions
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Beta, and documented as not available in ClickHouse Cloud services at present; the operator configures the model endpoint. Outputs depend on prompt and model.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI functions in SQL](../../capabilities/processing/ai-functions.md) (Processing and transformation) (primary): Call language models from SQL or DataFrame code to classify, extract, summarise or translate data at scale.
- [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) (Generative AI): Turn text, images or other content into vector embeddings for search and retrieval.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** preview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift ML](../aws/aws-redshift-ml.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [AI functions in Fabric](../microsoft/fabric-ai-functions.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery generative AI functions](../google-cloud/gcp-bigquery-ai-functions.md), [BigQuery DataFrames](../google-cloud/gcp-bigquery-dataframes.md), [AlloyDB for PostgreSQL](../google-cloud/gcp-alloydb.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Functions](../snowflake/snowflake-cortex-ai-functions.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Functions](../databricks/databricks-ai-functions.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud AI Assistant, AI Data Agents and MCP Server](../oracle/oracle-analytics-cloud-ai.md), [Oracle Select AI](../oracle/oracle-select-ai.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Intelligence](../ibm/confluent-intelligence.md) (preview) | [AI functions in SQL](../../capabilities/processing/ai-functions.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md), [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Prompt Studios](../dataiku/dataiku-prompt-studios.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
