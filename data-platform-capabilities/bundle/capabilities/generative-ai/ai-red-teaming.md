---
type: Capability
id: ai-red-teaming
title: AI red teaming
description: Probe models and agents adversarially for prompt injection, jailbreaks and unsafe behaviour before and after release.
broader: [genai-evaluation]
related: [ai-guardrails, ai-incident-management, ai-impact-assessment, agent-tool-access]
tags: [generative-ai]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Red teaming tries deliberately to make a system misbehave. Testers, increasingly helped by automated attack tools, attempt jailbreaks that bypass safety instructions, prompt injection through documents or tool results, extraction of system prompts or other users' data, generation of harmful content and misuse of agent tools. Findings lead to fixes in prompts, guardrails, permissions and tool design. For example, testers plant an instruction in a supplier PDF telling the assistant to email the contract to an outside address, and check whether the agent tries to do it.

Generative systems have weaknesses that ordinary penetration testing does not cover, because the model treats any text it reads as possible instructions. Approaches include expert-led exercises before launch, automated scans with libraries of attack prompts on every change, and continued testing after release as models and tools change. Frameworks such as the OWASP Top 10 for LLM applications and MITRE ATLAS help structure coverage. Evaluation measures quality under expected use; red teaming looks for failure under hostile use.

# Key considerations

- Test the whole system with its tools and data, not the model alone. The most serious findings usually involve what the agent can reach.
- Repeat testing after every model change. Safety behaviour differs between model versions.
- Automated attack libraries find known patterns; experts find weaknesses specific to your system. Use both.
- Turn each finding into a regression test so it stays fixed.

# Questions to ask

- What is the worst thing the system could do or reveal if misused?
- Does it read untrusted content such as emails, web pages or uploaded files?
- Do regulators or customers expect evidence of adversarial testing?
- Who will fix findings, and how quickly?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Generative AI](generative-ai.md) |
| Broader | [Generative AI evaluation](genai-evaluation.md) |
| Related | [Agent tool and data access](agent-tool-access.md), [AI guardrails](ai-guardrails.md), [AI impact assessment](../governance/ai-impact-assessment.md), [AI incident management](../governance/ai-incident-management.md) |

# Where it appears

- **Use cases:** [Agentic process automation](../../use-cases/usecase-agentic-automation.md) (benefits from) · [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (benefits from)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md)
- **Maturity tracks:** [AI and model governance](../../maturity/track-ai-governance.md) (from level 4, Measured) · [Generative AI](../../maturity/track-genai.md) (from level 4, Measured)
- **Frameworks:** [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 9 – Risk management system; Article 15 – Accuracy, robustness and cybersecurity · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): GOVERN 4 – Risk culture; MEASURE 2 – Evaluation for trustworthy characteristics; Generative AI Profile (NIST AI 600-1)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Foundry evaluations](../../technologies/microsoft/azure-foundry-evaluations.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Holistic AI Governance Platform](../../technologies/independent/holistic-ai-governance-platform.md), [Scale Data Engine](../../technologies/independent/scale-data-engine.md) |
