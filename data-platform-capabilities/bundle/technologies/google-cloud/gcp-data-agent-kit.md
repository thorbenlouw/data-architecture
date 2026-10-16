---
type: Technology
id: gcp-data-agent-kit
title: Data Agent Kit
description: IDE extension that connects coding agents and developers to Google Cloud data services through their remote MCP servers.
platform: platform-google-cloud
kind: software
availability: preview
realises: [ai-assisted-development, agent-tool-access, local-development]
resource: https://docs.cloud.google.com/data-agent-kit/use-mcp-servers
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Entered preview in July 2026; connects to AlloyDB, BigQuery, Bigtable, Cloud SQL, Cloud Storage, Knowledge Catalog, Managed Service for Apache Spark and Spanner servers.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) (Development and DataOps) (primary): Use AI assistants to write, explain, fix and optimise code, SQL and pipelines.
- [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) (Generative AI): Give agents governed access to data and actions through tools and protocols such as MCP.
- [IDE and local development](../../capabilities/development-lifecycle/local-development.md) (Development and DataOps): Develop in your own editor and run against the platform, with debugging and local tests.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** preview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Kiro](../aws/aws-kiro.md), [Amazon SageMaker Data Agent](../aws/aws-sagemaker-data-agent.md), [AWS Transform](../aws/aws-transform.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric MCP server](../microsoft/fabric-mcp-server.md), [Copilot in Fabric](../microsoft/fabric-copilot.md) (preview), [Copilot in Power BI](../microsoft/powerbi-copilot.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Extension for Visual Studio Code](../snowflake/snowflake-vscode-extension.md) (preview), [Snowflake CoCo](../snowflake/snowflake-coco.md), [SnowConvert AI](../snowflake/snowflake-snowconvert-ai.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Genie Code](../databricks/databricks-genie-code.md), [Databricks agentic code converter](../databricks/databricks-agentic-code-converter.md) (preview) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE Copilot for Data Integration](../informatica/informatica-claire-copilot-data-integration.md), [CLAIRE GPT](../informatica/informatica-claire-gpt.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Tera](../teradata/teradata-tera.md) (preview) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir MCP and Ontology MCP](../palantir/palantir-mcp.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt Copilot](../independent/dbt-copilot.md), [Hex](../independent/hex.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
