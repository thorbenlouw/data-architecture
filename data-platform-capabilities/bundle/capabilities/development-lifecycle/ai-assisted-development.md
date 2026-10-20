---
type: Capability
id: ai-assisted-development
title: AI-assisted development
description: Use AI assistants to write, explain, fix and optimise code, SQL and pipelines.
aliases: [coding assistants, copilots]
broader: [development-lifecycle]
related:
- ai-context-layer
- ai-generated-documentation
- data-testing
- conversational-analytics
- code-translation
depends_on: [foundation-model-access]
tags: [development-lifecycle]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Assistants built on large language models work inside notebooks, SQL editors and IDEs. They complete code as you type, write a query from a plain-language request, explain an unfamiliar stored procedure, suggest a fix for an error and propose faster rewrites of slow queries. Assistants built into the platform are given context such as table schemas, column descriptions, query history and lineage, so a request for "monthly churn by region" becomes SQL against the right tables rather than guessed ones.

Assistants shorten routine work and help people writing in a dialect they know less well. The risks are code that runs but is subtly wrong, such as a join that duplicates rows, and sending sensitive schema details or data to an external model service. Output quality depends on the metadata the assistant can see, so documentation and semantic context matter more once assistants are in use. An assistant responds to a person one step at a time; a data engineering agent takes a goal and carries out several steps itself.

# Key considerations

- Check what the assistant sends to the model provider: code, schemas, sample rows or query results. Confirm this is covered by your data processing terms.
- Generated code needs the same review and tests as human code. The volume of changes grows faster than review capacity unless testing is automated.
- An assistant respects the user's permissions only if it is built to. Confirm it cannot read metadata or data the user cannot.
- Record which changes were AI-assisted if your governance or audit policy requires it.

# Questions to ask

- Which languages and tools do developers spend most of their time in?
- What may be sent to an external model provider under your security and privacy policies?
- How complete are table and column descriptions today, given that assistants depend on them?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Development and DataOps](development-lifecycle.md) |
| Broader | [Development and DataOps](development-lifecycle.md) |
| Narrower | [Data engineering agents](data-engineering-agents.md) |
| Related | [AI context layer](../metadata/ai-context-layer.md), [AI-generated documentation](../metadata/ai-generated-documentation.md), [Code and SQL translation](../platform-operations/code-translation.md), [Conversational analytics](../analytics-bi/conversational-analytics.md), [Data pipeline testing](data-testing.md) |
| Depends on | [Foundation model access](../generative-ai/foundation-model-access.md) |

# Where it appears

- **Maturity tracks:** [Path to live](../../maturity/track-path-to-live.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Data Agent](../../technologies/aws/aws-sagemaker-data-agent.md), [AWS Transform](../../technologies/aws/aws-transform.md), [Kiro](../../technologies/aws/aws-kiro.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Copilot in Fabric](../../technologies/microsoft/fabric-copilot.md) (preview), [Copilot in Power BI](../../technologies/microsoft/powerbi-copilot.md), [Fabric MCP server](../../technologies/microsoft/fabric-mcp-server.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery Migration Service](../../technologies/google-cloud/gcp-bigquery-migration-service.md), [Data Agent Kit](../../technologies/google-cloud/gcp-data-agent-kit.md) (preview), [Gemini in BigQuery](../../technologies/google-cloud/gcp-gemini-in-bigquery.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | CoCo (formerly Cortex Code; replacing Snowflake Copilot) | [SnowConvert AI](../../technologies/snowflake/snowflake-snowconvert-ai.md), [Snowflake CoCo](../../technologies/snowflake/snowflake-coco.md), [Snowflake Extension for Visual Studio Code](../../technologies/snowflake/snowflake-vscode-extension.md) (preview), [Snowflake Copilot](../../technologies/snowflake/snowflake-copilot.md) (deprecated) |
| [Databricks](../../platforms/platform-databricks.md) | Genie Code | [Databricks agentic code converter](../../technologies/databricks/databricks-agentic-code-converter.md) (preview), [Genie Code](../../technologies/databricks/databricks-genie-code.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../../technologies/clickhouse/clickhouse-sql-console.md) |
| [Informatica](../../platforms/platform-informatica.md) | CLAIRE Copilot | [CLAIRE Copilot for Data Integration](../../technologies/informatica/informatica-claire-copilot-data-integration.md), [CLAIRE GPT](../../technologies/informatica/informatica-claire-gpt.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Tera](../../technologies/teradata/teradata-tera.md) (preview) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir MCP and Ontology MCP](../../technologies/palantir/palantir-mcp.md) |
| [SAS](../../platforms/platform-sas.md) | SAS Viya Copilot | [SAS Viya Copilot](../../technologies/sas/sas-viya-copilot.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku Code Studios](../../technologies/dataiku/dataiku-code-studios.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [dbt Copilot](../../technologies/independent/dbt-copilot.md), [Hex](../../technologies/independent/hex.md) |

Narrower capabilities are realised by a further 13 technologies; see their pages.
