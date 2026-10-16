---
type: Persona
id: persona-ml-engineer
title: ML engineer
description: Takes models to production and keeps them running reliably.
cares_about:
- model-deployment
- real-time-inference
- batch-inference
- model-registry
- ml-pipelines
- ml-cicd
- model-monitoring
- drift-detection
- inference-logging
- model-performance-monitoring
- online-feature-store
- feature-store
- continuous-training
- shadow-deployment
- canary-ab-testing
- champion-challenger
- model-lineage
- runtime-management
- generative-model-serving
- gpu-compute
- container-services
- streaming-inference
- model-governance
- experiment-tracking
- ai-supply-chain-security
patterns: [fti-pipelines]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ML engineers usually come from software or data engineering. They work in a central ML platform team or alongside data scientists in a product team, and build the training and inference pipelines, deployment and serving infrastructure, monitoring and retraining that keep models working once they are live.

Success is a release path in which a new model version is tested, reviewed and deployed automatically, meets its latency and availability targets, is monitored for drift and quality, and can be rolled back in minutes. Every one-off, hand-built deployment is a likely future incident.

# Goals

- Make releasing a new model version routine and reversible.
- Keep production models within their latency, availability and quality targets.
- Detect drift and respond before it affects business outcomes.
- Keep training and serving features consistent.

# Jobs

- Turn notebook code into tested ML pipelines.
- Package and deploy models for batch, real-time or streaming inference.
- Set up model monitoring, inference logging and alerts.
- Run shadow, canary and champion-challenger releases.
- Automate retraining and promotion through environments.
- Maintain the feature store and model registry.
- Host open-weight and fine-tuned language models on GPUs and tune them for throughput, latency and cost.
- Maintain the base images and approved library sets that training jobs and serving endpoints use.

# Pain points

- Models arrive as notebooks with hidden dependencies and manual steps.
- Ground truth arrives late, so performance problems surface weeks after drift starts.
- Online and offline feature logic diverge over time.
- GPU serving is expensive and capacity is limited.
- Approval and documentation steps for models are manual.
- Each team builds its own serving stack for open-weight language models, and GPUs sit idle between peaks.

# Questions they ask

- Batch, real-time or streaming inference for this model, given how its predictions are used?
- How do we serve features online with exactly the logic used in training?
- Which release strategy and rollback plan does this model's risk level call for?
- What must we log for audit and retraining, and for how long?
- Should we host this open-weight model ourselves or call a provider endpoint, given volume, latency and data terms?
- Can this model file from a public hub be loaded safely, and who approved it?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities they rely on most

