---
type: Capability
id: champion-challenger
title: Champion-challenger
description: Run challenger models alongside the champion and promote a challenger when it proves better.
broader: [model-release-strategies]
related: [model-evaluation, model-governance, model-performance-monitoring, model-registry]
depends_on: [inference-logging]
tags: [mlops]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The model in production is the champion; alternatives are challengers. Challengers score the same cases, either in shadow or on a small, randomly assigned share of live decisions, and are compared with the champion over an agreed period on agreed metrics. A collections team might let the champion choose the treatment for 90 per cent of overdue accounts while two challengers handle 5 per cent each, then promote whichever recovers the most per account after three months.

The method comes from credit risk and decisioning, where it runs continuously rather than once per release: there is always a champion and usually a challenger. This gives a standing record that the production model is still the best available, which model risk teams and regulators value. It differs from a one-off A/B test mainly in being an ongoing process with formal promotion decisions. Challengers can be retrained versions, different algorithms, or simple rules that test whether the model adds value at all.

# Key considerations

- Agree the metric, sample size and comparison period before starting, and record each promotion decision with its evidence.
- Assignment to champion or challenger must be random and recorded, or differences between groups will bias the comparison.
- Include a simple rule-based challenger from time to time. It shows whether the model still justifies its complexity.
- Live challengers make real decisions about customers, so each needs the same approval as a production model.

# Questions to ask

- Do regulators or model risk teams expect evidence that the production model is still the best option?
- How long after a decision is its outcome known?
- Is there enough volume to give each challenger a statistically meaningful sample?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [ML operations](mlops.md) |
| Broader | [Model release strategies](model-release-strategies.md) |
| Related | [Canary and A/B testing](canary-ab-testing.md), [Decision management](../serving/decision-management.md), [Model evaluation](../machine-learning/model-evaluation.md), [Model governance](model-governance.md), [Model performance monitoring](model-performance-monitoring.md), [Model registry](../machine-learning/model-registry.md), [Shadow deployment](shadow-deployment.md) |
| Depends on | [Inference logging](inference-logging.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (benefits from) · [Credit decisioning](../../use-cases/usecase-credit-decisioning.md) (benefits from) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (benefits from)
- **Personas:** [ML engineer](../../personas/persona-ml-engineer.md)
- **Maturity tracks:** [MLOps](../../maturity/track-mlops.md) (from level 5, Optimising)
- **Frameworks:** [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Model validation

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Independent vendors](../../platforms/platform-independent.md) |  | [DataRobot AI Platform](../../technologies/independent/datarobot-ai-platform.md) |
