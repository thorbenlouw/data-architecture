---
type: Technology
id: sap-ai-agent-hub
title: SAP AI Agent Hub
description: Capability of SAP LeanIX that discovers SAP and non-SAP AI agents and MCP servers, maps them to applications and processes, and tracks which are approved for use.
aliases: [SAP LeanIX AI Agent Hub]
platform: platform-sap
kind: feature
availability: ga
realises: [agent-registry, ai-system-discovery]
resource: https://www.leanix.net/en/blog/sap-leanix-announces-launch-of-ai-agent-hub-and-key-industry-partnerships
tags: [sap]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Generally available in SAP LeanIX Application Portfolio Management since November 2025. Agents are found through integrations with SAP, Google and Microsoft agent repositories and through an API based on the [Agent2Agent protocol](../open-source/agent2agent-protocol.md) for agents built in-house. Lifecycle status controls which agents are approved, and an agent portal publishes the approved list.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) (Generative AI) (primary): Keep a governed inventory of agents, tools and MCP servers with owners and permissions so they can be found, approved and controlled.
- [AI system discovery](../../capabilities/governance/ai-system-discovery.md) (Governance and compliance): Find the AI models, agents and services in use, including unapproved ones, to build and maintain the AI inventory.

**Platform:** [SAP](../../platforms/platform-sap.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Agent Registry](../aws/aws-agent-registry.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI system discovery](../../capabilities/governance/ai-system-discovery.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Foundry Control Plane](../microsoft/azure-foundry-control-plane.md) (preview) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Registry](../google-cloud/gcp-agent-registry.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks managed MCP servers](../databricks/databricks-managed-mcp-servers.md) (preview), [Unity Gateway](../databricks/databricks-unity-gateway.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica CDGC AI governance](../informatica/informatica-cdgc-ai-governance.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI system discovery](../../capabilities/governance/ai-system-discovery.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Credo AI Governance Platform](../independent/credo-ai-governance-platform.md), [Collibra AI Command Center](../independent/collibra-ai-command-center.md) (unconfirmed), [Kong Konnect](../independent/kong-konnect.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI system discovery](../../capabilities/governance/ai-system-discovery.md) |
