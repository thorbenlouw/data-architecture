---
type: Use Case
id: usecase-agentic-automation
title: Agentic process automation
description: AI agents complete multi-step business tasks using enterprise data and tools under controls.
aliases: [AI agents for operations, agentic workflows]
requires:
- {capability: agent-tool-access, level: 3, why: 'Agents read data and act in business systems only through governed, described tools.'}
- {capability: agent-runtime, level: 3, why: 'Agents run as managed services with durable state, scaling and sandboxed code execution.'}
- {capability: agent-identity, level: 3, why: 'Each agent has its own identity and acts with scoped, short-lived access on behalf of a named user.'}
- {capability: foundation-model-access, level: 3, why: Planning and reasoning use approved models inside the security boundary.}
- {capability: retrieval-augmented-generation, level: 2, why: Agents ground decisions in current policies and procedures.}
- {capability: human-oversight, level: 3, why: 'High-impact actions need approval, and people must be able to pause or stop agents.'}
- {capability: ai-guardrails, level: 3, why: Inputs and outputs are filtered so injected instructions in emails or documents cannot trigger actions.}
- {capability: genai-evaluation, level: 3, why: Agents are tested on realistic cases for accuracy and safe behaviour before each release.}
- {capability: genai-observability, level: 3, why: 'Every step, tool call and decision is traced for debugging and audit.'}
- {capability: audit-logging, level: 3, why: Actions taken in business systems must be attributable and tamper-evident.}
- {capability: agent-registry, level: 2, why: 'The organisation must know which agents and tools exist, who owns them and what they may do.'}
- {capability: ai-governance, level: 2, why: Each agent needs a risk classification and approval before it acts on real cases.}
- {capability: ai-spend-controls, level: 2, why: 'Step, token and cost limits stop runaway loops.'}
benefits_from:
- {capability: agent-memory, why: Carries context across long-running cases and sessions.}
- {capability: ai-red-teaming, why: Tests agents against manipulation before attackers try.}
- {capability: ai-context-layer, why: Helps agents use structured data and business definitions correctly.}
- {capability: agent-interoperability, why: Lets agents hand work to agents on other platforms.}
- {capability: ai-gateway, why: 'Centralises model routing, quotas and logging across providers.'}
- {capability: prompt-management, why: Versions agent instructions and tool descriptions.}
- {capability: ai-incident-management, why: Records and reports agent malfunctions in a consistent way.}
- {capability: document-processing, why: 'Extracts fields from invoices, claims and forms that agents work on.'}
- {capability: permission-aware-retrieval, why: Keeps agent answers within what the acting user may see.}
- capability: shadow-deployment
  why: Runs a new agent version on real cases with tool calls stubbed, comparing its proposed actions with those of staff or the current version before it acts.
personas:
- persona-ai-engineer
- persona-business-user
- persona-security-officer
- persona-risk-compliance
- persona-platform-engineer
- persona-software-engineer
patterns: []
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Many business processes, such as invoice exceptions, customer onboarding, claims triage, IT requests and supplier queries, involve people reading information from several systems, deciding and taking routine actions. AI agents can do much of this: a model plans the steps, calls tools to read data and documents, takes actions in business systems through governed interfaces, and hands over to a person when a decision exceeds its authority or confidence.

Good looks like a measurable share of cases completed end to end, faster cycle times, every action traceable to the agent and to the person or process it acted for, approvals enforced for high-impact actions, and the ability to pause any agent at once. Agents are released and changed only after evaluation on realistic cases, and incidents are investigated from full traces.

# Non-functional requirements

- Every action is recorded with the agent, the user or process it acted for, its inputs and its outcome.
- Actions above set thresholds, such as payment value, wait for human approval.
- Per-task limits on steps, time and cost are enforced.
- All agents, or any one of them, can be paused within minutes.
- Logs are kept for the audit period that applies to the process.

# Risks

