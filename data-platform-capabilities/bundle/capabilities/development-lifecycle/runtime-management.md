---
type: Capability
id: runtime-management
title: Runtime and environment management
description: Define, version and upgrade the engine runtimes, libraries and images that notebooks, jobs and model serving run on, so code reruns the same way and upgrades do not break it.
aliases:
- runtime versions
- library management
- dependency management
- dependency pinning
- base images
- ML runtimes
- package mirrors
- upgrade management
broader: [development-lifecycle, platform-operations, machine-learning]
related: [ci-cd, infrastructure-as-code, container-services, experiment-tracking, data-testing]
depends_on: [version-control]
tags: [development-lifecycle]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Every notebook, job and model endpoint runs on a stack of versions: the engine release, such as Spark or Airflow, the language runtime, libraries and drivers, and often a vendor runtime that bundles them. The platform lets teams define that stack once, as a curated runtime, a lock file or a container image, give it a version and attach it to work. A fraud model trained on version 7 of a shared training environment is then served from the same definition, so a library upgrade elsewhere cannot change its behaviour. Serverless services often upgrade the engine underneath you and let you choose only an environment version for libraries.

Data and ML code lives for years. A pipeline untouched since 2022 can break when its runtime reaches end of support, when a library changes behaviour or when a default such as ANSI SQL mode changes, and a notebook may not rerun because a library moved. Without an inventory, upgrades wait until a security fix forces a rushed project. Schema change management handles table structures; container services run containers; this capability decides what software the work runs on and keeps it reproducible.

# Key considerations

- Keep an inventory of runtime and library versions per job and endpoint, taken from platform telemetry rather than documentation.
- Pin exact versions in lock files or images. Version ranges resolve differently next month and can change results without any error.
- Test upgrades on representative jobs and compare outputs, not only whether they run. Changed defaults often give different results silently.
- Serve packages through an approved mirror with vulnerability and licence checks. Malicious packages on public indexes are a common attack on data teams.
- Record the environment version with every training run and deployment, so a model can be rebuilt with what it was trained on.

# Questions to ask

- How many runtime and library versions are in use across production jobs and endpoints today?
- How long did the last platform-wide runtime upgrade take, and what broke?
- Could you rerun a notebook or training job from a year ago with the same libraries?
- Must libraries come from an approved internal repository?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Development and DataOps](development-lifecycle.md) |
| Broader | [Development and DataOps](development-lifecycle.md), [Platform operations](../platform-operations/platform-operations.md), [Machine learning development](../machine-learning/machine-learning.md) |
| Related | [AI supply chain security](../security/ai-supply-chain-security.md), [CI/CD](ci-cd.md), [Container services](../compute/container-services.md), [Data pipeline testing](data-testing.md), [Experiment tracking](../machine-learning/experiment-tracking.md), [Infrastructure as code](../platform-operations/infrastructure-as-code.md) |
| Depends on | [Version control integration](version-control.md) |

# Where it appears

- **Use cases:** [Self-service domain onboarding](../../use-cases/usecase-domain-onboarding.md) (benefits from)
- **Personas:** [Data engineer](../../personas/persona-data-engineer.md) · [Data platform engineer](../../personas/persona-platform-engineer.md) · [Data scientist](../../personas/persona-data-scientist.md) · [ML engineer](../../personas/persona-ml-engineer.md)
- **Maturity tracks:** [ML development](../../maturity/track-ml-development.md) (from level 2, Managed) · [Path to live](../../maturity/track-path-to-live.md) (from level 3, Defined) · [Platform self-service](../../maturity/track-platform-self-service.md) (from level 3, Defined)
- **Frameworks:** [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Level 1 – ML pipeline automation

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon EMR on EC2](../../technologies/aws/aws-emr-on-ec2.md), [Amazon EMR Serverless](../../technologies/aws/aws-emr-serverless.md), [Amazon Managed Workflows for Apache Airflow](../../technologies/aws/aws-mwaa.md), [AWS Glue ETL](../../technologies/aws/aws-glue-etl.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Apache Spark in Microsoft Fabric](../../technologies/microsoft/fabric-spark.md), [Azure Machine Learning registries and MLflow tracking](../../technologies/microsoft/azure-ml-registries-mlflow.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Managed Service for Apache Airflow](../../technologies/google-cloud/gcp-managed-airflow.md), [Google Cloud Managed Service for Apache Spark serverless](../../technologies/google-cloud/gcp-managed-spark-serverless.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Container Runtime for ML](../../technologies/snowflake/snowflake-container-runtime.md), [Snowpark](../../technologies/snowflake/snowflake-snowpark.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks classic compute (Databricks Runtime clusters)](../../technologies/databricks/databricks-classic-compute.md), [Databricks serverless compute](../../technologies/databricks/databricks-serverless-compute.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera AI Workbench](../../technologies/cloudera/cloudera-ai-workbench.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Data Science](../../technologies/oracle/oracle-oci-data-science.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Dataiku](../../technologies/independent/dataiku.md), [Domino Enterprise AI Platform](../../technologies/independent/domino-enterprise-ai-platform.md) |
