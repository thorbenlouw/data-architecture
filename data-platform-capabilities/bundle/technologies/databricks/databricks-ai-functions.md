---
type: Technology
id: databricks-ai-functions
title: Databricks AI Functions
description: SQL and Python functions that call models over table data. They include ai_query, ai_extract, ai_classify, ai_summarize, ai_translate, ai_mask, ai_forecast and ai_similarity, with ai_search, ai_prep_search and ai_transcribe in Beta.
platform: platform-databricks
kind: feature
availability: ga
realises: [ai-functions, batch-inference, deidentification, audio-video-processing]
resource: https://docs.databricks.com/aws/en/large-language-models/ai-functions
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ai_query became GA in June 2026 and is the recommended route for batch LLM inference. ai_extract and ai_classify became GA in June 2026 with no-code Agent Bricks UIs. An AI Functions REST API became GA in August 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI functions in SQL](../../capabilities/processing/ai-functions.md) (Processing and transformation) (primary): Call language models from SQL or DataFrame code to classify, extract, summarise or translate data at scale.
- [Batch inference](../../capabilities/mlops/batch-inference.md) (ML operations): Score large datasets with a model on a schedule.
- [De-identification](../../capabilities/governance/deidentification.md) (Governance and compliance): Pseudonymise, tokenise or anonymise data so it can be used with less privacy risk.
- [Audio and video processing](../../capabilities/specialised-data/audio-video-processing.md) (Specialised data types): Transcribe and extract content from audio and video at scale for analysis and retrieval.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift ML](../aws/aws-redshift-ml.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md), [Batch inference](../../capabilities/mlops/batch-inference.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [AI functions in Fabric](../microsoft/fabric-ai-functions.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery generative AI functions](../google-cloud/gcp-bigquery-ai-functions.md), [BigQuery DataFrames](../google-cloud/gcp-bigquery-dataframes.md), [AlloyDB for PostgreSQL](../google-cloud/gcp-alloydb.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Functions](../snowflake/snowflake-cortex-ai-functions.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md), [Audio and video processing](../../capabilities/specialised-data/audio-video-processing.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse AI functions](../clickhouse/clickhouse-ai-functions.md) (preview) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud AI Assistant, AI Data Agents and MCP Server](../oracle/oracle-analytics-cloud-ai.md), [Oracle Select AI](../oracle/oracle-select-ai.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Intelligence](../ibm/confluent-intelligence.md) (preview) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md), [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Prompt Studios](../dataiku/dataiku-prompt-studios.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md) |
