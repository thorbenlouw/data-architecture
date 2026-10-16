---
type: Technology
id: aws-sagemaker-mlflow
title: Amazon SageMaker AI with MLflow
description: Managed MLflow, provided as serverless MLflow Apps, for tracking experiments, comparing runs and tracing generative AI applications.
aliases: [SageMaker AI MLflow Apps]
formerly: [Amazon SageMaker with MLflow]
platform: platform-aws
kind: feature
availability: ga
realises: [experiment-tracking, genai-observability, model-evaluation]
resource: https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Serverless MLflow Apps (December 2025) replaced sized tracking servers, are free of extra charge and upgrade MLflow versions in place. Shareable across accounts with AWS RAM and usable from Unified Studio.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) (Machine learning development) (primary): Record parameters, code versions, data and metrics for each training run so results can be compared and reproduced.
- [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) (Generative AI): Trace model and agent calls with their prompts, responses, latency, cost and user feedback.
- [Model evaluation](../../capabilities/machine-learning/model-evaluation.md) (Machine learning development): Assess models against holdout data, baselines and business criteria before release.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon SageMaker AI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning registries and MLflow tracking](../microsoft/azure-ml-registries-mlflow.md), [Data Science in Microsoft Fabric](../microsoft/fabric-data-science.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Experiments on Agent Platform](../google-cloud/gcp-agent-platform-experiments.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Experiments](../snowflake/snowflake-ml-experiments.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Managed MLflow on Databricks](../databricks/databricks-managed-mlflow.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Workbench](../cloudera/cloudera-ai-workbench.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [MLflow](../open-source/mlflow.md), [DVC (Data Version Control)](../open-source/dvc.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md), [Model evaluation](../../capabilities/machine-learning/model-evaluation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Comet ML](../independent/comet.md), [Weights & Biases](../independent/weights-and-biases.md), [Domino Enterprise AI Platform](../independent/domino-enterprise-ai-platform.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
