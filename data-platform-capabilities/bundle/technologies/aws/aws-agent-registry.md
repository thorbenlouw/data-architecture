---
type: Technology
id: aws-agent-registry
title: AWS Agent Registry
description: Private, governed catalogue of agents, tools, skills and MCP servers that people and agents can search through the console, APIs or an MCP endpoint.
platform: platform-aws
kind: feature
availability: ga
realises: [agent-registry, ai-system-discovery]
resource: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Preview April 2026, GA August 2026 under the agent-registry namespace. Can discover AgentCore runtimes and gateways across an AWS Organization automatically and be shared with AWS RAM.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) (Generative AI) (primary): Keep a governed inventory of agents, tools and MCP servers with owners and permissions so they can be found, approved and controlled.
- [AI system discovery](../../capabilities/governance/ai-system-discovery.md) (Governance and compliance): Find the AI models, agents and services in use, including unapproved ones, to build and maintain the AI inventory.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Foundry Control Plane](../microsoft/azure-foundry-control-plane.md) (preview) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Registry](../google-cloud/gcp-agent-registry.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks managed MCP servers](../databricks/databricks-managed-mcp-servers.md) (preview), [Unity Gateway](../databricks/databricks-unity-gateway.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica CDGC AI governance](../informatica/informatica-cdgc-ai-governance.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI system discovery](../../capabilities/governance/ai-system-discovery.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Agent Hub](../sap/sap-ai-agent-hub.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI system discovery](../../capabilities/governance/ai-system-discovery.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Agent Management](../dataiku/dataiku-agent-management.md) (preview), [Dataiku Govern](../dataiku/dataiku-govern.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI system discovery](../../capabilities/governance/ai-system-discovery.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Credo AI Governance Platform](../independent/credo-ai-governance-platform.md), [Collibra AI Command Center](../independent/collibra-ai-command-center.md) (unconfirmed), [Kong Konnect](../independent/kong-konnect.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI system discovery](../../capabilities/governance/ai-system-discovery.md) |
