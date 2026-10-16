---
type: Capability
id: model-deployment
title: Model deployment
description: Package and release models into production for batch, real-time or streaming use.
broader: [mlops]
related: [container-services, environment-promotion, ml-cicd, model-governance]
depends_on: [model-registry]
tags: [mlops]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A registered model does nothing until it is wired into a production process. The model, its preprocessing code and its library dependencies are packaged, often as a container image or a portable format such as ONNX, and attached to a batch job, a serving endpoint or a stream processor. A deployment record states which model version runs where, with what configuration and compute, and how to roll it back.

The serving pattern follows from how predictions are used. Nightly propensity scores loaded into a CRM suit batch; a fraud check during card authorisation needs real-time; anomaly detection on sensor events suits streaming. Deployments often fail on environment mismatch, where the model needs a library version or feature calculation that production lacks. Deployment is separate from release strategy: deployment makes a version runnable, while a release strategy decides how much live traffic it gets and when it replaces the current version.

# Key considerations

- Package preprocessing with the model or fetch features from a shared store. Recreating preprocessing in the calling application causes skew.
- Validate input schemas at the serving boundary, so malformed requests fail clearly instead of producing silent nonsense.
- Keep the previous version deployable and rehearse rollback before it is needed.
- Decide who runs the endpoint or job day to day, including out-of-hours support.

# Questions to ask

- How is each prediction consumed: in a nightly file, during a user request, or on each event?
- What latency, throughput and availability does the consuming system need?
- How long does deploying a model take today, and how many people are involved?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [ML operations](mlops.md) |
| Broader | [ML operations](mlops.md) |
| Narrower | [Batch inference](batch-inference.md), [Edge inference](edge-inference.md), [Generative model serving](generative-model-serving.md), [Real-time inference](real-time-inference.md), [Streaming inference](streaming-inference.md) |
| Related | [CI/CD for machine learning](ml-cicd.md), [Container services](../compute/container-services.md), [Data application distribution](../data-sharing/application-sharing.md), [Environment promotion](../development-lifecycle/environment-promotion.md), [Model governance](model-governance.md) |
| Depends on | [Model registry](../machine-learning/model-registry.md) |
| Needed by | [Model release strategies](model-release-strategies.md) |

# Where it appears

- **Personas:** [ML engineer](../../personas/persona-ml-engineer.md)
- **Maturity tracks:** [MLOps](../../maturity/track-mlops.md) (from level 2, Managed)
- **Frameworks:** [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Level 1 – ML pipeline automation · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Annex A.6 – AI system life cycle · [Microsoft MLOps maturity model](../../frameworks/framework-microsoft-mlops-maturity.md): Level 3 – Automated model deployment · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): MANAGE 2 – Maximising benefit and minimising harm

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [SAP](../../platforms/platform-sap.md) |  | [SAP AI Foundation (SAP AI Core and generative AI hub)](../../technologies/sap/sap-ai-foundation.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata ModelOps](../../technologies/teradata/teradata-modelops.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Modeling Objectives and model assets](../../technologies/palantir/palantir-modeling-objectives.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [DataRobot AI Platform](../../technologies/independent/datarobot-ai-platform.md), [Domino Enterprise AI Platform](../../technologies/independent/domino-enterprise-ai-platform.md) |

Narrower capabilities are realised by a further 31 technologies; see their pages.
