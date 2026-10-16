---
type: Capability
id: model-explainability
title: Model explainability
description: Explain which inputs drive a model's predictions, overall and for individual predictions.
aliases: [XAI, SHAP, feature attribution]
broader: [model-evaluation]
related: [fairness-assessment, model-governance, human-oversight, ai-impact-assessment, inference-logging]
tags: [machine-learning]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Global explanations rank which inputs matter most across all predictions, for example that income and existing debt drive most credit decisions. Local explanations break down one prediction, showing that this applicant's score fell mainly because of two recent missed payments. Common techniques are permutation importance, SHAP values based on Shapley values from game theory, partial dependence plots, and counterfactuals that state what would need to change for a different outcome.

Explanations help teams debug models and help users trust them, and law or regulation sometimes requires reasons for automated decisions, such as adverse action notices in lending. Some models, such as linear models and small decision trees, are interpretable by design. Others need post-hoc methods, which approximate the model and can mislead when inputs are strongly correlated. Explainability is not the same as fairness assessment: knowing which inputs drive a decision does not show whether outcomes are fair across groups.

# Key considerations

- Post-hoc explanations approximate the model. Treat them as evidence, not proof, especially when inputs are correlated.
- Explaining every live prediction can cost more than making it. Decide which decisions need explanations at serving time.
- Explanations shown to customers or staff need plain wording and review. Raw feature names and numbers explain little to most people.
- Where interpretability is required, consider a simpler model rather than explaining a complex one.

# Questions to ask

- Must reasons be given to people affected by model decisions?
- Do validation or audit teams need to understand model behaviour before approval?
- Are explanations needed for each live prediction or only during review?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Machine learning development](machine-learning.md) |
| Broader | [Model evaluation](model-evaluation.md) |
| Related | [AI impact assessment](../governance/ai-impact-assessment.md), [Augmented analytics](../analytics-bi/augmented-analytics.md), [Bias and fairness assessment](fairness-assessment.md), [Decision management](../serving/decision-management.md), [Human oversight of AI](../governance/human-oversight.md), [Inference logging](../mlops/inference-logging.md), [Model governance](../mlops/model-governance.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (requires, level 2) · [Credit decisioning](../../use-cases/usecase-credit-decisioning.md) (requires, level 3) · [IoT predictive maintenance](../../use-cases/usecase-iot-predictive-maintenance.md) (benefits from) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (requires, level 2)
- **Personas:** [Data scientist](../../personas/persona-data-scientist.md)
- **Maturity tracks:** [AI and model governance](../../maturity/track-ai-governance.md) (from level 3, Defined) · [ML development](../../maturity/track-ml-development.md) (from level 4, Measured)
- **Frameworks:** [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 13 – Transparency and information to deployers; Article 14 – Human oversight · [GDPR](../../frameworks/framework-gdpr.md): Article 22 – Automated individual decision-making · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Annex A.8 – Information for interested parties · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): MEASURE 2 – Evaluation for trustworthy characteristics

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Clarify](../../technologies/aws/aws-sagemaker-clarify.md) (deprecated) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning Responsible AI dashboard](../../technologies/microsoft/azure-ml-responsible-ai-dashboard.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform Model Evaluation](../../technologies/google-cloud/gcp-agent-platform-model-evaluation.md), [BigQuery ML](../../technologies/google-cloud/gcp-bigquery-ml.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Model Registry](../../technologies/snowflake/snowflake-model-registry.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Managed MLflow on Databricks](../../technologies/databricks/databricks-managed-mlflow.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [MySQL HeatWave AutoML and HeatWave GenAI](../../technologies/oracle/oracle-heatwave-automl-genai.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Fiddler AI Control Plane](../../technologies/independent/fiddler-ai-control-plane.md), [H2O.ai Platform (Driverless AI and h2oGPTe)](../../technologies/independent/h2o-ai.md) |
