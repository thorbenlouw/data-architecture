---
type: Technology
id: gcp-bigquery-conversational-analytics
title: BigQuery conversational analytics
description: Natural-language question answering over BigQuery tables, views, graphs and Lakehouse tables through configurable data agents with instructions, glossary terms and verified queries.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [conversational-analytics, ai-agents, ai-context-layer]
resource: https://docs.cloud.google.com/bigquery/docs/conversational-analytics
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA June 2026. Data agents are reusable through the Conversational Analytics API, Data Studio and Gemini Enterprise (publishing GA October 2026), and can span several projects and datasets. Verified queries were previously called golden queries.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) (Analytics and BI) (primary): Ask questions of data in natural language and get answers, charts or SQL back.
- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI): Build systems in which models plan, call tools and act over several steps to complete a task.
- [AI context layer](../../capabilities/metadata/ai-context-layer.md) (Metadata and discovery): Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick Sight](../aws/aws-quick-sight.md), [Amazon SageMaker Data Agent](../aws/aws-sagemaker-data-agent.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric data agent](../microsoft/fabric-data-agent.md), [Copilot in Power BI](../microsoft/powerbi-copilot.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake CoWork](../snowflake/snowflake-cowork.md), [Snowflake Cortex Analyst](../snowflake/snowflake-cortex-analyst.md), [Snowflake Cortex Agents](../snowflake/snowflake-cortex-agents.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Genie Agents](../databricks/databricks-genie-agents.md), [Genie One](../databricks/databricks-genie-one.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Agents](../clickhouse/clickhouse-agents.md) (preview), [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE GPT](../informatica/informatica-claire-gpt.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Visualization](../cloudera/cloudera-data-visualization.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud AI Assistant, AI Data Agents and MCP Server](../oracle/oracle-analytics-cloud-ai.md), [Oracle Select AI](../oracle/oracle-select-ai.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule and Joule agents](../sap/sap-joule.md), [Dremio Cloud](../sap/dremio-cloud.md), [SAP Analytics Cloud](../sap/sap-analytics-cloud.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [AI context layer](../../capabilities/metadata/ai-context-layer.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Tera](../teradata/teradata-tera.md) (preview) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Analyst](../palantir/palantir-aip-analyst.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Semantic Models](../dataiku/dataiku-semantic-models.md) (unconfirmed) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Tableau Next](../independent/tableau-next.md), [ThoughtSpot Spotter](../independent/thoughtspot-spotter.md), [Alteryx One](../independent/alteryx-one.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
