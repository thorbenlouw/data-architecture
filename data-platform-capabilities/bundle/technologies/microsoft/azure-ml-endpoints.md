---
type: Technology
id: azure-ml-endpoints
title: Azure Machine Learning online and batch endpoints
description: Deploys models to managed real-time endpoints with traffic splitting and mirroring, or to batch endpoints that score large datasets.
aliases: [Azure Machine Learning managed online endpoints, Kubernetes online endpoints]
platform: platform-microsoft
kind: feature
availability: ga
realises:
- real-time-inference
- batch-inference
- canary-ab-testing
- shadow-deployment
- generative-model-serving
- edge-inference
resource: https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Mirrored traffic supports shadow testing and traffic percentages support canary releases. Managed online endpoints can also host open-weight language models from the model catalogue on GPU virtual machines. Kubernetes online endpoints run on AKS or Azure Arc-enabled clusters, so models can be served on premises or at edge sites while deployments are managed from Azure.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Real-time inference](../../capabilities/mlops/real-time-inference.md) (ML operations) (primary): Serve predictions through low-latency endpoints.
- [Batch inference](../../capabilities/mlops/batch-inference.md) (ML operations): Score large datasets with a model on a schedule.
- [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md) (ML operations): Route a share of live traffic to a new model and compare outcomes before full rollout.
- [Shadow deployment](../../capabilities/mlops/shadow-deployment.md) (ML operations): Run a new model on live traffic without acting on its outputs, to compare it with the production model.
- [Generative model serving](../../capabilities/mlops/generative-model-serving.md) (ML operations): Host open-weight or fine-tuned language and multimodal models on dedicated accelerators, tuned for token throughput, response latency and cost.
- [Edge inference](../../capabilities/mlops/edge-inference.md) (ML operations): Run models on devices or local sites close to where data is produced, with updates managed centrally.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Azure Machine Learning

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker AI inference](../aws/aws-sagemaker-inference.md) | [Batch inference](../../capabilities/mlops/batch-inference.md), [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Endpoints](../google-cloud/gcp-agent-platform-endpoints.md) | [Batch inference](../../capabilities/mlops/batch-inference.md), [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Model Serving in Snowpark Container Services](../snowflake/snowflake-model-serving.md) | [Batch inference](../../capabilities/mlops/batch-inference.md), [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md), [Shadow deployment](../../capabilities/mlops/shadow-deployment.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Model Serving](../databricks/databricks-model-serving.md) | [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Inference service](../cloudera/cloudera-ai-inference-service.md) | [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Container Runtime](../sas/sas-container-runtime.md) | [Edge inference](../../capabilities/mlops/edge-inference.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Deployer and API nodes](../dataiku/dataiku-deployer.md) | [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [KServe](../open-source/kserve.md), [vLLM](../open-source/vllm.md), [Ray](../open-source/ray.md) | [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md), [Batch inference](../../capabilities/mlops/batch-inference.md) |
