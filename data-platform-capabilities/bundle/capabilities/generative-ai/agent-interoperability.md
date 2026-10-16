---
type: Capability
id: agent-interoperability
title: Agent-to-agent interoperability
description: Let agents built on different platforms discover, delegate to and call each other through open protocols.
aliases: [A2A]
broader: [ai-agents]
related: [agent-registry, agent-tool-access, application-integration, genai-observability]
depends_on: [agent-identity]
tags: [generative-ai]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Agents built by different teams or vendors need a common way to find each other and hand over work. Open protocols such as Agent2Agent (A2A) define how an agent publishes a description of what it can do, known as an agent card, how another agent sends it a task, and how status updates, messages and results flow back, including for tasks that run for hours. For example, a procurement agent on one platform delegates a supplier risk check to a risk agent on another, receives progress updates and gets a structured report back, without either side exposing its internals.

This matters once agents are spread across business applications, cloud platforms and internal builds. MCP connects an agent to tools and data; agent-to-agent protocols connect it to a peer that does its own reasoning and may ask for clarification. Adoption is still early, so many organisations simply expose agents to each other as tools for now. Identity propagation, data sharing terms and cost attribution across organisations are the hard parts.

# Key considerations

- Carry identity and authorisation through every delegation. Otherwise the called agent works with its own, often wider, permissions.
- Delegating to an external agent sends data outside your boundary. Treat it like any other data sharing agreement.
- Debugging across agents needs trace identifiers that pass between platforms.
- Protocols are still changing. Keep protocol handling in a thin layer so changes do not ripple through every agent.

# Questions to ask

- Will agents need to call agents owned by other teams, vendors or partners?
- Which platforms in the estate support open agent protocols today?
- Who is accountable when a delegated task goes wrong?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Generative AI](generative-ai.md) |
| Broader | [AI agents](ai-agents.md) |
| Related | [Agent and tool registry](agent-registry.md), [Agent tool and data access](agent-tool-access.md), [Application integration](../ingestion-integration/application-integration.md), [Generative AI observability](genai-observability.md) |
| Depends on | [Agent identity and authorisation](agent-identity.md) |

# Where it appears

- **Use cases:** [Agentic process automation](../../use-cases/usecase-agentic-automation.md) (benefits from)
- **Maturity tracks:** [Generative AI](../../maturity/track-genai.md) (from level 5, Optimising)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Bedrock AgentCore](../../technologies/aws/aws-bedrock-agentcore.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Foundry Agent Service](../../technologies/microsoft/azure-foundry-agent-service.md), [Microsoft Agent Framework](../../technologies/microsoft/azure-agent-framework.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery Data Engineering Agent](../../technologies/google-cloud/gcp-bigquery-data-engineering-agent.md), [Google Agent Development Kit](../../technologies/google-cloud/gcp-agent-development-kit.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [CLAIRE Agents](../../technologies/informatica/informatica-claire-agents.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx Orchestrate](../../technologies/ibm/ibm-watsonx-orchestrate.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Agent2Agent (A2A) protocol](../../technologies/open-source/agent2agent-protocol.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [MuleSoft Anypoint Platform](../../technologies/independent/mulesoft-anypoint-platform.md) |
