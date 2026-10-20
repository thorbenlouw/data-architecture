---
type: Technology
id: databricks-agent-evaluation
title: Databricks Agent Evaluation (MLflow GenAI evaluation)
description: Evaluates agents and LLM applications against datasets, using built-in and custom scorers, LLM judges and human feedback, and also monitors production traces.
formerly: [Mosaic AI Agent Evaluation]
platform: platform-databricks
kind: feature
availability: ga
realises: [genai-evaluation, data-labelling, training-dataset-management]
resource: https://docs.databricks.com/aws/en/mlflow/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Agent Evaluation now runs on MLflow 3 evaluation APIs rather than a separate SDK. Customer-managed keys for evaluation features were added in May 2026, and retrieval-quality evaluation for AI Search is in Beta.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) (Generative AI) (primary): Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges.
- [Data labelling](../../capabilities/machine-learning/data-labelling.md) (Machine learning development): Create and manage labelled examples for supervised learning, using people, rules or models.
- [Training and evaluation dataset management](../../capabilities/machine-learning/training-dataset-management.md) (Machine learning development): Assemble, version, document and govern the datasets used to train, validate and test models, including evaluation sets for generative AI.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Agent Bricks

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore Evaluations](../aws/aws-bedrock-agentcore-evaluations.md), [Amazon Bedrock Evaluations](../aws/aws-bedrock-evaluations.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Foundry evaluations](../microsoft/azure-foundry-evaluations.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Gen AI evals on Agent Platform](../google-cloud/gcp-gen-ai-evals.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake AI Observability](../snowflake/snowflake-ai-observability.md), [Snowflake Cortex AI Function Studio](../snowflake/snowflake-cortex-ai-function-studio.md) (preview) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [Langfuse](../clickhouse/clickhouse-langfuse.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Training and evaluation dataset management](../../capabilities/machine-learning/training-dataset-management.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md), [IBM watsonx.governance](../ibm/ibm-watsonx-governance.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Retrieval Agent Manager](../sas/sas-retrieval-agent-manager.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku LLM Mesh](../dataiku/dataiku-llm-mesh.md), [Dataiku Visual Agents and Code Agents](../dataiku/dataiku-agents.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [MLflow](../open-source/mlflow.md), [Evidently](../open-source/evidently.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Training and evaluation dataset management](../../capabilities/machine-learning/training-dataset-management.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Labelbox](../independent/labelbox.md), [Snorkel AI](../independent/snorkel-ai.md), [Braintrust](../independent/braintrust.md) | [Data labelling](../../capabilities/machine-learning/data-labelling.md), [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Training and evaluation dataset management](../../capabilities/machine-learning/training-dataset-management.md) |
