---
type: Technology
id: snowflake-cortex-ai-gateway
title: Snowflake Cortex AI Gateway
description: A single governed endpoint for AI clients that routes model calls, records traces and token use, and attributes spend to teams and users under budgets and quotas.
platform: platform-snowflake
kind: feature
availability: preview
realises: [ai-gateway, genai-observability, cost-attribution, ai-spend-controls]
resource: https://docs.snowflake.com/user-guide/snowflake-cortex/cortex-ai-gateway
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Preview since September 2026, in AWS commercial regions only. It is a different object from the Snowflake ML GATEWAY, which routes traffic between model-serving endpoints.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI gateway](../../capabilities/generative-ai/ai-gateway.md) (Generative AI) (primary): Route, secure, rate-limit and track model calls across providers from one place.
- [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) (Generative AI): Trace model and agent calls with their prompts, responses, latency, cost and user feedback.
- [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) (Platform operations): Attribute spend to teams, products and workloads using tags and usage data.
- [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) (Platform operations): Limit, prioritise and attribute model and agent consumption per user, team or application.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** preview  
**Product family:** Snowflake Cortex AI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore Gateway](../aws/aws-bedrock-agentcore-gateway.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure API Management](../microsoft/azure-api-management.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Gateway](../google-cloud/gcp-agent-gateway.md), [Apigee](../google-cloud/gcp-apigee.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Gateway](../databricks/databricks-unity-gateway.md), [Databricks budgets](../databricks/databricks-budgets.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md), [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir AIP and AIP Model Catalog](../palantir/palantir-aip.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku LLM Mesh](../dataiku/dataiku-llm-mesh.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [LiteLLM](../open-source/litellm.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Kong Konnect](../independent/kong-konnect.md), [Redpanda Agentic Data Plane](../independent/redpanda-agentic-data-plane.md) (unconfirmed), [LangSmith](../independent/langsmith.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
