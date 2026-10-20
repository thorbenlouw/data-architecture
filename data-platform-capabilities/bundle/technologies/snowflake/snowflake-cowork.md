---
type: Technology
id: snowflake-cowork
title: Snowflake CoWork
description: A conversational agent application for business users that answers questions over structured and unstructured data, runs deep research, and produces artefacts, documents and scheduled automations.
formerly: [Snowflake Intelligence]
platform: platform-snowflake
kind: saas
availability: ga
realises: [conversational-analytics, ai-agents, data-alerting, enterprise-ai-assistant]
resource: https://docs.snowflake.com/en/user-guide/snowflake-cortex/snowflake-cowork
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Renamed in June 2026. It runs on the Cortex Agents API under existing Snowflake governance and has web and iOS clients. Deep Research and Automations are GA, and some newer features (HTML generation, user skills) are in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) (Analytics and BI) (primary): Ask questions of data in natural language and get answers, charts or SQL back.
- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI): Build systems in which models plan, call tools and act over several steps to complete a task.
- [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) (Analytics and BI): Notify people when data crosses thresholds, or deliver reports to them on a schedule.
- [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md) (Generative AI): Give staff a governed, ready-made assistant that answers questions and completes tasks across structured and unstructured enterprise data.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick Sight](../aws/aws-quick-sight.md), [Amazon SageMaker Data Agent](../aws/aws-sagemaker-data-agent.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric data agent](../microsoft/fabric-data-agent.md), [Copilot in Power BI](../microsoft/powerbi-copilot.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery conversational analytics](../google-cloud/gcp-bigquery-conversational-analytics.md), [Gemini Enterprise](../google-cloud/gcp-gemini-enterprise.md), [Conversational Analytics in Looker](../google-cloud/gcp-looker-conversational-analytics.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Genie Agents](../databricks/databricks-genie-agents.md), [Genie One](../databricks/databricks-genie-one.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Agents](../clickhouse/clickhouse-agents.md) (preview), [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE GPT](../informatica/informatica-claire-gpt.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Visualization](../cloudera/cloudera-data-visualization.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud AI Assistant, AI Data Agents and MCP Server](../oracle/oracle-analytics-cloud-ai.md), [Oracle Select AI](../oracle/oracle-select-ai.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule and Joule agents](../sap/sap-joule.md), [Dremio Cloud](../sap/dremio-cloud.md), [SAP Analytics Cloud](../sap/sap-analytics-cloud.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Tera](../teradata/teradata-tera.md) (preview) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Analyst](../palantir/palantir-aip-analyst.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Semantic Models](../dataiku/dataiku-semantic-models.md) (unconfirmed) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [ThoughtSpot Spotter](../independent/thoughtspot-spotter.md), [Tableau Next](../independent/tableau-next.md), [ThoughtSpot Analytics](../independent/thoughtspot-analytics.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
