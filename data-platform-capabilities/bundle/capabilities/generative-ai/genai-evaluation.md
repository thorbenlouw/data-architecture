---
type: Capability
id: genai-evaluation
title: Generative AI evaluation
description: Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges.
aliases: [LLM evals, LLM-as-judge]
broader: [generative-ai]
related: [model-evaluation, prompt-management, genai-observability, human-oversight, data-labelling]
tags: [generative-ai]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Evaluation runs a system against a set of test cases and scores the results. Scores come from exact checks such as valid JSON, a correct query result or a required citation; from human reviewers; and from model-based judges, where a second model rates outputs against a rubric such as faithfulness to sources or relevance. For agents, evaluation also checks the path: whether the right tools were called and the task was completed. For example, before changing a policy assistant's retrieval settings, the team runs 300 questions with known answers and blocks the change if faithfulness drops.

Outputs vary between runs and there is rarely one right answer, so ordinary unit tests are not enough. Offline evaluation gates releases; online evaluation scores a sample of live traffic. Test sets come from real questions, expert-written cases and synthetic generation. Model judges must be checked against human ratings before they are trusted. Model evaluation for predictive ML compares predictions with known labels; observability records what happened but does not judge it.

# Key considerations

- Build test sets from real questions and past failures. General benchmarks say little about your use case.
- Check model judges against human ratings, and re-check whenever the judge model changes.
- Score retrieval, generation and the end-to-end result separately, so a drop can be located.
- Run evaluation automatically on every prompt, model or retrieval change, with thresholds that block release.
- Track cost and latency alongside quality. A small gain in quality at three times the cost may not be acceptable.

# Questions to ask

- What does a good answer look like, and who is qualified to judge it?
- Is there a set of real questions with agreed answers?
- Which failures are unacceptable, such as wrong figures or unsafe advice?
- How often will models, prompts or content change and need re-evaluation?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Generative AI](generative-ai.md) |
| Broader | [Generative AI](generative-ai.md) |
| Narrower | [AI red teaming](ai-red-teaming.md) |
| Related | [AI agents](ai-agents.md), [AI context layer](../metadata/ai-context-layer.md), [AI functions in SQL](../processing/ai-functions.md), [AI governance](../governance/ai-governance.md), [AI impact assessment](../governance/ai-impact-assessment.md), [AI incident management](../governance/ai-incident-management.md), [Conversational analytics](../analytics-bi/conversational-analytics.md), [Data labelling](../machine-learning/data-labelling.md), [Generative AI observability](genai-observability.md), [Human oversight of AI](../governance/human-oversight.md), [Model evaluation](../machine-learning/model-evaluation.md), [Prompt management](prompt-management.md), [Retrieval-augmented generation](retrieval-augmented-generation.md), [Synthetic data generation](../development-lifecycle/synthetic-data.md), [Training and evaluation dataset management](../machine-learning/training-dataset-management.md), [Unstructured data quality](../data-quality/unstructured-data-quality.md) |
| Needed by | [Model customisation](model-customisation.md) |

# Where it appears

- **Use cases:** [Agentic process automation](../../use-cases/usecase-agentic-automation.md) (requires, level 3) · [Conversational analytics for business users](../../use-cases/usecase-conversational-bi.md) (requires, level 3) · [Document data extraction](../../use-cases/usecase-document-extraction.md) (requires, level 3) · [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (requires, level 3)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md)
- **Maturity tracks:** [AI and model governance](../../maturity/track-ai-governance.md) (from level 2, Managed) · [Generative AI](../../maturity/track-genai.md) (from level 3, Defined)
- **Frameworks:** [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): MEASURE 1 – Methods and metrics; MEASURE 2 – Evaluation for trustworthy characteristics; MEASURE 4 – Feedback on measurement; Generative AI Profile (NIST AI 600-1)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Bedrock AgentCore Evaluations](../../technologies/aws/aws-bedrock-agentcore-evaluations.md), [Amazon Bedrock Evaluations](../../technologies/aws/aws-bedrock-evaluations.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Foundry evaluations](../../technologies/microsoft/azure-foundry-evaluations.md), [Azure Machine Learning prompt flow](../../technologies/microsoft/azure-prompt-flow.md) (deprecated) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Gen AI evals | [Gen AI evals on Agent Platform](../../technologies/google-cloud/gcp-gen-ai-evals.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake AI Observability](../../technologies/snowflake/snowflake-ai-observability.md), [Snowflake Cortex AI Function Studio](../../technologies/snowflake/snowflake-cortex-ai-function-studio.md) (preview) |
| [Databricks](../../platforms/platform-databricks.md) | Agent Evaluation | [Databricks Agent Evaluation (MLflow GenAI evaluation)](../../technologies/databricks/databricks-agent-evaluation.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [Langfuse](../../technologies/clickhouse/clickhouse-langfuse.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx Orchestrate](../../technologies/ibm/ibm-watsonx-orchestrate.md), [IBM watsonx.governance](../../technologies/ibm/ibm-watsonx-governance.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [AIP Logic and AIP Evals](../../technologies/palantir/palantir-aip-logic.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS Retrieval Agent Manager](../../technologies/sas/sas-retrieval-agent-manager.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | Quality Guard | [Dataiku LLM Mesh](../../technologies/dataiku/dataiku-llm-mesh.md), [Dataiku Visual Agents and Code Agents](../../technologies/dataiku/dataiku-agents.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Evidently](../../technologies/open-source/evidently.md), [MLflow](../../technologies/open-source/mlflow.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Arize AX](../../technologies/independent/arize-ax.md), [Braintrust](../../technologies/independent/braintrust.md), [Comet ML](../../technologies/independent/comet.md), [Holistic AI Governance Platform](../../technologies/independent/holistic-ai-governance-platform.md), [Labelbox](../../technologies/independent/labelbox.md), [LangSmith](../../technologies/independent/langsmith.md), [Monte Carlo Agent Observability](../../technologies/independent/monte-carlo-agent-observability.md), [Scale Data Engine](../../technologies/independent/scale-data-engine.md), [Snorkel AI](../../technologies/independent/snorkel-ai.md), [Splunk Agent Observability](../../technologies/independent/galileo.md), [Weights & Biases](../../technologies/independent/weights-and-biases.md) |

Narrower capabilities are realised by a further 3 technologies; see their pages.
