---
type: Technology
id: labelbox
title: Labelbox
description: Labelling and data curation software together with an expert network (Alignerr) that produces preference, rubric and evaluation data for model training.
platform: platform-independent
vendor: Labelbox
kind: saas
availability: ga
realises: [data-labelling, genai-evaluation, training-dataset-management]
resource: https://labelbox.com/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

In 2026 Labelbox leads with services for frontier AI labs, such as Horizon RL environments and Terra robotics data, rather than its self-service annotation tool, so check what is offered for enterprise labelling. Its catalogue is used to search, curate and version the data sent for labelling.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data labelling](../../capabilities/machine-learning/data-labelling.md) (Machine learning development) (primary): Create and manage labelled examples for supervised learning, using people, rules or models.
- [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) (Generative AI): Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges.
- [Training and evaluation dataset management](../../capabilities/machine-learning/training-dataset-management.md) (Machine learning development): Assemble, version, document and govern the datasets used to train, validate and test models, including evaluation sets for generative AI.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning data labeling](../microsoft/azure-ml-data-labeling.md) | [Data labelling](../../capabilities/machine-learning/data-labelling.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Data Labeling on Agent Platform](../google-cloud/gcp-data-labeling.md) | [Data labelling](../../capabilities/machine-learning/data-labelling.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Agent Evaluation (MLflow GenAI evaluation)](../databricks/databricks-agent-evaluation.md) | [Data labelling](../../capabilities/machine-learning/data-labelling.md), [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Training and evaluation dataset management](../../capabilities/machine-learning/training-dataset-management.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [Langfuse](../clickhouse/clickhouse-langfuse.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Training and evaluation dataset management](../../capabilities/machine-learning/training-dataset-management.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku labeling](../dataiku/dataiku-labeling.md) | [Data labelling](../../capabilities/machine-learning/data-labelling.md) |
