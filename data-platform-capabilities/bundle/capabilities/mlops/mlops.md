---
type: Capability
id: mlops
title: ML operations
description: Deploy, run, monitor and improve models in production reliably.
aliases: [MLOps, model operations]
broader: []
related: [platform-observability, ci-cd, ai-governance, audit-logging, model-lineage]
depends_on: [model-registry]
order: 9
tags: [mlops]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ML operations covers a model's life after approval: putting it into production, keeping it running, noticing when it stops working and replacing it safely. A fraud model, for instance, might sit behind an endpoint that must answer within 50 milliseconds, run first in shadow beside the current model, be watched for shifts in transaction patterns, and be retrained each month as newly confirmed fraud cases arrive.

The parts follow that life. Deployment packages a model for batch, real-time or streaming use. Release strategies such as shadow, champion-challenger and canary limit the harm a worse model can do. Monitoring, built on inference logs, watches inputs, outputs, quality and service health. Continuous training and CI/CD close the loop by retraining, testing and promoting new versions automatically. Model governance runs across all of it, recording who approved what, on what evidence.

Models differ from ordinary software because they can fail silently: the service stays up and returns answers, but the answers get worse as the world changes. True outcomes often arrive weeks later, so teams watch early signals such as input drift in the meantime. Maturity is usually described in stages, from manual hand-over of model files, through automated training pipelines, to automated retraining, testing and release.

# Key considerations

- Decide who owns each production model: its builder, a platform team or the product team. Alerts without an owner go unanswered.
- Match the serving pattern to the decision. Many cases framed as real-time are well served by daily batch scores, at far lower cost and risk.
- Log inputs and outputs from the first release. Monitoring, audit, debugging and retraining all depend on them, and they cannot be recreated later.
- Plan for delayed outcomes. If true results take weeks, decide which early signals will prompt investigation meanwhile.
- Keep rollback fast. The previous model version, its features and its configuration must stay deployable.

# Questions to ask

- How quickly must predictions be returned, and at what volume?
- What would it cost the business if a model gave wrong answers unnoticed for a week?
- How long does it take today to get a new model version into production, and who has to be involved?
- Are any models subject to regulatory approval or model risk management rules?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Narrower | [CI/CD for machine learning](ml-cicd.md), [Continuous training](continuous-training.md), [Model deployment](model-deployment.md), [Model governance](model-governance.md), [Model monitoring](model-monitoring.md), [Model release strategies](model-release-strategies.md) |
| Related | [AI governance](../governance/ai-governance.md), [Audit logging](../security/audit-logging.md), [CI/CD](../development-lifecycle/ci-cd.md), [Model lineage](../metadata/model-lineage.md), [Platform observability](../platform-operations/platform-observability.md) |
| Depends on | [Model registry](../machine-learning/model-registry.md) |

# Where it appears

- **Maturity tracks:** [MLOps](../../maturity/track-mlops.md)

# How platforms provide it

No technology in this bundle realises this capability directly yet.

Narrower capabilities are realised by a further 70 technologies; see their pages.
