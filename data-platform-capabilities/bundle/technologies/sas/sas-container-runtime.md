---
type: Technology
id: sas-container-runtime
title: SAS Container Runtime
description: Packaging of SAS and Python models and decisions as lightweight OCI containers with a REST scoring endpoint that run on any container platform without a SAS Viya deployment.
aliases: [SCR]
platform: platform-sas
kind: feature
availability: ga
realises: [real-time-inference, edge-inference]
resource: https://support.sas.com/en/software/container-runtime.html
tags: [sas]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:10:17Z'}
---

Each image holds one model or decision and has no run-time dependency on SAS Viya; SAS Viya publishes images to container registries in Azure, AWS, Google Cloud or a private Docker registry from [SAS Model Manager](sas-model-manager.md) or [SAS Intelligent Decisioning](sas-intelligent-decisioning.md). Inside SAS Viya, the separate SAS Micro Analytic Service scores the same models and decisions in real time.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Real-time inference](../../capabilities/mlops/real-time-inference.md) (ML operations) (primary): Serve predictions through low-latency endpoints.
- [Edge inference](../../capabilities/mlops/edge-inference.md) (ML operations): Run models on devices or local sites close to where data is produced, with updates managed centrally.

**Platform:** [SAS](../../platforms/platform-sas.md)  
**Availability:** ga  
**Product family:** SAS Viya

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker AI inference](../aws/aws-sagemaker-inference.md) | [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning online and batch endpoints](../microsoft/azure-ml-endpoints.md) | [Edge inference](../../capabilities/mlops/edge-inference.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Endpoints](../google-cloud/gcp-agent-platform-endpoints.md) | [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Model Serving in Snowpark Container Services](../snowflake/snowflake-model-serving.md) | [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Model Serving](../databricks/databricks-model-serving.md) | [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Inference service](../cloudera/cloudera-ai-inference-service.md) | [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Deployer and API nodes](../dataiku/dataiku-deployer.md) | [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [KServe](../open-source/kserve.md), [vLLM](../open-source/vllm.md), [Ray](../open-source/ray.md) | [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