- Injected instructions in emails or documents trigger unauthorised actions.
- Agents hold broad, standing credentials instead of scoped, per-task access.
- Small errors compound over many steps and go unnoticed without evaluation and sampling.
- Processes are automated before accuracy is measured, so mistakes reach customers.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [Agent tool and data access](../capabilities/generative-ai/agent-tool-access.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 3 (Defined) | Agents read data and act in business systems only through governed, described tools. |
| [Agent hosting and runtime](../capabilities/generative-ai/agent-runtime.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 3 (Defined) | Agents run as managed services with durable state, scaling and sandboxed code execution. |
| [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 3 (Defined) | Each agent has its own identity and acts with scoped, short-lived access on behalf of a named user. |
| [Foundation model access](../capabilities/generative-ai/foundation-model-access.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 3 (Defined) | Planning and reasoning use approved models inside the security boundary. |
| [Retrieval-augmented generation](../capabilities/generative-ai/retrieval-augmented-generation.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 2 (Managed) | Agents ground decisions in current policies and procedures. |
| [Human oversight of AI](../capabilities/governance/human-oversight.md) | [Governance and compliance](../capabilities/governance/governance.md) | 3 (Defined) | High-impact actions need approval, and people must be able to pause or stop agents. |
| [AI guardrails](../capabilities/generative-ai/ai-guardrails.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 3 (Defined) | Inputs and outputs are filtered so injected instructions in emails or documents cannot trigger actions. |
| [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 3 (Defined) | Agents are tested on realistic cases for accuracy and safe behaviour before each release. |
| [Generative AI observability](../capabilities/generative-ai/genai-observability.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 3 (Defined) | Every step, tool call and decision is traced for debugging and audit. |
| [Audit logging](../capabilities/security/audit-logging.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Actions taken in business systems must be attributable and tamper-evident. |
| [Agent and tool registry](../capabilities/generative-ai/agent-registry.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 2 (Managed) | The organisation must know which agents and tools exist, who owns them and what they may do. |
| [AI governance](../capabilities/governance/ai-governance.md) | [Governance and compliance](../capabilities/governance/governance.md) | 2 (Managed) | Each agent needs a risk classification and approval before it acts on real cases. |
| [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | 2 (Managed) | Step, token and cost limits stop runaway loops. |

# Capabilities that help

| Capability | Why |
|---|---|
| [Agent memory](../capabilities/generative-ai/agent-memory.md) | Carries context across long-running cases and sessions. |
| [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md) | Tests agents against manipulation before attackers try. |
| [AI context layer](../capabilities/metadata/ai-context-layer.md) | Helps agents use structured data and business definitions correctly. |
| [Agent-to-agent interoperability](../capabilities/generative-ai/agent-interoperability.md) | Lets agents hand work to agents on other platforms. |
| [AI gateway](../capabilities/generative-ai/ai-gateway.md) | Centralises model routing, quotas and logging across providers. |
| [Prompt management](../capabilities/generative-ai/prompt-management.md) | Versions agent instructions and tool descriptions. |
| [AI incident management](../capabilities/governance/ai-incident-management.md) | Records and reports agent malfunctions in a consistent way. |
| [Document processing](../capabilities/processing/document-processing.md) | Extracts fields from invoices, claims and forms that agents work on. |
| [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md) | Keeps agent answers within what the acting user may see. |
| [Shadow deployment](../capabilities/mlops/shadow-deployment.md) | Runs a new agent version on real cases with tool calls stubbed, comparing its proposed actions with those of staff or the current version before it acts. |

# Personas

- [AI engineer](../personas/persona-ai-engineer.md): Builds applications and agents on foundation models and enterprise data.
- [Business user](../personas/persona-business-user.md): Uses data, reports and AI assistants to make decisions, without deep technical skills.
- [Security and privacy officer](../personas/persona-security-officer.md): Protects data and makes sure it is used lawfully.
- [Risk and compliance officer](../personas/persona-risk-compliance.md): Needs assurance, with evidence, that data controls meet regulatory and internal requirements.
- [Data platform engineer](../personas/persona-platform-engineer.md): Builds and runs the shared data platform and its self-service tooling.
- [Software engineer](../personas/persona-software-engineer.md): Builds applications that produce data for the platform or consume data from it.

# Frameworks that apply

- [EU AI Act](../frameworks/framework-eu-ai-act.md): Regulation (EU) 2024/1689, which sets risk-based rules for placing AI systems and general-purpose AI models on the EU market and using them.
- [ISO/IEC 42001:2023](../frameworks/framework-iso-iec-42001.md): The international standard for an AI management system, setting requirements for governing AI responsibly within an organisation.
- [NIST AI Risk Management Framework (AI RMF 1.0)](../frameworks/framework-nist-ai-rmf.md): A voluntary framework for managing AI risk through four functions, Govern, Map, Measure and Manage, broken into categories and subcategories of outcomes.

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 12 of 13 | [Human oversight of AI](../capabilities/governance/human-oversight.md) |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 12 of 13 (+1 in preview) | [Agent and tool registry](../capabilities/generative-ai/agent-registry.md) (preview only) |
| [Google Cloud](../platforms/platform-google-cloud.md) | 12 of 13 | [Human oversight of AI](../capabilities/governance/human-oversight.md) |
| [Snowflake](../platforms/platform-snowflake.md) | 9 of 13 | [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md), [AI governance](../capabilities/governance/ai-governance.md) |
| [Databricks](../platforms/platform-databricks.md) | 10 of 13 (+2 in preview) | [Human oversight of AI](../capabilities/governance/human-oversight.md), [Agent hosting and runtime](../capabilities/generative-ai/agent-runtime.md) (preview only), [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md) (preview only) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 4 of 13 (+1 in preview) | [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [Foundation model access](../capabilities/generative-ai/foundation-model-access.md), [Retrieval-augmented generation](../capabilities/generative-ai/retrieval-augmented-generation.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md), [AI governance](../capabilities/governance/ai-governance.md), [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md), [Agent hosting and runtime](../capabilities/generative-ai/agent-runtime.md) (preview only) |
| [Informatica](../platforms/platform-informatica.md) | 5 of 13 | [Agent hosting and runtime](../capabilities/generative-ai/agent-runtime.md), [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [Foundation model access](../capabilities/generative-ai/foundation-model-access.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md), [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 2 of 13 (+3 in preview) | [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md), [AI governance](../capabilities/governance/ai-governance.md), [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md), [Agent tool and data access](../capabilities/generative-ai/agent-tool-access.md) (preview only), [Agent hosting and runtime](../capabilities/generative-ai/agent-runtime.md) (preview only), [Retrieval-augmented generation](../capabilities/generative-ai/retrieval-augmented-generation.md) (preview only) |
| [Oracle](../platforms/platform-oracle.md) | 6 of 13 | [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md), [AI governance](../capabilities/governance/ai-governance.md), [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md) |
| [SAP](../platforms/platform-sap.md) | 7 of 13 | [Agent hosting and runtime](../capabilities/generative-ai/agent-runtime.md), [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md), [Audit logging](../capabilities/security/audit-logging.md), [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md) |
| [Teradata](../platforms/platform-teradata.md) | 3 of 13 (+5 in preview) | [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [Foundation model access](../capabilities/generative-ai/foundation-model-access.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md), [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md), [Agent hosting and runtime](../capabilities/generative-ai/agent-runtime.md) (preview only), [Human oversight of AI](../capabilities/governance/human-oversight.md) (preview only), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md) (preview only), [Generative AI observability](../capabilities/generative-ai/genai-observability.md) (preview only), [AI governance](../capabilities/governance/ai-governance.md) (preview only) |
| [IBM](../platforms/platform-ibm.md) | 10 of 13 | [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md) |
| [Palantir](../platforms/platform-palantir.md) | 9 of 13 | [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md) |
| [SAS](../platforms/platform-sas.md) | 6 of 13 | [Agent hosting and runtime](../capabilities/generative-ai/agent-runtime.md), [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md), [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md) |
| [Dataiku](../platforms/platform-dataiku.md) | 11 of 13 | [Agent hosting and runtime](../capabilities/generative-ai/agent-runtime.md), [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 10 of 13 | [Agent hosting and runtime](../capabilities/generative-ai/agent-runtime.md), [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md) |
| [Independent vendors](../platforms/platform-independent.md) | 13 of 13 |  |
