---
type: Capability
id: ai-gateway
title: AI gateway
description: Route, secure, rate-limit and track model calls across providers from one place.
aliases: [LLM gateway, model router]
broader: [foundation-model-access]
related: [ai-spend-controls, ai-guardrails, genai-observability, secrets-management, agent-tool-access]
depends_on: [identity-authentication]
tags: [generative-ai]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

An AI gateway is a proxy between applications and model providers. Because every call passes through it, one component can authenticate the caller, choose the provider and model, enforce request and token limits, retry or switch to another provider on errors, cache repeated responses, redact sensitive fields and record each call with its cost. For example, a support chatbot calls a single endpoint; the gateway sends simple questions to a small, cheap model and harder ones to a larger model, and moves traffic to a second provider when the first starts returning errors.

It becomes necessary once several teams and providers are involved, because otherwise each application handles its own keys, logging and limits differently. It may be an open-source proxy you deploy, a feature of a cloud platform, or an API management product extended for model traffic, and many now also proxy MCP tool calls. A gateway often hosts guardrails and emits traces, but its core job is routing and control rather than content checking or quality measurement.

# Key considerations

- The gateway sits in the path of every call. Its latency and availability become those of every AI application, so run it redundantly and close to callers.
- Providers differ in tool calling, structured output and prompt caching. A lowest-common-denominator interface can hide features teams need.
- Semantic caching, which reuses answers to similar prompts, cuts cost but can return stale answers or another user's content. Scope caches to the user or tenant where permissions differ.
- Logging full prompts and responses creates a sensitive data store. Apply masking, access control and retention to it.
- Holding provider keys in the gateway means application teams never handle them, and keys can be rotated in one place.

# Questions to ask

- How many model providers and AI applications are in use or planned?
- Who needs AI usage and cost broken down by team or application, and how often?
- Is failover between providers or regions required?
- Should agent tool traffic also pass through central control?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Generative AI](generative-ai.md) |
| Broader | [Foundation model access](foundation-model-access.md) |
| Related | [Agent tool and data access](agent-tool-access.md), [AI governance](../governance/ai-governance.md), [AI guardrails](ai-guardrails.md), [AI system discovery](../governance/ai-system-discovery.md), [AI usage and spend controls](../platform-operations/ai-spend-controls.md), [Generative AI observability](genai-observability.md), [Generative model serving](../mlops/generative-model-serving.md), [Network security](../security/network-security.md), [Secrets management](../security/secrets-management.md) |
| Depends on | [Identity and authentication](../security/identity-authentication.md) |
| Needed by | [AI usage and spend controls](../platform-operations/ai-spend-controls.md) |

# Where it appears

- **Use cases:** [Agentic process automation](../../use-cases/usecase-agentic-automation.md) (benefits from) · [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (benefits from)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md)
- **Maturity tracks:** [Generative AI](../../maturity/track-genai.md) (from level 3, Defined)
- **Frameworks:** [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Annex A.10 – Third-party and customer relationships · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): GOVERN 6 – Third-party risk; MANAGE 3 – Third-party risk monitoring

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Bedrock AgentCore Gateway](../../technologies/aws/aws-bedrock-agentcore-gateway.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure API Management](../../technologies/microsoft/azure-api-management.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Agent Gateway | [Apigee](../../technologies/google-cloud/gcp-apigee.md), [Google Cloud Agent Gateway](../../technologies/google-cloud/gcp-agent-gateway.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Cortex AI Gateway](../../technologies/snowflake/snowflake-cortex-ai-gateway.md) (preview) |
| [Databricks](../../platforms/platform-databricks.md) | Unity Gateway | [Unity Gateway](../../technologies/databricks/databricks-unity-gateway.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Generative AI (OCI Enterprise AI)](../../technologies/oracle/oracle-oci-generative-ai.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP AI Foundation (SAP AI Core and generative AI hub)](../../technologies/sap/sap-ai-foundation.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir AIP and AIP Model Catalog](../../technologies/palantir/palantir-aip.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | LLM Mesh | [Dataiku LLM Mesh](../../technologies/dataiku/dataiku-llm-mesh.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [LiteLLM](../../technologies/open-source/litellm.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Kong Konnect](../../technologies/independent/kong-konnect.md), [LangSmith](../../technologies/independent/langsmith.md), [Redpanda Agentic Data Plane](../../technologies/independent/redpanda-agentic-data-plane.md) (unconfirmed) |
