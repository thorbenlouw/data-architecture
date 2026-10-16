---
type: Technology
id: aws-bedrock-knowledge-bases
title: Amazon Bedrock Knowledge Bases
description: Managed retrieval-augmented generation that ingests content, parses and chunks it, embeds and indexes it, and retrieves relevant passages with citations.
aliases: [Amazon Bedrock Managed Knowledge Base]
platform: platform-aws
kind: feature
availability: ga
realises:
- retrieval-augmented-generation
- retrieval-pipelines
- unstructured-ingestion
- vector-search
- permission-aware-retrieval
resource: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Two types exist. Managed Knowledge Base (GA June 2026, AWS's replacement for Kendra) runs the whole pipeline with connectors for S3, SharePoint, Confluence, Google Drive, OneDrive and web crawl, document-level ACL filtering and AgentCore Gateway integration. Customer-managed knowledge bases use your own vector store (OpenSearch Serverless, Aurora, S3 Vectors, Neptune Analytics for GraphRAG) and can also translate questions into SQL over structured stores such as Redshift.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) (Generative AI) (primary): Ground model answers in your own content by retrieving relevant passages at query time.
- [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) (Generative AI): Parse, chunk, embed and index content, and keep indexes in step as sources change.
- [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) (Ingestion and integration): Bring documents, images, audio and other unstructured content into the platform together with their metadata.
- [Vector search](../../capabilities/generative-ai/vector-search.md) (Generative AI): Store embeddings and find the most similar items quickly.
- [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md) (Generative AI): Filter retrieved content by each user's permissions in the source systems so AI answers never reveal what the user could not open.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon Bedrock

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Foundry IQ](../microsoft/azure-foundry-iq.md), [Azure AI Search](../microsoft/azure-ai-search.md) | [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Search](../google-cloud/gcp-agent-search.md), [Agent Platform RAG Engine](../google-cloud/gcp-rag-engine.md) | [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Knowledge Extensions](../snowflake/snowflake-cortex-knowledge-extensions.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica AI recipes (Application Integration)](../informatica/informatica-ai-recipes.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Studios (RAG, Fine Tuning and Synthetic Data Studios)](../cloudera/cloudera-ai-studios.md) (preview) | [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Vector Search](../oracle/oracle-ai-vector-search.md), [MySQL HeatWave AutoML and HeatWave GenAI](../oracle/oracle-heatwave-automl-genai.md), [Oracle AI Database Private Agent Factory](../oracle/oracle-ai-private-agent-factory.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud vector engine](../sap/sap-hana-cloud-vector-engine.md), [SAP Knowledge Graph](../sap/sap-knowledge-graph.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise Vector Store](../teradata/teradata-enterprise-vector-store.md) | [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [IBM](../../platforms/platform-ibm.md) | [OpenSearch and OpenRAG in IBM watsonx.data](../ibm/ibm-watsonx-data-opensearch-openrag.md) | [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Chatbot Studio](../palantir/palantir-aip-chatbot-studio.md) | [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [LlamaIndex](../open-source/llamaindex.md), [pgvector](../open-source/pgvector.md), [Qdrant](../open-source/qdrant.md) | [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Pinecone](../independent/pinecone.md), [H2O.ai Platform (Driverless AI and h2oGPTe)](../independent/h2o-ai.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
