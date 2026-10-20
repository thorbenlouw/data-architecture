---
type: Technology
id: dataiku-labeling
title: Dataiku labeling
description: Labeling recipe in which people classify or annotate images, text and tabular records to create training data.
aliases: [Labeling recipe]
platform: platform-dataiku
kind: feature
availability: ga
realises: [data-labelling]
resource: https://doc.dataiku.com/dss/latest/machine-learning/labeling.html
tags: [dataiku]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

Image tasks cover classification and object detection, and text tasks cover classification and span annotation. The recipe sits in the Flow and exposes the annotations as a labels dataset that Visual ML can train on. The separate ML-assisted Labeling plugin adds active learning, ranking unlabelled tabular rows and images by model uncertainty so the most informative are labelled first.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data labelling](../../capabilities/machine-learning/data-labelling.md) (Machine learning development) (primary): Create and manage labelled examples for supervised learning, using people, rules or models.

**Platform:** [Dataiku](../../platforms/platform-dataiku.md)  
**Availability:** ga  
**Product family:** Dataiku Platform for AI Success

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning data labeling](../microsoft/azure-ml-data-labeling.md) | [Data labelling](../../capabilities/machine-learning/data-labelling.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Data Labeling on Agent Platform](../google-cloud/gcp-data-labeling.md) | [Data labelling](../../capabilities/machine-learning/data-labelling.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Agent Evaluation (MLflow GenAI evaluation)](../databricks/databricks-agent-evaluation.md) | [Data labelling](../../capabilities/machine-learning/data-labelling.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Labelbox](../independent/labelbox.md), [Snorkel AI](../independent/snorkel-ai.md), [Scale Data Engine](../independent/scale-data-engine.md) | [Data labelling](../../capabilities/machine-learning/data-labelling.md) |
