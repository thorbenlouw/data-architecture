---
type: Technology
id: informatica-ai-recipes
title: Informatica AI recipes (Application Integration)
description: Prebuilt Application Integration processes for generative AI patterns such as AI agents, retrieval over documents, chat with a file, and LLM calls to several model providers.
platform: platform-informatica
kind: feature
availability: ga
realises: [retrieval-augmented-generation, ai-agents]
resource: https://onlinehelp.informatica.com/IICS/prod/CAI/en/index.htm
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

These are templates you copy and adapt, not a managed RAG service. Spring 2026 added recipes for customer support case processing, Azure OpenAI multifunction calling and Slack and Teams handlers. CDI can also prepare unstructured data for vector databases.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) (Generative AI) (primary): Ground model answers in your own content by retrieving relevant passages at query time.
- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI): Build systems in which models plan, call tools and act over several steps to complete a task.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud, Informatica Application Integration

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock Knowledge Bases](../aws/aws-bedrock-knowledge-bases.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Foundry IQ](../microsoft/azure-foundry-iq.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform RAG Engine](../google-cloud/gcp-rag-engine.md), [Google Cloud Agent Search](../google-cloud/gcp-agent-search.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Knowledge Extensions](../snowflake/snowflake-cortex-knowledge-extensions.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Agent Bricks](../databricks/databricks-agent-bricks.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Studios (RAG, Fine Tuning and Synthetic Data Studios)](../cloudera/cloudera-ai-studios.md) (preview) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database Private Agent Factory](../oracle/oracle-ai-private-agent-factory.md), [Oracle AI Vector Search](../oracle/oracle-ai-vector-search.md), [Oracle Select AI](../oracle/oracle-select-ai.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud vector engine](../sap/sap-hana-cloud-vector-engine.md), [SAP Knowledge Graph](../sap/sap-knowledge-graph.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise Vector Store](../teradata/teradata-enterprise-vector-store.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [IBM](../../platforms/platform-ibm.md) | [OpenSearch and OpenRAG in IBM watsonx.data](../ibm/ibm-watsonx-data-opensearch-openrag.md) | [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Chatbot Studio](../palantir/palantir-aip-chatbot-studio.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [LlamaIndex](../open-source/llamaindex.md), [LangChain](../open-source/langchain.md), [pgvector](../open-source/pgvector.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [H2O.ai Platform (Driverless AI and h2oGPTe)](../independent/h2o-ai.md), [Pinecone](../independent/pinecone.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
