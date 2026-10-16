---
type: Capability
id: shadow-deployment
title: Shadow deployment
description: Run a new model on live traffic without acting on its outputs, to compare it with the production model.
aliases: [shadow mode, dark launch]
broader: [model-release-strategies]
related: [canary-ab-testing, champion-challenger, model-performance-monitoring, real-time-inference]
depends_on: [inference-logging]
tags: [mlops]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The new model receives a copy of the same live requests as the production model and its predictions are logged, but only the production model's answers go back to the caller. A bank testing a new fraud model can run it in shadow for two weeks, then compare for each transaction the two scores, the alerts each would have raised, and later which transactions proved fraudulent. For batch scoring, the equivalent is scoring the same input with both models and writing the new model's output to a separate table.

Shadow is the safest live test, because no decision depends on the new model. It exposes problems offline tests miss: different input data, missing features, slow responses and shifted score distributions. Its limit is that it cannot measure effects that depend on acting on predictions. A recommender in shadow cannot show whether users would have clicked its suggestions, because nobody saw them. That needs a canary or A/B test afterwards.

# Key considerations

- Copy traffic asynchronously or with strict timeouts, so failures in the shadow model cannot affect callers.
- The shadow model must not cause side effects such as sending messages, writing records or calling downstream services.
- Shadow doubles inference compute for the mirrored traffic. Sample requests if full mirroring costs too much.
- Log both predictions with a shared request id, so they can be joined to each other and to later outcomes.

# Questions to ask

- Can the serving layer copy live requests to a second model without adding latency?
- Does the model's value depend on people seeing its output, which shadow cannot measure?
- How long must shadow run to see enough cases, including rare ones such as fraud?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [ML operations](mlops.md) |
| Broader | [Model release strategies](model-release-strategies.md) |
| Related | [Canary and A/B testing](canary-ab-testing.md), [Champion-challenger](champion-challenger.md), [Model performance monitoring](model-performance-monitoring.md), [Real-time inference](real-time-inference.md) |
| Depends on | [Inference logging](inference-logging.md) |

# Where it appears

- **Use cases:** [Agentic process automation](../../use-cases/usecase-agentic-automation.md) (benefits from) · [Credit decisioning](../../use-cases/usecase-credit-decisioning.md) (benefits from) · [Document data extraction](../../use-cases/usecase-document-extraction.md) (benefits from) · [Personalised recommendations](../../use-cases/usecase-recommendations.md) (benefits from) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (benefits from)
- **Personas:** [ML engineer](../../personas/persona-ml-engineer.md)
- **Maturity tracks:** [MLOps](../../maturity/track-mlops.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker AI inference](../../technologies/aws/aws-sagemaker-inference.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning online and batch endpoints](../../technologies/microsoft/azure-ml-endpoints.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Model Serving in Snowpark Container Services](../../technologies/snowflake/snowflake-model-serving.md) |
