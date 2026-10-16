---
type: Technology
id: snowflake-ml-experiments
title: Snowflake ML Experiments
description: Records runs with parameters, metrics, artefacts and logs inside experiments, with autologging for common libraries and side-by-side comparison in Snowsight.
platform: platform-snowflake
kind: feature
availability: ga
realises: [experiment-tracking]
resource: https://docs.snowflake.com/en/developer-guide/snowflake-ml/experiments
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Generally available since 19 February 2026. There are limits of 500 runs per experiment and 500 experiments per schema.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) (Machine learning development) (primary): Record parameters, code versions, data and metrics for each training run so results can be compared and reproduced.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake ML

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker AI with MLflow](../aws/aws-sagemaker-mlflow.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning registries and MLflow tracking](../microsoft/azure-ml-registries-mlflow.md), [Data Science in Microsoft Fabric](../microsoft/fabric-data-science.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Experiments on Agent Platform](../google-cloud/gcp-agent-platform-experiments.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Managed MLflow on Databricks](../databricks/databricks-managed-mlflow.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Workbench](../cloudera/cloudera-ai-workbench.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [MLflow](../open-source/mlflow.md), [DVC (Data Version Control)](../open-source/dvc.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Comet ML](../independent/comet.md), [Weights & Biases](../independent/weights-and-biases.md), [Domino Enterprise AI Platform](../independent/domino-enterprise-ai-platform.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
