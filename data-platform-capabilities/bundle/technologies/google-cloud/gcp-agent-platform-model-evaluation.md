---
type: Technology
id: gcp-agent-platform-model-evaluation
title: Agent Platform Model Evaluation
description: Computes evaluation metrics for registered models on test data, including data and model bias metrics, and, with Explainable AI, gives feature attributions for predictions.
formerly: [Vertex AI Model Evaluation]
platform: platform-google-cloud
kind: feature
availability: ga
realises: [model-evaluation, model-explainability, fairness-assessment]
resource: https://docs.cloud.google.com/vertex-ai/docs/evaluation/introduction
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Model evaluation](../../capabilities/machine-learning/model-evaluation.md) (Machine learning development) (primary): Assess models against holdout data, baselines and business criteria before release.
- [Model explainability](../../capabilities/machine-learning/model-explainability.md) (Machine learning development): Explain which inputs drive a model's predictions, overall and for individual predictions.
- [Bias and fairness assessment](../../capabilities/machine-learning/fairness-assessment.md) (Machine learning development): Measure whether a model's outcomes differ unfairly across groups of people.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Gemini Enterprise Agent Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock Evaluations](../aws/aws-bedrock-evaluations.md), [Amazon SageMaker AI with MLflow](../aws/aws-sagemaker-mlflow.md) | [Model evaluation](../../capabilities/machine-learning/model-evaluation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning Responsible AI dashboard](../microsoft/azure-ml-responsible-ai-dashboard.md) | [Bias and fairness assessment](../../capabilities/machine-learning/fairness-assessment.md), [Model explainability](../../capabilities/machine-learning/model-explainability.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Modeling Objectives and model assets](../palantir/palantir-modeling-objectives.md) | [Model evaluation](../../capabilities/machine-learning/model-evaluation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [MLflow](../open-source/mlflow.md) | [Model evaluation](../../capabilities/machine-learning/model-evaluation.md) |
