---
type: Technology
id: teradata-modelops
title: Teradata ModelOps
description: Model lifecycle service that validates, deploys and monitors in-database and imported models, with drift alerts, a feature catalogue and audit trails of the data used.
platform: platform-teradata
kind: feature
availability: ga
realises: [model-deployment, drift-detection, model-governance, model-registry, model-performance-monitoring]
resource: https://www.teradata.com/platform/modelops
tags: [teradata]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Works with Bring Your Own Model (BYOM), which scores PMML, ONNX, H2O and similar models inside the database. Part of AI Studio.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Model deployment](../../capabilities/mlops/model-deployment.md) (ML operations) (primary): Package and release models into production for batch, real-time or streaming use.
- [Drift detection](../../capabilities/mlops/drift-detection.md) (ML operations): Detect when live input data, or its relationship to outcomes, moves away from what the model was trained on.
- [Model governance](../../capabilities/mlops/model-governance.md) (ML operations): Keep an inventory of models with owners, approvals, documentation and risk ratings throughout their life.
- [Model registry](../../capabilities/machine-learning/model-registry.md) (Machine learning development): Version, document and manage the lifecycle of trained models from candidate to production.
- [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) (ML operations): Measure prediction quality over time against ground truth as it arrives.

**Platform:** [Teradata](../../platforms/platform-teradata.md)  
**Availability:** ga  
**Product family:** Teradata AI Studio

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Databricks](../../platforms/platform-databricks.md) | [Models in Unity Catalog](../databricks/databricks-models-in-unity-catalog.md) | [Model governance](../../capabilities/mlops/model-governance.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [Model deployment](../../capabilities/mlops/model-deployment.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Modeling Objectives and model assets](../palantir/palantir-modeling-objectives.md) | [Model deployment](../../capabilities/mlops/model-deployment.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [DataRobot AI Platform](../independent/datarobot-ai-platform.md), [Domino Enterprise AI Platform](../independent/domino-enterprise-ai-platform.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model deployment](../../capabilities/mlops/model-deployment.md), [Model governance](../../capabilities/mlops/model-governance.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
