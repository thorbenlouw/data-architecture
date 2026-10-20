---
type: Technology
id: dataiku
title: Dataiku DSS
description: Platform in which teams build data pipelines, models, generative AI applications and agents as shared projects, with managed code environments, Git-based version control, containerised execution and per-user security.
aliases: [Dataiku, Data Science Studio, Platform for AI Success, Universal AI Platform]
platform: platform-dataiku
kind: software
availability: ga
realises:
- runtime-management
- version-control
- container-services
- compute-user-isolation
- secrets-management
- audit-logging
- data-consumer-portal
resource: https://www.dataiku.com/product/
tags: [dataiku]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

Code environments fix the Python and R packages each project uses. Elastic AI computation runs recipes, notebooks, model training and webapps in containers on managed Kubernetes (EKS, AKS, GKE) or OpenShift, the User Isolation Framework runs each user's code under their own identity, and an audit trail records every user action and can be sent to Kafka or the Event Server. The Secrets Manager, added in version 15.1, reads secrets from AWS, Azure or Google Cloud secret stores. Workspaces and a consumer home page give business users the dashboards, applications, webapps, datasets and wiki articles shared with them. Its generative AI gateway is [Dataiku LLM Mesh](dataiku-llm-mesh.md).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) (Development and DataOps) (primary): Define, version and upgrade the engine runtimes, libraries and images that notebooks, jobs and model serving run on, so code reruns the same way and upgrades do not break it.
- [Version control integration](../../capabilities/development-lifecycle/version-control.md) (Development and DataOps): Keep code and configuration in Git and work with branches from inside the platform.
- [Container services](../../capabilities/compute/container-services.md) (Query and compute): Run custom containerised applications and services next to the data, inside the platform's security boundary.
- [Shared compute isolation](../../capabilities/security/compute-user-isolation.md) (Security and access): Sandbox each user's code on shared compute so nobody can bypass access controls or affect other users.
- [Secrets management](../../capabilities/security/secrets-management.md) (Security and access): Store and rotate the credentials and keys used by pipelines and tools without putting them in code.
- [Audit logging](../../capabilities/security/audit-logging.md) (Security and access): Record who accessed or changed what, when and from where, and keep the records tamper-evident.
- [Data consumer portal](../../capabilities/analytics-bi/data-consumer-portal.md) (Analytics and BI): Give business users one place to find the dashboards, apps and AI agents shared with them, without engineering tools.

**Platform:** [Dataiku](../../platforms/platform-dataiku.md)  
**Availability:** ga  
**Product family:** Dataiku Platform for AI Success

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon EMR Serverless](../aws/aws-emr-serverless.md), [Amazon EMR on EC2](../aws/aws-emr-on-ec2.md), [Amazon Managed Workflows for Apache Airflow](../aws/aws-mwaa.md) | [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning registries and MLflow tracking](../microsoft/azure-ml-registries-mlflow.md), [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md) | [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Managed Service for Apache Airflow](../google-cloud/gcp-managed-airflow.md), [Google Cloud Managed Service for Apache Spark serverless](../google-cloud/gcp-managed-spark-serverless.md) | [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpark](../snowflake/snowflake-snowpark.md), [Snowflake Container Runtime for ML](../snowflake/snowflake-container-runtime.md) | [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks serverless compute](../databricks/databricks-serverless-compute.md), [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md) | [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Workbench](../cloudera/cloudera-ai-workbench.md) | [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Domino Enterprise AI Platform](../independent/domino-enterprise-ai-platform.md) | [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
