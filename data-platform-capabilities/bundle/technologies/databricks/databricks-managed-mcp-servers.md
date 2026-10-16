---
type: Technology
id: databricks-managed-mcp-servers
title: Databricks managed MCP servers
description: Hosted Model Context Protocol servers that expose Unity Catalog functions, AI Search indexes, Genie Agents and Genie One to agents as tools. External MCP servers can also be registered as Unity Catalog MCP services.
platform: platform-databricks
kind: feature
availability: preview
realises: [agent-tool-access, agent-registry]
resource: https://docs.databricks.com/aws/en/release-notes/product/2026/september
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Managed MCP servers entered Public Preview in January 2026. The Genie One MCP server became GA in September 2026 as system.ai.genie_one_mcp, and its Beta endpoint is withdrawn on 31 October 2026. Unity Gateway applies tool filtering and policies, and managed OAuth is available for some external MCP servers.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) (Generative AI) (primary): Give agents governed access to data and actions through tools and protocols such as MCP.
- [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) (Generative AI): Keep a governed inventory of agents, tools and MCP servers with owners and permissions so they can be found, approved and controlled.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** preview  
**Product family:** Agent Bricks

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore Gateway](../aws/aws-bedrock-agentcore-gateway.md), [Amazon Bedrock AgentCore Policy](../aws/aws-bedrock-agentcore-policy.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric MCP server](../microsoft/fabric-mcp-server.md), [Fabric data agent](../microsoft/fabric-data-agent.md), [Fabric IQ ontology](../microsoft/fabric-iq-ontology.md) (preview) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud remote MCP servers](../google-cloud/gcp-remote-mcp-servers.md), [MCP Toolbox for Databases](../google-cloud/gcp-mcp-toolbox-for-databases.md), [Data Agent Kit](../google-cloud/gcp-data-agent-kit.md) (preview) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake-managed MCP server](../snowflake/snowflake-managed-mcp-server.md), [Snowflake Cortex Agents](../snowflake/snowflake-cortex-agents.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse MCP server (open-source and Remote MCP in Cloud)](../clickhouse/clickhouse-mcp-server.md), [ClickHouse Agents](../clickhouse/clickhouse-agents.md) (preview) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Headless Data Management (Informatica MCP servers)](../informatica/informatica-headless-data-management.md), [Informatica AI Agent Engineering](../informatica/informatica-ai-agent-engineering.md) (unconfirmed) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Agent Studio](../cloudera/cloudera-agent-studio.md) (preview) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Select AI Agent and Autonomous AI Database MCP Server](../oracle/oracle-select-ai-agent.md), [Oracle Analytics Cloud AI Assistant, AI Data Agents and MCP Server](../oracle/oracle-analytics-cloud-ai.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule Studio](../sap/sap-joule-studio.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise MCP](../teradata/teradata-enterprise-mcp.md), [Teradata Enterprise AgentStack](../teradata/teradata-agentstack.md) (preview) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md), [Confluent Intelligence](../ibm/confluent-intelligence.md) (preview) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir MCP and Ontology MCP](../palantir/palantir-mcp.md), [AIP Chatbot Studio](../palantir/palantir-aip-chatbot-studio.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Model Context Protocol (MCP)](../open-source/model-context-protocol.md), [LangGraph](../open-source/langgraph.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Airbyte Agents](../independent/airbyte-agents.md) (unconfirmed), [Kong Konnect](../independent/kong-konnect.md), [Redpanda Agentic Data Plane](../independent/redpanda-agentic-data-plane.md) (unconfirmed) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) |
