---
type: Technology
id: fabric-mcp-server
title: Fabric MCP server
description: A Model Context Protocol server that gives AI coding assistants and agents access to Fabric APIs, item definitions and OneLake.
platform: platform-microsoft
kind: open-source
availability: ga
realises: [agent-tool-access, ai-assisted-development, local-development]
resource: https://blog.fabric.microsoft.com/en-us/blog/fabric-march-2026-feature-summary
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The local server for code assistants became GA in March 2026; a remote Fabric MCP server and workload specific servers (Data Factory, Warehouse, Eventhouse) are preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) (Generative AI) (primary): Give agents governed access to data and actions through tools and protocols such as MCP.
- [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) (Development and DataOps): Use AI assistants to write, explain, fix and optimise code, SQL and pipelines.
- [IDE and local development](../../capabilities/development-lifecycle/local-development.md) (Development and DataOps): Develop in your own editor and run against the platform, with debugging and local tests.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore Gateway](../aws/aws-bedrock-agentcore-gateway.md), [Amazon Bedrock AgentCore Policy](../aws/aws-bedrock-agentcore-policy.md), [Kiro](../aws/aws-kiro.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Data Agent Kit](../google-cloud/gcp-data-agent-kit.md) (preview), [Google Cloud remote MCP servers](../google-cloud/gcp-remote-mcp-servers.md), [MCP Toolbox for Databases](../google-cloud/gcp-mcp-toolbox-for-databases.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake-managed MCP server](../snowflake/snowflake-managed-mcp-server.md), [Snowflake Cortex Agents](../snowflake/snowflake-cortex-agents.md), [Snowflake Extension for Visual Studio Code](../snowflake/snowflake-vscode-extension.md) (preview) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks managed MCP servers](../databricks/databricks-managed-mcp-servers.md) (preview), [Unity Gateway](../databricks/databricks-unity-gateway.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse MCP server (open-source and Remote MCP in Cloud)](../clickhouse/clickhouse-mcp-server.md), [ClickHouse Agents](../clickhouse/clickhouse-agents.md) (preview) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Headless Data Management (Informatica MCP servers)](../informatica/informatica-headless-data-management.md), [Informatica AI Agent Engineering](../informatica/informatica-ai-agent-engineering.md) (unconfirmed) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Agent Studio](../cloudera/cloudera-agent-studio.md) (preview) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Select AI Agent and Autonomous AI Database MCP Server](../oracle/oracle-select-ai-agent.md), [Oracle Analytics Cloud AI Assistant, AI Data Agents and MCP Server](../oracle/oracle-analytics-cloud-ai.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule Studio](../sap/sap-joule-studio.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise MCP](../teradata/teradata-enterprise-mcp.md), [Teradata Enterprise AgentStack](../teradata/teradata-agentstack.md) (preview) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Intelligence](../ibm/confluent-intelligence.md) (preview), [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir MCP and Ontology MCP](../palantir/palantir-mcp.md), [AIP Chatbot Studio](../palantir/palantir-aip-chatbot-studio.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Model Context Protocol (MCP)](../open-source/model-context-protocol.md), [LangGraph](../open-source/langgraph.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Airbyte Agents](../independent/airbyte-agents.md) (unconfirmed), [AtScale](../independent/atscale.md), [dbt Semantic Layer](../independent/dbt-semantic-layer.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
