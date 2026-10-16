---
type: Technology
id: snowflake-cortex-ai-functions
title: Snowflake Cortex AI Functions
description: SQL functions such as AI_COMPLETE, AI_CLASSIFY, AI_FILTER, AI_AGG, AI_SUMMARIZE_AGG, AI_EMBED, AI_SENTIMENT, AI_TRANSLATE, AI_TRANSCRIBE and AI_REDACT that apply hosted models to columns and files.
formerly: [Cortex AISQL, Cortex LLM functions]
platform: platform-snowflake
kind: feature
availability: ga
realises:
- ai-functions
- foundation-model-access
- embedding-generation
- deidentification
- audio-video-processing
- ai-spend-controls
resource: https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Some individual functions are still in preview. Models from Anthropic, OpenAI, Meta, Mistral and others run inside Snowflake, and cross-region inference is optional. Per-function privileges and spend controls became GA in 2026, and response caching was added in September 2026. Embeddings from AI_EMBED are stored in the native VECTOR type, which supports brute-force similarity functions in SQL. Use Cortex Search for indexed retrieval.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI functions in SQL](../../capabilities/processing/ai-functions.md) (Processing and transformation) (primary): Call language models from SQL or DataFrame code to classify, extract, summarise or translate data at scale.
- [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) (Generative AI): Use hosted large language and multimodal models through managed APIs inside the platform's security boundary.
- [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) (Generative AI): Turn text, images or other content into vector embeddings for search and retrieval.
- [De-identification](../../capabilities/governance/deidentification.md) (Governance and compliance): Pseudonymise, tokenise or anonymise data so it can be used with less privacy risk.
- [Audio and video processing](../../capabilities/specialised-data/audio-video-processing.md) (Specialised data types): Transcribe and extract content from audio and video at scale for analysis and retrieval.
- [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) (Platform operations): Limit, prioritise and attribute model and agent consumption per user, team or application.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake Cortex AI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift ML](../aws/aws-redshift-ml.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [AI functions in Fabric](../microsoft/fabric-ai-functions.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery generative AI functions](../google-cloud/gcp-bigquery-ai-functions.md), [BigQuery DataFrames](../google-cloud/gcp-bigquery-dataframes.md), [AlloyDB for PostgreSQL](../google-cloud/gcp-alloydb.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Functions](../databricks/databricks-ai-functions.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md), [Audio and video processing](../../capabilities/specialised-data/audio-video-processing.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse AI functions](../clickhouse/clickhouse-ai-functions.md) (preview) | [AI functions in SQL](../../capabilities/processing/ai-functions.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud AI Assistant, AI Data Agents and MCP Server](../oracle/oracle-analytics-cloud-ai.md), [Oracle Select AI](../oracle/oracle-select-ai.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Intelligence](../ibm/confluent-intelligence.md) (preview) | [AI functions in SQL](../../capabilities/processing/ai-functions.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md), [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
