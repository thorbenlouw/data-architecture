---
type: Capability
id: human-oversight
title: Human oversight of AI
description: Route model and agent decisions to people for review, approval or override, and let them pause or stop a system.
aliases: [human in the loop, HITL]
broader: [ai-governance, ai-agents]
related: [ai-impact-assessment, ai-incident-management, genai-evaluation, agent-runtime, audit-logging]
tags: [governance]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Oversight places people at defined points in an AI system's work. Approval gates hold an action until someone accepts it. Review queues collect low-confidence or high-impact outputs for checking. Override lets a reviewer change a decision, and stop controls pause an agent or switch a feature off. For example, a refunds agent may issue refunds under 50 pounds directly, but larger ones wait in a queue that shows the customer's history and the agent's reasoning, so an operator can approve or reject them.

It is the main control for irreversible actions and for decisions that affect people's rights, and the EU AI Act requires effective human oversight of high-risk systems. Patterns include approving every action, monitoring with the power to intervene, and reviewing a sample after the fact. The design problem is avoiding rubber-stamping: reviewers need context, time and the authority to say no. Evaluation tests a system before release and guardrails apply automated checks; oversight puts a person's judgement into the live flow.

# Key considerations

- Set review thresholds by impact and reversibility rather than reviewing everything. Too many approvals train people to click accept.
- Show reviewers the inputs, sources and reasoning, not only the proposed action.
- The agent runtime must be able to pause durably while waiting for a decision, sometimes for days.
- Record every review decision. Decisions are audit evidence and also labelled examples for evaluation.
- Test that the stop control works, and agree who may use it.

# Questions to ask

- Which decisions or actions are irreversible or affect people's rights or money?
- Who has the authority and time to review, and how quickly must they respond?
- Which regulations require documented human oversight for the intended uses?
- How will you detect reviewers approving without checking?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Governance and compliance](governance.md) |
| Broader | [AI governance](ai-governance.md), [AI agents](../generative-ai/ai-agents.md) |
| Related | [Agent hosting and runtime](../generative-ai/agent-runtime.md), [AI impact assessment](ai-impact-assessment.md), [AI incident management](ai-incident-management.md), [Audit logging](../security/audit-logging.md), [Data engineering agents](../development-lifecycle/data-engineering-agents.md), [Decision management](../serving/decision-management.md), [Generative AI evaluation](../generative-ai/genai-evaluation.md), [Model explainability](../machine-learning/model-explainability.md) |

# Where it appears

- **Use cases:** [Agentic process automation](../../use-cases/usecase-agentic-automation.md) (requires, level 3) · [Credit decisioning](../../use-cases/usecase-credit-decisioning.md) (requires, level 2) · [Document data extraction](../../use-cases/usecase-document-extraction.md) (requires, level 3) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (requires, level 2)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md) · [Risk and compliance officer](../../personas/persona-risk-compliance.md)
- **Maturity tracks:** [AI and model governance](../../maturity/track-ai-governance.md) (from level 4, Measured) · [Generative AI](../../maturity/track-genai.md) (from level 4, Measured)
- **Frameworks:** [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 14 – Human oversight; Article 26 – Obligations of deployers; Article 27 – Fundamental rights impact assessment · [GDPR](../../frameworks/framework-gdpr.md): Article 22 – Automated individual decision-making · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Annex A.9 – Use of AI systems · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): MAP 2 – Categorisation; MAP 3 – Benefits and costs; MANAGE 2 – Maximising benefit and minimising harm; MANAGE 4 – Response, recovery and communication

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric operations agent](../../technologies/microsoft/fabric-operations-agent.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Joule Studio](../../technologies/sap/sap-joule-studio.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Enterprise AgentStack](../../technologies/teradata/teradata-agentstack.md) (preview), [Teradata Tera](../../technologies/teradata/teradata-tera.md) (preview) |
| [Palantir](../../platforms/platform-palantir.md) |  | [AIP Logic and AIP Evals](../../technologies/palantir/palantir-aip-logic.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku Visual Agents and Code Agents](../../technologies/dataiku/dataiku-agents.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [LangGraph](../../technologies/open-source/langgraph.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Matillion Maia](../../technologies/independent/matillion-maia.md) |
