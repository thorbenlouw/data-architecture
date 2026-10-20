---
type: Technology
id: databricks-genie-agents
title: Genie Agents
description: Domain-specific chat interfaces that analysts curate with tables, metric views, example SQL and instructions. They answer business questions in natural language with SQL, tables and charts.
formerly: [Genie spaces, AI/BI Genie]
platform: platform-databricks
kind: feature
availability: ga
realises: [conversational-analytics, ai-context-layer]
resource: https://docs.databricks.com/aws/en/genie-agents/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Renamed in July 2026. Genie Agents can be shared externally through OpenSharing (Beta), used from Slack and Teams, and used as tools by other agents. Billing for Genie One and Genie Agents is paused until 31 January 2027.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) (Analytics and BI) (primary): Ask questions of data in natural language and get answers, charts or SQL back.
- [AI context layer](../../capabilities/metadata/ai-context-layer.md) (Metadata and discovery): Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Genie, Databricks AI/BI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick Sight](../aws/aws-quick-sight.md), [Amazon SageMaker Data Agent](../aws/aws-sagemaker-data-agent.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric data agent](../microsoft/fabric-data-agent.md), [Copilot in Power BI](../microsoft/powerbi-copilot.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery conversational analytics](../google-cloud/gcp-bigquery-conversational-analytics.md), [Conversational Analytics in Looker](../google-cloud/gcp-looker-conversational-analytics.md), [BigQuery data canvas](../google-cloud/gcp-bigquery-data-canvas.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Analyst](../snowflake/snowflake-cortex-analyst.md), [Snowflake CoWork](../snowflake/snowflake-cowork.md), [Snowflake Cortex Agents](../snowflake/snowflake-cortex-agents.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md), [ClickHouse Agents](../clickhouse/clickhouse-agents.md) (preview) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE GPT](../informatica/informatica-claire-gpt.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Visualization](../cloudera/cloudera-data-visualization.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud AI Assistant, AI Data Agents and MCP Server](../oracle/oracle-analytics-cloud-ai.md), [Oracle Select AI](../oracle/oracle-select-ai.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md), [SAP Joule and Joule agents](../sap/sap-joule.md), [SAP Analytics Cloud](../sap/sap-analytics-cloud.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Tera](../teradata/teradata-tera.md) (preview) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Analyst](../palantir/palantir-aip-analyst.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Semantic Models](../dataiku/dataiku-semantic-models.md) (unconfirmed) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Tableau Next](../independent/tableau-next.md), [ThoughtSpot Spotter](../independent/thoughtspot-spotter.md), [ThoughtSpot Analytics](../independent/thoughtspot-analytics.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
