---
type: Capability
id: model-performance-monitoring
title: Model performance monitoring
description: Measure prediction quality over time against ground truth as it arrives.
broader: [model-monitoring]
related: [model-evaluation, drift-detection, continuous-training, champion-challenger]
depends_on: [inference-logging]
tags: [mlops]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Each logged prediction is joined to the outcome it tried to predict once that outcome is known, and quality metrics are calculated over time. A churn model's January predictions are matched in March to the customers who actually left, giving precision, recall and calibration for the January cohort, broken down by model version and segment. The join needs a stable key, such as a prediction or request id, and outcomes recorded as data in the platform.

This is the only direct measure of whether a model still works; drift and output checks are proxies. The difficulties are delay and bias in outcomes. Loan defaults take months to appear, and outcomes are seen only for cases the model let through, since rejected applicants never get the chance to default. Teams respond with partial early outcomes, small random samples exempt from the model's decisions, and human review of samples. Unlike evaluation before release, it uses live data and real outcomes rather than a fixed test set.

# Key considerations

- Plan how outcomes will be captured and linked to predictions before release. Adding the link afterwards is often impossible.
- Correct for selection bias where the model's decisions determine which outcomes are seen, for example with a small random holdout.
- Report by cohort of prediction date, not outcome date, so quality trends are easy to read.
- Set minimum sample sizes before reporting a metric, so small cohorts do not raise false alarms.

# Questions to ask

- Where and when are true outcomes recorded, and can they be linked to individual predictions?
- How long is the delay between prediction and outcome?
- What fall in quality should trigger retraining or rollback?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [ML operations](mlops.md) |
| Broader | [Model monitoring](model-monitoring.md) |
| Related | [Canary and A/B testing](canary-ab-testing.md), [Champion-challenger](champion-challenger.md), [Continuous training](continuous-training.md), [Drift detection](drift-detection.md), [Model evaluation](../machine-learning/model-evaluation.md), [Model release strategies](model-release-strategies.md), [Shadow deployment](shadow-deployment.md) |
| Depends on | [Inference logging](inference-logging.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (requires, level 2) · [Credit decisioning](../../use-cases/usecase-credit-decisioning.md) (requires, level 3) · [Demand forecasting](../../use-cases/usecase-demand-forecasting.md) (requires, level 3) · [IoT predictive maintenance](../../use-cases/usecase-iot-predictive-maintenance.md) (benefits from) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (requires, level 3)
- **Personas:** [ML engineer](../../personas/persona-ml-engineer.md)
- **Maturity tracks:** [MLOps](../../maturity/track-mlops.md) (from level 4, Measured)
- **Frameworks:** [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 15 – Accuracy, robustness and cybersecurity; Article 72 – Post-market monitoring · [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Model monitoring · [Microsoft MLOps maturity model](../../frameworks/framework-microsoft-mlops-maturity.md): Level 4 – Full MLOps automated operations · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): MEASURE 4 – Feedback on measurement

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Model Monitor](../../technologies/aws/aws-sagemaker-model-monitor.md) (deprecated) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning model monitoring](../../technologies/microsoft/azure-ml-model-monitoring.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake ML Observability (model monitors)](../../technologies/snowflake/snowflake-ml-observability.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks data profiling](../../technologies/databricks/databricks-data-profiling.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata ModelOps](../../technologies/teradata/teradata-modelops.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.governance](../../technologies/ibm/ibm-watsonx-governance.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Evidently](../../technologies/open-source/evidently.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Arize AX](../../technologies/independent/arize-ax.md), [DataRobot AI Platform](../../technologies/independent/datarobot-ai-platform.md), [Fiddler AI Control Plane](../../technologies/independent/fiddler-ai-control-plane.md) |
