---
type: Technology
id: gcp-model-armor
title: Model Armor
description: Screens prompts and responses for prompt injection, jailbreaks, harmful content, malicious URLs and sensitive data, for any model or agent.
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [ai-guardrails, data-loss-prevention]
resource: https://docs.cloud.google.com/model-armor/overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Integrates with Agent Gateway, Apigee, Gemini Enterprise, Google Cloud MCP servers and networking services, and uses Sensitive Data Protection for sensitive-data detection. Image screening is in preview. Also sold within Security Command Center.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) (Generative AI) (primary): Check model inputs, outputs and agent tool calls against policy to block harmful content, data leakage, prompt injection and disallowed actions.
- [Data loss prevention](../../capabilities/security/data-loss-prevention.md) (Security and access): Detect and block sensitive data leaving approved boundaries.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock Guardrails](../aws/aws-bedrock-guardrails.md), [Amazon Bedrock AgentCore Policy](../aws/aws-bedrock-agentcore-policy.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md), [Data loss prevention](../../capabilities/security/data-loss-prevention.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure AI Content Safety](../microsoft/azure-ai-content-safety.md), [Microsoft Purview Data Loss Prevention](../microsoft/purview-data-loss-prevention.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md), [Data loss prevention](../../capabilities/security/data-loss-prevention.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Guardrails](../snowflake/snowflake-cortex-ai-guardrails.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Gateway](../databricks/databricks-unity-gateway.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise AgentStack](../teradata/teradata-agentstack.md) (preview) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [NeMo Guardrails](../open-source/nemo-guardrails.md), [Microsoft Presidio](../open-source/presidio.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Dataiku LLM Mesh](../independent/dataiku-llm-mesh.md), [Splunk Agent Observability](../independent/galileo.md), [Skyflow Data Privacy Vault](../independent/skyflow-data-privacy-vault.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
