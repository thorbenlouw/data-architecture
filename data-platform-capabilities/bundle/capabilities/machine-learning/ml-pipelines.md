---
type: Capability
id: ml-pipelines
title: ML pipelines
description: Automate the steps from data preparation to training and evaluation as repeatable pipelines.
aliases: [training pipelines]
broader: [machine-learning]
related: [continuous-training, ml-cicd, data-quality-rules, experiment-tracking, asset-based-orchestration]
depends_on: [workflow-orchestration]
tags: [machine-learning]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A pipeline chains the steps of building a model, such as extracting data, validating it, computing features, training, evaluating and registering, into a workflow that runs the same way every time. Each step runs in a defined environment, passes versioned outputs to the next, and records what it did. A weekly demand-forecast pipeline might pull the latest sales, check row counts and distributions, retrain, compare the new model with the current one on the last four weeks, and register it only if it is better.

Pipelines turn a notebook result into something another person can rerun, on new data, on a schedule, and they are the basis for continuous training. They can run on general workflow orchestrators or on ML pipeline tools that add artefact tracking, caching of unchanged steps and GPU scheduling. An ML pipeline differs from a data pipeline mainly in its outputs and checks: it produces models and evaluation reports, and it must stop on poor model quality, not only on bad data.

# Key considerations

- Build the pipeline early in a project. Converting notebooks at the end is where many models stall.
- Cache step outputs keyed by their inputs and code, so reruns skip unchanged work.
- Validate data before training, so a broken upstream feed fails the pipeline instead of producing a bad model.
- Use the same orchestrator as data pipelines where possible, so dependencies between data jobs and model jobs are visible in one place.

# Questions to ask

- How are models retrained today, and could anyone do it if the original author left?
- Do model pipelines depend on data pipelines owned by other teams?
- Are step caching or GPU scheduling needed, or would the existing orchestrator do?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Machine learning development](machine-learning.md) |
| Broader | [Machine learning development](machine-learning.md) |
| Related | [CI/CD for machine learning](../mlops/ml-cicd.md), [Continuous training](../mlops/continuous-training.md), [Data quality rules](../data-quality/data-quality-rules.md), [Data-aware orchestration](../orchestration/asset-based-orchestration.md), [Experiment tracking](experiment-tracking.md) |
| Depends on | [Workflow orchestration](../orchestration/workflow-orchestration.md) |
| Needed by | [Continuous training](../mlops/continuous-training.md) |

# Where it appears

- **Use cases:** [Demand forecasting](../../use-cases/usecase-demand-forecasting.md) (requires, level 3)
- **Personas:** [ML engineer](../../personas/persona-ml-engineer.md)
- **Maturity tracks:** [ML development](../../maturity/track-ml-development.md) (from level 3, Defined)
- **Frameworks:** [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Level 1 – ML pipeline automation · [Microsoft MLOps maturity model](../../frameworks/framework-microsoft-mlops-maturity.md): Level 2 – Automated training

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Pipelines](../../technologies/aws/aws-sagemaker-pipelines.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning](../../technologies/microsoft/azure-machine-learning.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform Pipelines](../../technologies/google-cloud/gcp-agent-platform-pipelines.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake ML Jobs](../../technologies/snowflake/snowflake-ml-jobs.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Data Science](../../technologies/oracle/oracle-oci-data-science.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata AI Studio](../../technologies/teradata/teradata-ai-studio.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [DVC (Data Version Control)](../../technologies/open-source/dvc.md), [Kubeflow](../../technologies/open-source/kubeflow.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Dataiku](../../technologies/independent/dataiku.md) |
