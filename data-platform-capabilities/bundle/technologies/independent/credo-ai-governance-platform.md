---
type: Technology
id: credo-ai-governance-platform
title: Credo AI Governance Platform
description: Keeps a registry of AI systems, agents, models and vendors and turns regulations and policies into controls, risk assessments and evidence.
platform: platform-independent
vendor: Credo AI
kind: saas
availability: ga
realises:
- ai-governance
- model-governance
- compliance-evidence
- ai-system-discovery
- agent-registry
- ai-impact-assessment
resource: https://www.credo.ai/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Includes policy packs for the EU AI Act, NIST AI RMF, ISO/IEC 42001 and others, shadow AI detection, vendor risk and the GAIA assistant. Agent governance (Agent Registry and Agent Governor) was a research preview in October 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI governance](../../capabilities/governance/ai-governance.md) (Governance and compliance) (primary): Inventory AI systems and govern their risk, approval, documentation and use in line with regulation.
- [Model governance](../../capabilities/mlops/model-governance.md) (ML operations): Keep an inventory of models with owners, approvals, documentation and risk ratings throughout their life.
- [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) (Governance and compliance): Map regulatory requirements to platform controls and produce evidence for auditors.
- [AI system discovery](../../capabilities/governance/ai-system-discovery.md) (Governance and compliance): Find the AI models, agents and services in use, including unapproved ones, to build and maintain the AI inventory.
- [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) (Generative AI): Keep a governed inventory of agents, tools and MCP servers with owners and permissions so they can be found, approved and controlled.
- [AI impact assessment](../../capabilities/governance/ai-impact-assessment.md) (Governance and compliance): Assess and record an AI system's effects on people and society before release and whenever it changes.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Foundry Control Plane](../microsoft/azure-foundry-control-plane.md) (preview), [Microsoft Purview Compliance Manager](../microsoft/purview-compliance-manager.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI governance](../../capabilities/governance/ai-governance.md), [Model governance](../../capabilities/mlops/model-governance.md), [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Governance Hub](../databricks/databricks-governance-hub.md) (preview) | [AI governance](../../capabilities/governance/ai-governance.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica CDGC AI governance](../informatica/informatica-cdgc-ai-governance.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI governance](../../capabilities/governance/ai-governance.md), [AI system discovery](../../capabilities/governance/ai-system-discovery.md), [Model governance](../../capabilities/mlops/model-governance.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.governance](../ibm/ibm-watsonx-governance.md) | [AI governance](../../capabilities/governance/ai-governance.md), [AI impact assessment](../../capabilities/governance/ai-impact-assessment.md), [AI system discovery](../../capabilities/governance/ai-system-discovery.md), [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS AI Navigator](../sas/sas-ai-navigator.md) | [AI governance](../../capabilities/governance/ai-governance.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Govern](../dataiku/dataiku-govern.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI governance](../../capabilities/governance/ai-governance.md), [Model governance](../../capabilities/mlops/model-governance.md) |
