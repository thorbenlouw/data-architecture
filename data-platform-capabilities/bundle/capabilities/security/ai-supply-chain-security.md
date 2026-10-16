---
type: Capability
id: ai-supply-chain-security
title: AI supply chain security
description: Check third-party models, model files, libraries and tool servers for tampering and malicious code before use, and record what each AI system is built from.
aliases: [AI bill of materials, AI-BOM, ML-BOM, model scanning, model signing]
broader: [security, ai-governance]
related: [model-governance, agent-registry, runtime-management, model-registry, ai-system-discovery]
tags: [security]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

AI systems are assembled from parts made elsewhere: open-weight models and adapters from public hubs, Python libraries, datasets and MCP servers. Model files saved in Python's pickle format run arbitrary code when loaded, and a tool server can change its tool descriptions after approval. Supply chain security scans and verifies each part before use, keeps approved copies in an internal registry or mirror, and records an AI bill of materials listing the models, datasets, libraries and tools each system uses. For example, a model from a public hub is scanned, its signature checked and converted to a format that cannot execute code before anyone loads it.

It extends software supply chain practice to artefacts that ordinary dependency scanners miss, using standards such as Sigstore-based model signing and CycloneDX or SPDX bills of materials. The bill of materials also shows which systems are affected when a model licence or a library vulnerability changes. Model governance records approvals; this capability checks that what runs is what was approved.

# Key considerations

- Prefer weight formats that cannot execute code, such as safetensors, and block pickle-based model files from outside sources.
- Pull models, packages and tool servers through internal mirrors, so training and serving networks need no direct access to public hubs.
- Pin and hash every external artefact, and review it again when its version or tool descriptions change.
- Generate the bill of materials from the registry, environment definitions and agent configuration. Lists kept by hand are incomplete within weeks.

# Questions to ask

- Can staff load models from public hubs into environments that hold sensitive data?
- Could you list every system that uses a particular open-weight model or library version?
- Do customers or regulators ask for a bill of materials for the AI systems you supply?
- Who approves a new external model or MCP server, and which checks do they run?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Security and access](security.md) |
| Broader | [Security and access](security.md), [AI governance](../governance/ai-governance.md) |
| Related | [Agent and tool registry](../generative-ai/agent-registry.md), [AI system discovery](../governance/ai-system-discovery.md), [Model governance](../mlops/model-governance.md), [Model registry](../machine-learning/model-registry.md), [Runtime and environment management](../development-lifecycle/runtime-management.md) |

# Where it appears

- **Personas:** [ML engineer](../../personas/persona-ml-engineer.md)
- **Maturity tracks:** [AI and model governance](../../maturity/track-ai-governance.md) (from level 3, Defined)
- **Frameworks:** [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 15 – Accuracy, robustness and cybersecurity · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Annex A.4 – Resources for AI systems; Annex A.10 – Third-party and customer relationships · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): GOVERN 6 – Third-party risk; MAP 4 – Risks of components; MANAGE 3 – Third-party risk monitoring

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [OpenSSF Model Signing](../../technologies/open-source/sigstore-model-signing.md) |
