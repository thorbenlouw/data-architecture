---
type: Capability
id: agent-tool-access
title: Agent tool and data access
description: Give agents governed access to data and actions through tools and protocols such as MCP.
aliases: [MCP servers, function calling, tool use]
broader: [ai-agents]
related: [data-apis, ai-context-layer, semantic-layer, audit-logging]
depends_on: [access-control]
tags: [generative-ai]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A tool is a described function a model can call. Its name, purpose and input schema are given to the model, which returns a structured request that the runtime executes and feeds back. The Model Context Protocol (MCP) standardises this: an MCP server publishes tools, readable resources and prompt templates, and any MCP client can discover and use them. For example, an MCP server for the data platform offers tools to search the catalogue, run read-only SQL against certified tables and fetch a metric definition, each run with the calling user's permissions.

Tool design decides what agents can do and how safely. Platforms increasingly ship MCP servers over their catalogue, SQL engine and semantic layer, and teams wrap internal APIs as custom tools. Narrow, task-specific tools are easier for models to use correctly and easier to secure than broad ones such as unrestricted SQL or shell access. This capability covers what agents can reach; agent identity covers who the call runs as, and the registry covers which tools are approved.

# Key considerations

- Write tool names and descriptions for the model, with clear purposes and examples. Vague descriptions lead to wrong or missed calls.
- Prefer read-only tools, and narrow write tools that validate their inputs, over general-purpose ones.
- Large tool outputs fill the model's context. Page, filter and summarise results so only the needed fields come back.
- Third-party MCP servers run code and see your data. Vet and pin them like any dependency, because a changed tool description can carry injected instructions.
- Enforce permissions inside the tool server. Instructions asking the model to behave are not a control.

# Questions to ask

- Which data and actions should agents reach, and which must they never reach?
- Must tools also serve clients outside the platform, such as desktop assistants or code editors?
- Who builds, reviews and maintains tool servers?
- How are tool calls authorised and recorded for audit?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Generative AI](generative-ai.md) |
| Broader | [AI agents](ai-agents.md) |
| Related | [Agent and tool registry](agent-registry.md), [Agent identity and authorisation](agent-identity.md), [Agent-to-agent interoperability](agent-interoperability.md), [AI context layer](../metadata/ai-context-layer.md), [AI gateway](ai-gateway.md), [AI red teaming](ai-red-teaming.md), [Audit logging](../security/audit-logging.md), [Data APIs](../serving/data-apis.md), [File-system access to object storage](../storage/object-file-access.md), [Semantic layer](../analytics-bi/semantic-layer.md) |
| Depends on | [Access control](../security/access-control.md) |
| Needed by | [Data engineering agents](../development-lifecycle/data-engineering-agents.md) |

# Where it appears

- **Use cases:** [Agentic process automation](../../use-cases/usecase-agentic-automation.md) (requires, level 3)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md)
- **Maturity tracks:** [Generative AI](../../maturity/track-genai.md) (from level 3, Defined)
- **Frameworks:** [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Context · [Open Data Product Standard (ODPS)](../../frameworks/framework-bitol-odps.md): Context

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | AgentCore Gateway | [Amazon Bedrock AgentCore Gateway](../../technologies/aws/aws-bedrock-agentcore-gateway.md), [Amazon Bedrock AgentCore Policy](../../technologies/aws/aws-bedrock-agentcore-policy.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric data agent](../../technologies/microsoft/fabric-data-agent.md), [Fabric IQ ontology](../../technologies/microsoft/fabric-iq-ontology.md) (preview), [Fabric MCP server](../../technologies/microsoft/fabric-mcp-server.md), [Foundry Agent Service](../../technologies/microsoft/azure-foundry-agent-service.md), [Foundry IQ](../../technologies/microsoft/azure-foundry-iq.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Google Cloud remote MCP servers | [Data Agent Kit](../../technologies/google-cloud/gcp-data-agent-kit.md) (preview), [Google Agent Development Kit](../../technologies/google-cloud/gcp-agent-development-kit.md), [Google Cloud Agent Gateway](../../technologies/google-cloud/gcp-agent-gateway.md), [Google Cloud remote MCP servers](../../technologies/google-cloud/gcp-remote-mcp-servers.md), [MCP Toolbox for Databases](../../technologies/google-cloud/gcp-mcp-toolbox-for-databases.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | Snowflake-managed MCP server | [Snowflake Cortex Agents](../../technologies/snowflake/snowflake-cortex-agents.md), [Snowflake-managed MCP server](../../technologies/snowflake/snowflake-managed-mcp-server.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks managed MCP servers](../../technologies/databricks/databricks-managed-mcp-servers.md) (preview), [Unity Gateway](../../technologies/databricks/databricks-unity-gateway.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | ClickHouse MCP server / Remote MCP | [ClickHouse Agents](../../technologies/clickhouse/clickhouse-agents.md) (preview), [ClickHouse MCP server (open-source and Remote MCP in Cloud)](../../technologies/clickhouse/clickhouse-mcp-server.md) |
| [Informatica](../../platforms/platform-informatica.md) | Informatica Headless and MCP servers | [Informatica AI Agent Engineering](../../technologies/informatica/informatica-ai-agent-engineering.md) (unconfirmed), [Informatica Headless Data Management (Informatica MCP servers)](../../technologies/informatica/informatica-headless-data-management.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera AI Agent Studio](../../technologies/cloudera/cloudera-agent-studio.md) (preview) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Analytics Cloud AI Assistant, AI Data Agents and MCP Server](../../technologies/oracle/oracle-analytics-cloud-ai.md), [Oracle Select AI Agent and Autonomous AI Database MCP Server](../../technologies/oracle/oracle-select-ai-agent.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Joule Studio](../../technologies/sap/sap-joule-studio.md) |
| [Teradata](../../platforms/platform-teradata.md) | Enterprise MCP | [Teradata Enterprise AgentStack](../../technologies/teradata/teradata-agentstack.md) (preview), [Teradata Enterprise MCP](../../technologies/teradata/teradata-enterprise-mcp.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Confluent Intelligence](../../technologies/ibm/confluent-intelligence.md) (preview), [IBM watsonx Orchestrate](../../technologies/ibm/ibm-watsonx-orchestrate.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [AIP Chatbot Studio](../../technologies/palantir/palantir-aip-chatbot-studio.md), [Palantir MCP and Ontology MCP](../../technologies/palantir/palantir-mcp.md) |
| [SAS](../../platforms/platform-sas.md) | SAS Viya MCP Server | [SAS Viya MCP Server](../../technologies/sas/sas-viya-mcp-server.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku Visual Agents and Code Agents](../../technologies/dataiku/dataiku-agents.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [LangGraph](../../technologies/open-source/langgraph.md), [Model Context Protocol (MCP)](../../technologies/open-source/model-context-protocol.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Airbyte Agents](../../technologies/independent/airbyte-agents.md) (unconfirmed), [Atlan](../../technologies/independent/atlan.md), [AtScale](../../technologies/independent/atscale.md), [Boomi Enterprise Platform](../../technologies/independent/boomi-enterprise-platform.md), [dbt Semantic Layer](../../technologies/independent/dbt-semantic-layer.md), [Kong Konnect](../../technologies/independent/kong-konnect.md), [Materialize](../../technologies/independent/materialize.md), [MuleSoft Anypoint Platform](../../technologies/independent/mulesoft-anypoint-platform.md), [Redpanda Agentic Data Plane](../../technologies/independent/redpanda-agentic-data-plane.md) (unconfirmed), [Select Star](../../technologies/independent/select-star.md), [Tableau Next](../../technologies/independent/tableau-next.md) |
