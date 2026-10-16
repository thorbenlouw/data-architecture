---
type: Maturity Track
id: track-mlops
title: MLOps
description: How automatically and safely models are released, run, monitored and improved in production.
covers:
- mlops
- model-deployment
- batch-inference
- real-time-inference
- streaming-inference
- model-release-strategies
- shadow-deployment
- champion-challenger
- canary-ab-testing
- model-monitoring
- drift-detection
- model-performance-monitoring
- inference-logging
- continuous-training
- ml-cicd
- model-governance
- model-lineage
- edge-inference
related_tracks: [track-ml-development, track-ai-governance, track-path-to-live, track-genai]
levels:
- level: 1
  name: Initial
  summary: Models reach production by hand, and nobody is sure which version is running (Google level 0, Microsoft level 0).
  criteria:
  - A data scientist hands a model file or notebook to engineers, who rewrite or wrap it for production.
  - Batch scores are produced by running a notebook or script by hand or from a personal schedule.
  - No record links the model in production to the code and data that trained it.
  - Model problems come to light when business users report odd outcomes.
  capabilities: [batch-inference]
  external_levels: {framework-microsoft-mlops-maturity: 0, framework-google-mlops-levels: 0}
- level: 2
  name: Managed
  summary: Data pipelines and application code are automated, but model release is a manual, team-specific procedure (Microsoft level 1).
  criteria:
  - Models are packaged in a standard format or container and deployed by a written runbook, with a named person approving each release.
  - Real-time models run behind managed endpoints with the same latency and error-rate monitoring as other services.
  - Every prediction is logged with its inputs, output, model version and timestamp.
  - Each production endpoint and batch scoring job records which model version it runs, so the running version can be looked up rather than guessed.
  - Data pipelines feeding the model and applications calling it have CI/CD, while the model itself is still copied in by hand.
  capabilities: [model-deployment, real-time-inference, inference-logging]
  external_levels: {framework-microsoft-mlops-maturity: 1, framework-google-mlops-levels: 0}
- level: 3
  name: Defined
  summary: An automated training pipeline retrains and redeploys models in production, and every deployed model traces back to its run (Google level 1, Microsoft level 2).
  criteria:
  - The training pipeline itself is deployed to production, retrains on a schedule or when new data lands, and pushes validated models to serving.
  - Each deployed model version links to its registry entry, pipeline run, training data snapshot and feature definitions.
  - Batch, real-time, streaming and edge deployments use platform templates instead of team-built serving stacks, and devices or sites receive model updates from the central registry.
  - Input feature distributions are compared with the training baseline at least daily, and drift past a set threshold alerts the owner.
  - High-risk models need a recorded approval from a reviewer outside the building team before each release.
  capabilities:
  - continuous-training
  - model-lineage
  - streaming-inference
  - model-monitoring
  - drift-detection
  - model-governance
  - edge-inference
  external_levels: {framework-microsoft-mlops-maturity: 2, framework-google-mlops-levels: 1}
- level: 4
  name: Measured
  summary: CI/CD tests and releases pipeline code and models automatically, and live prediction quality is measured against targets (Google level 2, Microsoft level 3).
  criteria:
  - A change to pipeline code triggers unit, data validation and integration tests, and a passing build deploys the pipeline to staging and production with no manual steps.
  - A candidate is promoted only when automated checks show it meets or beats the current model on agreed metrics.
  - New models run in shadow or on a small share of traffic, and the comparison is recorded before full rollout.
  - Prediction quality is measured against ground truth as it arrives, with a target per model and an alert on breach.
  - Rolling back to the previous model version is one automated action, rehearsed at least quarterly.
  capabilities:
  - ml-cicd
  - model-release-strategies
  - shadow-deployment
  - canary-ab-testing
  - model-performance-monitoring
  external_levels: {framework-microsoft-mlops-maturity: 3, framework-google-mlops-levels: 2}
