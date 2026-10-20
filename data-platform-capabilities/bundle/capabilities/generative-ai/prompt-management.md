---
type: Capability
id: prompt-management
title: Prompt management
description: Version, test and reuse prompts and model configurations.
broader: [generative-ai]
related: [genai-evaluation, genai-observability, version-control, environment-promotion, experiment-tracking]
tags: [generative-ai]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Prompts are stored as versioned artefacts apart from application code: the template text and its variables, together with the model and settings such as temperature and output schema. A registry keeps every version with labels such as production and staging, so an application fetches the current production prompt at run time and teams can change it without redeploying. For example, a product team edits a summarisation prompt, runs it against fifty test cases, compares scores with the live version and promotes it, keeping the old version for rollback.

Small wording changes can shift behaviour widely, and without versioning nobody can say which prompt produced a given output. Prompts may be managed in a registry within an observability or ML platform, kept in Git alongside code, or generated and tuned programmatically against an evaluation set. Linking each trace to the prompt version that produced it makes incidents explainable. Model customisation changes the weights; prompt management changes the instructions, and evaluation measures the effect of either.

# Key considerations

- Treat the prompt, model version and parameters as one unit. The same prompt behaves differently on another model.
- Fetching prompts at run time allows quick changes but bypasses code review. Require approval before a version gets the production label.
- Record the prompt version on every trace so an output can be traced to its instructions.
- Prompts can contain business rules or confidential instructions. Control who can read and edit them.

# Questions to ask

- Who edits prompts: engineers, product owners or domain experts?
- How often do prompts change, and how are changes tested?
- Could you say which prompt version produced a particular output last month?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Generative AI](generative-ai.md) |
| Broader | [Generative AI](generative-ai.md) |
| Related | [Environment promotion](../development-lifecycle/environment-promotion.md), [Experiment tracking](../machine-learning/experiment-tracking.md), [Generative AI evaluation](genai-evaluation.md), [Generative AI observability](genai-observability.md), [Version control integration](../development-lifecycle/version-control.md) |

# Where it appears

- **Use cases:** [Agentic process automation](../../use-cases/usecase-agentic-automation.md) (benefits from) · [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (requires, level 2)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md)
- **Maturity tracks:** [Generative AI](../../maturity/track-genai.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Bedrock Prompt management](../../technologies/aws/aws-bedrock-prompt-management.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning prompt flow](../../technologies/microsoft/azure-prompt-flow.md) (deprecated) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Agent Studio](../../technologies/google-cloud/gcp-agent-studio.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Cortex AI Function Studio](../../technologies/snowflake/snowflake-cortex-ai-function-studio.md) (preview) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Managed MLflow on Databricks](../../technologies/databricks/databricks-managed-mlflow.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [Langfuse](../../technologies/clickhouse/clickhouse-langfuse.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP AI Foundation (SAP AI Core and generative AI hub)](../../technologies/sap/sap-ai-foundation.md), [SAP Joule Studio](../../technologies/sap/sap-joule-studio.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.ai](../../technologies/ibm/ibm-watsonx-ai.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [AIP Logic and AIP Evals](../../technologies/palantir/palantir-aip-logic.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS Agentic AI Accelerator](../../technologies/sas/sas-agentic-ai-accelerator.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | Prompt Studios | [Dataiku Prompt Studios](../../technologies/dataiku/dataiku-prompt-studios.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [MLflow](../../technologies/open-source/mlflow.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Arize AX](../../technologies/independent/arize-ax.md), [Braintrust](../../technologies/independent/braintrust.md), [Comet ML](../../technologies/independent/comet.md), [LangSmith](../../technologies/independent/langsmith.md) |
