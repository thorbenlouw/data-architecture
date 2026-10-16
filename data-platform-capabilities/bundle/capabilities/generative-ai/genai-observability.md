---
type: Capability
id: genai-observability
title: Generative AI observability
description: Trace model and agent calls with their prompts, responses, latency, cost and user feedback.
aliases: [LLM tracing]
broader: [generative-ai]
related:
- platform-observability
- inference-logging
- ai-spend-controls
- genai-evaluation
- ai-incident-management
tags: [generative-ai]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Each request is recorded as a trace: the user input, the assembled prompt, the documents retrieved, each model call with its tokens, latency and cost, each tool call and its result, and the final output, all linked by one identifier. User feedback such as ratings, edits and complaints is attached to the same trace. For example, a rise in complaints about an assistant is traced within minutes to a retrieval step that began returning an archived price list after an index change.

Service metrics such as error rate and latency cannot explain why an answer was wrong; you need the content of each step. The OpenTelemetry semantic conventions for generative AI are becoming the common trace format, so traces can flow into existing monitoring tools. Traces feed evaluation of sampled traffic, cost attribution and incident investigation. Platform observability covers jobs and queries, and inference logging for predictive models records inputs and outputs; this capability follows multi-step model and agent behaviour.

# Key considerations

- Traces hold prompts, documents and outputs that may be sensitive. Apply access control, masking and retention to them.
- Tracing all high-volume traffic in full is costly. Sample, but keep every error and every flagged case.
- Use one trace format across frameworks and agents so multi-agent flows link up.
- Collect user feedback in the product and attach it to traces, or the best quality signal is lost.

# Questions to ask

- When an answer is wrong, can you see what was retrieved and which prompt was used?
- Who needs access to traces, and may they see the content of prompts and answers?
- How is AI cost currently broken down by application, team and user?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Generative AI](generative-ai.md) |
| Broader | [Generative AI](generative-ai.md) |
| Related | [Agent hosting and runtime](agent-runtime.md), [Agent-to-agent interoperability](agent-interoperability.md), [AI agents](ai-agents.md), [AI gateway](ai-gateway.md), [AI incident management](../governance/ai-incident-management.md), [AI usage and spend controls](../platform-operations/ai-spend-controls.md), [Document and unstructured lineage](../metadata/unstructured-lineage.md), [Generative AI evaluation](genai-evaluation.md), [Inference logging](../mlops/inference-logging.md), [Model monitoring](../mlops/model-monitoring.md), [Platform observability](../platform-operations/platform-observability.md), [Prompt management](prompt-management.md) |

# Where it appears

- **Use cases:** [Agentic process automation](../../use-cases/usecase-agentic-automation.md) (requires, level 3) · [Conversational analytics for business users](../../use-cases/usecase-conversational-bi.md) (requires, level 2) · [Document data extraction](../../use-cases/usecase-document-extraction.md) (requires, level 2) · [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (requires, level 2)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md)
- **Maturity tracks:** [Generative AI](../../maturity/track-genai.md) (from level 2, Managed)
- **Frameworks:** [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 12 – Record-keeping; Article 72 – Post-market monitoring · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): GOVERN 5 – Engagement with external stakeholders; MEASURE 3 – Tracking risks over time; Generative AI Profile (NIST AI 600-1)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Bedrock AgentCore](../../technologies/aws/aws-bedrock-agentcore.md), [Amazon SageMaker AI with MLflow](../../technologies/aws/aws-sagemaker-mlflow.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Foundry Control Plane](../../technologies/microsoft/azure-foundry-control-plane.md) (preview), [Microsoft Foundry observability and tracing](../../technologies/microsoft/azure-foundry-observability.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Agent Observability](../../technologies/google-cloud/gcp-agent-observability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake AI Observability](../../technologies/snowflake/snowflake-ai-observability.md), [Snowflake Cortex AI Gateway](../../technologies/snowflake/snowflake-cortex-ai-gateway.md) (preview) |
| [Databricks](../../platforms/platform-databricks.md) | MLflow Tracing | [MLflow Tracing on Databricks](../../technologies/databricks/databricks-mlflow-tracing.md), [Unity Gateway](../../technologies/databricks/databricks-unity-gateway.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | Langfuse | [Langfuse](../../technologies/clickhouse/clickhouse-langfuse.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Enterprise AgentStack](../../technologies/teradata/teradata-agentstack.md) (preview) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx Orchestrate](../../technologies/ibm/ibm-watsonx-orchestrate.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [MLflow](../../technologies/open-source/mlflow.md), [OpenTelemetry semantic conventions for generative AI](../../technologies/open-source/opentelemetry-genai-semantic-conventions.md) (preview) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Arize AX](../../technologies/independent/arize-ax.md), [Braintrust](../../technologies/independent/braintrust.md), [Comet ML](../../technologies/independent/comet.md), [Fiddler AI Control Plane](../../technologies/independent/fiddler-ai-control-plane.md), [LangSmith](../../technologies/independent/langsmith.md), [Monte Carlo Agent Observability](../../technologies/independent/monte-carlo-agent-observability.md), [Splunk Agent Observability](../../technologies/independent/galileo.md) |
