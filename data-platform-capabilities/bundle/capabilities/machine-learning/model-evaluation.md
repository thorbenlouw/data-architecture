---
type: Capability
id: model-evaluation
title: Model evaluation
description: Assess models against holdout data, baselines and business criteria before release.
aliases: [model validation, offline evaluation, backtesting]
broader: [machine-learning]
related:
- genai-evaluation
- point-in-time-joins
- champion-challenger
- model-performance-monitoring
- data-versioning
tags: [machine-learning]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A trained model is tested on data it did not see in training and compared with a baseline, such as the current production model or a simple rule. Metrics depend on the task: precision and recall for fraud detection, mean absolute error for forecasts, calibration for probabilities used in pricing. Good evaluation also breaks results down by segment, such as region or customer type, and by recent time periods, because a model can be accurate overall and poor for one group or one month.

Evaluation decides whether a model is released, so the test must match how it will be used. For time-dependent problems a random split leaks future information; testing on a later period than training is safer. Business criteria count as much as statistics: a fraud model is judged by losses prevented per alert reviewed, not accuracy, which misleads on rare events. Offline evaluation before release differs from online comparison through shadow, canary or A/B tests and from monitoring in production.

# Key considerations

- Agree the metric and acceptance threshold with the business before training, so they are not chosen to fit the results.
- Use time-based splits for any problem where the future can differ from the past.
- Version evaluation datasets and reuse them, so successive model versions are compared on the same data.
- Report results by segment and across decision thresholds, not as one headline number.

# Questions to ask

- What does a wrong prediction cost, and is a false alarm worse than a miss?
- What baseline must a new model beat to be released?
- Who signs off evaluation results, and must the evidence be kept?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Machine learning development](machine-learning.md) |
| Broader | [Machine learning development](machine-learning.md) |
| Narrower | [Bias and fairness assessment](fairness-assessment.md), [Model explainability](model-explainability.md) |
| Related | [AutoML](automl.md), [Champion-challenger](../mlops/champion-challenger.md), [Continuous training](../mlops/continuous-training.md), [Data versioning](../storage/data-versioning.md), [Generative AI evaluation](../generative-ai/genai-evaluation.md), [Hyperparameter tuning](hyperparameter-tuning.md), [Model performance monitoring](../mlops/model-performance-monitoring.md), [Model release strategies](../mlops/model-release-strategies.md), [Point-in-time correct joins](point-in-time-joins.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (requires, level 2) · [Credit decisioning](../../use-cases/usecase-credit-decisioning.md) (requires, level 3) · [Demand forecasting](../../use-cases/usecase-demand-forecasting.md) (requires, level 3)
- **Personas:** [Data scientist](../../personas/persona-data-scientist.md)
- **Maturity tracks:** [ML development](../../maturity/track-ml-development.md) (from level 3, Defined)
- **Frameworks:** [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 9 – Risk management system; Article 15 – Accuracy, robustness and cybersecurity · [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Level 0 – Manual process; Model validation · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Annex A.6 – AI system life cycle · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): MAP 3 – Benefits and costs; MEASURE 1 – Methods and metrics; MEASURE 2 – Evaluation for trustworthy characteristics

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Bedrock Evaluations](../../technologies/aws/aws-bedrock-evaluations.md), [Amazon SageMaker AI with MLflow](../../technologies/aws/aws-sagemaker-mlflow.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform Model Evaluation](../../technologies/google-cloud/gcp-agent-platform-model-evaluation.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Modeling Objectives and model assets](../../technologies/palantir/palantir-modeling-objectives.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [MLflow](../../technologies/open-source/mlflow.md) |

Narrower capabilities are realised by a further 11 technologies; see their pages.
