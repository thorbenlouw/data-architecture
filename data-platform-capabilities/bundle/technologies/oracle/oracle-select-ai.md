---
type: Technology
id: oracle-select-ai
title: Oracle Select AI
description: Autonomous AI Database feature that turns natural-language prompts into SQL, answers questions with retrieval over vector stores, and generates synthetic data, using configured LLM providers.
platform: platform-oracle
kind: feature
availability: ga
realises: [conversational-analytics, ai-functions, retrieval-augmented-generation, synthetic-data]
resource: https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/select-ai.html
tags: [oracle]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Configured through AI profiles in the DBMS_CLOUD_AI package and invoked with the AI keyword in SELECT or from PL/SQL, Python and Java. Uses OCI Generative AI or third-party providers such as OpenAI, Azure OpenAI and Google.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) (Analytics and BI) (primary): Ask questions of data in natural language and get answers, charts or SQL back.
- [AI functions in SQL](../../capabilities/processing/ai-functions.md) (Processing and transformation): Call language models from SQL or DataFrame code to classify, extract, summarise or translate data at scale.
- [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) (Generative AI): Ground model answers in your own content by retrieving relevant passages at query time.
- [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) (Development and DataOps): Generate artificial data that keeps the useful properties of real data without exposing real records.

**Platform:** [Oracle](../../platforms/platform-oracle.md)  
**Availability:** ga  
**Product family:** Oracle Autonomous AI Database

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Data Agent](../aws/aws-sagemaker-data-agent.md), [Amazon Quick Sight](../aws/aws-quick-sight.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric data agent](../microsoft/fabric-data-agent.md), [Copilot in Power BI](../microsoft/powerbi-copilot.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery conversational analytics](../google-cloud/gcp-bigquery-conversational-analytics.md), [Conversational Analytics in Looker](../google-cloud/gcp-looker-conversational-analytics.md), [BigQuery data canvas](../google-cloud/gcp-bigquery-data-canvas.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Analyst](../snowflake/snowflake-cortex-analyst.md), [Snowflake CoWork](../snowflake/snowflake-cowork.md), [Snowflake Cortex Agents](../snowflake/snowflake-cortex-agents.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Genie Agents](../databricks/databricks-genie-agents.md), [Genie One](../databricks/databricks-genie-one.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md), [ClickHouse Agents](../clickhouse/clickhouse-agents.md) (preview) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE GPT](../informatica/informatica-claire-gpt.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Visualization](../cloudera/cloudera-data-visualization.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule and Joule agents](../sap/sap-joule.md), [Dremio Cloud](../sap/dremio-cloud.md), [SAP Analytics Cloud](../sap/sap-analytics-cloud.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Tera](../teradata/teradata-tera.md) (preview) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Analyst](../palantir/palantir-aip-analyst.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [ThoughtSpot Spotter](../independent/thoughtspot-spotter.md), [ThoughtSpot Analytics](../independent/thoughtspot-analytics.md), [Tableau Next](../independent/tableau-next.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
