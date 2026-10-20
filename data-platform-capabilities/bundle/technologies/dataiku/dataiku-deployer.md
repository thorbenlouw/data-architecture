---
type: Technology
id: dataiku-deployer
title: Dataiku Deployer and API nodes
description: Deployment of project bundles to automation nodes and of models and functions as real-time API services on API nodes, Kubernetes or external machine learning platforms, with several endpoint versions able to share traffic.
aliases: [Project Deployer, API Deployer, API node, Automation node]
platform: platform-dataiku
kind: feature
availability: ga
realises: [environment-promotion, real-time-inference, canary-ab-testing, ml-cicd, inference-logging]
resource: https://doc.dataiku.com/dss/latest/deployment/index.html
tags: [dataiku]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

Bundles carry a project from design to automation nodes, and Govern deployment policies can require a final approval before release. API services can also be deployed to Amazon SageMaker, Azure Machine Learning, Google Vertex AI, Databricks and Snowflake Snowpark Container Services, though only one endpoint per service is exposed there. On API nodes, traffic can be split between endpoint versions by probability for A/B tests, and query logs record which version answered each request. Version 15.1 added an activity monitoring screen for agents deployed with the Project Deployer.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) (Development and DataOps) (primary): Promote the same artefacts through development, test and production with environment-specific configuration.
- [Real-time inference](../../capabilities/mlops/real-time-inference.md) (ML operations): Serve predictions through low-latency endpoints.
- [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md) (ML operations): Route a share of live traffic to a new model and compare outcomes before full rollout.
- [CI/CD for machine learning](../../capabilities/mlops/ml-cicd.md) (ML operations): Test and promote model code, pipelines and models through environments automatically.
- [Inference logging](../../capabilities/mlops/inference-logging.md) (ML operations): Capture model inputs, outputs and metadata for monitoring, audit and retraining.

**Platform:** [Dataiku](../../platforms/platform-dataiku.md)  
**Availability:** ga  
**Product family:** Dataiku Platform for AI Success

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS CloudFormation](../aws/aws-cloudformation.md), [AWS CodePipeline](../aws/aws-codepipeline.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric variable library](../microsoft/fabric-variable-library.md), [Fabric deployment pipelines](../microsoft/fabric-deployment-pipelines.md), [fabric-cicd](../microsoft/fabric-cicd-library.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Build](../google-cloud/gcp-cloud-build.md), [Agent Platform Endpoints](../google-cloud/gcp-agent-platform-endpoints.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md), [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Inference logging](../../capabilities/mlops/inference-logging.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake CLI](../snowflake/snowflake-cli.md), [Snowflake DCM Projects](../snowflake/snowflake-dcm-projects.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Declarative Automation Bundles](../databricks/databricks-declarative-automation-bundles.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Terraform provider](../clickhouse/clickhouse-terraform.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir DevOps and Marketplace](../palantir/palantir-devops-marketplace.md), [Palantir Global Branching](../palantir/palantir-global-branching.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [SQLMesh](../open-source/sqlmesh.md), [KServe](../open-source/kserve.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md), [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Inference logging](../../capabilities/mlops/inference-logging.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt platform](../independent/dbt-platform.md), [Dagster+](../independent/dagster-plus.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
