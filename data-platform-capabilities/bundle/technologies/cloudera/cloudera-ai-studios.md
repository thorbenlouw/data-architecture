---
type: Technology
id: cloudera-ai-studios
title: Cloudera AI Studios (RAG, Fine Tuning and Synthetic Data Studios)
description: Low-code applications in Cloudera AI for building retrieval-augmented chat over documents, fine-tuning open models and generating synthetic datasets.
aliases: [RAG Studio, Fine Tuning Studio, Synthetic Data Studio]
platform: platform-cloudera
kind: feature
availability: preview
realises: [retrieval-augmented-generation, model-customisation, synthetic-data, retrieval-pipelines]
resource: https://docs.cloudera.com/machine-learning/cloud/use-ai-studios/index.html
tags: [cloudera]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Launched in 2025 and still labelled Technical Preview in the docs. They run as applications inside an AI Workbench project, using the workbench's compute and data access.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) (Generative AI) (primary): Ground model answers in your own content by retrieving relevant passages at query time.
- [Model customisation](../../capabilities/generative-ai/model-customisation.md) (Generative AI): Adapt foundation models to a domain through fine-tuning, distillation or further training.
- [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) (Development and DataOps): Generate artificial data that keeps the useful properties of real data without exposing real records.
- [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) (Generative AI): Parse, chunk, embed and index content, and keep indexes in step as sources change.

**Platform:** [Cloudera](../../platforms/platform-cloudera.md)  
**Availability:** preview  
**Product family:** Cloudera AI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock Knowledge Bases](../aws/aws-bedrock-knowledge-bases.md) | [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Foundry IQ](../microsoft/azure-foundry-iq.md) | [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform RAG Engine](../google-cloud/gcp-rag-engine.md), [Google Cloud Agent Search](../google-cloud/gcp-agent-search.md) | [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Knowledge Extensions](../snowflake/snowflake-cortex-knowledge-extensions.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica AI recipes (Application Integration)](../informatica/informatica-ai-recipes.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Select AI](../oracle/oracle-select-ai.md), [Oracle AI Database Private Agent Factory](../oracle/oracle-ai-private-agent-factory.md), [Oracle AI Vector Search](../oracle/oracle-ai-vector-search.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud vector engine](../sap/sap-hana-cloud-vector-engine.md), [SAP Knowledge Graph](../sap/sap-knowledge-graph.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise Vector Store](../teradata/teradata-enterprise-vector-store.md) | [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [IBM](../../platforms/platform-ibm.md) | [OpenSearch and OpenRAG in IBM watsonx.data](../ibm/ibm-watsonx-data-opensearch-openrag.md) | [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Chatbot Studio](../palantir/palantir-aip-chatbot-studio.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [LlamaIndex](../open-source/llamaindex.md), [LangChain](../open-source/langchain.md), [pgvector](../open-source/pgvector.md) | [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [H2O.ai Platform (Driverless AI and h2oGPTe)](../independent/h2o-ai.md), [Pinecone](../independent/pinecone.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
