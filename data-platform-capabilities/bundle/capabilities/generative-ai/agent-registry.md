---
type: Capability
id: agent-registry
title: Agent and tool registry
description: Keep a governed inventory of agents, tools and MCP servers with owners and permissions so they can be found, approved and controlled.
aliases: [MCP registry, agent catalogue]
broader: [ai-agents, ai-governance]
related: [model-registry, ai-system-discovery, data-catalogue, agent-tool-access, agent-identity]
tags: [generative-ai]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The registry records each agent, tool and MCP server in use: its purpose, owner, version, the models it calls, the tools and data it may reach, its approval status and risk rating. Agent runtimes and clients consult it to find approved tools, and administrators use it to allow, block or retire them. For example, a team publishes a new MCP server for the HR system. It appears in the registry as pending, security reviews the scopes it requests, and only after approval can agents in other workspaces discover and connect to it.

Without a registry, agents and tool servers multiply unnoticed, and nobody can say which agents can reach customer data. Registries appear as agent and tool catalogues in data and cloud platforms, as MCP registries that follow the open MCP registry format, and as AI inventories in governance tools. AI system discovery finds systems that were never registered, and a model registry versions trained models; this registry is the approved list agents and tools are checked against.

# Key considerations

- Make registration a condition of deployment or network access. Voluntary registries go out of date.
- Record the tools and data scopes each agent uses, not only the agent itself. Risk comes from the combination.
- A tool's description or behaviour can change after approval. Version entries and trigger review on change.
- Feed the same records into the AI inventory used for regulatory reporting, so there is one list rather than two.

# Questions to ask

- How many agents and tool servers exist today, and who would know?
- Who approves a new agent or tool, and against which criteria?
- Must external or third-party MCP servers be allowed or blocked centrally?
- Which regulatory inventories must the registry feed?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Generative AI](generative-ai.md) |
| Broader | [AI agents](ai-agents.md), [AI governance](../governance/ai-governance.md) |
| Related | [Agent identity and authorisation](agent-identity.md), [Agent tool and data access](agent-tool-access.md), [Agent-to-agent interoperability](agent-interoperability.md), [AI supply chain security](../security/ai-supply-chain-security.md), [AI system discovery](../governance/ai-system-discovery.md), [Data catalogue](../metadata/data-catalogue.md), [Enterprise AI assistant](enterprise-ai-assistant.md), [Model registry](../machine-learning/model-registry.md) |

# Where it appears

- **Use cases:** [Agentic process automation](../../use-cases/usecase-agentic-automation.md) (requires, level 2)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md)
- **Maturity tracks:** [AI and model governance](../../maturity/track-ai-governance.md) (from level 3, Defined) · [Generative AI](../../maturity/track-genai.md) (from level 3, Defined)
- **Frameworks:** [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 6 and Annex III – Classification as high-risk · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Clause 4 – Context of the organisation; Annex A.4 – Resources for AI systems · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): GOVERN 1 – Policies, processes and practices; MAP 1 – Context

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Agent Registry](../../technologies/aws/aws-agent-registry.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Foundry Control Plane](../../technologies/microsoft/azure-foundry-control-plane.md) (preview) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Agent Registry](../../technologies/google-cloud/gcp-agent-registry.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks managed MCP servers](../../technologies/databricks/databricks-managed-mcp-servers.md) (preview), [Unity Gateway](../../technologies/databricks/databricks-unity-gateway.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica CDGC AI governance](../../technologies/informatica/informatica-cdgc-ai-governance.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP AI Agent Hub](../../technologies/sap/sap-ai-agent-hub.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx Orchestrate](../../technologies/ibm/ibm-watsonx-orchestrate.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku Agent Management](../../technologies/dataiku/dataiku-agent-management.md) (preview), [Dataiku Govern](../../technologies/dataiku/dataiku-govern.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Boomi Enterprise Platform](../../technologies/independent/boomi-enterprise-platform.md), [Collibra AI Command Center](../../technologies/independent/collibra-ai-command-center.md) (unconfirmed), [Credo AI Governance Platform](../../technologies/independent/credo-ai-governance-platform.md), [Kong Konnect](../../technologies/independent/kong-konnect.md), [MuleSoft Anypoint Platform](../../technologies/independent/mulesoft-anypoint-platform.md), [Redpanda Agentic Data Plane](../../technologies/independent/redpanda-agentic-data-plane.md) (unconfirmed) |
