---
type: Capability
id: conversational-analytics
title: Conversational analytics
description: Ask questions of data in natural language and get answers, charts or SQL back.
aliases: [natural language query, text-to-SQL, NLQ]
broader: [analytics-bi, generative-ai]
related: [semantic-layer, metric-definitions, genai-evaluation, enterprise-ai-assistant, ad-hoc-analysis]
depends_on: [foundation-model-access, ai-context-layer]
tags: [analytics-bi]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A sales manager types "which regions missed target last month?". A language model maps the words to tables, columns and metrics, generates a query, runs it with the user's own permissions, and returns a number, table or chart together with the query it used and a short explanation. Follow-up questions such as "and by product?" refine the previous answer rather than starting again.

It widens access to people who will not learn SQL or a BI tool. Accuracy depends more on context than on the model: questions answered against a semantic layer with governed metrics, synonyms and verified example queries are far more reliable than free SQL generation over raw tables. Variants range from a chat box inside a BI tool to agents that run multi-step analyses and write up findings. It is ad hoc analysis with a natural-language interface. It differs from augmented analytics, which surfaces insights without being asked.

# Key considerations

- Show the generated query and the definitions used, so users and reviewers can check answers rather than trust them blindly.
- Limit scope to curated, well-described data at first. Broad access to raw tables produces plausible but wrong answers.
- Build an evaluation set of real questions with known answers, and rerun it after any change to the model, prompts or data.
- Queries must run as the asking user, so row and column security apply exactly as in other tools.

# Questions to ask

- Which user groups would ask questions, and what would a wrong answer cost them?
- Do governed metric definitions and documented tables exist for the domains in scope?
- How will you measure answer accuracy before and after release?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Analytics and BI](analytics-bi.md) |
| Broader | [Analytics and BI](analytics-bi.md), [Generative AI](../generative-ai/generative-ai.md) |
| Related | [Ad hoc analysis](ad-hoc-analysis.md), [AI context layer](../metadata/ai-context-layer.md), [AI-assisted development](../development-lifecycle/ai-assisted-development.md), [Augmented analytics](augmented-analytics.md), [Enterprise AI assistant](../generative-ai/enterprise-ai-assistant.md), [Generative AI evaluation](../generative-ai/genai-evaluation.md), [Governed metric definitions](metric-definitions.md), [Semantic layer](semantic-layer.md) |
| Depends on | [Foundation model access](../generative-ai/foundation-model-access.md), [AI context layer](../metadata/ai-context-layer.md) |

# Where it appears

- **Use cases:** [Conversational analytics for business users](../../use-cases/usecase-conversational-bi.md) (requires, level 3) · [Self-service BI](../../use-cases/usecase-self-service-bi.md) (benefits from)
- **Personas:** [Business user](../../personas/persona-business-user.md) · [Data analyst](../../personas/persona-data-analyst.md)
- **Maturity tracks:** [Analytics and BI](../../maturity/track-analytics-bi.md) (from level 4, Measured) · [Generative AI](../../maturity/track-genai.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Quick Sight topics and Amazon Quick chat | [Amazon Quick Sight](../../technologies/aws/aws-quick-sight.md), [Amazon SageMaker Data Agent](../../technologies/aws/aws-sagemaker-data-agent.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Copilot in Power BI; Fabric data agent | [Copilot in Power BI](../../technologies/microsoft/powerbi-copilot.md), [Fabric data agent](../../technologies/microsoft/fabric-data-agent.md), [Power BI Q&A](../../technologies/microsoft/powerbi-q-and-a.md) (deprecated) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Conversational Analytics and data agents | [BigQuery conversational analytics](../../technologies/google-cloud/gcp-bigquery-conversational-analytics.md), [BigQuery data canvas](../../technologies/google-cloud/gcp-bigquery-data-canvas.md), [Conversational Analytics in Looker](../../technologies/google-cloud/gcp-looker-conversational-analytics.md), [Gemini Enterprise](../../technologies/google-cloud/gcp-gemini-enterprise.md), [Google Data Studio](../../technologies/google-cloud/gcp-data-studio.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | Cortex Analyst and Snowflake CoWork (formerly Snowflake Intelligence) | [Snowflake Cortex Agents](../../technologies/snowflake/snowflake-cortex-agents.md), [Snowflake Cortex Analyst](../../technologies/snowflake/snowflake-cortex-analyst.md), [Snowflake CoWork](../../technologies/snowflake/snowflake-cowork.md) |
| [Databricks](../../platforms/platform-databricks.md) | Genie Agents and Genie One | [Genie Agents](../../technologies/databricks/databricks-genie-agents.md), [Genie One](../../technologies/databricks/databricks-genie-one.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | ClickHouse Assistant (AI Chat) and ClickHouse Agents | [ClickHouse Agents](../../technologies/clickhouse/clickhouse-agents.md) (preview), [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../../technologies/clickhouse/clickhouse-sql-console.md) |
| [Informatica](../../platforms/platform-informatica.md) | CLAIRE GPT | [CLAIRE GPT](../../technologies/informatica/informatica-claire-gpt.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Visualization](../../technologies/cloudera/cloudera-data-visualization.md) |
| [Oracle](../../platforms/platform-oracle.md) | Select AI | [Oracle Analytics Cloud AI Assistant, AI Data Agents and MCP Server](../../technologies/oracle/oracle-analytics-cloud-ai.md), [Oracle Select AI](../../technologies/oracle/oracle-select-ai.md) |
| [SAP](../../platforms/platform-sap.md) | Joule / Just Ask | [Dremio Cloud](../../technologies/sap/dremio-cloud.md), [SAP Analytics Cloud](../../technologies/sap/sap-analytics-cloud.md), [SAP Joule and Joule agents](../../technologies/sap/sap-joule.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Tera](../../technologies/teradata/teradata-tera.md) (preview) |
| [Palantir](../../platforms/platform-palantir.md) |  | [AIP Analyst](../../technologies/palantir/palantir-aip-analyst.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku Semantic Models](../../technologies/dataiku/dataiku-semantic-models.md) (unconfirmed) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Alteryx One](../../technologies/independent/alteryx-one.md), [Cube Cloud](../../technologies/independent/cube-cloud.md), [dbt Charts](../../technologies/independent/dbt-charts.md) (unconfirmed), [Hex](../../technologies/independent/hex.md), [Omni Analytics](../../technologies/independent/omni.md), [Qlik Cloud Analytics](../../technologies/independent/qlik-cloud-analytics.md), [Secoda](../../technologies/independent/secoda.md), [Tableau Cloud](../../technologies/independent/tableau-cloud.md), [Tableau Next](../../technologies/independent/tableau-next.md), [ThoughtSpot Analytics](../../technologies/independent/thoughtspot-analytics.md), [ThoughtSpot Spotter](../../technologies/independent/thoughtspot-spotter.md) |
