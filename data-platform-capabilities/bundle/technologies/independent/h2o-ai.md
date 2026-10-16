---
type: Technology
id: h2o-ai
title: H2O.ai Platform (Driverless AI and h2oGPTe)
description: Self-hostable AI platform that combines Driverless AI for AutoML with explanations and h2oGPTe for document question answering, retrieval-augmented generation and agents.
aliases: [H2O Driverless AI, Driverless AI, h2oGPTe]
platform: platform-independent
vendor: H2O.ai
kind: software
availability: ga
realises: [automl, model-explainability, retrieval-augmented-generation, ai-agents, enterprise-ai-assistant]
resource: https://h2o.ai/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Often chosen by regulated or government buyers who need on-premises or air-gapped deployment. Driverless AI automates feature engineering and tuning and exports scoring pipelines. H2O's AI Super Agent orchestrates its predictive, generative and agentic tools.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AutoML](../../capabilities/machine-learning/automl.md) (Machine learning development) (primary): Try features, algorithms and settings automatically to produce a good baseline model with little code.
- [Model explainability](../../capabilities/machine-learning/model-explainability.md) (Machine learning development): Explain which inputs drive a model's predictions, overall and for individual predictions.
- [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) (Generative AI): Ground model answers in your own content by retrieving relevant passages at query time.
- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI): Build systems in which models plan, call tools and act over several steps to complete a task.
- [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md) (Generative AI): Give staff a governed, ready-made assistant that answers questions and completes tasks across structured and unstructured enterprise data.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Autopilot](../aws/aws-sagemaker-autopilot.md), [Amazon SageMaker Canvas](../aws/aws-sagemaker-canvas.md) | [AutoML](../../capabilities/machine-learning/automl.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Automated machine learning (AutoML) in Azure Machine Learning](../microsoft/azure-ml-automl.md), [Data Science in Microsoft Fabric](../microsoft/fabric-data-science.md) | [AutoML](../../capabilities/machine-learning/automl.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform AutoML](../google-cloud/gcp-agent-platform-automl.md) | [AutoML](../../capabilities/machine-learning/automl.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Functions](../snowflake/snowflake-ml-functions.md) | [AutoML](../../capabilities/machine-learning/automl.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AutoML](../databricks/databricks-automl.md) | [AutoML](../../capabilities/machine-learning/automl.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica AI recipes (Application Integration)](../informatica/informatica-ai-recipes.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave AutoML and HeatWave GenAI](../oracle/oracle-heatwave-automl-genai.md) | [AutoML](../../capabilities/machine-learning/automl.md), [Model explainability](../../capabilities/machine-learning/model-explainability.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [AutoML](../../capabilities/machine-learning/automl.md) |
