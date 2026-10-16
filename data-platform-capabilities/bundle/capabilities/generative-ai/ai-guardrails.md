---
type: Capability
id: ai-guardrails
title: AI guardrails
description: Check model inputs, outputs and agent tool calls against policy to block harmful content, data leakage, prompt injection and disallowed actions.
aliases: [content safety, content filters, prompt shields, safety filters]
broader: [generative-ai]
related: [data-loss-prevention, ai-red-teaming, ai-gateway, data-classification, deidentification]
tags: [generative-ai]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Guardrails are checks placed around the model. Input checks look for prompt injection, jailbreak attempts, off-topic requests and sensitive data that should not be sent. Output checks look for harmful content, personal data, leaked secrets, unsupported claims and broken formats. Tool-call checks test each action an agent proposes, such as an email recipient or a refund amount, against rules before it runs. Each check can block, redact, rewrite or send the case to a person. For example, a policy stops a support agent emailing any address outside the customer's record, whatever the conversation says.

Models follow instructions imperfectly, so policies need enforcing outside the model. Checks use rules and patterns, safety and injection classifiers, model-based judges, grounding checks against sources and policy languages evaluated on tool-call parameters. They run in the AI gateway, the application or the agent runtime. Guardrails do not replace permission design: an agent that cannot reach data cannot leak it. Red teaming tests whether guardrails hold.

# Key considerations

- Each check adds latency and false positives. Measure both and tune thresholds per use case.
- Prompt injection detection is unreliable on its own. Combine it with least-privilege tools and approval for risky actions.
- Streamed responses are hard to check before the user sees them. Decide whether to buffer, check in chunks or check afterwards.
- Apply a common baseline policy centrally, with additions for specific use cases, so behaviour is consistent.
- Log blocked events and review them. Patterns reveal attacks and poorly designed prompts.

# Questions to ask

- Which content and data must never appear in inputs or outputs?
- How many wrongly blocked requests will users tolerate?
- Are there sector rules about advice or statements the system must not make?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Generative AI](generative-ai.md) |
| Broader | [Generative AI](generative-ai.md) |
| Related | [AI agents](ai-agents.md), [AI gateway](ai-gateway.md), [AI governance](../governance/ai-governance.md), [AI red teaming](ai-red-teaming.md), [Data classification](../governance/data-classification.md), [Data loss prevention](../security/data-loss-prevention.md), [De-identification](../governance/deidentification.md) |

# Where it appears

- **Use cases:** [Agentic process automation](../../use-cases/usecase-agentic-automation.md) (requires, level 3) · [Conversational analytics for business users](../../use-cases/usecase-conversational-bi.md) (benefits from) · [Document data extraction](../../use-cases/usecase-document-extraction.md) (requires, level 2) · [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (requires, level 3)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md) · [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [AI and model governance](../../maturity/track-ai-governance.md) (from level 2, Managed) · [Generative AI](../../maturity/track-genai.md) (from level 3, Defined)
- **Frameworks:** [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 5 – Prohibited AI practices; Article 14 – Human oversight; Article 15 – Accuracy, robustness and cybersecurity; Article 50 – Transparency obligations · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Annex A.9 – Use of AI systems · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): MEASURE 2 – Evaluation for trustworthy characteristics; MANAGE 2 – Maximising benefit and minimising harm; Generative AI Profile (NIST AI 600-1)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Bedrock Guardrails; AgentCore Policy | [Amazon Bedrock AgentCore Policy](../../technologies/aws/aws-bedrock-agentcore-policy.md), [Amazon Bedrock Guardrails](../../technologies/aws/aws-bedrock-guardrails.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Guardrails and controls (formerly content filters) | [Azure AI Content Safety](../../technologies/microsoft/azure-ai-content-safety.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Model Armor | [Google Cloud Agent Gateway](../../technologies/google-cloud/gcp-agent-gateway.md), [Model Armor](../../technologies/google-cloud/gcp-model-armor.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Cortex AI Guardrails](../../technologies/snowflake/snowflake-cortex-ai-guardrails.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Unity Gateway](../../technologies/databricks/databricks-unity-gateway.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Generative AI (OCI Enterprise AI)](../../technologies/oracle/oracle-oci-generative-ai.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP AI Foundation (SAP AI Core and generative AI hub)](../../technologies/sap/sap-ai-foundation.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Enterprise AgentStack](../../technologies/teradata/teradata-agentstack.md) (preview) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx Orchestrate](../../technologies/ibm/ibm-watsonx-orchestrate.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Microsoft Presidio](../../technologies/open-source/presidio.md), [NeMo Guardrails](../../technologies/open-source/nemo-guardrails.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Bigeye AI Trust Platform](../../technologies/independent/bigeye.md), [Dataiku LLM Mesh](../../technologies/independent/dataiku-llm-mesh.md), [Fiddler AI Control Plane](../../technologies/independent/fiddler-ai-control-plane.md), [Protegrity Data Security Platform](../../technologies/independent/protegrity-data-security-platform.md), [Securiti DataAI Command Platform](../../technologies/independent/securiti-dataai-command-platform.md), [Skyflow Data Privacy Vault](../../technologies/independent/skyflow-data-privacy-vault.md), [Splunk Agent Observability](../../technologies/independent/galileo.md) |
