---
type: Technology
id: tableau-next
title: Tableau Next
description: API-first agentic analytics product on Salesforce's Hyperforce that uses Data 360 as its data layer and Tableau Semantics as its semantic model.
platform: platform-independent
vendor: Tableau (Salesforce)
kind: saas
availability: ga
realises: [conversational-analytics, semantic-layer, ai-agents, agent-tool-access, ai-context-layer]
resource: https://www.tableau.com/products/tableau-next
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Tableau Semantics is an AI-assisted semantic layer in Data 360. Tableau Next MCP exposes its analytics and semantics to outside agents. It is sold on its own or in the Tableau+ bundle with Tableau Cloud, and is separate from classic Tableau workbooks.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) (Analytics and BI) (primary): Ask questions of data in natural language and get answers, charts or SQL back.
- [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) (Analytics and BI): Define business entities, measures and relationships once so every tool calculates them the same way.
- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI): Build systems in which models plan, call tools and act over several steps to complete a task.
- [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) (Generative AI): Give agents governed access to data and actions through tools and protocols such as MCP.
- [AI context layer](../../capabilities/metadata/ai-context-layer.md) (Metadata and discovery): Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick Sight](../aws/aws-quick-sight.md), [Amazon SageMaker Data Agent](../aws/aws-sagemaker-data-agent.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric data agent](../microsoft/fabric-data-agent.md), [Copilot in Power BI](../microsoft/powerbi-copilot.md), [Fabric IQ ontology](../microsoft/fabric-iq-ontology.md) (preview) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery conversational analytics](../google-cloud/gcp-bigquery-conversational-analytics.md), [Conversational Analytics in Looker](../google-cloud/gcp-looker-conversational-analytics.md), [Gemini Enterprise](../google-cloud/gcp-gemini-enterprise.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Agents](../snowflake/snowflake-cortex-agents.md), [Snowflake CoWork](../snowflake/snowflake-cowork.md), [Snowflake Cortex Analyst](../snowflake/snowflake-cortex-analyst.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Genie Agents](../databricks/databricks-genie-agents.md), [Genie One](../databricks/databricks-genie-one.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Agents](../clickhouse/clickhouse-agents.md) (preview), [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE GPT](../informatica/informatica-claire-gpt.md), [Informatica AI Agent Engineering](../informatica/informatica-ai-agent-engineering.md) (unconfirmed) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Visualization](../cloudera/cloudera-data-visualization.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud AI Assistant, AI Data Agents and MCP Server](../oracle/oracle-analytics-cloud-ai.md), [Oracle Select AI](../oracle/oracle-select-ai.md), [Oracle Select AI Agent and Autonomous AI Database MCP Server](../oracle/oracle-select-ai-agent.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md), [SAP Joule and Joule agents](../sap/sap-joule.md), [SAP Analytics Cloud](../sap/sap-analytics-cloud.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Tera](../teradata/teradata-tera.md) (preview) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Analyst](../palantir/palantir-aip-analyst.md) | [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Semantic Models](../dataiku/dataiku-semantic-models.md) (unconfirmed) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
