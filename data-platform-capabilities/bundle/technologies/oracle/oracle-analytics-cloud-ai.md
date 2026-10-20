---
type: Technology
id: oracle-analytics-cloud-ai
title: Oracle Analytics Cloud AI Assistant, AI Data Agents and MCP Server
description: Generative AI features in Oracle Analytics Cloud for asking questions of data in natural language, building dataset-specific agents and exposing governed analytics to external AI clients through MCP.
platform: platform-oracle
kind: feature
availability: ga
realises: [conversational-analytics, agent-tool-access, ai-functions]
resource: https://docs.oracle.com/en/cloud/paas/analytics-cloud/acsdv/oracle-analytics-cloud-mcp-server.html
tags: [oracle]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

AI Data Agents and AI functions in custom calculations arrived in the March 2026 update. The MCP server lets clients such as Claude Desktop or VS Code query governed subject areas.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) (Analytics and BI) (primary): Ask questions of data in natural language and get answers, charts or SQL back.
- [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) (Generative AI): Give agents governed access to data and actions through tools and protocols such as MCP.
- [AI functions in SQL](../../capabilities/processing/ai-functions.md) (Processing and transformation): Call language models from SQL or DataFrame code to classify, extract, summarise or translate data at scale.

**Platform:** [Oracle](../../platforms/platform-oracle.md)  
**Availability:** ga  
**Product family:** Oracle Analytics

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Data Agent](../aws/aws-sagemaker-data-agent.md), [Amazon Quick Sight](../aws/aws-quick-sight.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric data agent](../microsoft/fabric-data-agent.md), [Copilot in Power BI](../microsoft/powerbi-copilot.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery conversational analytics](../google-cloud/gcp-bigquery-conversational-analytics.md), [Conversational Analytics in Looker](../google-cloud/gcp-looker-conversational-analytics.md), [BigQuery data canvas](../google-cloud/gcp-bigquery-data-canvas.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Analyst](../snowflake/snowflake-cortex-analyst.md), [Snowflake Cortex Agents](../snowflake/snowflake-cortex-agents.md), [Snowflake CoWork](../snowflake/snowflake-cowork.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Genie Agents](../databricks/databricks-genie-agents.md), [Genie One](../databricks/databricks-genie-one.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Agents](../clickhouse/clickhouse-agents.md) (preview), [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE GPT](../informatica/informatica-claire-gpt.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Visualization](../cloudera/cloudera-data-visualization.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule and Joule agents](../sap/sap-joule.md), [Dremio Cloud](../sap/dremio-cloud.md), [SAP Analytics Cloud](../sap/sap-analytics-cloud.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Tera](../teradata/teradata-tera.md) (preview) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Analyst](../palantir/palantir-aip-analyst.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Semantic Models](../dataiku/dataiku-semantic-models.md) (unconfirmed) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Tableau Next](../independent/tableau-next.md), [ThoughtSpot Spotter](../independent/thoughtspot-spotter.md), [ThoughtSpot Analytics](../independent/thoughtspot-analytics.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
