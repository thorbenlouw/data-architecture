---
type: Technology
id: agent2agent-protocol
title: Agent2Agent (A2A) protocol
description: Open protocol for AI agents built on different frameworks to discover each other's capabilities and delegate tasks to one another.
aliases: [A2A, Agent2Agent]
platform: platform-open-source
kind: open-standard
availability: ga
realises: [agent-interoperability]
resource: https://a2a-protocol.org/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0. Created by Google, donated to the Linux Foundation in 2025 and part of the Agentic AI Foundation since August 2026. Version 1.0, the first stable specification, was released in March 2026, and version 1.0.1 (May 2026) is the latest release. It complements [MCP](../open-source/model-context-protocol.md), which connects agents to tools rather than to other agents.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md) (Generative AI) (primary): Let agents built on different platforms discover, delegate to and call each other through open protocols.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore](../aws/aws-bedrock-agentcore.md) | [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Agent Framework](../microsoft/azure-agent-framework.md), [Foundry Agent Service](../microsoft/azure-foundry-agent-service.md) | [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Data Engineering Agent](../google-cloud/gcp-bigquery-data-engineering-agent.md), [Google Agent Development Kit](../google-cloud/gcp-agent-development-kit.md) | [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE Agents](../informatica/informatica-claire-agents.md) | [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Visual Agents and Code Agents](../dataiku/dataiku-agents.md) | [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [MuleSoft Anypoint Platform](../independent/mulesoft-anypoint-platform.md) | [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md) |
