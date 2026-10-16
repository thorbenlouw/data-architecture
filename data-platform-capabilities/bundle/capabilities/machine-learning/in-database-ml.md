---
type: Capability
id: in-database-ml
title: In-database machine learning
description: Train and run models using SQL inside the data platform.
aliases: [SQL ML, ML functions]
broader: [machine-learning]
related: [automl, user-defined-functions, batch-inference, ai-functions, workload-isolation]
depends_on: [sql-query-engine]
tags: [machine-learning]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Users train and score models with SQL statements, inside the warehouse or lakehouse engine, on data that never leaves it. An analyst writes one statement that creates a model from a table of customer history with churned as the label, then calls a prediction function in an ordinary SELECT to score every active customer. Supported algorithms usually include linear and logistic regression, tree ensembles, clustering, time-series forecasting and anomaly detection. Some engines also import models trained elsewhere, in formats such as ONNX, for scoring.

It suits teams that work in SQL, standard model types, and data too sensitive or too large to move. Operations become simpler: scoring is a query, scheduled like any other and covered by the platform's access control and lineage. The limits are the choice of algorithms, less control over training and debugging, and cost when the engine is not designed for iterative training. Training in Python next to the data is the other common option, offering any library at the price of separate environments.

# Key considerations

- Check which algorithms and tuning options exist before committing. Moving a model to another environment later usually means retraining it.
- Training in a shared warehouse uses the same compute as reporting. Isolate it or schedule it outside peak hours.
- Make sure models created in SQL are versioned, documented and visible to model governance, not just objects in a schema.
- Importing externally trained models for scoring is a useful middle path: train anywhere, score where the data is.

# Questions to ask

- Do the people building models work mainly in SQL?
- Must data stay inside the platform for security or residency reasons?
- Are the models needed standard types such as regression, classification, forecasting or clustering?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Machine learning development](machine-learning.md) |
| Broader | [Machine learning development](machine-learning.md) |
| Related | [AI functions in SQL](../processing/ai-functions.md), [AutoML](automl.md), [Batch inference](../mlops/batch-inference.md), [Pretrained predictive models](pretrained-predictive-models.md), [User-defined functions and procedures](../processing/user-defined-functions.md), [Workload isolation](../compute/workload-isolation.md) |
| Depends on | [SQL query engine](../compute/sql-query-engine.md) |

# Where it appears

- **Maturity tracks:** [ML development](../../maturity/track-ml-development.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Redshift ML (CREATE MODEL) | [Amazon Redshift ML](../../technologies/aws/aws-redshift-ml.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | BigQuery ML | [BigQuery ML](../../technologies/google-cloud/gcp-bigquery-ml.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake ML Functions](../../technologies/snowflake/snowflake-ml-functions.md) |
| [Oracle](../../platforms/platform-oracle.md) | Oracle Machine Learning / HeatWave AutoML | [MySQL HeatWave AutoML and HeatWave GenAI](../../technologies/oracle/oracle-heatwave-automl-genai.md), [Oracle AI Database 26ai](../../technologies/oracle/oracle-ai-database-26ai.md) |
| [Teradata](../../platforms/platform-teradata.md) | In-database analytics / ClearScape Analytics | [Teradata Bring Your Own Model (BYOM)](../../technologies/teradata/teradata-byom.md), [Teradata in-database analytics functions](../../technologies/teradata/teradata-in-database-analytics.md) |
