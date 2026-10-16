---
type: Technology
id: powerbi-copilot
title: Copilot in Power BI
description: Natural-language assistance that summarises reports, answers data questions, creates report pages and helps write DAX and model descriptions.
aliases: [Power BI Copilot]
platform: platform-microsoft
kind: feature
availability: ga
realises: [conversational-analytics, augmented-analytics, ai-assisted-development, ai-generated-documentation]
resource: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The report Copilot pane is GA; the standalone, cross-report Power BI agent and app agent are preview, as are AI auto-descriptions for semantic models. Needs F2+ or P1+ capacity; Pro or PPU alone is not enough.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) (Analytics and BI) (primary): Ask questions of data in natural language and get answers, charts or SQL back.
- [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md) (Analytics and BI): Use automation and machine learning to surface insights, anomalies and explanations without being asked.
- [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) (Development and DataOps): Use AI assistants to write, explain, fix and optimise code, SQL and pipelines.
- [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md) (Metadata and discovery): Draft descriptions, tags and documentation for data assets using AI, for people to review.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Power BI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Data Agent](../aws/aws-sagemaker-data-agent.md), [Amazon Quick Sight](../aws/aws-quick-sight.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Conversational Analytics in Looker](../google-cloud/gcp-looker-conversational-analytics.md), [BigQuery conversational analytics](../google-cloud/gcp-bigquery-conversational-analytics.md), [BigQuery data canvas](../google-cloud/gcp-bigquery-data-canvas.md) | [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Analyst](../snowflake/snowflake-cortex-analyst.md), [Snowflake CoWork](../snowflake/snowflake-cowork.md), [Snowflake Cortex Agents](../snowflake/snowflake-cortex-agents.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Genie Agents](../databricks/databricks-genie-agents.md), [Genie One](../databricks/databricks-genie-one.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md), [ClickHouse Agents](../clickhouse/clickhouse-agents.md) (preview) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE GPT](../informatica/informatica-claire-gpt.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Visualization](../cloudera/cloudera-data-visualization.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud AI Assistant, AI Data Agents and MCP Server](../oracle/oracle-analytics-cloud-ai.md), [Oracle Select AI](../oracle/oracle-select-ai.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Analytics Cloud](../sap/sap-analytics-cloud.md), [SAP Joule and Joule agents](../sap/sap-joule.md), [Dremio Cloud](../sap/dremio-cloud.md) | [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Tera](../teradata/teradata-tera.md) (preview) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Analyst](../palantir/palantir-aip-analyst.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [ThoughtSpot Spotter](../independent/thoughtspot-spotter.md), [ThoughtSpot Analytics](../independent/thoughtspot-analytics.md), [Tableau Next](../independent/tableau-next.md) | [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
