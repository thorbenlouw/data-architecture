---
type: Capability
id: ai-governance
title: AI governance
description: Inventory AI systems and govern their risk, approval, documentation and use in line with regulation.
aliases: [responsible AI]
broader: [governance]
related: [model-governance, genai-evaluation, ai-guardrails, model-registry, ai-gateway]
tags: [governance]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

AI governance applies governance to AI systems: trained models, applications built on foundation models, and agents. Its core is an inventory recording each system's owner, intended purpose, risk tier, the data and models it uses and its approval status. Around that sit processes to assess risk before release, document systems, monitor them in use, handle incidents and retire them. For example, a customer-service agent that can issue refunds is registered, rated, approved with conditions such as a refund limit with human review above it, and reviewed again when its model changes.

Regulation increasingly expects this. The EU AI Act sorts AI systems into risk tiers, places duties such as risk management, documentation, logging and human oversight on high-risk systems, and sets transparency duties for some others; ISO/IEC 42001 and the NIST AI Risk Management Framework describe management practices. Model governance covers the lifecycle of individual models. AI governance is broader: it also covers purchased AI services, AI features inside other tools and AI use across the organisation.

# Key considerations

- Agree a working definition of an AI system and a risk-tiering scheme first. Inventories stall on arguments about what counts.
- Record whether the organisation is the provider or the deployer of each system. Many regulatory duties depend on that role.
- Link inventory entries to the models, prompts, datasets and evaluation results on the platform, so documentation stays current instead of being written once.
- Make approval proportionate to risk. A light path for low-risk uses stops teams building outside the process.
- Plan for AI that arrives inside purchased software, which needs the same inventory and assessment as systems you build.

# Questions to ask

- Which AI systems are in use today, built or bought, and who owns each?
- Does any use fall into a high-risk category under the EU AI Act or sector rules?
- Who approves a new AI use case, and what evidence do they need?
- How are AI systems monitored once live, and who can suspend them?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Governance and compliance](governance.md) |
| Broader | [Governance and compliance](governance.md) |
| Narrower | [Agent and tool registry](../generative-ai/agent-registry.md), [AI content marking and provenance](../generative-ai/ai-content-provenance.md), [AI impact assessment](ai-impact-assessment.md), [AI incident management](ai-incident-management.md), [AI supply chain security](../security/ai-supply-chain-security.md), [AI system discovery](ai-system-discovery.md), [Human oversight of AI](human-oversight.md) |
| Related | [Machine learning development](../machine-learning/machine-learning.md), [ML operations](../mlops/mlops.md), [Generative AI](../generative-ai/generative-ai.md), [AI gateway](../generative-ai/ai-gateway.md), [AI guardrails](../generative-ai/ai-guardrails.md), [Generative AI evaluation](../generative-ai/genai-evaluation.md), [Model governance](../mlops/model-governance.md), [Model lineage](../metadata/model-lineage.md), [Model registry](../machine-learning/model-registry.md) |

# Where it appears

- **Use cases:** [Agentic process automation](../../use-cases/usecase-agentic-automation.md) (requires, level 2) · [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (requires, level 2)
- **Personas:** [Chief data officer](../../personas/persona-cdo.md) · [Risk and compliance officer](../../personas/persona-risk-compliance.md)
- **Maturity tracks:** [AI and model governance](../../maturity/track-ai-governance.md) (from level 2, Managed)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Handling Ethics · [DCAM v3](../../frameworks/framework-edm-dcam.md): 8 Analytics Management · [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 4 – AI literacy; Article 5 – Prohibited AI practices; Article 6 and Annex III – Classification as high-risk; Article 9 – Risk management system; Article 17 – Quality management system; Article 26 – Obligations of deployers; Article 49 – Registration; Article 50 – Transparency obligations · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Clause 4 – Context of the organisation; Clause 5 – Leadership; Clause 6 – Planning; Clause 7 – Support; Clause 8 – Operation; Clause 10 – Improvement; Annex A.2 – Policies related to AI; Annex A.3 – Internal organisation; Annex A.9 – Use of AI systems · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): GOVERN 1 – Policies, processes and practices; GOVERN 3 – Workforce diversity and inclusion; GOVERN 4 – Risk culture; GOVERN 5 – Engagement with external stakeholders; MAP 1 – Context; MAP 2 – Categorisation; MANAGE 1 – Risk response

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Foundry Control Plane](../../technologies/microsoft/azure-foundry-control-plane.md) (preview), [Microsoft Purview Compliance Manager](../../technologies/microsoft/purview-compliance-manager.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Governance Hub](../../technologies/databricks/databricks-governance-hub.md) (preview) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica CDGC AI governance](../../technologies/informatica/informatica-cdgc-ai-governance.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.governance](../../technologies/ibm/ibm-watsonx-governance.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Collibra AI Command Center](../../technologies/independent/collibra-ai-command-center.md) (unconfirmed), [Credo AI Governance Platform](../../technologies/independent/credo-ai-governance-platform.md), [Holistic AI Governance Platform](../../technologies/independent/holistic-ai-governance-platform.md), [OneTrust AI Governance](../../technologies/independent/onetrust-ai-governance.md) |

Narrower capabilities are realised by a further 35 technologies; see their pages.
