---
type: Technology
id: collibra-ai-command-center
title: Collibra AI Command Center
description: Registry and control plane for AI use cases, models and agents that links each one to its data, policies and assessments and tracks production trust signals.
platform: platform-independent
vendor: Collibra
kind: saas
availability: unconfirmed
realises: [ai-governance, model-governance, compliance-evidence, agent-registry, ai-impact-assessment]
resource: https://www.collibra.com/products/ai-command-center
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

New in 2026 and presented alongside the earlier Collibra AI Governance assessments (EU AI Act and NIST AI RMF templates). It adds a registry of AI use cases, models and agents, guardian agents that supervise agent behaviour, machine-readable "agent contracts" and trust scores drawn from production signals. Collibra bought trail ML on 5 October 2026 to automate control assessment and add runtime policy enforcement where agents run. Collibra does not publish a release stage for the product or its components.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI governance](../../capabilities/governance/ai-governance.md) (Governance and compliance) (primary): Inventory AI systems and govern their risk, approval, documentation and use in line with regulation.
- [Model governance](../../capabilities/mlops/model-governance.md) (ML operations): Keep an inventory of models with owners, approvals, documentation and risk ratings throughout their life.
- [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) (Governance and compliance): Map regulatory requirements to platform controls and produce evidence for auditors.
- [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) (Generative AI): Keep a governed inventory of agents, tools and MCP servers with owners and permissions so they can be found, approved and controlled.
- [AI impact assessment](../../capabilities/governance/ai-impact-assessment.md) (Governance and compliance): Assess and record an AI system's effects on people and society before release and whenever it changes.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** unconfirmed

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Foundry Control Plane](../microsoft/azure-foundry-control-plane.md) (preview), [Microsoft Purview Compliance Manager](../microsoft/purview-compliance-manager.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI governance](../../capabilities/governance/ai-governance.md), [Model governance](../../capabilities/mlops/model-governance.md), [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Governance Hub](../databricks/databricks-governance-hub.md) (preview) | [AI governance](../../capabilities/governance/ai-governance.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica CDGC AI governance](../informatica/informatica-cdgc-ai-governance.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI governance](../../capabilities/governance/ai-governance.md), [Model governance](../../capabilities/mlops/model-governance.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.governance](../ibm/ibm-watsonx-governance.md) | [AI governance](../../capabilities/governance/ai-governance.md), [AI impact assessment](../../capabilities/governance/ai-impact-assessment.md), [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md), [Model governance](../../capabilities/mlops/model-governance.md) |
