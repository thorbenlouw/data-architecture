---
type: Framework
id: framework-nist-ai-rmf
title: NIST AI Risk Management Framework (AI RMF 1.0)
description: A voluntary framework for managing AI risk through four functions, Govern, Map, Measure and Manage, broken into categories and subcategories of outcomes.
aliases: [NIST AI RMF, AI RMF, NIST AI 100-1, NIST AI 600-1, NIST Generative AI Profile]
kind: control-framework
publisher: National Institute of Standards and Technology (NIST)
resource: https://www.nist.gov/itl/ai-risk-management-framework
related: [framework-iso-iec-42001, framework-eu-ai-act]
applies_to:
- usecase-agentic-automation
- usecase-rag-assistant
- usecase-credit-decisioning
- persona-risk-compliance
- persona-ai-engineer
- persona-ml-engineer
mappings:
- ref: GOVERN 1 – Policies, processes and practices
  summary: AI risk policies and practices are in place, transparent and applied across the organisation, including an inventory of AI systems and a way to retire them.
  capabilities: [ai-governance, ai-system-discovery, agent-registry, data-policy-management, compliance-evidence]
- ref: GOVERN 2 – Accountability structures
  summary: Roles and responsibilities for AI risk are assigned and the people in them are trained.
  capabilities: [model-governance, data-ownership]
- ref: GOVERN 3 – Workforce diversity and inclusion
  summary: Diverse teams and perspectives inform AI risk decisions throughout the lifecycle.
  capabilities: [ai-governance]
- ref: GOVERN 4 – Risk culture
  summary: Teams think critically about AI risk, communicate about it openly and have practices for testing, identifying incidents and sharing information.
  capabilities: [ai-incident-management, ai-red-teaming, ai-governance]
- ref: GOVERN 5 – Engagement with external stakeholders
  summary: Feedback from people outside the team is collected and used in design and operation.
  capabilities: [genai-observability, ai-governance]
- ref: GOVERN 6 – Third-party risk
  summary: Risks from third-party software, data and supply chains, including intellectual property risks, are addressed in policy with contingency plans.
  capabilities: [ai-supply-chain-security, data-usage-rights, foundation-model-access, ai-gateway, model-governance]
- ref: MAP 1 – Context
  summary: The purpose, users, setting and requirements of each AI system are understood and documented.
  capabilities: [model-governance, agent-registry, ai-governance]
- ref: MAP 2 – Categorisation
  summary: Each system is categorised, including its tasks, limits of knowledge and how people will oversee its output.
  capabilities: [model-governance, human-oversight, ai-governance]
- ref: MAP 3 – Benefits and costs
  summary: Expected benefits and costs are compared against suitable benchmarks, and processes for human oversight are defined.
  capabilities: [model-evaluation, human-oversight, cost-attribution]
- ref: MAP 4 – Risks of components
  summary: Risks and benefits of all components, including third-party data and models, are mapped, together with legal risks such as infringing others' rights.
  capabilities: [model-lineage, data-lineage, ai-supply-chain-security, data-usage-rights, foundation-model-access]
- ref: MAP 5 – Impacts
  summary: Likely impacts on individuals, groups, organisations and society are described.
  capabilities: [ai-impact-assessment, fairness-assessment]
- ref: MEASURE 1 – Methods and metrics
  summary: Suitable methods and metrics for AI risks are chosen and applied.
  capabilities: [model-evaluation, genai-evaluation, training-dataset-management]
- ref: MEASURE 2 – Evaluation for trustworthy characteristics
  summary: Systems are tested for validity, safety, security, explainability, privacy and fairness.
  capabilities:
  - model-evaluation
  - genai-evaluation
  - ai-red-teaming
  - fairness-assessment
  - model-explainability
  - ai-guardrails
- ref: MEASURE 3 – Tracking risks over time
  summary: Identified and emerging risks are tracked in production.
  capabilities: [model-monitoring, drift-detection, genai-observability]
- ref: MEASURE 4 – Feedback on measurement
  summary: The effectiveness of measurement is checked with feedback from users and experts.
  capabilities: [model-performance-monitoring, genai-evaluation]
