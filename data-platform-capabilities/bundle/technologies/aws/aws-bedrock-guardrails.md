---
type: Technology
id: aws-bedrock-guardrails
title: Amazon Bedrock Guardrails
description: Configurable filters that check model inputs and outputs for harmful content, denied topics, banned words, personal data, ungrounded answers and rule violations.
platform: platform-aws
kind: feature
availability: ga
realises: [ai-guardrails, deidentification, data-loss-prevention]
resource: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Includes contextual grounding checks and Automated Reasoning checks against formal rules. The ApplyGuardrail API works with any model, including ones outside Bedrock, and guardrails can be enforced across accounts. AgentCore Policy can apply them at the agent gateway.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) (Generative AI) (primary): Check model inputs, outputs and agent tool calls against policy to block harmful content, data leakage, prompt injection and disallowed actions.
- [De-identification](../../capabilities/governance/deidentification.md) (Governance and compliance): Pseudonymise, tokenise or anonymise data so it can be used with less privacy risk.
- [Data loss prevention](../../capabilities/security/data-loss-prevention.md) (Security and access): Detect and block sensitive data leaving approved boundaries.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon Bedrock

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure AI Content Safety](../microsoft/azure-ai-content-safety.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Model Armor](../google-cloud/gcp-model-armor.md), [Google Cloud Agent Gateway](../google-cloud/gcp-agent-gateway.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md), [Data loss prevention](../../capabilities/security/data-loss-prevention.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Guardrails](../snowflake/snowflake-cortex-ai-guardrails.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Gateway](../databricks/databricks-unity-gateway.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise AgentStack](../teradata/teradata-agentstack.md) (preview) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [NeMo Guardrails](../open-source/nemo-guardrails.md), [Microsoft Presidio](../open-source/presidio.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Skyflow Data Privacy Vault](../independent/skyflow-data-privacy-vault.md), [Protegrity Data Security Platform](../independent/protegrity-data-security-platform.md), [Dataiku LLM Mesh](../independent/dataiku-llm-mesh.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md), [De-identification](../../capabilities/governance/deidentification.md) |