| Capability | Domain | What it does |
|---|---|---|
| [Model deployment](../capabilities/mlops/model-deployment.md) | [ML operations](../capabilities/mlops/mlops.md) | Package and release models into production for batch, real-time or streaming use. |
| [Real-time inference](../capabilities/mlops/real-time-inference.md) | [ML operations](../capabilities/mlops/mlops.md) | Serve predictions through low-latency endpoints. |
| [Batch inference](../capabilities/mlops/batch-inference.md) | [ML operations](../capabilities/mlops/mlops.md) | Score large datasets with a model on a schedule. |
| [Model registry](../capabilities/machine-learning/model-registry.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | Version, document and manage the lifecycle of trained models from candidate to production. |
| [ML pipelines](../capabilities/machine-learning/ml-pipelines.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | Automate the steps from data preparation to training and evaluation as repeatable pipelines. |
| [CI/CD for machine learning](../capabilities/mlops/ml-cicd.md) | [ML operations](../capabilities/mlops/mlops.md) | Test and promote model code, pipelines and models through environments automatically. |
| [Model monitoring](../capabilities/mlops/model-monitoring.md) | [ML operations](../capabilities/mlops/mlops.md) | Track the health of production models, including inputs, outputs, quality and service metrics. |
| [Drift detection](../capabilities/mlops/drift-detection.md) | [ML operations](../capabilities/mlops/mlops.md) | Detect when live input data, or its relationship to outcomes, moves away from what the model was trained on. |
| [Inference logging](../capabilities/mlops/inference-logging.md) | [ML operations](../capabilities/mlops/mlops.md) | Capture model inputs, outputs and metadata for monitoring, audit and retraining. |
| [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md) | [ML operations](../capabilities/mlops/mlops.md) | Measure prediction quality over time against ground truth as it arrives. |
| [Online feature store](../capabilities/machine-learning/online-feature-store.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | Serve the latest feature values to models in milliseconds. |
| [Feature store](../capabilities/machine-learning/feature-store.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | Manage features centrally so they are reused, documented and served consistently for training and inference. |
| [Continuous training](../capabilities/mlops/continuous-training.md) | [ML operations](../capabilities/mlops/mlops.md) | Retrain and redeploy models automatically when data, drift or schedules call for it. |
| [Shadow deployment](../capabilities/mlops/shadow-deployment.md) | [ML operations](../capabilities/mlops/mlops.md) | Run a new model on live traffic without acting on its outputs, to compare it with the production model. |
| [Canary and A/B testing](../capabilities/mlops/canary-ab-testing.md) | [ML operations](../capabilities/mlops/mlops.md) | Route a share of live traffic to a new model and compare outcomes before full rollout. |
| [Champion-challenger](../capabilities/mlops/champion-challenger.md) | [ML operations](../capabilities/mlops/mlops.md) | Run challenger models alongside the champion and promote a challenger when it proves better. |
| [Model lineage](../capabilities/metadata/model-lineage.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Track the data, features, code and runs behind each model and its predictions. |
| [Runtime and environment management](../capabilities/development-lifecycle/runtime-management.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | Define, version and upgrade the engine runtimes, libraries and images that notebooks, jobs and model serving run on, so code reruns the same way and upgrades do not break it. |
| [Generative model serving](../capabilities/mlops/generative-model-serving.md) | [ML operations](../capabilities/mlops/mlops.md) | Host open-weight or fine-tuned language and multimodal models on dedicated accelerators, tuned for token throughput, response latency and cost. |
| [GPU and accelerated compute](../capabilities/compute/gpu-compute.md) | [Query and compute](../capabilities/compute/compute.md) | Use GPUs or other accelerators for model training, inference and accelerated data processing. |
| [Container services](../capabilities/compute/container-services.md) | [Query and compute](../capabilities/compute/compute.md) | Run custom containerised applications and services next to the data, inside the platform's security boundary. |
| [Streaming inference](../capabilities/mlops/streaming-inference.md) | [ML operations](../capabilities/mlops/mlops.md) | Apply models to events as they flow through a stream. |
| [Model governance](../capabilities/mlops/model-governance.md) | [ML operations](../capabilities/mlops/mlops.md) | Keep an inventory of models with owners, approvals, documentation and risk ratings throughout their life. |
| [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | Record parameters, code versions, data and metrics for each training run so results can be compared and reproduced. |
| [AI supply chain security](../capabilities/security/ai-supply-chain-security.md) | [Security and access](../capabilities/security/security.md) | Check third-party models, model files, libraries and tool servers for tampering and malicious code before use, and record what each AI system is built from. |

# Patterns

- [Feature, training and inference pipelines](../patterns/fti-pipelines.md)

# Use cases they take part in

- [Churn prediction](../use-cases/usecase-churn-prediction.md): Score customers regularly by likelihood to leave so teams can act before they do.
- [Credit decisioning](../use-cases/usecase-credit-decisioning.md): Score credit applications and decide to approve, decline or refer them, with reasons, fairness checks and model risk controls.
- [Demand forecasting](../use-cases/usecase-demand-forecasting.md): Forecast demand by product, location and time to plan stock, staff and supply.
- [IoT predictive maintenance](../use-cases/usecase-iot-predictive-maintenance.md): Analyse sensor telemetry to predict equipment failures before they happen.
- [Personalised recommendations](../use-cases/usecase-recommendations.md): Recommend products or content to each user in real time.
- [Real-time fraud detection](../use-cases/usecase-fraud-detection.md): Score transactions in milliseconds and block or flag suspicious ones.

# Frameworks they work with

- [EU AI Act](../frameworks/framework-eu-ai-act.md): Regulation (EU) 2024/1689, which sets risk-based rules for placing AI systems and general-purpose AI models on the EU market and using them.
- [Google Cloud MLOps levels](../frameworks/framework-google-mlops-levels.md): Google Cloud's three-level description of how far an organisation has automated the building, training and release of machine learning systems.
- [ISO/IEC 42001:2023](../frameworks/framework-iso-iec-42001.md): The international standard for an AI management system, setting requirements for governing AI responsibly within an organisation.
- [Microsoft MLOps maturity model](../frameworks/framework-microsoft-mlops-maturity.md): A five-level model from Microsoft that describes MLOps maturity across people, model creation, model release and application integration.
- [NIST AI Risk Management Framework (AI RMF 1.0)](../frameworks/framework-nist-ai-rmf.md): A voluntary framework for managing AI risk through four functions, Govern, Map, Measure and Manage, broken into categories and subcategories of outcomes.
