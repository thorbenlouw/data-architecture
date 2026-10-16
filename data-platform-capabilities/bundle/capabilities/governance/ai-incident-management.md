---
type: Capability
id: ai-incident-management
title: AI incident management
description: Record, investigate and report incidents and malfunctions involving AI systems, including notifying regulators where required.
broader: [ai-governance]
related: [genai-observability, data-issue-management, ai-red-teaming, genai-evaluation, human-oversight]
depends_on: [inference-logging]
tags: [governance]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

An AI incident is an event in which an AI system causes or nearly causes harm, or acts outside its intended limits: a chatbot reveals another customer's data, or an agent makes a payment nobody approved. Incident management records the event and links it to the system, model version, prompts, inputs and outputs involved. It assigns an owner, contains the problem by rolling back or switching off the system, finds the cause and tracks fixes. Where the law requires, it also notifies regulators or affected people.

AI incidents differ from ordinary IT incidents because the system may run exactly as built while its outputs are wrong, unfair or unsafe, so monitoring for errors and outages does not catch them. Under the EU AI Act, providers of high-risk systems must report serious incidents to market surveillance authorities within set deadlines, and deployers who identify one must inform the provider. An incident may also be a personal data breach. Lessons feed back into evaluation sets, guardrails and impact assessments.

# Key considerations

- Capture enough to reproduce an incident: model and prompt versions, retrieved content, tool calls and outputs. Without inference logs most investigations stall.
- Give each AI system a tested way to stop or roll back quickly, such as a feature flag or a fallback model.
- Agree severity criteria and reporting routes with legal in advance, since regulatory deadlines run from when you become aware of an incident.
- Extend the existing incident process with AI-specific fields where possible, so incidents are not lost between teams.
- Turn each incident into a test case for evaluation and red teaming.

# Questions to ask

- How would users or staff report a harmful or wrong AI output today?
- Can you reconstruct what a model or agent saw and did for a given request last month?
- Which incidents would need reporting to a regulator, and who decides?
- How quickly can each AI system be switched off or rolled back?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Governance and compliance](governance.md) |
| Broader | [AI governance](ai-governance.md) |
| Related | [AI red teaming](../generative-ai/ai-red-teaming.md), [Data breach response](../security/data-breach-response.md), [Data issue management](../data-quality/data-issue-management.md), [Generative AI evaluation](../generative-ai/genai-evaluation.md), [Generative AI observability](../generative-ai/genai-observability.md), [Human oversight of AI](human-oversight.md), [Model monitoring](../mlops/model-monitoring.md), [Platform incident management](../platform-operations/platform-incident-management.md) |
| Depends on | [Inference logging](../mlops/inference-logging.md) |

# Where it appears

- **Use cases:** [Agentic process automation](../../use-cases/usecase-agentic-automation.md) (benefits from)
- **Personas:** [Risk and compliance officer](../../personas/persona-risk-compliance.md)
- **Maturity tracks:** [AI and model governance](../../maturity/track-ai-governance.md) (from level 4, Measured)
- **Frameworks:** [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 17 – Quality management system; Article 26 – Obligations of deployers; Article 73 – Reporting of serious incidents · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Clause 10 – Improvement; Annex A.8 – Information for interested parties · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): GOVERN 4 – Risk culture; MANAGE 4 – Response, recovery and communication; Generative AI Profile (NIST AI 600-1)

# How platforms provide it

No technology in this bundle realises this capability directly yet.
