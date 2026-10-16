---
type: Technology
id: scale-data-engine
title: Scale Data Engine
description: Managed labelling and training data production that combines human experts and model assistance, covering computer vision, text, preference and evaluation data.
platform: platform-independent
vendor: Scale AI
kind: saas
availability: ga
realises: [data-labelling, genai-evaluation, model-customisation, ai-red-teaming, training-dataset-management]
resource: https://scale.com/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Meta took a large minority stake in Scale in 2025, and some model builders then reconsidered using it. The Scale GenAI Platform and Scale Donovan (defence) are separate products.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data labelling](../../capabilities/machine-learning/data-labelling.md) (Machine learning development) (primary): Create and manage labelled examples for supervised learning, using people, rules or models.
- [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) (Generative AI): Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges.
- [Model customisation](../../capabilities/generative-ai/model-customisation.md) (Generative AI): Adapt foundation models to a domain through fine-tuning, distillation or further training.
- [AI red teaming](../../capabilities/generative-ai/ai-red-teaming.md) (Generative AI): Probe models and agents adversarially for prompt injection, jailbreaks and unsafe behaviour before and after release.
- [Training and evaluation dataset management](../../capabilities/machine-learning/training-dataset-management.md) (Machine learning development): Assemble, version, document and govern the datasets used to train, validate and test models, including evaluation sets for generative AI.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning data labeling](../microsoft/azure-ml-data-labeling.md), [Microsoft Foundry evaluations](../microsoft/azure-foundry-evaluations.md) | [Data labelling](../../capabilities/machine-learning/data-labelling.md), [AI red teaming](../../capabilities/generative-ai/ai-red-teaming.md), [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Data Labeling on Agent Platform](../google-cloud/gcp-data-labeling.md) | [Data labelling](../../capabilities/machine-learning/data-labelling.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Agent Evaluation (MLflow GenAI evaluation)](../databricks/databricks-agent-evaluation.md) | [Data labelling](../../capabilities/machine-learning/data-labelling.md), [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Training and evaluation dataset management](../../capabilities/machine-learning/training-dataset-management.md) |
