---
type: Technology
id: azure-foundry-control-plane
title: Foundry Control Plane
description: A fleet-wide view of agents, models and tools with inventory, compliance status, guardrail policies and health across Foundry projects.
platform: platform-microsoft
kind: feature
availability: preview
realises: [ai-governance, model-governance, genai-observability, agent-registry]
resource: https://learn.microsoft.com/azure/foundry/control-plane/overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Integrates with Entra, Defender, Purview and Azure Policy; advanced governance requires the AI Gateway.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI governance](../../capabilities/governance/ai-governance.md) (Governance and compliance) (primary): Inventory AI systems and govern their risk, approval, documentation and use in line with regulation.
- [Model governance](../../capabilities/mlops/model-governance.md) (ML operations): Keep an inventory of models with owners, approvals, documentation and risk ratings throughout their life.
- [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) (Generative AI): Trace model and agent calls with their prompts, responses, latency, cost and user feedback.
- [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) (Generative AI): Keep a governed inventory of agents, tools and MCP servers with owners and permissions so they can be found, approved and controlled.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** preview  
**Product family:** Microsoft Foundry

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Governance Hub](../databricks/databricks-governance-hub.md) (preview) | [AI governance](../../capabilities/governance/ai-governance.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica CDGC AI governance](../informatica/informatica-cdgc-ai-governance.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI governance](../../capabilities/governance/ai-governance.md), [Model governance](../../capabilities/mlops/model-governance.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.governance](../ibm/ibm-watsonx-governance.md) | [AI governance](../../capabilities/governance/ai-governance.md), [Model governance](../../capabilities/mlops/model-governance.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS AI Navigator](../sas/sas-ai-navigator.md) | [AI governance](../../capabilities/governance/ai-governance.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Govern](../dataiku/dataiku-govern.md), [Dataiku Agent Management](../dataiku/dataiku-agent-management.md) (preview) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI governance](../../capabilities/governance/ai-governance.md), [Model governance](../../capabilities/mlops/model-governance.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra AI Command Center](../independent/collibra-ai-command-center.md) (unconfirmed), [Credo AI Governance Platform](../independent/credo-ai-governance-platform.md), [OneTrust AI Governance](../independent/onetrust-ai-governance.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI governance](../../capabilities/governance/ai-governance.md), [Model governance](../../capabilities/mlops/model-governance.md) |