- level: 5
  name: Optimising
  summary: Production monitoring feeds retraining, evaluation and promotion automatically, and people review exceptions (Microsoft level 4).
  criteria:
  - A drift or performance breach starts retraining, evaluation and challenger deployment without manual action.
  - Challengers run continuously against the champion and are promoted automatically when they win by a set margin over a set period.
  - Retraining frequency per model is tuned from its measured accuracy decay and the cost of each run.
  - Ground truth and user feedback are joined to logged predictions automatically to build the next training set.
  capabilities: [champion-challenger]
  external_levels: {framework-microsoft-mlops-maturity: 4, framework-google-mlops-levels: 2}
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up shortens the time from an approved model to a production release from weeks to hours, catches degrading models before the business notices, and makes retraining routine and evidenced. The levels follow Microsoft's MLOps maturity model one to one, from its level 0 (No MLOps) at Initial to level 4 (Full MLOps automated operations) at Optimising, with Google Cloud's three levels fitted in. Initial is Google level 0 (manual process). Managed is Microsoft level 1 (DevOps but no MLOps), which Google does not separate. Defined is Google level 1 (ML pipeline automation), where the deployed training pipeline delivers retrained models; it covers Microsoft level 2 and the automated model delivery that Microsoft places at level 3. Measured is Google level 2 and Microsoft level 3, where CI/CD builds, tests and releases the pipelines as well as the models. Optimising adds Microsoft's closed loop, in which production metrics trigger retraining and promotion. Typical blockers are the handover gap between data scientists and engineers, ground truth that arrives late or never, and release approvals designed for application code.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Models reach production by hand, and nobody is sure which version is running (Google level 0, Microsoft level 0).

- A data scientist hands a model file or notebook to engineers, who rewrite or wrap it for production.
- Batch scores are produced by running a notebook or script by hand or from a personal schedule.
- No record links the model in production to the code and data that trained it.
- Model problems come to light when business users report odd outcomes.

**Capabilities first relied on:** [Batch inference](../capabilities/mlops/batch-inference.md)

**Corresponds to:** [Microsoft MLOps maturity model](../frameworks/framework-microsoft-mlops-maturity.md) level 0; [Google Cloud MLOps levels](../frameworks/framework-google-mlops-levels.md) level 0

## Level 2: Managed

Data pipelines and application code are automated, but model release is a manual, team-specific procedure (Microsoft level 1).

- Models are packaged in a standard format or container and deployed by a written runbook, with a named person approving each release.
- Real-time models run behind managed endpoints with the same latency and error-rate monitoring as other services.
- Every prediction is logged with its inputs, output, model version and timestamp.
- Each production endpoint and batch scoring job records which model version it runs, so the running version can be looked up rather than guessed.
- Data pipelines feeding the model and applications calling it have CI/CD, while the model itself is still copied in by hand.

**Capabilities first relied on:** [Model deployment](../capabilities/mlops/model-deployment.md), [Real-time inference](../capabilities/mlops/real-time-inference.md), [Inference logging](../capabilities/mlops/inference-logging.md)

**Corresponds to:** [Microsoft MLOps maturity model](../frameworks/framework-microsoft-mlops-maturity.md) level 1; [Google Cloud MLOps levels](../frameworks/framework-google-mlops-levels.md) level 0

## Level 3: Defined

An automated training pipeline retrains and redeploys models in production, and every deployed model traces back to its run (Google level 1, Microsoft level 2).

- The training pipeline itself is deployed to production, retrains on a schedule or when new data lands, and pushes validated models to serving.
- Each deployed model version links to its registry entry, pipeline run, training data snapshot and feature definitions.
- Batch, real-time, streaming and edge deployments use platform templates instead of team-built serving stacks, and devices or sites receive model updates from the central registry.
- Input feature distributions are compared with the training baseline at least daily, and drift past a set threshold alerts the owner.
- High-risk models need a recorded approval from a reviewer outside the building team before each release.

