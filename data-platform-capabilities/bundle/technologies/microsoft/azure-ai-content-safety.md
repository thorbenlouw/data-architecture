---
type: Technology
id: azure-ai-content-safety
title: Azure AI Content Safety
description: Classifies text and images for harmful content and detects prompt injection, jailbreaks and ungrounded output, used by Foundry guardrails.
aliases: [Prompt Shields]
platform: platform-microsoft
kind: managed-service
availability: ga
realises: [ai-guardrails]
resource: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Part of Foundry Tools. Guardrails for models are GA in Foundry; guardrails for agents are preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) (Generative AI) (primary): Check model inputs, outputs and agent tool calls against policy to block harmful content, data leakage, prompt injection and disallowed actions.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Foundry Tools

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore Policy](../aws/aws-bedrock-agentcore-policy.md), [Amazon Bedrock Guardrails](../aws/aws-bedrock-guardrails.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Model Armor](../google-cloud/gcp-model-armor.md), [Google Cloud Agent Gateway](../google-cloud/gcp-agent-gateway.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Guardrails](../snowflake/snowflake-cortex-ai-guardrails.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Gateway](../databricks/databricks-unity-gateway.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise AgentStack](../teradata/teradata-agentstack.md) (preview) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [NeMo Guardrails](../open-source/nemo-guardrails.md), [Microsoft Presidio](../open-source/presidio.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Dataiku LLM Mesh](../independent/dataiku-llm-mesh.md), [Splunk Agent Observability](../independent/galileo.md), [Skyflow Data Privacy Vault](../independent/skyflow-data-privacy-vault.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
