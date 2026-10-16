---
type: Capability
id: canary-ab-testing
title: Canary and A/B testing
description: Route a share of live traffic to a new model and compare outcomes before full rollout.
aliases: [traffic splitting, online experiments]
broader: [model-release-strategies]
related: [shadow-deployment, champion-challenger, real-time-inference, model-performance-monitoring]
depends_on: [inference-logging]
tags: [mlops]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Both methods send a share of live traffic to the new model and act on its predictions. A canary release starts small, say 1 per cent of requests, watches errors, latency and early quality signals, and raises the share in steps, rolling back automatically if a threshold is breached. An A/B test splits users or requests between versions in fixed proportions long enough to measure a difference in a business outcome such as conversion rate.

A canary asks whether the new version is safe; an A/B test asks whether it is better. Both need a router in front of the model, consistent assignment so the same user sees the same version, and logs recording which version served each request. They measure what shadow cannot: the effect of acting on predictions. The cost is that some users get a worse model for a while. Multi-armed bandits are a variant that shift traffic towards the better version during the test, trading statistical clarity for less exposure.

# Key considerations

- Assign by user or account rather than by request when experience should be consistent or outcomes are measured per person.
- Work out the sample size needed to detect the expected difference before starting. Stopping early when results look good produces false wins.
- Automate canary rollback on clear service thresholds, so a bad release is withdrawn without waiting for a person.
- Check for interference when several tests run on the same users at the same time.

# Questions to ask

- Which business metric decides whether the new model is better, and how large a difference matters?
- How much traffic is available, and how long would a test need to run?
- Can some customers be exposed to an unproven model, and with what safeguards?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [ML operations](mlops.md) |
| Broader | [Model release strategies](model-release-strategies.md) |
| Related | [Champion-challenger](champion-challenger.md), [Experimentation and causal measurement](../analytics-bi/experimentation.md), [Model performance monitoring](model-performance-monitoring.md), [Real-time inference](real-time-inference.md), [Shadow deployment](shadow-deployment.md) |
| Depends on | [Inference logging](inference-logging.md) |

# Where it appears

- **Use cases:** [Personalised recommendations](../../use-cases/usecase-recommendations.md) (requires, level 3)
- **Personas:** [ML engineer](../../personas/persona-ml-engineer.md)
- **Maturity tracks:** [MLOps](../../maturity/track-mlops.md) (from level 4, Measured)
- **Frameworks:** [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Model validation

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Bedrock AgentCore Evaluations](../../technologies/aws/aws-bedrock-agentcore-evaluations.md), [Amazon SageMaker AI inference](../../technologies/aws/aws-sagemaker-inference.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning online and batch endpoints](../../technologies/microsoft/azure-ml-endpoints.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform Endpoints](../../technologies/google-cloud/gcp-agent-platform-endpoints.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Model Serving in Snowpark Container Services](../../technologies/snowflake/snowflake-model-serving.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Model Serving](../../technologies/databricks/databricks-model-serving.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera AI Inference service](../../technologies/cloudera/cloudera-ai-inference-service.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [KServe](../../technologies/open-source/kserve.md) |
