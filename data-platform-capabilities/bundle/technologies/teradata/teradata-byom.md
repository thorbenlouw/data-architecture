---
type: Technology
id: teradata-byom
title: Teradata Bring Your Own Model (BYOM)
description: Database functions that score externally trained models, such as ONNX and PMML, in parallel inside Teradata without exporting data.
platform: platform-teradata
kind: feature
availability: ga
realises: [batch-inference, in-database-ml]
resource: https://www.teradata.com/platform/in-database
tags: [teradata]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ONNX support also allows embedding models to run in the database for vector generation. Usually paired with ModelOps for deployment governance.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Batch inference](../../capabilities/mlops/batch-inference.md) (ML operations) (primary): Score large datasets with a model on a schedule.
- [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) (Machine learning development): Train and run models using SQL inside the data platform.

**Platform:** [Teradata](../../platforms/platform-teradata.md)  
**Availability:** ga  
**Product family:** Teradata AI Studio

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift ML](../aws/aws-redshift-ml.md), [Amazon SageMaker Canvas](../aws/aws-sagemaker-canvas.md), [Amazon SageMaker AI inference](../aws/aws-sagemaker-inference.md) | [Batch inference](../../capabilities/mlops/batch-inference.md), [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data Science in Microsoft Fabric](../microsoft/fabric-data-science.md), [Azure Machine Learning online and batch endpoints](../microsoft/azure-ml-endpoints.md) | [Batch inference](../../capabilities/mlops/batch-inference.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery ML](../google-cloud/gcp-bigquery-ml.md), [Dataflow ML](../google-cloud/gcp-dataflow-ml.md), [Agent Platform Endpoints](../google-cloud/gcp-agent-platform-endpoints.md) | [Batch inference](../../capabilities/mlops/batch-inference.md), [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Model Registry](../snowflake/snowflake-model-registry.md), [Snowflake Model Serving in Snowpark Container Services](../snowflake/snowflake-model-serving.md) | [Batch inference](../../capabilities/mlops/batch-inference.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Functions](../databricks/databricks-ai-functions.md) | [Batch inference](../../capabilities/mlops/batch-inference.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [vLLM](../open-source/vllm.md), [Ray](../open-source/ray.md) | [Batch inference](../../capabilities/mlops/batch-inference.md) |