- ref: MANAGE 1 – Risk response
  summary: Mapped and measured risks are prioritised and acted on.
  capabilities: [model-governance, ai-governance]
- ref: MANAGE 2 – Maximising benefit and minimising harm
  summary: Strategies are in place to sustain value and to disengage or deactivate systems that behave outside their intended use.
  capabilities: [human-oversight, model-release-strategies, ai-guardrails, model-deployment]
- ref: MANAGE 3 – Third-party risk monitoring
  summary: Risks from third-party models and components, including pre-trained models, are monitored and controlled.
  capabilities: [ai-supply-chain-security, ai-gateway, model-monitoring, foundation-model-access]
- ref: MANAGE 4 – Response, recovery and communication
  summary: Plans for monitoring, appeal and override, incident response, recovery and communication are documented and followed.
  capabilities: [ai-incident-management, human-oversight, model-monitoring, model-registry]
- ref: Generative AI Profile (NIST AI 600-1)
  summary: Applies the framework to risks specific to generative AI, such as confabulation, data leakage and harmful content, with emphasis on testing before release, content provenance and incident disclosure.
  capabilities:
  - genai-evaluation
  - ai-red-teaming
  - ai-content-provenance
  - ai-guardrails
  - genai-observability
  - ai-incident-management
  - unstructured-lineage
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

NIST published AI RMF 1.0 (NIST AI 100-1) in January 2023, with a Playbook, crosswalks to other standards and a Generative AI Profile (NIST AI 600-1) in July 2024. NIST says the framework is being revised under the White House AI Action Plan, and in April 2026 it released a concept note for a critical infrastructure profile; as of October 2026 version 1.0 is still current. It is widely used in the United States and by multinationals as a common language for AI risk, organised as 19 categories across the four functions and seven characteristics of trustworthy AI. The Measure and Manage functions map most directly to evaluation, monitoring and guardrail capabilities.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Mapping to capabilities

