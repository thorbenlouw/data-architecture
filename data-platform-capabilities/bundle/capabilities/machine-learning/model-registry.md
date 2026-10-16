---
type: Capability
id: model-registry
title: Model registry
description: Version, document and manage the lifecycle of trained models from candidate to production.
aliases: [model catalogue]
broader: [machine-learning]
related: [model-lineage, experiment-tracking, environment-promotion, table-catalogue]
tags: [machine-learning]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A registry stores trained models as named, numbered versions, each linked to the run that produced it, its metrics, its input and output schema, documentation and approval state. A team registers fraud-detector version 14, attaches the evaluation report, has it reviewed and gives it an alias such as champion. Deployment tools then ask for the version holding that alias rather than a file path, so promotion or rollback is a change of label.

It is the hand-off point between development and operations, and where auditors look to see which version ran when. Without one, models are files in storage named final_v3_fixed. Registries range from a module of an experiment-tracking tool to part of a central catalogue that also governs tables, giving one permission model for data and models. The registry manages versions and their technical state; model governance adds risk ratings, owners, policies and approvals across the whole inventory.

# Key considerations

- Register each model with its input signature and dependencies, so serving can validate requests and rebuild the environment.
- Prefer aliases or tags resolved at release time over fixed stage names that suit only one workflow.
- Limit who can promote a version to production, and log every promotion.
- Keep the registry in the same catalogue and permission system as data where possible, so access to a model reflects access to its training data.

# Questions to ask

- How do you know today which model version is in production and who approved it?
- How many teams and models will share the registry?
- Must models move between workspaces, regions or environments?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Machine learning development](machine-learning.md) |
| Broader | [Machine learning development](machine-learning.md) |
| Related | [Agent and tool registry](../generative-ai/agent-registry.md), [AI governance](../governance/ai-governance.md), [AI supply chain security](../security/ai-supply-chain-security.md), [AI system discovery](../governance/ai-system-discovery.md), [Champion-challenger](../mlops/champion-challenger.md), [CI/CD for machine learning](../mlops/ml-cicd.md), [Environment promotion](../development-lifecycle/environment-promotion.md), [Experiment tracking](experiment-tracking.md), [Model customisation](../generative-ai/model-customisation.md), [Model lineage](../metadata/model-lineage.md), [Model release strategies](../mlops/model-release-strategies.md), [Table catalogue](../storage/table-catalogue.md) |
| Needed by | [ML operations](../mlops/mlops.md), [Continuous training](../mlops/continuous-training.md), [Edge inference](../mlops/edge-inference.md), [Model deployment](../mlops/model-deployment.md), [Model governance](../mlops/model-governance.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (requires, level 2) · [Credit decisioning](../../use-cases/usecase-credit-decisioning.md) (requires, level 3) · [Personalised recommendations](../../use-cases/usecase-recommendations.md) (requires, level 2) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (requires, level 3)
- **Patterns:** [Feature, training and inference pipelines](../../patterns/fti-pipelines.md)
- **Personas:** [Data scientist](../../personas/persona-data-scientist.md) · [ML engineer](../../personas/persona-ml-engineer.md)
- **Maturity tracks:** [ML development](../../maturity/track-ml-development.md) (from level 2, Managed)
- **Frameworks:** [DCAM v3](../../frameworks/framework-edm-dcam.md): 8 Analytics Management · [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 11 and Annex IV – Technical documentation · [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Level 2 – CI/CD pipeline automation; ML metadata management · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Annex A.6 – AI system life cycle · [Microsoft MLOps maturity model](../../frameworks/framework-microsoft-mlops-maturity.md): Level 2 – Automated training · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): MANAGE 4 – Response, recovery and communication

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Model Registry](../../technologies/aws/aws-sagemaker-model-registry.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning registries and MLflow tracking](../../technologies/microsoft/azure-ml-registries-mlflow.md), [Data Science in Microsoft Fabric](../../technologies/microsoft/fabric-data-science.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform Model Registry](../../technologies/google-cloud/gcp-agent-platform-model-registry.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Model Registry](../../technologies/snowflake/snowflake-model-registry.md) |
| [Databricks](../../platforms/platform-databricks.md) | Models in Unity Catalog | [Models in Unity Catalog](../../technologies/databricks/databricks-models-in-unity-catalog.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | AI Registry | [Cloudera AI Registry](../../technologies/cloudera/cloudera-ai-registry.md) |
| [Oracle](../../platforms/platform-oracle.md) | Model catalog | [OCI Data Science](../../technologies/oracle/oracle-oci-data-science.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata ModelOps](../../technologies/teradata/teradata-modelops.md) |
| [Palantir](../../platforms/platform-palantir.md) | Modeling Objectives | [Palantir Modeling Objectives and model assets](../../technologies/palantir/palantir-modeling-objectives.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Kubeflow](../../technologies/open-source/kubeflow.md), [MLflow](../../technologies/open-source/mlflow.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Comet ML](../../technologies/independent/comet.md), [DataRobot AI Platform](../../technologies/independent/datarobot-ai-platform.md), [Weights & Biases](../../technologies/independent/weights-and-biases.md) |
