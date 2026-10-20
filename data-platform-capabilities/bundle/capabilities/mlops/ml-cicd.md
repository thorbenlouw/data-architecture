---
type: Capability
id: ml-cicd
title: CI/CD for machine learning
description: Test and promote model code, pipelines and models through environments automatically.
broader: [mlops, ci-cd]
related: [environment-promotion, data-testing, infrastructure-as-code, ml-pipelines, model-registry]
depends_on: [version-control]
tags: [mlops]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Three things change in an ML system: code, data and models, and each needs automated checks. A change to feature code triggers unit tests and a run on a sample dataset. A change to the training pipeline triggers a full training run in a test environment. A newly trained model triggers evaluation checks, a load test of its serving package and promotion to staging. Promotion to production follows the same automated path, with approvals where policy requires them.

Ordinary software CI/CD tests code against fixed expectations. ML adds statistical tests, such as whether accuracy fell, and artefacts that are large and come from long jobs rather than builds that take seconds. There are two promotion styles. One promotes the trained model artefact from environment to environment, which is simpler and ships exactly what was tested. The other promotes code and retrains in each environment on that environment's data, which suits cases where production data cannot be used in lower environments.

# Key considerations

- Decide early whether to promote model artefacts or code. It determines what is tested and where production data is needed.
- Separate fast checks on every commit from slow training and evaluation runs triggered on merge or on a schedule.
- Test the serving package, not only the model: dependency versions, input schemas and latency under load.
- Keep pipeline definitions, environment configuration and approval rules in version control.

# Questions to ask

- How many manual steps and people stand between a merged change and a model in production today?
- Can production data be used in development and test environments?
- Which approvals are mandatory before a model goes live?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [ML operations](mlops.md) |
| Broader | [ML operations](mlops.md), [CI/CD](../development-lifecycle/ci-cd.md) |
| Related | [Development and DataOps](../development-lifecycle/development-lifecycle.md), [Data pipeline testing](../development-lifecycle/data-testing.md), [Environment promotion](../development-lifecycle/environment-promotion.md), [Infrastructure as code](../platform-operations/infrastructure-as-code.md), [ML pipelines](../machine-learning/ml-pipelines.md), [Model deployment](model-deployment.md), [Model registry](../machine-learning/model-registry.md) |
| Depends on | [Version control integration](../development-lifecycle/version-control.md) |

# Where it appears

- **Personas:** [ML engineer](../../personas/persona-ml-engineer.md)
- **Maturity tracks:** [MLOps](../../maturity/track-mlops.md) (from level 4, Measured) · [Path to live](../../maturity/track-path-to-live.md) (from level 4, Measured)
- **Frameworks:** [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 17 – Quality management system · [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Level 2 – CI/CD pipeline automation · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Clause 8 – Operation; Annex A.6 – AI system life cycle · [Microsoft MLOps maturity model](../../frameworks/framework-microsoft-mlops-maturity.md): Level 3 – Automated model deployment

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Pipelines](../../technologies/aws/aws-sagemaker-pipelines.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning registries and MLflow tracking](../../technologies/microsoft/azure-ml-registries-mlflow.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Managed MLflow on Databricks](../../technologies/databricks/databricks-managed-mlflow.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Modeling Objectives and model assets](../../technologies/palantir/palantir-modeling-objectives.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS Model Manager](../../technologies/sas/sas-model-manager.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku Deployer and API nodes](../../technologies/dataiku/dataiku-deployer.md) |
