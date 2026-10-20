---
type: Capability
id: ai-functions
title: AI functions in SQL
description: Call language models from SQL or DataFrame code to classify, extract, summarise or translate data at scale.
aliases: [AI SQL, LLM functions]
broader: [processing, generative-ai]
related: [embedding-generation, ai-spend-controls, genai-evaluation, in-database-ml, unstructured-data]
depends_on: [foundation-model-access]
tags: [processing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Language model calls are exposed as SQL or DataFrame functions, so a prompt is applied to every row a query returns. `SELECT ticket_id, ai_classify(body, ['billing', 'delivery', 'fault']) FROM tickets` sends each support ticket to a model and returns a category. Typical functions classify, extract fields into a fixed structure, summarise, translate, score sentiment or create embeddings. The platform handles batching, retries, rate limits and access to models inside its security boundary.

Analysts and engineers can process large volumes of text without building separate model-serving code, and results stay next to the data where they can be joined, governed and audited. Each call costs far more and takes far longer than an ordinary function, outputs are not fully repeatable, and model versions change underneath. AI functions suit batch enrichment of text columns; interactive applications are better served by a model endpoint. In-database machine learning is different: it trains and runs predictive models on numeric and categorical features.

# Key considerations

- Estimate cost before running on a whole table. Test on a sample and cap tokens per call.
- Store each result with the model name, version and prompt so it can be reproduced or recomputed.
- Outputs vary between runs. Use structured output schemas, low randomness settings and validation rules.
- Check what data leaves the platform boundary and whether the model provider retains it.
- Measure accuracy against a labelled sample before results appear in reports.

# Questions to ask

- How much text needs classifying, extracting or summarising, and how often?
- How accurate must results be, and how will accuracy be measured?
- What cost per thousand rows is acceptable?
- Are there rules about which data may be sent to which models?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Processing and transformation](processing.md) |
| Broader | [Processing and transformation](processing.md), [Generative AI](../generative-ai/generative-ai.md) |
| Related | [AI usage and spend controls](../platform-operations/ai-spend-controls.md), [Audio and video processing](../specialised-data/audio-video-processing.md), [Document processing](document-processing.md), [Embedding generation](../generative-ai/embedding-generation.md), [Generative AI evaluation](../generative-ai/genai-evaluation.md), [In-database machine learning](../machine-learning/in-database-ml.md), [Unstructured data management](../specialised-data/unstructured-data.md), [User-defined functions and procedures](user-defined-functions.md) |
| Depends on | [Foundation model access](../generative-ai/foundation-model-access.md) |

# Where it appears

- **Use cases:** [Document data extraction](../../use-cases/usecase-document-extraction.md) (benefits from)
- **Maturity tracks:** [Generative AI](../../maturity/track-genai.md) (from level 3, Defined) · [Transformation engineering](../../maturity/track-transformation.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Redshift ML](../../technologies/aws/aws-redshift-ml.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | AI functions | [AI functions in Fabric](../../technologies/microsoft/fabric-ai-functions.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | BigQuery generative AI functions (AI.GENERATE and related) | [AlloyDB for PostgreSQL](../../technologies/google-cloud/gcp-alloydb.md), [BigQuery DataFrames](../../technologies/google-cloud/gcp-bigquery-dataframes.md), [BigQuery generative AI functions](../../technologies/google-cloud/gcp-bigquery-ai-functions.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | Cortex AI Functions (formerly Cortex AISQL) | [Snowflake Cortex AI Functions](../../technologies/snowflake/snowflake-cortex-ai-functions.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks AI Functions](../../technologies/databricks/databricks-ai-functions.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse AI functions](../../technologies/clickhouse/clickhouse-ai-functions.md) (preview) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Analytics Cloud AI Assistant, AI Data Agents and MCP Server](../../technologies/oracle/oracle-analytics-cloud-ai.md), [Oracle Select AI](../../technologies/oracle/oracle-select-ai.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Confluent Intelligence](../../technologies/ibm/confluent-intelligence.md) (preview) |
| [Palantir](../../platforms/platform-palantir.md) |  | [AIP Logic and AIP Evals](../../technologies/palantir/palantir-aip-logic.md), [Palantir Pipeline Builder](../../technologies/palantir/palantir-pipeline-builder.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku Prompt Studios](../../technologies/dataiku/dataiku-prompt-studios.md) |