**Capabilities first relied on:** [Continuous training](../capabilities/mlops/continuous-training.md), [Model lineage](../capabilities/metadata/model-lineage.md), [Streaming inference](../capabilities/mlops/streaming-inference.md), [Model monitoring](../capabilities/mlops/model-monitoring.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Model governance](../capabilities/mlops/model-governance.md), [Edge inference](../capabilities/mlops/edge-inference.md)

**Corresponds to:** [Microsoft MLOps maturity model](../frameworks/framework-microsoft-mlops-maturity.md) level 2; [Google Cloud MLOps levels](../frameworks/framework-google-mlops-levels.md) level 1

## Level 4: Measured

CI/CD tests and releases pipeline code and models automatically, and live prediction quality is measured against targets (Google level 2, Microsoft level 3).

- A change to pipeline code triggers unit, data validation and integration tests, and a passing build deploys the pipeline to staging and production with no manual steps.
- A candidate is promoted only when automated checks show it meets or beats the current model on agreed metrics.
- New models run in shadow or on a small share of traffic, and the comparison is recorded before full rollout.
- Prediction quality is measured against ground truth as it arrives, with a target per model and an alert on breach.
- Rolling back to the previous model version is one automated action, rehearsed at least quarterly.

**Capabilities first relied on:** [CI/CD for machine learning](../capabilities/mlops/ml-cicd.md), [Model release strategies](../capabilities/mlops/model-release-strategies.md), [Shadow deployment](../capabilities/mlops/shadow-deployment.md), [Canary and A/B testing](../capabilities/mlops/canary-ab-testing.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md)

**Corresponds to:** [Microsoft MLOps maturity model](../frameworks/framework-microsoft-mlops-maturity.md) level 3; [Google Cloud MLOps levels](../frameworks/framework-google-mlops-levels.md) level 2

## Level 5: Optimising

Production monitoring feeds retraining, evaluation and promotion automatically, and people review exceptions (Microsoft level 4).

- A drift or performance breach starts retraining, evaluation and challenger deployment without manual action.
- Challengers run continuously against the champion and are promoted automatically when they win by a set margin over a set period.
- Retraining frequency per model is tuned from its measured accuracy decay and the cost of each run.
- Ground truth and user feedback are joined to logged predictions automatically to build the next training set.

**Capabilities first relied on:** [Champion-challenger](../capabilities/mlops/champion-challenger.md)

**Corresponds to:** [Microsoft MLOps maturity model](../frameworks/framework-microsoft-mlops-maturity.md) level 4; [Google Cloud MLOps levels](../frameworks/framework-google-mlops-levels.md) level 2

# Capabilities in scope

[ML operations](../capabilities/mlops/mlops.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Canary and A/B testing](../capabilities/mlops/canary-ab-testing.md), [Champion-challenger](../capabilities/mlops/champion-challenger.md), [CI/CD for machine learning](../capabilities/mlops/ml-cicd.md), [Continuous training](../capabilities/mlops/continuous-training.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Edge inference](../capabilities/mlops/edge-inference.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Model deployment](../capabilities/mlops/model-deployment.md), [Model governance](../capabilities/mlops/model-governance.md), [Model lineage](../capabilities/metadata/model-lineage.md), [Model monitoring](../capabilities/mlops/model-monitoring.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Model release strategies](../capabilities/mlops/model-release-strategies.md), [Real-time inference](../capabilities/mlops/real-time-inference.md), [Shadow deployment](../capabilities/mlops/shadow-deployment.md), [Streaming inference](../capabilities/mlops/streaming-inference.md)

# Related tracks

- [ML development](track-ml-development.md): How repeatably the organisation turns data into trained, evaluated and documented models.
- [AI and model governance](track-ai-governance.md): How well the organisation knows its AI systems, assesses their risks and impacts, controls their behaviour and evidences this to regulators and customers.
- [Path to live](track-path-to-live.md): How safely, quickly and repeatably changes to data and AI workloads move from a developer's first commit to production.
- [Generative AI](track-genai.md): How safely and reliably the organisation builds, evaluates and runs applications that use language models and agents with its own data.

Levels follow the shared [maturity scale](maturity-scale.md).
