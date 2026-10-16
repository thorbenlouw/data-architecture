---
type: Capability
id: ai-impact-assessment
title: AI impact assessment
description: Assess and record an AI system's effects on people and society before release and whenever it changes.
aliases: [fundamental rights impact assessment, algorithmic impact assessment]
broader: [ai-governance]
related:
- privacy-impact-assessment
- fairness-assessment
- model-explainability
- genai-evaluation
- model-governance
tags: [governance]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

An AI impact assessment looks at who an AI system affects and how, beyond its technical performance. It records the intended purpose and users, the people subject to its outputs, foreseeable misuse, risks such as discrimination, errors, loss of privacy or unsafe actions, and the measures that address them, such as human review, thresholds or a narrower scope. For example, before a model that ranks job applicants goes live, the assessment examines whether it disadvantages groups of applicants, how candidates can challenge a decision and who reviews rejections.

The EU AI Act requires some deployers of high-risk systems, including public bodies and organisations using AI for credit scoring or for life and health insurance pricing, to carry out a fundamental rights impact assessment. Other frameworks and many internal policies expect similar assessments more widely. They are most useful when repeated whenever the model, data, purpose or users change, and linked to evaluation evidence such as fairness tests. They overlap with data protection impact assessments, and many organisations combine the two.

# Key considerations

- Trigger reassessment from changes recorded on the platform, such as a new model version, new training data or a new user group.
- Involve people who understand the affected groups, not only the engineering team.
- Link each identified risk to tests and monitoring, for example fairness metrics tracked in production, so mitigations are checked rather than asserted.
- Use one template covering privacy, fairness, safety and security, so teams do not fill in four overlapping forms.

# Questions to ask

- Does the system make or support decisions about people, such as eligibility, pricing or employment?
- Which groups could be harmed by errors, and how would they notice and challenge an outcome?
- What test evidence supports the claims in the assessment?
- Which changes to the system would require a new assessment?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Governance and compliance](governance.md) |
| Broader | [AI governance](ai-governance.md) |
| Related | [AI red teaming](../generative-ai/ai-red-teaming.md), [Bias and fairness assessment](../machine-learning/fairness-assessment.md), [Generative AI evaluation](../generative-ai/genai-evaluation.md), [Human oversight of AI](human-oversight.md), [Model explainability](../machine-learning/model-explainability.md), [Model governance](../mlops/model-governance.md), [Privacy impact assessment](privacy-impact-assessment.md) |

# Where it appears

- **Use cases:** [Credit decisioning](../../use-cases/usecase-credit-decisioning.md) (requires, level 2)
- **Personas:** [Risk and compliance officer](../../personas/persona-risk-compliance.md)
- **Maturity tracks:** [AI and model governance](../../maturity/track-ai-governance.md) (from level 3, Defined)
- **Frameworks:** [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 9 – Risk management system; Article 27 – Fundamental rights impact assessment · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Clause 6 – Planning; Clause 8 – Operation; Annex A.5 – Assessing impacts of AI systems · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): MAP 5 – Impacts

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.governance](../../technologies/ibm/ibm-watsonx-governance.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Collibra AI Command Center](../../technologies/independent/collibra-ai-command-center.md) (unconfirmed), [Credo AI Governance Platform](../../technologies/independent/credo-ai-governance-platform.md), [OneTrust AI Governance](../../technologies/independent/onetrust-ai-governance.md) |
