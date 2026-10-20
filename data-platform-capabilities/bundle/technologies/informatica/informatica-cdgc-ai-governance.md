---
type: Technology
id: informatica-cdgc-ai-governance
title: Informatica CDGC AI governance
description: Catalogues AI models, multi-agent systems and their data and links them to policies, owners and lineage, including assets scanned from platforms such as Google Vertex AI.
platform: platform-informatica
kind: feature
availability: ga
realises: [ai-governance, model-governance, agent-registry, ai-system-discovery]
resource: https://www.informatica.com/blogs/new-informatica-capabilities-clear-the-path-to-ai-ready-data.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Expanded in the Fall 2025 release. The Agent Fabric Context Catalog (GA Spring 2026) extends this to a combined directory of data assets and AI agents, with governance tools published as MCP servers.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI governance](../../capabilities/governance/ai-governance.md) (Governance and compliance) (primary): Inventory AI systems and govern their risk, approval, documentation and use in line with regulation.
- [Model governance](../../capabilities/mlops/model-governance.md) (ML operations): Keep an inventory of models with owners, approvals, documentation and risk ratings throughout their life.
- [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) (Generative AI): Keep a governed inventory of agents, tools and MCP servers with owners and permissions so they can be found, approved and controlled.
- [AI system discovery](../../capabilities/governance/ai-system-discovery.md) (Governance and compliance): Find the AI models, agents and services in use, including unapproved ones, to build and maintain the AI inventory.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud, Cloud Data Governance and Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Agent Registry](../aws/aws-agent-registry.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI system discovery](../../capabilities/governance/ai-system-discovery.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Foundry Control Plane](../microsoft/azure-foundry-control-plane.md) (preview), [Microsoft Purview Compliance Manager](../microsoft/purview-compliance-manager.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI governance](../../capabilities/governance/ai-governance.md), [Model governance](../../capabilities/mlops/model-governance.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Governance Hub](../databricks/databricks-governance-hub.md) (preview) | [AI governance](../../capabilities/governance/ai-governance.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Agent Hub](../sap/sap-ai-agent-hub.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI system discovery](../../capabilities/governance/ai-system-discovery.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.governance](../ibm/ibm-watsonx-governance.md) | [AI governance](../../capabilities/governance/ai-governance.md), [AI system discovery](../../capabilities/governance/ai-system-discovery.md), [Model governance](../../capabilities/mlops/model-governance.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS AI Navigator](../sas/sas-ai-navigator.md) | [AI governance](../../capabilities/governance/ai-governance.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Govern](../dataiku/dataiku-govern.md), [Dataiku Agent Management](../dataiku/dataiku-agent-management.md) (preview) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI governance](../../capabilities/governance/ai-governance.md), [Model governance](../../capabilities/mlops/model-governance.md), [AI system discovery](../../capabilities/governance/ai-system-discovery.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Credo AI Governance Platform](../independent/credo-ai-governance-platform.md), [Collibra AI Command Center](../independent/collibra-ai-command-center.md) (unconfirmed), [OneTrust AI Governance](../independent/onetrust-ai-governance.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI governance](../../capabilities/governance/ai-governance.md), [AI system discovery](../../capabilities/governance/ai-system-discovery.md), [Model governance](../../capabilities/mlops/model-governance.md) |
