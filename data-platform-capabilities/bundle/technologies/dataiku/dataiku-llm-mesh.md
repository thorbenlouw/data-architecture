---
type: Technology
id: dataiku-llm-mesh
title: Dataiku LLM Mesh
description: Gateway through which Dataiku projects, agents and applications call commercial, cloud-hosted and self-hosted LLMs, with guardrails, cost quotas, rate limits, evaluation and logging.
aliases: [LLM Guard Services, Cost Guard, Safe Guard, Quality Guard]
platform: platform-dataiku
kind: feature
availability: ga
realises: [ai-gateway, ai-guardrails, ai-spend-controls, genai-evaluation, model-customisation]
resource: https://doc.dataiku.com/dss/latest/generative-ai/index.html
tags: [dataiku]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

Projects call models through LLM connections in the mesh rather than directly. Guardrails (PII, toxicity, prompt injection, topic boundaries, bias and custom checks) can be set on connections, agents or individual uses. Cost Control sets alerting and blocking budgets filtered by provider, connection, project or user, though custom quotas need the Advanced LLM Mesh licence, and no dollar cost is calculated for Amazon SageMaker or Databricks Mosaic AI models. Rate limiting is configured separately. Also supports fine-tuning, locally run Hugging Face models, and Evaluate LLM recipes (Advanced LLM Mesh) with LLM-as-a-judge, BLEU, ROUGE and BERTScore metrics. Dataiku markets these controls as LLM Guard Services: Cost Guard, Safe Guard and Quality Guard.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI gateway](../../capabilities/generative-ai/ai-gateway.md) (Generative AI) (primary): Route, secure, rate-limit and track model calls across providers from one place.
- [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) (Generative AI): Check model inputs, outputs and agent tool calls against policy to block harmful content, data leakage, prompt injection and disallowed actions.
- [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) (Platform operations): Limit, prioritise and attribute model and agent consumption per user, team or application.
- [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) (Generative AI): Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges.
- [Model customisation](../../capabilities/generative-ai/model-customisation.md) (Generative AI): Adapt foundation models to a domain through fine-tuning, distillation or further training.

**Platform:** [Dataiku](../../platforms/platform-dataiku.md)  
**Availability:** ga  
**Product family:** Dataiku Platform for AI Success, Dataiku LLM Mesh

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore Gateway](../aws/aws-bedrock-agentcore-gateway.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure API Management](../microsoft/azure-api-management.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Gateway](../google-cloud/gcp-agent-gateway.md), [Apigee](../google-cloud/gcp-apigee.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Gateway](../snowflake/snowflake-cortex-ai-gateway.md) (preview) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Gateway](../databricks/databricks-unity-gateway.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md), [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir AIP and AIP Model Catalog](../palantir/palantir-aip.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [LiteLLM](../open-source/litellm.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Kong Konnect](../independent/kong-konnect.md), [Redpanda Agentic Data Plane](../independent/redpanda-agentic-data-plane.md) (unconfirmed), [LangSmith](../independent/langsmith.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md), [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
