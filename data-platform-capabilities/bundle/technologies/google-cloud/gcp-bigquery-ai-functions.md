---
type: Technology
id: gcp-bigquery-ai-functions
title: BigQuery generative AI functions
description: SQL functions such as AI.GENERATE, AI.GENERATE_TABLE, AI.IF, AI.CLASSIFY, AI.SCORE, AI.AGG and AI.EMBED that call Gemini and partner models over table rows and unstructured objects.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [ai-functions, embedding-generation, ai-spend-controls]
resource: https://docs.cloud.google.com/bigquery/docs/generative-ai-overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

AI.IF, AI.SCORE and AI.CLASSIFY went GA in April 2026 and AI.AGG in October 2026; optimised mode for some functions is in preview. Remote models reach Gemini, Claude, Mistral, Llama and open models on Agent Platform. Daily token quotas (GA June 2026) cap spend.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI functions in SQL](../../capabilities/processing/ai-functions.md) (Processing and transformation) (primary): Call language models from SQL or DataFrame code to classify, extract, summarise or translate data at scale.
- [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) (Generative AI): Turn text, images or other content into vector embeddings for search and retrieval.
- [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) (Platform operations): Limit, prioritise and attribute model and agent consumption per user, team or application.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift ML](../aws/aws-redshift-ml.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [AI functions in Fabric](../microsoft/fabric-ai-functions.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Functions](../snowflake/snowflake-cortex-ai-functions.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Functions](../databricks/databricks-ai-functions.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse AI functions](../clickhouse/clickhouse-ai-functions.md) (preview) | [AI functions in SQL](../../capabilities/processing/ai-functions.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud AI Assistant, AI Data Agents and MCP Server](../oracle/oracle-analytics-cloud-ai.md), [Oracle Select AI](../oracle/oracle-select-ai.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Intelligence](../ibm/confluent-intelligence.md) (preview) | [AI functions in SQL](../../capabilities/processing/ai-functions.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md), [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
