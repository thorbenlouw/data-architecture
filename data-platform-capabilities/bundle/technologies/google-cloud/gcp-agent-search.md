---
type: Technology
id: gcp-agent-search
title: Google Cloud Agent Search
description: Managed enterprise search and retrieval over websites, documents, structured data and connected applications, used to ground agents and chat applications.
aliases: [Agent Search, Agent Search for Commerce]
formerly: [Vertex AI Search, AI Applications, Vertex AI Search and Conversation, Generative AI App Builder]
platform: platform-google-cloud
kind: managed-service
availability: ga
realises:
- retrieval-augmented-generation
- retrieval-pipelines
- vector-search
- permission-aware-retrieval
- full-text-search
resource: https://docs.cloud.google.com/generative-ai-app-builder/docs/introduction
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Handles parsing, chunking, embedding and ranking internally, and also offers recommendations and media and healthcare (FHIR) search; the API is still Discovery Engine. Gemini Enterprise uses the same search technology for employee-facing search.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) (Generative AI) (primary): Ground model answers in your own content by retrieving relevant passages at query time.
- [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) (Generative AI): Parse, chunk, embed and index content, and keep indexes in step as sources change.
- [Vector search](../../capabilities/generative-ai/vector-search.md) (Generative AI): Store embeddings and find the most similar items quickly.
- [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md) (Generative AI): Filter retrieved content by each user's permissions in the source systems so AI answers never reveal what the user could not open.
- [Full-text search](../../capabilities/specialised-data/full-text-search.md) (Specialised data types): Index text for full-text search, relevance ranking and fast filtering.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Gemini Enterprise Agent Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock Knowledge Bases](../aws/aws-bedrock-knowledge-bases.md) | [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Foundry IQ](../microsoft/azure-foundry-iq.md), [Azure AI Search](../microsoft/azure-ai-search.md) | [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Full-text search](../../capabilities/specialised-data/full-text-search.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Knowledge Extensions](../snowflake/snowflake-cortex-knowledge-extensions.md), [Snowflake Cortex Search](../snowflake/snowflake-cortex-search.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Search](../databricks/databricks-ai-search.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica AI recipes (Application Integration)](../informatica/informatica-ai-recipes.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Studios (RAG, Fine Tuning and Synthetic Data Studios)](../cloudera/cloudera-ai-studios.md) (preview) | [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Vector Search](../oracle/oracle-ai-vector-search.md), [MySQL HeatWave AutoML and HeatWave GenAI](../oracle/oracle-heatwave-automl-genai.md), [Oracle AI Database Private Agent Factory](../oracle/oracle-ai-private-agent-factory.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud vector engine](../sap/sap-hana-cloud-vector-engine.md), [SAP Knowledge Graph](../sap/sap-knowledge-graph.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise Vector Store](../teradata/teradata-enterprise-vector-store.md) | [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [IBM](../../platforms/platform-ibm.md) | [OpenSearch and OpenRAG in IBM watsonx.data](../ibm/ibm-watsonx-data-opensearch-openrag.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Chatbot Studio](../palantir/palantir-aip-chatbot-studio.md) | [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Milvus](../open-source/milvus.md), [LlamaIndex](../open-source/llamaindex.md), [pgvector](../open-source/pgvector.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Pinecone](../independent/pinecone.md), [H2O.ai Platform (Driverless AI and h2oGPTe)](../independent/h2o-ai.md) | [Full-text search](../../capabilities/specialised-data/full-text-search.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
