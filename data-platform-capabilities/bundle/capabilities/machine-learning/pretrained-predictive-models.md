---
type: Capability
id: pretrained-predictive-models
title: Pretrained predictive models
description: Forecast, classify or detect anomalies on business tables with pretrained models, without training a model for each use case.
aliases: [tabular foundation models, time-series foundation models]
broader: [machine-learning]
related: [automl, foundation-model-access, in-database-ml, time-series-data, enterprise-planning]
tags: [machine-learning]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

These models are trained in advance on large collections of tables or time series, and then predict on a new table without a model being trained for that use case. A user points a forecasting model at three years of daily sales per store and gets forecasts with prediction intervals, or gives a tabular model a few thousand labelled rows and asks it to classify the rest. Some work only from examples supplied at prediction time, known as in-context learning; others are briefly fine-tuned on the new data.

They lower the cost of the many small prediction tasks that would not justify a data science project, and often give a strong baseline quickly. Their limits are still being mapped: caps on input size, cost per prediction, weaker results on unusual data, and less transparency than a model you trained. They differ from AutoML, which trains and tunes a new model each time, and from language models called through AI functions, which work on text rather than numeric prediction.

# Key considerations

- Benchmark against a simple trained baseline on your own data before adopting. Results vary by dataset.
- Check limits on rows, columns and context size. Many models handle thousands of rows per call, not millions.
- Find out where inference runs and whether table data leaves the platform's security boundary.
- Validation evidence and explanations may be thinner than for trained models, which matters for regulated decisions.

# Questions to ask

- How many forecasting or classification tasks are too small to justify building a custom model?
- Must predictions be explainable to regulators or customers?
- Can table data be sent to a hosted model, or must inference stay inside the platform?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Machine learning development](machine-learning.md) |
| Broader | [Machine learning development](machine-learning.md) |
| Related | [Augmented analytics](../analytics-bi/augmented-analytics.md), [AutoML](automl.md), [Foundation model access](../generative-ai/foundation-model-access.md), [In-database machine learning](in-database-ml.md), [Planning and forecasting](../analytics-bi/enterprise-planning.md), [Time-series data](../specialised-data/time-series-data.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (benefits from) · [Demand forecasting](../../use-cases/usecase-demand-forecasting.md) (benefits from) · [IoT predictive maintenance](../../use-cases/usecase-iot-predictive-maintenance.md) (benefits from)
- **Personas:** [Data scientist](../../personas/persona-data-scientist.md)
- **Maturity tracks:** [ML development](../../maturity/track-ml-development.md) (from level 5, Optimising)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery ML](../../technologies/google-cloud/gcp-bigquery-ml.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP AI Foundation (SAP AI Core and generative AI hub)](../../technologies/sap/sap-ai-foundation.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.ai](../../technologies/ibm/ibm-watsonx-ai.md) |
