---
type: Capability
id: retrieval-augmented-generation
title: Retrieval-augmented generation
description: Ground model answers in your own content by retrieving relevant passages at query time.
aliases: [RAG, grounded generation, grounding, knowledge bases]
broader: [generative-ai]
related:
- knowledge-graphs
- ai-context-layer
- unstructured-data-quality
- genai-evaluation
- unstructured-lineage
depends_on: [foundation-model-access, vector-search]
tags: [generative-ai]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

When a question arrives, the system searches a knowledge source for relevant passages, places them in the model's prompt with instructions to answer from them, and returns the answer with citations. The model supplies language and reasoning; the retrieved passages supply the facts. For example, an HR assistant asked about parental leave retrieves the current policy sections for the employee's country and answers with links to them, rather than relying on training data.

This is the usual way to use private or frequently changing content without retraining a model. Designs range from a single search per question, through hybrid search with reranking and query rewriting, to agentic retrieval where the model runs several searches and decides when it has enough. Structured sources can be queried with SQL or traversed as a knowledge graph rather than searched as text. Larger context windows reduce, but do not remove, the need to choose content. Fine-tuning changes how a model behaves; retrieval changes what it knows at the moment of answering.

# Key considerations

- Evaluate retrieval separately from generation. If the right passage is not retrieved, no prompt change will fix the answer.
- Require citations and check that each one points to content that was actually retrieved, so users can verify answers.
- Outdated or conflicting documents produce confident wrong answers. Content ownership and clean-up matter as much as the technology.
- Retrieved text is untrusted input. Instructions hidden in a document can steer the model, so limit what the model can do with them.
- Apply the user's permissions when retrieving, not only when content is loaded into the index.

# Questions to ask

- Which content sources must answers draw on, and who owns each one?
- How soon after a source document changes must answers reflect it?
- Do users need citations they can check, for example for regulated advice?
- Is some of the needed information structured data that is better queried than searched?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Generative AI](generative-ai.md) |
| Broader | [Generative AI](generative-ai.md) |
| Narrower | [Permission-aware retrieval](permission-aware-retrieval.md), [Retrieval pipelines](retrieval-pipelines.md) |
| Related | [AI context layer](../metadata/ai-context-layer.md), [Document and unstructured lineage](../metadata/unstructured-lineage.md), [Full-text search](../specialised-data/full-text-search.md), [Generative AI evaluation](genai-evaluation.md), [Graph data](../specialised-data/graph-data.md), [Knowledge graphs](../specialised-data/knowledge-graphs.md), [Unstructured data quality](../data-quality/unstructured-data-quality.md), [Vector search](vector-search.md) |
| Depends on | [Foundation model access](foundation-model-access.md), [Vector search](vector-search.md) |

# Where it appears

- **Use cases:** [Agentic process automation](../../use-cases/usecase-agentic-automation.md) (requires, level 2)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md)
- **Maturity tracks:** [Generative AI](../../maturity/track-genai.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Bedrock Knowledge Bases | [Amazon Bedrock Knowledge Bases](../../technologies/aws/aws-bedrock-knowledge-bases.md), [Amazon Q Business](../../technologies/aws/aws-q-business.md) (deprecated) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Foundry IQ knowledge bases; agentic retrieval | [Foundry IQ](../../technologies/microsoft/azure-foundry-iq.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | RAG Engine; Agent Search (formerly Vertex AI Search) | [Agent Platform RAG Engine](../../technologies/google-cloud/gcp-rag-engine.md), [Google Cloud Agent Search](../../technologies/google-cloud/gcp-agent-search.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Cortex Knowledge Extensions](../../technologies/snowflake/snowflake-cortex-knowledge-extensions.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Agent Bricks Knowledge Assistant and Supervisor Agent](../../technologies/databricks/databricks-knowledge-assistant-supervisor-agent.md) (deprecated) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica AI recipes (Application Integration)](../../technologies/informatica/informatica-ai-recipes.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera AI Studios (RAG, Fine Tuning and Synthetic Data Studios)](../../technologies/cloudera/cloudera-ai-studios.md) (preview) |
| [Oracle](../../platforms/platform-oracle.md) |  | [MySQL HeatWave AutoML and HeatWave GenAI](../../technologies/oracle/oracle-heatwave-automl-genai.md), [Oracle AI Database Private Agent Factory](../../technologies/oracle/oracle-ai-private-agent-factory.md), [Oracle AI Vector Search](../../technologies/oracle/oracle-ai-vector-search.md), [Oracle Select AI](../../technologies/oracle/oracle-select-ai.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP HANA Cloud vector engine](../../technologies/sap/sap-hana-cloud-vector-engine.md), [SAP Knowledge Graph](../../technologies/sap/sap-knowledge-graph.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Enterprise Vector Store](../../technologies/teradata/teradata-enterprise-vector-store.md) |
| [IBM](../../platforms/platform-ibm.md) | OpenRAG | [OpenSearch and OpenRAG in IBM watsonx.data](../../technologies/ibm/ibm-watsonx-data-opensearch-openrag.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [AIP Chatbot Studio](../../technologies/palantir/palantir-aip-chatbot-studio.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [LangChain](../../technologies/open-source/langchain.md), [LlamaIndex](../../technologies/open-source/llamaindex.md), [Milvus](../../technologies/open-source/milvus.md), [pgvector](../../technologies/open-source/pgvector.md), [Qdrant](../../technologies/open-source/qdrant.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [H2O.ai Platform (Driverless AI and h2oGPTe)](../../technologies/independent/h2o-ai.md), [Pinecone](../../technologies/independent/pinecone.md) |

Narrower capabilities are realised by a further 28 technologies; see their pages.
