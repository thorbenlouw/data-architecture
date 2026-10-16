---
type: Technology
id: teradata-tera
title: Teradata Tera
description: Agentic workspace in which Teradata agents analyse data, write code, tune queries and run multi-step data tasks, grounded in governed metadata, lineage and policies.
aliases: [Tera]
platform: platform-teradata
kind: saas
availability: preview
realises:
- ai-assisted-development
- conversational-analytics
- ai-agents
- ai-context-layer
- human-oversight
- agent-runtime
- data-engineering-agents
resource: https://www.teradata.com/press-releases/2026/tera-an-agentic-coworker
tags: [teradata]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Announced as an "agentic coworker" on 22 September 2026, with Tera Context Engine (a context graph of metadata, lineage and semantics), Tera Harness (execution with approvals and checkpoints) and Agent Skills due in the fourth quarter of 2026. Early access is by request. It works across non-Teradata platforms through MCP.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) (Development and DataOps) (primary): Use AI assistants to write, explain, fix and optimise code, SQL and pipelines.
- [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) (Analytics and BI): Ask questions of data in natural language and get answers, charts or SQL back.
- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI): Build systems in which models plan, call tools and act over several steps to complete a task.
- [AI context layer](../../capabilities/metadata/ai-context-layer.md) (Metadata and discovery): Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly.
- [Human oversight of AI](../../capabilities/governance/human-oversight.md) (Governance and compliance): Route model and agent decisions to people for review, approval or override, and let them pause or stop a system.
- [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md) (Generative AI): Deploy and run agents as managed services with identity, durable state, scaling and sandboxed code execution.
- [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) (Development and DataOps): Use AI agents that plan, build, test and repair pipelines and models from goals, under platform governance.

**Platform:** [Teradata](../../platforms/platform-teradata.md)  
**Availability:** preview  
**Product family:** Teradata Autonomous Knowledge Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Data Agent](../aws/aws-sagemaker-data-agent.md), [Kiro](../aws/aws-kiro.md), [AWS Transform](../aws/aws-transform.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Copilot in Fabric](../microsoft/fabric-copilot.md) (preview), [Copilot in Power BI](../microsoft/powerbi-copilot.md), [Fabric MCP server](../microsoft/fabric-mcp-server.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Gemini in BigQuery](../google-cloud/gcp-gemini-in-bigquery.md), [Data Agent Kit](../google-cloud/gcp-data-agent-kit.md) (preview), [BigQuery Migration Service](../google-cloud/gcp-bigquery-migration-service.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake CoCo](../snowflake/snowflake-coco.md), [SnowConvert AI](../snowflake/snowflake-snowconvert-ai.md), [Snowflake Extension for Visual Studio Code](../snowflake/snowflake-vscode-extension.md) (preview) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Genie Code](../databricks/databricks-genie-code.md), [Databricks agentic code converter](../databricks/databricks-agentic-code-converter.md) (preview) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE Copilot for Data Integration](../informatica/informatica-claire-copilot-data-integration.md), [CLAIRE GPT](../informatica/informatica-claire-gpt.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir MCP and Ontology MCP](../palantir/palantir-mcp.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt Copilot](../independent/dbt-copilot.md), [Hex](../independent/hex.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
