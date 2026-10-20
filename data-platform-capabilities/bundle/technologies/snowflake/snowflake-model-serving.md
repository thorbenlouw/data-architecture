---
type: Technology
id: snowflake-model-serving
title: Snowflake Model Serving in Snowpark Container Services
description: Deploys registry models as autoscaling CPU or GPU inference services with HTTP endpoints, with gateway-based traffic splitting for shadow and canary releases.
platform: platform-snowflake
kind: feature
availability: ga
realises: [real-time-inference, canary-ab-testing, shadow-deployment, batch-inference]
resource: https://docs.snowflake.com/en/developer-guide/snowflake-ml/model-registry/container
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Endpoints authenticate with programmatic access tokens and can use PrivateLink. A gateway in front of several services splits traffic between them by percentage for canary and A/B releases. It can also mirror a share of requests to shadow endpoints whose responses are not returned to clients; shadow traffic is in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Real-time inference](../../capabilities/mlops/real-time-inference.md) (ML operations) (primary): Serve predictions through low-latency endpoints.
- [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md) (ML operations): Route a share of live traffic to a new model and compare outcomes before full rollout.
- [Shadow deployment](../../capabilities/mlops/shadow-deployment.md) (ML operations): Run a new model on live traffic without acting on its outputs, to compare it with the production model.
- [Batch inference](../../capabilities/mlops/batch-inference.md) (ML operations): Score large datasets with a model on a schedule.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake ML

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker AI inference](../aws/aws-sagemaker-inference.md) | [Batch inference](../../capabilities/mlops/batch-inference.md), [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md), [Shadow deployment](../../capabilities/mlops/shadow-deployment.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning online and batch endpoints](../microsoft/azure-ml-endpoints.md) | [Batch inference](../../capabilities/mlops/batch-inference.md), [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md), [Shadow deployment](../../capabilities/mlops/shadow-deployment.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Endpoints](../google-cloud/gcp-agent-platform-endpoints.md) | [Batch inference](../../capabilities/mlops/batch-inference.md), [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Model Serving](../databricks/databricks-model-serving.md) | [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Inference service](../cloudera/cloudera-ai-inference-service.md) | [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Container Runtime](../sas/sas-container-runtime.md) | [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Deployer and API nodes](../dataiku/dataiku-deployer.md) | [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [KServe](../open-source/kserve.md), [vLLM](../open-source/vllm.md), [Ray](../open-source/ray.md) | [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md), [Batch inference](../../capabilities/mlops/batch-inference.md) |
