---
type: Capability
id: embedding-generation
title: Embedding generation
description: Turn text, images or other content into vector embeddings for search and retrieval.
broader: [vector-search]
related: [foundation-model-access, retrieval-pipelines, ai-functions, gpu-compute]
tags: [generative-ai]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

An embedding model converts an input into a fixed-length vector. Text models handle sentences or passages; multimodal models place images and text in the same vector space, so a text query can find pictures. Embeddings are produced twice: in bulk over existing content, and again for each query at search time, and both must use the same model. For example, two million product descriptions are embedded overnight in batches, while each shopper's search phrase is embedded in milliseconds and compared with them.

The model choice sets retrieval quality, vector size and running cost. Embeddings can come from hosted APIs, from open-weight models on your own GPUs, or from SQL functions applied to table columns. Selection criteria include languages covered, maximum input length, vector dimensions and whether a domain-specific model exists for areas such as law or medicine. This capability produces the vectors. Storing and querying them is vector search, and deciding what to embed and when to refresh it is the work of retrieval pipelines.

# Key considerations

- Documents and queries must be embedded with the same model and version. Mixing versions makes similarity scores meaningless.
- Re-embedding a large corpus after a model upgrade costs time and money. Plan for it, and use batch interfaces or your own GPUs for bulk runs.
- Each model has an input limit. Longer text is often truncated without warning unless it is split into chunks first.
- Some models expect different instructions or modes for queries and documents. Ignoring this lowers retrieval quality noticeably.
- Evaluate candidate models on your own queries. Public leaderboard rankings often do not carry over to a specific domain.

# Questions to ask

- Which content types and languages must be embedded?
- How large is the corpus and how often does it change?
- May content be sent to an external embedding service, or must this run in-house?
- How will retrieval quality be measured to compare models?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Generative AI](generative-ai.md) |
| Broader | [Vector search](vector-search.md) |
| Related | [AI functions in SQL](../processing/ai-functions.md), [Foundation model access](foundation-model-access.md), [GPU and accelerated compute](../compute/gpu-compute.md), [Multimodal data formats](../storage/multimodal-data-formats.md), [Retrieval pipelines](retrieval-pipelines.md) |
| Needed by | [Retrieval pipelines](retrieval-pipelines.md) |

# Where it appears

- **Use cases:** [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (requires, level 2) · [Personalised recommendations](../../use-cases/usecase-recommendations.md) (benefits from)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md)
- **Maturity tracks:** [Generative AI](../../maturity/track-genai.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Bedrock](../../technologies/aws/aws-bedrock.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [AI functions in Fabric](../../technologies/microsoft/fabric-ai-functions.md), [Azure AI Search](../../technologies/microsoft/azure-ai-search.md), [Azure OpenAI in Foundry Models](../../technologies/microsoft/azure-openai.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform Vector Search](../../technologies/google-cloud/gcp-vector-search.md), [BigQuery generative AI functions](../../technologies/google-cloud/gcp-bigquery-ai-functions.md), [BigQuery vector search](../../technologies/google-cloud/gcp-bigquery-vector-search.md), [Gemini models on Agent Platform](../../technologies/google-cloud/gcp-gemini-models.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Cortex AI Functions](../../technologies/snowflake/snowflake-cortex-ai-functions.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks AI Search](../../technologies/databricks/databricks-ai-search.md), [Databricks Foundation Model APIs](../../technologies/databricks/databricks-foundation-model-apis.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse AI functions](../../technologies/clickhouse/clickhouse-ai-functions.md) (preview) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle AI Vector Search](../../technologies/oracle/oracle-ai-vector-search.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP HANA Cloud vector engine](../../technologies/sap/sap-hana-cloud-vector-engine.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Enterprise Vector Store](../../technologies/teradata/teradata-enterprise-vector-store.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Confluent Intelligence](../../technologies/ibm/confluent-intelligence.md) (preview) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku Knowledge Banks](../../technologies/dataiku/dataiku-knowledge-banks.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [MongoDB Atlas](../../technologies/independent/mongodb-atlas.md), [Pinecone](../../technologies/independent/pinecone.md), [Unstructured.io](../../technologies/independent/unstructured.md), [Weaviate Cloud](../../technologies/independent/weaviate-cloud.md) |
