---
type: Technology
id: gcp-agent-gateway
title: Google Cloud Agent Gateway
description: Gateway that sits between agents, models and tools to enforce identity, policy, content screening and network controls on agent traffic.
aliases: [Agent Gateway]
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [ai-gateway, agent-tool-access, ai-guardrails, network-security, agent-identity]
resource: https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA June 2026, with Model Armor integration (GA), VPC Service Controls and Cloud Trace. Semantic governance policies, which use a model to judge agent actions against natural-language rules, and the Agent Identity API are in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI gateway](../../capabilities/generative-ai/ai-gateway.md) (Generative AI) (primary): Route, secure, rate-limit and track model calls across providers from one place.
- [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) (Generative AI): Give agents governed access to data and actions through tools and protocols such as MCP.
- [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) (Generative AI): Check model inputs, outputs and agent tool calls against policy to block harmful content, data leakage, prompt injection and disallowed actions.
- [Network security](../../capabilities/security/network-security.md) (Security and access): Keep data traffic on private networks and restrict where the platform can be reached from.
- [Agent identity and authorisation](../../capabilities/generative-ai/agent-identity.md) (Generative AI): Give each agent its own identity and scoped, short-lived access to data on behalf of named users, enforced at request time.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Gemini Enterprise Agent Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore Gateway](../aws/aws-bedrock-agentcore-gateway.md), [Amazon Bedrock AgentCore Policy](../aws/aws-bedrock-agentcore-policy.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [Agent identity and authorisation](../../capabilities/generative-ai/agent-identity.md), [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure API Management](../microsoft/azure-api-management.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Gateway](../snowflake/snowflake-cortex-ai-gateway.md) (preview) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Gateway](../databricks/databricks-unity-gateway.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir AIP and AIP Model Catalog](../palantir/palantir-aip.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku LLM Mesh](../dataiku/dataiku-llm-mesh.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [LiteLLM](../open-source/litellm.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Kong Konnect](../independent/kong-konnect.md), [Redpanda Agentic Data Plane](../independent/redpanda-agentic-data-plane.md) (unconfirmed), [LangSmith](../independent/langsmith.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI gateway](../../capabilities/generative-ai/ai-gateway.md) |
