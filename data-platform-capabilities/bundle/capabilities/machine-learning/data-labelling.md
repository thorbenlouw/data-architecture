---
type: Capability
id: data-labelling
title: Data labelling
description: Create and manage labelled examples for supervised learning, using people, rules or models.
aliases: [annotation, ground truth]
broader: [machine-learning]
related: [unstructured-data, genai-evaluation, deidentification, data-versioning, synthetic-data]
tags: [machine-learning]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Supervised models learn from examples with known answers: images marked with the objects in them, emails marked as spam or not, insurance claims marked as fraudulent. Labelling work is organised into tasks shown to annotators in an interface, with written guidelines, quality checks such as known-answer questions and agreement between annotators, and a record of who labelled what. Labels can also come from business outcomes, rules written as code, or a model that pre-labels examples for people to correct.

Label quality caps model quality, and labelling is often the slowest and most expensive part of a project. Active learning cuts cost by sending people the examples the model is least sure about. Rule-based labelling scales quickly but copies the rules' mistakes. Labelled sets are also used as test sets for generative AI. Where labels already come from business processes, such as recorded chargebacks, the work is mostly joining and cleaning data rather than annotation.

# Key considerations

- Write guidelines with examples of hard cases and revise them as disagreements appear. Ambiguous guidelines show up as noisy labels.
- Measure agreement between annotators and audit samples throughout, not only at the start.
- Annotators see raw data. Apply the same access controls, de-identification and contract terms as for any other processing, especially with external workforces.
- Version labelled datasets and guidelines together, so a model can be traced to the labels it learned from.

# Questions to ask

- Do the labels you need already exist in business systems, or must people create them?
- Does correct labelling need domain experts such as clinicians or underwriters?
- Can the data be shown to external annotators, or must labelling stay in-house?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Machine learning development](machine-learning.md) |
| Broader | [Machine learning development](machine-learning.md) |
| Related | [Data versioning](../storage/data-versioning.md), [De-identification](../governance/deidentification.md), [Document processing](../processing/document-processing.md), [Entity resolution](../master-data/entity-resolution.md), [Generative AI evaluation](../generative-ai/genai-evaluation.md), [Model customisation](../generative-ai/model-customisation.md), [Multimodal data formats](../storage/multimodal-data-formats.md), [Synthetic data generation](../development-lifecycle/synthetic-data.md), [Training and evaluation dataset management](training-dataset-management.md), [Unstructured data management](../specialised-data/unstructured-data.md) |

# Where it appears

- **Use cases:** [Document data extraction](../../use-cases/usecase-document-extraction.md) (requires, level 2) · [IoT predictive maintenance](../../use-cases/usecase-iot-predictive-maintenance.md) (requires, level 2) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (benefits from)
- **Personas:** [Data scientist](../../personas/persona-data-scientist.md)
- **Maturity tracks:** [ML development](../../maturity/track-ml-development.md) (from level 2, Managed)
- **Frameworks:** [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 10 – Data and data governance · [ISO 8000 (data quality)](../../frameworks/framework-iso-8000.md): ISO/CD TR 8000-320 – AI training data quality (in development) · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Annex A.7 – Data for AI systems

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Ground Truth](../../technologies/aws/aws-sagemaker-ground-truth.md) (deprecated) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning data labeling](../../technologies/microsoft/azure-ml-data-labeling.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Data Labeling on Agent Platform](../../technologies/google-cloud/gcp-data-labeling.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Agent Evaluation (MLflow GenAI evaluation)](../../technologies/databricks/databricks-agent-evaluation.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | Labeling | [Dataiku labeling](../../technologies/dataiku/dataiku-labeling.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Labelbox](../../technologies/independent/labelbox.md), [Scale Data Engine](../../technologies/independent/scale-data-engine.md), [Snorkel AI](../../technologies/independent/snorkel-ai.md) |