| Area | Summary | Capabilities |
|---|---|---|
| GOVERN 1 – Policies, processes and practices | AI risk policies and practices are in place, transparent and applied across the organisation, including an inventory of AI systems and a way to retire them. | [AI governance](../capabilities/governance/ai-governance.md), [AI system discovery](../capabilities/governance/ai-system-discovery.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md), [Policy management](../capabilities/governance/data-policy-management.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) |
| GOVERN 2 – Accountability structures | Roles and responsibilities for AI risk are assigned and the people in them are trained. | [Model governance](../capabilities/mlops/model-governance.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md) |
| GOVERN 3 – Workforce diversity and inclusion | Diverse teams and perspectives inform AI risk decisions throughout the lifecycle. | [AI governance](../capabilities/governance/ai-governance.md) |
| GOVERN 4 – Risk culture | Teams think critically about AI risk, communicate about it openly and have practices for testing, identifying incidents and sharing information. | [AI incident management](../capabilities/governance/ai-incident-management.md), [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md), [AI governance](../capabilities/governance/ai-governance.md) |
| GOVERN 5 – Engagement with external stakeholders | Feedback from people outside the team is collected and used in design and operation. | [Generative AI observability](../capabilities/generative-ai/genai-observability.md), [AI governance](../capabilities/governance/ai-governance.md) |
| GOVERN 6 – Third-party risk | Risks from third-party software, data and supply chains, including intellectual property risks, are addressed in policy with contingency plans. | [AI supply chain security](../capabilities/security/ai-supply-chain-security.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Foundation model access](../capabilities/generative-ai/foundation-model-access.md), [AI gateway](../capabilities/generative-ai/ai-gateway.md), [Model governance](../capabilities/mlops/model-governance.md) |
| MAP 1 – Context | The purpose, users, setting and requirements of each AI system are understood and documented. | [Model governance](../capabilities/mlops/model-governance.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md), [AI governance](../capabilities/governance/ai-governance.md) |
| MAP 2 – Categorisation | Each system is categorised, including its tasks, limits of knowledge and how people will oversee its output. | [Model governance](../capabilities/mlops/model-governance.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [AI governance](../capabilities/governance/ai-governance.md) |
| MAP 3 – Benefits and costs | Expected benefits and costs are compared against suitable benchmarks, and processes for human oversight are defined. | [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md) |
| MAP 4 – Risks of components | Risks and benefits of all components, including third-party data and models, are mapped, together with legal risks such as infringing others' rights. | [Model lineage](../capabilities/metadata/model-lineage.md), [Data lineage](../capabilities/metadata/data-lineage.md), [AI supply chain security](../capabilities/security/ai-supply-chain-security.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Foundation model access](../capabilities/generative-ai/foundation-model-access.md) |
| MAP 5 – Impacts | Likely impacts on individuals, groups, organisations and society are described. | [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md) |
| MEASURE 1 – Methods and metrics | Suitable methods and metrics for AI risks are chosen and applied. | [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md) |
| MEASURE 2 – Evaluation for trustworthy characteristics | Systems are tested for validity, safety, security, explainability, privacy and fairness. | [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md) |
| MEASURE 3 – Tracking risks over time | Identified and emerging risks are tracked in production. | [Model monitoring](../capabilities/mlops/model-monitoring.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md) |
| MEASURE 4 – Feedback on measurement | The effectiveness of measurement is checked with feedback from users and experts. | [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md) |
| MANAGE 1 – Risk response | Mapped and measured risks are prioritised and acted on. | [Model governance](../capabilities/mlops/model-governance.md), [AI governance](../capabilities/governance/ai-governance.md) |
| MANAGE 2 – Maximising benefit and minimising harm | Strategies are in place to sustain value and to disengage or deactivate systems that behave outside their intended use. | [Human oversight of AI](../capabilities/governance/human-oversight.md), [Model release strategies](../capabilities/mlops/model-release-strategies.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [Model deployment](../capabilities/mlops/model-deployment.md) |
| MANAGE 3 – Third-party risk monitoring | Risks from third-party models and components, including pre-trained models, are monitored and controlled. | [AI supply chain security](../capabilities/security/ai-supply-chain-security.md), [AI gateway](../capabilities/generative-ai/ai-gateway.md), [Model monitoring](../capabilities/mlops/model-monitoring.md), [Foundation model access](../capabilities/generative-ai/foundation-model-access.md) |
| MANAGE 4 – Response, recovery and communication | Plans for monitoring, appeal and override, incident response, recovery and communication are documented and followed. | [AI incident management](../capabilities/governance/ai-incident-management.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Model monitoring](../capabilities/mlops/model-monitoring.md), [Model registry](../capabilities/machine-learning/model-registry.md) |
| Generative AI Profile (NIST AI 600-1) | Applies the framework to risks specific to generative AI, such as confabulation, data leakage and harmful content, with emphasis on testing before release, content provenance and incident disclosure. | [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md), [AI content marking and provenance](../capabilities/generative-ai/ai-content-provenance.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md), [AI incident management](../capabilities/governance/ai-incident-management.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md) |

# Related frameworks

- [ISO/IEC 42001:2023](framework-iso-iec-42001.md): The international standard for an AI management system, setting requirements for governing AI responsibly within an organisation.
- [EU AI Act](framework-eu-ai-act.md): Regulation (EU) 2024/1689, which sets risk-based rules for placing AI systems and general-purpose AI models on the EU market and using them.

# Applies to

- [Agentic process automation](../use-cases/usecase-agentic-automation.md) (use case): AI agents complete multi-step business tasks using enterprise data and tools under controls.
- [Knowledge assistant](../use-cases/usecase-rag-assistant.md) (use case): A generative AI assistant that answers questions from internal documents, with citations.
- [Credit decisioning](../use-cases/usecase-credit-decisioning.md) (use case): Score credit applications and decide to approve, decline or refer them, with reasons, fairness checks and model risk controls.
- [Risk and compliance officer](../personas/persona-risk-compliance.md) (persona): Needs assurance, with evidence, that data controls meet regulatory and internal requirements.
- [AI engineer](../personas/persona-ai-engineer.md) (persona): Builds applications and agents on foundation models and enterprise data.
- [ML engineer](../personas/persona-ml-engineer.md) (persona): Takes models to production and keeps them running reliably.
