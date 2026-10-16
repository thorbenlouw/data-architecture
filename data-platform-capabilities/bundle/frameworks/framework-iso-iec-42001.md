---
type: Framework
id: framework-iso-iec-42001
title: ISO/IEC 42001:2023
description: The international standard for an AI management system, setting requirements for governing AI responsibly within an organisation.
aliases: [ISO 42001, ISO/IEC 42001, AIMS, AI management system standard]
kind: standard
publisher: ISO and IEC (JTC 1/SC 42)
resource: https://www.iso.org/standard/42001
related: [framework-eu-ai-act, framework-nist-ai-rmf]
applies_to:
- usecase-agentic-automation
- usecase-rag-assistant
- usecase-credit-decisioning
- persona-risk-compliance
- persona-cdo
- persona-ai-engineer
- persona-ml-engineer
mappings:
- ref: Clause 4 – Context of the organisation
  summary: Define the scope of the AI management system, including which AI systems it covers, and the organisation's roles as an AI provider, producer or user.
  capabilities: [ai-governance, ai-system-discovery, agent-registry]
- ref: Clause 5 – Leadership
  summary: Top management sets an AI policy and assigns responsibilities.
  capabilities: [ai-governance, data-policy-management, model-governance]
- ref: Clause 6 – Planning
  summary: Assess and treat AI risks, carry out AI system impact assessments and set AI objectives.
  capabilities: [ai-impact-assessment, ai-governance, model-governance, fairness-assessment]
- ref: Clause 7 – Support
  summary: Provide resources, competence, awareness and controlled documentation for the management system.
  capabilities: [ai-governance, model-governance, compliance-evidence]
- ref: Clause 8 – Operation
  summary: Plan and control the processes that develop and run AI systems, and repeat risk and impact assessments as systems change.
  capabilities: [model-governance, ml-cicd, ai-impact-assessment, ai-governance]
- ref: Clause 9 – Performance evaluation
  summary: Monitor and measure the management system, audit it internally and review it with management.
  capabilities: [compliance-evidence, governance-metrics, model-monitoring]
- ref: Clause 10 – Improvement
  summary: Correct nonconformities, find their causes and improve the management system continually.
  capabilities: [ai-incident-management, compliance-evidence, ai-governance]
- ref: Annex A.2 – Policies related to AI
  summary: Document and review AI policies and align them with other organisational policies.
  capabilities: [ai-governance, data-policy-management]
- ref: Annex A.3 – Internal organisation
  summary: Define roles and responsibilities for AI and a way to report concerns.
  capabilities: [ai-governance, model-governance, data-ownership]
- ref: Annex A.4 – Resources for AI systems
  summary: Document the data, tools, computing resources and people that each AI system depends on.
  capabilities:
  - model-governance
  - agent-registry
  - ai-supply-chain-security
  - training-dataset-management
  - data-catalogue
  - compute-options
- ref: Annex A.5 – Assessing impacts of AI systems
  summary: Assess and document the effects of AI systems on individuals, groups and society.
  capabilities: [ai-impact-assessment, fairness-assessment, privacy-impact-assessment]
- ref: Annex A.6 – AI system life cycle
  summary: Manage AI systems through design, verification, deployment, operation and monitoring with documented criteria and event logs.
  capabilities: [model-registry, model-evaluation, ml-cicd, model-deployment, model-monitoring, inference-logging]
- ref: Annex A.7 – Data for AI systems
  summary: Manage data for AI, covering acquisition, quality, provenance and preparation.
  capabilities:
  - training-dataset-management
  - data-lineage
  - data-quality-rules
  - data-profiling
  - data-labelling
  - data-usage-rights
  - model-lineage
  - data-catalogue
- ref: Annex A.8 – Information for interested parties
  summary: Give users and others the information they need about AI systems, including how to report problems and how incidents are communicated.
  capabilities: [model-explainability, model-governance, ai-incident-management]
- ref: Annex A.9 – Use of AI systems
  summary: Make sure AI systems are used responsibly and according to their intended use.
  capabilities: [ai-guardrails, human-oversight, model-monitoring, ai-governance]
- ref: Annex A.10 – Third-party and customer relationships
  summary: Allocate responsibilities with suppliers and customers and manage risk from third-party AI components.
  capabilities: [ai-supply-chain-security, ai-gateway, foundation-model-access]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ISO/IEC 42001 was published in December 2023 (edition 1, no revision listed as of October 2026) and is a certifiable management system standard, built on the same structure as ISO/IEC 27001. Organisations that develop, provide or use AI adopt it to show auditors and customers that AI risk, impact and lifecycle are governed, and it is often used alongside the EU AI Act and the NIST AI RMF. Clauses 4 to 10 set the management system requirements, and Annex A lists reference controls whose objectives map well onto platform capabilities for data, lifecycle, monitoring and third parties. Certification is carried out by independent bodies, not by ISO.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Mapping to capabilities

