---
type: Technology
id: fabric-data-agent
title: Fabric data agent
description: A configurable conversational agent that answers natural-language questions by generating SQL, DAX or KQL over lakehouses, warehouses, semantic models, Eventhouses and ontologies.
formerly: [AI skill]
platform: platform-microsoft
kind: feature
availability: ga
realises: [conversational-analytics, agent-tool-access, ai-context-layer]
resource: https://learn.microsoft.com/en-us/fabric/data-science/concept-data-agent
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA from March 2026. Read-only, up to five sources, English only. Can be published to Microsoft 365 Copilot, Copilot Studio, Microsoft Foundry and Teams; Purview DSPM and DLP controls on agents are preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) (Analytics and BI) (primary): Ask questions of data in natural language and get answers, charts or SQL back.
- [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) (Generative AI): Give agents governed access to data and actions through tools and protocols such as MCP.
- [AI context layer](../../capabilities/metadata/ai-context-layer.md) (Metadata and discovery): Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Fabric IQ

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick Sight](../aws/aws-quick-sight.md), [Amazon SageMaker Data Agent](../aws/aws-sagemaker-data-agent.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery conversational analytics](../google-cloud/gcp-bigquery-conversational-analytics.md), [Conversational Analytics in Looker](../google-cloud/gcp-looker-conversational-analytics.md), [BigQuery data canvas](../google-cloud/gcp-bigquery-data-canvas.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Analyst](../snowflake/snowflake-cortex-analyst.md), [Snowflake Cortex Agents](../snowflake/snowflake-cortex-agents.md), [Snowflake CoWork](../snowflake/snowflake-cowork.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Genie Agents](../databricks/databricks-genie-agents.md), [Genie One](../databricks/databricks-genie-one.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Agents](../clickhouse/clickhouse-agents.md) (preview), [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE GPT](../informatica/informatica-claire-gpt.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Visualization](../cloudera/cloudera-data-visualization.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud AI Assistant, AI Data Agents and MCP Server](../oracle/oracle-analytics-cloud-ai.md), [Oracle Select AI](../oracle/oracle-select-ai.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md), [SAP Joule and Joule agents](../sap/sap-joule.md), [SAP Analytics Cloud](../sap/sap-analytics-cloud.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Tera](../teradata/teradata-tera.md) (preview) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Analyst](../palantir/palantir-aip-analyst.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Semantic Models](../dataiku/dataiku-semantic-models.md) (unconfirmed) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Tableau Next](../independent/tableau-next.md), [ThoughtSpot Spotter](../independent/thoughtspot-spotter.md), [ThoughtSpot Analytics](../independent/thoughtspot-analytics.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
