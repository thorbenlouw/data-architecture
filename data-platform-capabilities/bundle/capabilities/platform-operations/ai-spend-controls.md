---
type: Capability
id: ai-spend-controls
title: AI usage and spend controls
description: Limit, prioritise and attribute model and agent consumption per user, team or application.
aliases: [token budgets, AI quotas]
broader: [cost-management, generative-ai]
related: [genai-observability, ai-functions, reserved-capacity, spend-controls, data-engineering-agents]
depends_on: [ai-gateway]
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Model and agent use is billed per token, per request or per unit of provisioned throughput, and cost grows with prompt length, model choice and the number of steps an agent takes. Typical controls are token or request quotas per user, team or application; rate limits that protect shared capacity; routing rules that send simple requests to cheaper models; caps on agent steps or tool calls per task; and attribution of every call to the application and person behind it. An AI gateway is the usual place to enforce them.

Without controls, one badly designed agent loop, a batch job calling a large model on every row, or a popular internal assistant can multiply spend within days. AI calls often go to an external provider with its own billing, so the platform's normal cost reports may not show them. Priority matters too: production applications should keep access to scarce capacity when experiments compete for it. This capability extends general spend controls to the units and usage patterns specific to AI.

# Key considerations

- Record the cost of each call with its user, application and use case, so spend can be attributed and unit costs compared.
- Estimate cost before large batch runs of AI functions. Cost scales with row count and text length, and a trial on a sample shows the multiplier.
- Cap agent runs by steps, time and spend per task, so a stuck agent stops instead of retrying indefinitely.
- Caching repeated prompts and using smaller models where they perform well enough often save more than quotas do.

# Questions to ask

- Which teams and applications call models today, and do you know what each spends?
- Are model calls routed through one gateway, or do teams hold their own provider keys?
- Which AI workloads must keep capacity when demand exceeds supply?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Cost management](cost-management.md), [Generative AI](../generative-ai/generative-ai.md) |
| Related | [AI agents](../generative-ai/ai-agents.md), [AI functions in SQL](../processing/ai-functions.md), [AI gateway](../generative-ai/ai-gateway.md), [Budgets and spend controls](spend-controls.md), [Data engineering agents](../development-lifecycle/data-engineering-agents.md), [Foundation model access](../generative-ai/foundation-model-access.md), [Generative AI observability](../generative-ai/genai-observability.md), [Reserved and committed capacity](../compute/reserved-capacity.md) |
| Depends on | [AI gateway](../generative-ai/ai-gateway.md) |

# Where it appears

- **Use cases:** [Agentic process automation](../../use-cases/usecase-agentic-automation.md) (requires, level 2) · [Conversational analytics for business users](../../use-cases/usecase-conversational-bi.md) (benefits from) · [Document data extraction](../../use-cases/usecase-document-extraction.md) (benefits from) · [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (benefits from) · [Platform cost management and chargeback](../../use-cases/usecase-platform-cost-management.md) (requires, level 2)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md) · [Chief data officer](../../personas/persona-cdo.md) · [FinOps practitioner](../../personas/persona-finops-practitioner.md)
- **Maturity tracks:** [FinOps](../../maturity/track-finops.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Bedrock](../../technologies/aws/aws-bedrock.md), [Amazon Bedrock AgentCore Gateway](../../technologies/aws/aws-bedrock-agentcore-gateway.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure API Management](../../technologies/microsoft/azure-api-management.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Apigee](../../technologies/google-cloud/gcp-apigee.md), [BigQuery generative AI functions](../../technologies/google-cloud/gcp-bigquery-ai-functions.md), [Gemini models on Agent Platform](../../technologies/google-cloud/gcp-gemini-models.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake budgets](../../technologies/snowflake/snowflake-budgets.md), [Snowflake Cortex AI Functions](../../technologies/snowflake/snowflake-cortex-ai-functions.md), [Snowflake Cortex AI Gateway](../../technologies/snowflake/snowflake-cortex-ai-gateway.md) (preview) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks budgets](../../technologies/databricks/databricks-budgets.md), [Unity Gateway](../../technologies/databricks/databricks-unity-gateway.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir AIP and AIP Model Catalog](../../technologies/palantir/palantir-aip.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [LiteLLM](../../technologies/open-source/litellm.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Dataiku LLM Mesh](../../technologies/independent/dataiku-llm-mesh.md), [Kong Konnect](../../technologies/independent/kong-konnect.md), [Redpanda Agentic Data Plane](../../technologies/independent/redpanda-agentic-data-plane.md) (unconfirmed) |
