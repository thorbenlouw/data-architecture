---
type: Technology
id: aws-sagemaker-ground-truth
title: Amazon SageMaker Ground Truth
description: Labelling service that runs annotation jobs for images, text, video and point clouds using private, vendor or automated workforces.
platform: platform-aws
kind: feature
availability: deprecated
realises: [data-labelling]
resource: https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html
tags: [aws]
status: deprecated
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Closed to new customers from 30 July 2026; Ground Truth Plus reached end of support on 30 June 2026, and the Mechanical Turk public workforce option ended when Amazon Mechanical Turk closed on 30 September 2026. Augmented AI (A2I) is also in maintenance.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data labelling](../../capabilities/machine-learning/data-labelling.md) (Machine learning development) (primary): Create and manage labelled examples for supervised learning, using people, rules or models.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** deprecated  
**Product family:** Amazon SageMaker AI  
Not counted in platform coverage because it is deprecated.

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning data labeling](../microsoft/azure-ml-data-labeling.md) | [Data labelling](../../capabilities/machine-learning/data-labelling.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Data Labeling on Agent Platform](../google-cloud/gcp-data-labeling.md) | [Data labelling](../../capabilities/machine-learning/data-labelling.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Agent Evaluation (MLflow GenAI evaluation)](../databricks/databricks-agent-evaluation.md) | [Data labelling](../../capabilities/machine-learning/data-labelling.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Labelbox](../independent/labelbox.md), [Snorkel AI](../independent/snorkel-ai.md), [Scale Data Engine](../independent/scale-data-engine.md) | [Data labelling](../../capabilities/machine-learning/data-labelling.md) |