| Area | Summary | Capabilities |
|---|---|---|
| Clause 4 – Context of the organisation | Define the scope of the AI management system, including which AI systems it covers, and the organisation's roles as an AI provider, producer or user. | [AI governance](../capabilities/governance/ai-governance.md), [AI system discovery](../capabilities/governance/ai-system-discovery.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md) |
| Clause 5 – Leadership | Top management sets an AI policy and assigns responsibilities. | [AI governance](../capabilities/governance/ai-governance.md), [Policy management](../capabilities/governance/data-policy-management.md), [Model governance](../capabilities/mlops/model-governance.md) |
| Clause 6 – Planning | Assess and treat AI risks, carry out AI system impact assessments and set AI objectives. | [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [AI governance](../capabilities/governance/ai-governance.md), [Model governance](../capabilities/mlops/model-governance.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md) |
| Clause 7 – Support | Provide resources, competence, awareness and controlled documentation for the management system. | [AI governance](../capabilities/governance/ai-governance.md), [Model governance](../capabilities/mlops/model-governance.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) |
| Clause 8 – Operation | Plan and control the processes that develop and run AI systems, and repeat risk and impact assessments as systems change. | [Model governance](../capabilities/mlops/model-governance.md), [CI/CD for machine learning](../capabilities/mlops/ml-cicd.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [AI governance](../capabilities/governance/ai-governance.md) |
| Clause 9 – Performance evaluation | Monitor and measure the management system, audit it internally and review it with management. | [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md), [Model monitoring](../capabilities/mlops/model-monitoring.md) |
| Clause 10 – Improvement | Correct nonconformities, find their causes and improve the management system continually. | [AI incident management](../capabilities/governance/ai-incident-management.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [AI governance](../capabilities/governance/ai-governance.md) |
| Annex A.2 – Policies related to AI | Document and review AI policies and align them with other organisational policies. | [AI governance](../capabilities/governance/ai-governance.md), [Policy management](../capabilities/governance/data-policy-management.md) |
| Annex A.3 – Internal organisation | Define roles and responsibilities for AI and a way to report concerns. | [AI governance](../capabilities/governance/ai-governance.md), [Model governance](../capabilities/mlops/model-governance.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md) |
| Annex A.4 – Resources for AI systems | Document the data, tools, computing resources and people that each AI system depends on. | [Model governance](../capabilities/mlops/model-governance.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md), [AI supply chain security](../capabilities/security/ai-supply-chain-security.md), [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md), [Data catalogue](../capabilities/metadata/data-catalogue.md), [Compute provisioning options](../capabilities/compute/compute-options.md) |
| Annex A.5 – Assessing impacts of AI systems | Assess and document the effects of AI systems on individuals, groups and society. | [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Privacy impact assessment](../capabilities/governance/privacy-impact-assessment.md) |
| Annex A.6 – AI system life cycle | Manage AI systems through design, verification, deployment, operation and monitoring with documented criteria and event logs. | [Model registry](../capabilities/machine-learning/model-registry.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [CI/CD for machine learning](../capabilities/mlops/ml-cicd.md), [Model deployment](../capabilities/mlops/model-deployment.md), [Model monitoring](../capabilities/mlops/model-monitoring.md), [Inference logging](../capabilities/mlops/inference-logging.md) |
| Annex A.7 – Data for AI systems | Manage data for AI, covering acquisition, quality, provenance and preparation. | [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md), [Data lineage](../capabilities/metadata/data-lineage.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Data profiling](../capabilities/data-quality/data-profiling.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Model lineage](../capabilities/metadata/model-lineage.md), [Data catalogue](../capabilities/metadata/data-catalogue.md) |
| Annex A.8 – Information for interested parties | Give users and others the information they need about AI systems, including how to report problems and how incidents are communicated. | [Model explainability](../capabilities/machine-learning/model-explainability.md), [Model governance](../capabilities/mlops/model-governance.md), [AI incident management](../capabilities/governance/ai-incident-management.md) |
| Annex A.9 – Use of AI systems | Make sure AI systems are used responsibly and according to their intended use. | [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Model monitoring](../capabilities/mlops/model-monitoring.md), [AI governance](../capabilities/governance/ai-governance.md) |
| Annex A.10 – Third-party and customer relationships | Allocate responsibilities with suppliers and customers and manage risk from third-party AI components. | [AI supply chain security](../capabilities/security/ai-supply-chain-security.md), [AI gateway](../capabilities/generative-ai/ai-gateway.md), [Foundation model access](../capabilities/generative-ai/foundation-model-access.md) |

# Related frameworks

- [EU AI Act](framework-eu-ai-act.md): Regulation (EU) 2024/1689, which sets risk-based rules for placing AI systems and general-purpose AI models on the EU market and using them.
- [NIST AI Risk Management Framework (AI RMF 1.0)](framework-nist-ai-rmf.md): A voluntary framework for managing AI risk through four functions, Govern, Map, Measure and Manage, broken into categories and subcategories of outcomes.

# Applies to

- [Agentic process automation](../use-cases/usecase-agentic-automation.md) (use case): AI agents complete multi-step business tasks using enterprise data and tools under controls.
- [Knowledge assistant](../use-cases/usecase-rag-assistant.md) (use case): A generative AI assistant that answers questions from internal documents, with citations.
- [Credit decisioning](../use-cases/usecase-credit-decisioning.md) (use case): Score credit applications and decide to approve, decline or refer them, with reasons, fairness checks and model risk controls.
- [Risk and compliance officer](../personas/persona-risk-compliance.md) (persona): Needs assurance, with evidence, that data controls meet regulatory and internal requirements.
- [Chief data officer](../personas/persona-cdo.md) (persona): Accountable for the organisation's data strategy, value, risk and governance.
- [AI engineer](../personas/persona-ai-engineer.md) (persona): Builds applications and agents on foundation models and enterprise data.
- [ML engineer](../personas/persona-ml-engineer.md) (persona): Takes models to production and keeps them running reliably.
