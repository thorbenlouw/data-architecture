---
type: Technology
id: aws-bedrock-agentcore-policy
title: Amazon Bedrock AgentCore Policy
description: Deterministic rules, written in natural language or a Cedar-compatible language, that decide which tools an agent may call and with which parameters.
aliases: [AgentCore Policy]
platform: platform-aws
kind: feature
availability: ga
realises: [ai-guardrails, agent-tool-access, agent-identity]
resource: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA March 2026. Enforced at the Gateway outside the agent's code, so the agent cannot reason around it; can also apply Bedrock Guardrails to tool inputs and outputs.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) (Generative AI) (primary): Check model inputs, outputs and agent tool calls against policy to block harmful content, data leakage, prompt injection and disallowed actions.
- [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) (Generative AI): Give agents governed access to data and actions through tools and protocols such as MCP.
- [Agent identity and authorisation](../../capabilities/generative-ai/agent-identity.md) (Generative AI): Give each agent its own identity and scoped, short-lived access to data on behalf of named users, enforced at request time.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon Bedrock AgentCore

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure AI Content Safety](../microsoft/azure-ai-content-safety.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Gateway](../google-cloud/gcp-agent-gateway.md), [Model Armor](../google-cloud/gcp-model-armor.md) | [Agent identity and authorisation](../../capabilities/generative-ai/agent-identity.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Guardrails](../snowflake/snowflake-cortex-ai-guardrails.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Gateway](../databricks/databricks-unity-gateway.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise AgentStack](../teradata/teradata-agentstack.md) (preview) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [NeMo Guardrails](../open-source/nemo-guardrails.md), [Microsoft Presidio](../open-source/presidio.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Dataiku LLM Mesh](../independent/dataiku-llm-mesh.md), [Splunk Agent Observability](../independent/galileo.md), [Skyflow Data Privacy Vault](../independent/skyflow-data-privacy-vault.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
