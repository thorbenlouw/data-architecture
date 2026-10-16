---
type: Technology
id: dataiku
title: Dataiku
description: Collaborative platform for data preparation, visual and code-based machine learning, AutoML, deployment, monitoring and building AI agents, used by both analysts and data scientists.
aliases: [Dataiku DSS]
platform: platform-independent
vendor: Dataiku
kind: software
availability: ga
realises:
- data-preparation
- automl
- ml-pipelines
- model-governance
- ai-agents
- data-consumer-portal
- agent-registry
- runtime-management
resource: https://www.dataiku.com/product/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Dataiku Govern provides model registries, approvals and monitoring. Agent Hub and Agent Management cover building agents and managing their lifecycle, and Cobuild is a natural-language interface. Code environments fix the Python and R packages that each project uses. It pushes computation down to Snowflake, Databricks and other engines. Runs as Dataiku Cloud or self-managed. Its generative AI gateway is [Dataiku LLM Mesh](../independent/dataiku-llm-mesh.md).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Self-service data preparation](../../capabilities/processing/data-preparation.md) (Processing and transformation) (primary): Let analysts profile, clean and reshape data interactively without engineering help.
- [AutoML](../../capabilities/machine-learning/automl.md) (Machine learning development): Try features, algorithms and settings automatically to produce a good baseline model with little code.
- [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) (Machine learning development): Automate the steps from data preparation to training and evaluation as repeatable pipelines.
- [Model governance](../../capabilities/mlops/model-governance.md) (ML operations): Keep an inventory of models with owners, approvals, documentation and risk ratings throughout their life.
- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI): Build systems in which models plan, call tools and act over several steps to complete a task.
- [Data consumer portal](../../capabilities/analytics-bi/data-consumer-portal.md) (Analytics and BI): Give business users one place to find the dashboards, apps and AI agents shared with them, without engineering tools.
- [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) (Generative AI): Keep a governed inventory of agents, tools and MCP servers with owners and permissions so they can be found, approved and controlled.
- [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) (Development and DataOps): Define, version and upgrade the engine runtimes, libraries and images that notebooks, jobs and model serving run on, so code reruns the same way and upgrades do not break it.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue DataBrew](../aws/aws-glue-databrew.md), [Amazon SageMaker Canvas](../aws/aws-sagemaker-canvas.md) | [Self-service data preparation](../../capabilities/processing/data-preparation.md), [AutoML](../../capabilities/machine-learning/automl.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Dataflow Gen2](../microsoft/fabric-dataflow-gen2.md) | [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery data preparation](../google-cloud/gcp-bigquery-data-preparation.md) (preview), [Cloud Data Fusion](../google-cloud/gcp-data-fusion.md) | [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Designer](../databricks/databricks-lakeflow-designer.md) | [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud](../oracle/oracle-analytics-cloud.md) | [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Contour and Quiver](../palantir/palantir-contour-quiver.md) | [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [pandas](../open-source/pandas.md) | [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
