---
type: Technology
id: gcp-agent-registry
title: Google Cloud Agent Registry
description: Inventory of the agents, tools and MCP servers in an organisation, used to register, discover and govern them.
aliases: [Agent Registry]
platform: platform-google-cloud
kind: feature
availability: ga
realises: [agent-registry]
resource: https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA June 2026. Used by Agent Gateway and for publishing BigQuery data agents to Gemini Enterprise; a Skill Registry (preview) catalogues reusable agent skills.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) (Generative AI) (primary): Keep a governed inventory of agents, tools and MCP servers with owners and permissions so they can be found, approved and controlled.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Gemini Enterprise Agent Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Agent Registry](../aws/aws-agent-registry.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Foundry Control Plane](../microsoft/azure-foundry-control-plane.md) (preview) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks managed MCP servers](../databricks/databricks-managed-mcp-servers.md) (preview), [Unity Gateway](../databricks/databricks-unity-gateway.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica CDGC AI governance](../informatica/informatica-cdgc-ai-governance.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Agent Hub](../sap/sap-ai-agent-hub.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra AI Command Center](../independent/collibra-ai-command-center.md) (unconfirmed), [Kong Konnect](../independent/kong-konnect.md), [Credo AI Governance Platform](../independent/credo-ai-governance-platform.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) |
