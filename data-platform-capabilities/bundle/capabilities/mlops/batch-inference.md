---
type: Capability
id: batch-inference
title: Batch inference
description: Score large datasets with a model on a schedule.
aliases: [batch scoring]
broader: [model-deployment]
related: [offline-feature-store, user-defined-functions, workflow-orchestration, reverse-etl, in-database-ml]
tags: [mlops]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A nightly job scores every active customer for churn risk and writes the scores, with the model version and run date, to a table that a marketing tool reads in the morning. That is batch inference: a model applied to a whole dataset at once, run as a scheduled job on distributed or in-database compute. It is often written as a user-defined function applied across a table, so the work spreads across a cluster.

It is the cheapest and simplest serving pattern, and it suits any decision that can use predictions a few hours or a day old, which covers more cases than teams expect. Failures are easier to handle, since a failed job can rerun before anyone uses the output. The costs are staleness and wasted work scoring entities nobody looks at. A common hybrid precomputes batch scores and serves them from a key-value store, giving applications fast lookups without a live model.

# Key considerations

- Store the model version, feature snapshot and run time with every prediction, so results can be traced and compared.
- Compute features with the same logic as training, ideally from the same offline feature tables.
- Check output row counts and score distributions before publishing, so a broken run does not overwrite good predictions.
- Large models over large tables may need GPU batch jobs. Weigh the cost against how often scores really change.

# Questions to ask

- How fresh must predictions be for the decision they support?
- Where are predictions used: BI, operational tools or applications?
- How many entities are scored per run, and how long may the job take?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [ML operations](mlops.md) |
| Broader | [Model deployment](model-deployment.md) |
| Related | [In-database machine learning](../machine-learning/in-database-ml.md), [Offline feature store](../machine-learning/offline-feature-store.md), [Reverse ETL](../serving/reverse-etl.md), [User-defined functions and procedures](../processing/user-defined-functions.md), [Workflow orchestration](../orchestration/workflow-orchestration.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (requires, level 3) · [Demand forecasting](../../use-cases/usecase-demand-forecasting.md) (requires, level 3) · [Marketing audience activation](../../use-cases/usecase-marketing-activation.md) (benefits from)
- **Patterns:** [Feature, training and inference pipelines](../../patterns/fti-pipelines.md)
- **Personas:** [ML engineer](../../personas/persona-ml-engineer.md)
- **Maturity tracks:** [MLOps](../../maturity/track-mlops.md) (from level 1, Initial)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Redshift ML](../../technologies/aws/aws-redshift-ml.md), [Amazon SageMaker AI inference](../../technologies/aws/aws-sagemaker-inference.md), [Amazon SageMaker Canvas](../../technologies/aws/aws-sagemaker-canvas.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning online and batch endpoints](../../technologies/microsoft/azure-ml-endpoints.md), [Data Science in Microsoft Fabric](../../technologies/microsoft/fabric-data-science.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform Endpoints](../../technologies/google-cloud/gcp-agent-platform-endpoints.md), [BigQuery ML](../../technologies/google-cloud/gcp-bigquery-ml.md), [Dataflow ML](../../technologies/google-cloud/gcp-dataflow-ml.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Model Registry](../../technologies/snowflake/snowflake-model-registry.md), [Snowflake Model Serving in Snowpark Container Services](../../technologies/snowflake/snowflake-model-serving.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks AI Functions](../../technologies/databricks/databricks-ai-functions.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Bring Your Own Model (BYOM)](../../technologies/teradata/teradata-byom.md), [Teradata Elastic Python Compute](../../technologies/teradata/teradata-elastic-python-compute.md) |
| [SAS](../../platforms/platform-sas.md) | In-database scoring | [SAS Data Accelerator](../../technologies/sas/sas-data-accelerator.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku Visual ML](../../technologies/dataiku/dataiku-visual-ml.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Ray](../../technologies/open-source/ray.md), [vLLM](../../technologies/open-source/vllm.md) |
