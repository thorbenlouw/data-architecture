---
type: Capability
id: automl
title: AutoML
description: Try features, algorithms and settings automatically to produce a good baseline model with little code.
broader: [model-training]
related: [in-database-ml, pretrained-predictive-models, model-evaluation, augmented-analytics]
tags: [machine-learning]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

AutoML takes a labelled table and a target column, then tries data preparation steps, feature transformations, several algorithms and their settings, and returns a ranked list of models with their scores. Given past loan applications and an outcome column, it might try logistic regression, random forests and gradient boosting, handle missing values and categories, and report that a boosted model gives the best ranking accuracy. Many tools also generate the code or notebook behind the best model.

It gives analysts a usable model with little code and gives data scientists a quick baseline to beat. It works best for standard tabular classification, regression and forecasting. It does not replace understanding the problem: it will not notice leakage in the input table, a badly chosen target, or a metric that ignores the real cost of errors. Prefer tools that expose the generated pipeline, so the result can be reviewed, versioned and deployed like any other model.

# Key considerations

- Prefer tools that output inspectable code or pipelines. A black-box result is hard to review, maintain and govern.
- Check the input table for leakage first. AutoML will happily use columns that would not exist at prediction time.
- Set time and cost limits, because broad searches over large tables can run for hours.
- AutoML models still need the same evaluation, fairness checks and approval as models built by hand.

# Questions to ask

- Who will build models: data scientists, analysts, or both?
- Are the use cases mostly standard tabular prediction and forecasting?
- Must every model's logic be reviewable by a validation or model risk team?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Machine learning development](machine-learning.md) |
| Broader | [Model training](model-training.md) |
| Related | [Augmented analytics](../analytics-bi/augmented-analytics.md), [In-database machine learning](in-database-ml.md), [Model evaluation](model-evaluation.md), [Pretrained predictive models](pretrained-predictive-models.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (benefits from) · [Demand forecasting](../../use-cases/usecase-demand-forecasting.md) (benefits from)
- **Personas:** [Data scientist](../../personas/persona-data-scientist.md)
- **Maturity tracks:** [ML development](../../maturity/track-ml-development.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | SageMaker Canvas and Autopilot | [Amazon SageMaker Autopilot](../../technologies/aws/aws-sagemaker-autopilot.md), [Amazon SageMaker Canvas](../../technologies/aws/aws-sagemaker-canvas.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Automated machine learning (AutoML) in Azure Machine Learning](../../technologies/microsoft/azure-ml-automl.md), [Data Science in Microsoft Fabric](../../technologies/microsoft/fabric-data-science.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform AutoML](../../technologies/google-cloud/gcp-agent-platform-automl.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake ML Functions](../../technologies/snowflake/snowflake-ml-functions.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks AutoML](../../technologies/databricks/databricks-automl.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [MySQL HeatWave AutoML and HeatWave GenAI](../../technologies/oracle/oracle-heatwave-automl-genai.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.ai](../../technologies/ibm/ibm-watsonx-ai.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Dataiku](../../technologies/independent/dataiku.md), [DataRobot AI Platform](../../technologies/independent/datarobot-ai-platform.md), [H2O.ai Platform (Driverless AI and h2oGPTe)](../../technologies/independent/h2o-ai.md) |
