---
type: Technology
id: oracle-heatwave-automl-genai
title: MySQL HeatWave AutoML and HeatWave GenAI
description: In-database machine learning and generative AI routines in MySQL HeatWave, covering model training and scoring, embeddings, a vector store, RAG and natural-language to SQL.
aliases: [HeatWave AutoML, HeatWave GenAI]
platform: platform-oracle
kind: feature
availability: ga
realises: [in-database-ml, automl, vector-search, retrieval-augmented-generation, model-explainability]
resource: https://dev.mysql.com/doc/mysql-analytics/en/
tags: [oracle]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Called through SQL routines such as ML_TRAIN, ML_PREDICT_TABLE, ML_GENERATE, NL_SQL and VECTOR_STORE_LOAD. Models and LLMs run inside the HeatWave cluster, so data does not leave the service.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) (Machine learning development) (primary): Train and run models using SQL inside the data platform.
- [AutoML](../../capabilities/machine-learning/automl.md) (Machine learning development): Try features, algorithms and settings automatically to produce a good baseline model with little code.
- [Vector search](../../capabilities/generative-ai/vector-search.md) (Generative AI): Store embeddings and find the most similar items quickly.
- [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) (Generative AI): Ground model answers in your own content by retrieving relevant passages at query time.
- [Model explainability](../../capabilities/machine-learning/model-explainability.md) (Machine learning development): Explain which inputs drive a model's predictions, overall and for individual predictions.

**Platform:** [Oracle](../../platforms/platform-oracle.md)  
**Availability:** ga  
**Product family:** HeatWave

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift ML](../aws/aws-redshift-ml.md) | [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery ML](../google-cloud/gcp-bigquery-ml.md) | [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md), [Model explainability](../../capabilities/machine-learning/model-explainability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Functions](../snowflake/snowflake-ml-functions.md) | [AutoML](../../capabilities/machine-learning/automl.md), [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata in-database analytics functions](../teradata/teradata-in-database-analytics.md), [Teradata Bring Your Own Model (BYOM)](../teradata/teradata-byom.md) | [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [pgvector](../open-source/pgvector.md), [Qdrant](../open-source/qdrant.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [H2O.ai Platform (Driverless AI and h2oGPTe)](../independent/h2o-ai.md) | [AutoML](../../capabilities/machine-learning/automl.md), [Model explainability](../../capabilities/machine-learning/model-explainability.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
