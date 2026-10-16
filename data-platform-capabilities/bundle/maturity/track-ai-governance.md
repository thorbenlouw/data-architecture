---
type: Maturity Track
id: track-ai-governance
title: AI and model governance
description: How well the organisation knows its AI systems, assesses their risks and impacts, controls their behaviour and evidences this to regulators and customers.
covers:
- ai-governance
- ai-system-discovery
- ai-impact-assessment
- ai-incident-management
- model-governance
- ai-guardrails
- genai-evaluation
- ai-red-teaming
- fairness-assessment
- model-explainability
- human-oversight
- agent-registry
- ai-content-provenance
- ai-supply-chain-security
related_tracks: [track-mlops, track-ml-development, track-genai]
levels:
- level: 1
  name: Initial
  summary: AI use is unrecorded, approval is informal, and only builders check model behaviour.
  criteria:
  - Nobody holds a complete list of the models, agents and AI features in use, including those inside purchased software.
  - Approval of AI use, where it happens, is a one-off email or meeting with no recorded criteria.
  - Model behaviour is checked only by the people who built it, and mainly for accuracy.
  capabilities: []
- level: 2
  name: Managed
  summary: In-house AI systems are inventoried with risk ratings, and basic evaluation and filtering are required.
  criteria:
  - An inventory lists in-house AI systems with owner, purpose and risk rating.
  - An AI policy lists prohibited uses and the uses that need review.
  - The AI policy states which content categories applications must block, and each generative application's filter settings are recorded against it.
  - Models and applications that affect people are evaluated on a test set before release, and results are filed with the system.
  capabilities: [ai-governance, model-governance, ai-guardrails, genai-evaluation]
- level: 3
  name: Defined
  summary: A documented AI management process covers discovery, impact assessment, explainability, fairness, agent registration and checks on third-party AI components.
  criteria:
  - AI systems, including features in purchased software and unapproved tools, are discovered from network, identity and spend data and added to the inventory.
  - The approval record for each model that affects people includes its explanation report and fairness results, signed off by the risk or compliance function.
  - Unregistered agents, tools and MCP servers are blocked in production by gateway or network policy, and the registry is reconciled with discovered AI systems monthly.
  - Roles, approvals and documentation follow a written AI management process aligned with ISO/IEC 42001, and higher-risk uses have a recorded impact assessment before release and whenever they change materially.
  - Third-party models, model files, libraries and MCP servers are scanned for tampering and malicious code before use, and each inventory entry lists the models and components the system is built from.
  capabilities:
  - ai-system-discovery
  - ai-impact-assessment
  - model-explainability
  - fairness-assessment
  - agent-registry
  - ai-supply-chain-security
- level: 4
  name: Measured
  summary: Incidents, adversarial findings, human overrides and production risk signals are tracked against thresholds.
  criteria:
  - AI incidents are logged and investigated, and those the law requires are reported to regulators within the deadline.
  - Red-team findings are rated by severity, and a release with an open high-severity finding needs a documented risk acceptance from the system owner.
  - Override and reversal rates from human review of automated decisions are reported per system, and a rising rate triggers a review of that system.
  - Tests confirm that synthetic content released externally carries detectable marks, and the results are kept as evidence for transparency obligations.
  - Fairness metrics, guardrail block rates and evaluation scores in production are monitored against thresholds per system.
  capabilities: [ai-incident-management, ai-red-teaming, human-oversight, ai-content-provenance]
- level: 5
  name: Optimising
  summary: Risk ratings and controls are reassessed from monitoring evidence, and evidence for regulators is produced on demand.
  criteria:
  - Risk ratings and controls are reassessed automatically when monitoring shows drift, incidents or a change of use.
  - Lessons from incidents and audits update policies, evaluation sets and guardrails, and the changes are tracked.
  - Evidence for regulators and customers is generated from the inventory and monitoring data on demand.
  capabilities: []
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up means every model, agent and AI service in use is inventoried with an owner and risk rating, higher-risk systems are assessed, tested and overseen before and after release, and incidents are handled and reported. Level 3 corresponds to the documented AI management system that ISO/IEC 42001 certifies, and levels 4 and 5 add the measurement, monitoring and continual improvement expected by the Measure and Manage functions of the NIST AI RMF and by EU AI Act duties such as post-market monitoring and serious incident reporting. Typical blockers are AI arriving through SaaS features and staff tools rather than projects, risk reviews done once at approval, and evaluation that stops at accuracy.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

