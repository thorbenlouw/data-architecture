---
type: Capability
id: drift-detection
title: Drift detection
description: Detect when live input data, or its relationship to outcomes, moves away from what the model was trained on.
aliases: [data drift, concept drift, training-serving skew]
broader: [model-monitoring]
related: [data-anomaly-detection, data-profiling, continuous-training, fairness-assessment]
depends_on: [inference-logging]
tags: [mlops]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Live data is compared with a reference, usually the training data or a recent stable period, and an alert is raised when the difference passes a set level. Data drift is a change in the inputs, such as a campaign bringing in younger customers. Concept drift is a change in the link between inputs and outcome, such as fraudsters changing tactics. Training-serving skew is a third case: online and offline pipelines compute the same feature differently, so the model sees unfamiliar values from its first day. Common measures are the population stability index, Kolmogorov–Smirnov tests and shifts in the prediction distribution.

Drift checks give warning while true outcomes are still unknown. Tests on large volumes flag tiny, irrelevant changes, so alerts should weigh change size and feature importance. Concept drift is confirmed only once outcomes arrive. Skew is found by comparing logged served features with offline values for the same entities and times. Data anomaly detection watches tables in general; drift detection compares against what one model learned from.

# Key considerations

- Choose the reference window deliberately. Comparing with training data and with last week answer different questions.
- On large volumes, statistical tests flag trivial differences. Use effect-size measures and thresholds weighted by feature importance.
- Seasonal patterns look like drift. Compare with the same period last year or account for seasonality.
- Decide in advance what a drift alert triggers: investigation, retraining or rollback.

# Questions to ask

- How long after a prediction is the true outcome known?
- Which features does the model rely on most, and how volatile are they?
- Do known events such as promotions or seasons regularly shift the data?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [ML operations](mlops.md) |
| Broader | [Model monitoring](model-monitoring.md) |
| Related | [Bias and fairness assessment](../machine-learning/fairness-assessment.md), [Continuous training](continuous-training.md), [Data anomaly detection](../data-quality/data-anomaly-detection.md), [Data profiling](../data-quality/data-profiling.md), [Model performance monitoring](model-performance-monitoring.md) |
| Depends on | [Inference logging](inference-logging.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (benefits from) · [Credit decisioning](../../use-cases/usecase-credit-decisioning.md) (requires, level 2) · [IoT predictive maintenance](../../use-cases/usecase-iot-predictive-maintenance.md) (requires, level 2) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (requires, level 3)
- **Personas:** [ML engineer](../../personas/persona-ml-engineer.md)
- **Maturity tracks:** [MLOps](../../maturity/track-mlops.md) (from level 3, Defined)
- **Frameworks:** [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 15 – Accuracy, robustness and cybersecurity; Article 72 – Post-market monitoring · [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Data validation; Pipeline triggers · [Microsoft MLOps maturity model](../../frameworks/framework-microsoft-mlops-maturity.md): Level 4 – Full MLOps automated operations · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): MEASURE 3 – Tracking risks over time

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Model Monitor](../../technologies/aws/aws-sagemaker-model-monitor.md) (deprecated) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning model monitoring](../../technologies/microsoft/azure-ml-model-monitoring.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Model Monitoring on Agent Platform](../../technologies/google-cloud/gcp-model-monitoring.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake ML Observability (model monitors)](../../technologies/snowflake/snowflake-ml-observability.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks data profiling](../../technologies/databricks/databricks-data-profiling.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata ModelOps](../../technologies/teradata/teradata-modelops.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.governance](../../technologies/ibm/ibm-watsonx-governance.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Evidently](../../technologies/open-source/evidently.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Arize AX](../../technologies/independent/arize-ax.md), [DataRobot AI Platform](../../technologies/independent/datarobot-ai-platform.md), [Fiddler AI Control Plane](../../technologies/independent/fiddler-ai-control-plane.md) |
