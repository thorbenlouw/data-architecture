---
type: Capability
id: ai-system-discovery
title: AI system discovery
description: Find the AI models, agents and services in use, including unapproved ones, to build and maintain the AI inventory.
aliases: [shadow AI discovery]
broader: [ai-governance]
related: [ai-gateway, agent-registry, data-security-posture, model-registry, network-security]
tags: [governance]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

AI system discovery builds the AI inventory by looking for AI in use instead of relying on people to declare it. Sources include model registries and serving endpoints, calls to model provider APIs seen in AI gateway, network or expense data, notebooks and code that import model libraries, agent and MCP server configurations, and AI features switched on in purchased software. For example, a scan of outbound traffic finds a team sending customer emails to an external language model API, and the finding becomes a draft inventory entry for the owner to complete.

Inventories built from surveys alone miss much real use, especially unapproved "shadow AI" and AI features that vendors add to existing SaaS tools. Discovery must be continuous because new endpoints, agents and integrations appear all the time. It complements registries rather than replacing them: discovery finds candidates, and the registry holds the reviewed, owned record. It resembles data security posture management, which scans for sensitive data rather than AI use.

# Key considerations

- Route model traffic through an AI gateway where possible. Discovery then comes from normal operation rather than a separate scan.
- Decide what happens to findings: notify, require registration by a deadline, or block. Blocking without an approved alternative pushes use further out of sight.
- Include AI built into purchased tools and agents running on staff devices, not only models deployed on the platform.
- Match findings to existing inventory entries by endpoint, owner and model identifiers to avoid duplicates.

# Questions to ask

- How was the current AI inventory built, and how often is it checked against actual use?
- Do all model calls pass through a gateway or proxy that records them?
- Which purchased tools have AI features, and are they switched on?
- What should happen when unregistered AI use is found?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Governance and compliance](governance.md) |
| Broader | [AI governance](ai-governance.md) |
| Related | [Agent and tool registry](../generative-ai/agent-registry.md), [AI gateway](../generative-ai/ai-gateway.md), [AI supply chain security](../security/ai-supply-chain-security.md), [Data security posture management](../security/data-security-posture.md), [Model governance](../mlops/model-governance.md), [Model registry](../machine-learning/model-registry.md), [Network security](../security/network-security.md) |

# Where it appears

- **Personas:** [Chief data officer](../../personas/persona-cdo.md)
- **Maturity tracks:** [AI and model governance](../../maturity/track-ai-governance.md) (from level 3, Defined)
- **Frameworks:** [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 5 – Prohibited AI practices; Article 6 and Annex III – Classification as high-risk; Article 49 – Registration · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Clause 4 – Context of the organisation · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): GOVERN 1 – Policies, processes and practices

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Agent Registry](../../technologies/aws/aws-agent-registry.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Purview Data Security Posture Management](../../technologies/microsoft/purview-dspm.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Security Command Center](../../technologies/google-cloud/gcp-security-command-center.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica CDGC AI governance](../../technologies/informatica/informatica-cdgc-ai-governance.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP AI Agent Hub](../../technologies/sap/sap-ai-agent-hub.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM Guardium Data Security Center](../../technologies/ibm/ibm-guardium-data-security-center.md), [IBM watsonx.governance](../../technologies/ibm/ibm-watsonx-governance.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku Agent Management](../../technologies/dataiku/dataiku-agent-management.md) (preview) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [BigID Next](../../technologies/independent/bigid-next.md), [Credo AI Governance Platform](../../technologies/independent/credo-ai-governance-platform.md), [Holistic AI Governance Platform](../../technologies/independent/holistic-ai-governance-platform.md), [Privacera](../../technologies/independent/privacera.md), [Securiti DataAI Command Platform](../../technologies/independent/securiti-dataai-command-platform.md) |