AI use is unrecorded, approval is informal, and only builders check model behaviour.

- Nobody holds a complete list of the models, agents and AI features in use, including those inside purchased software.
- Approval of AI use, where it happens, is a one-off email or meeting with no recorded criteria.
- Model behaviour is checked only by the people who built it, and mainly for accuracy.

## Level 2: Managed

In-house AI systems are inventoried with risk ratings, and basic evaluation and filtering are required.

- An inventory lists in-house AI systems with owner, purpose and risk rating.
- An AI policy lists prohibited uses and the uses that need review.
- The AI policy states which content categories applications must block, and each generative application's filter settings are recorded against it.
- Models and applications that affect people are evaluated on a test set before release, and results are filed with the system.

**Capabilities first relied on:** [AI governance](../capabilities/governance/ai-governance.md), [Model governance](../capabilities/mlops/model-governance.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md)

## Level 3: Defined

A documented AI management process covers discovery, impact assessment, explainability, fairness, agent registration and checks on third-party AI components.

- AI systems, including features in purchased software and unapproved tools, are discovered from network, identity and spend data and added to the inventory.
- The approval record for each model that affects people includes its explanation report and fairness results, signed off by the risk or compliance function.
- Unregistered agents, tools and MCP servers are blocked in production by gateway or network policy, and the registry is reconciled with discovered AI systems monthly.
- Roles, approvals and documentation follow a written AI management process aligned with ISO/IEC 42001, and higher-risk uses have a recorded impact assessment before release and whenever they change materially.
- Third-party models, model files, libraries and MCP servers are scanned for tampering and malicious code before use, and each inventory entry lists the models and components the system is built from.

**Capabilities first relied on:** [AI system discovery](../capabilities/governance/ai-system-discovery.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md), [AI supply chain security](../capabilities/security/ai-supply-chain-security.md)

## Level 4: Measured

Incidents, adversarial findings, human overrides and production risk signals are tracked against thresholds.

- AI incidents are logged and investigated, and those the law requires are reported to regulators within the deadline.
- Red-team findings are rated by severity, and a release with an open high-severity finding needs a documented risk acceptance from the system owner.
- Override and reversal rates from human review of automated decisions are reported per system, and a rising rate triggers a review of that system.
- Tests confirm that synthetic content released externally carries detectable marks, and the results are kept as evidence for transparency obligations.
- Fairness metrics, guardrail block rates and evaluation scores in production are monitored against thresholds per system.

**Capabilities first relied on:** [AI incident management](../capabilities/governance/ai-incident-management.md), [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [AI content marking and provenance](../capabilities/generative-ai/ai-content-provenance.md)

## Level 5: Optimising

Risk ratings and controls are reassessed from monitoring evidence, and evidence for regulators is produced on demand.

- Risk ratings and controls are reassessed automatically when monitoring shows drift, incidents or a change of use.
- Lessons from incidents and audits update policies, evaluation sets and guardrails, and the changes are tracked.
- Evidence for regulators and customers is generated from the inventory and monitoring data on demand.

# Capabilities in scope

[Agent and tool registry](../capabilities/generative-ai/agent-registry.md), [AI content marking and provenance](../capabilities/generative-ai/ai-content-provenance.md), [AI governance](../capabilities/governance/ai-governance.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [AI impact assessment](../capabilities/governance/ai-impact-assessment.md), [AI incident management](../capabilities/governance/ai-incident-management.md), [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md), [AI supply chain security](../capabilities/security/ai-supply-chain-security.md), [AI system discovery](../capabilities/governance/ai-system-discovery.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Model governance](../capabilities/mlops/model-governance.md)

# Related tracks

- [MLOps](track-mlops.md): How automatically and safely models are released, run, monitored and improved in production.
- [ML development](track-ml-development.md): How repeatably the organisation turns data into trained, evaluated and documented models.
- [Generative AI](track-genai.md): How safely and reliably the organisation builds, evaluates and runs applications that use language models and agents with its own data.

Levels follow the shared [maturity scale](maturity-scale.md).
