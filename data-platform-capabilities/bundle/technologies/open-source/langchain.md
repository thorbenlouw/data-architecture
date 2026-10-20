---
type: Technology
id: langchain
title: LangChain
description: Framework with standard interfaces for models, tools, retrievers and vector stores for building LLM applications and agents.
platform: platform-open-source
kind: open-source
availability: ga
realises: [ai-agents, retrieval-augmented-generation, retrieval-pipelines]
resource: https://docs.langchain.com/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

MIT licence, company-led by LangChain Inc, which sells LangSmith for tracing and evaluation. LangChain 1.0 (October 2025) rebuilt its agent abstraction on LangGraph.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI) (primary): Build systems in which models plan, call tools and act over several steps to complete a task.
- [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) (Generative AI): Ground model answers in your own content by retrieving relevant passages at query time.
- [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md) (Generative AI): Parse, chunk, embed and index content, and keep indexes in step as sources change.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore](../aws/aws-bedrock-agentcore.md), [Amazon Quick](../aws/aws-quick.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Agent Framework](../microsoft/azure-agent-framework.md), [Fabric operations agent](../microsoft/fabric-operations-agent.md), [Foundry Agent Service](../microsoft/azure-foundry-agent-service.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Agent Development Kit](../google-cloud/gcp-agent-development-kit.md), [BigQuery conversational analytics](../google-cloud/gcp-bigquery-conversational-analytics.md), [Agent Platform RAG Engine](../google-cloud/gcp-rag-engine.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Agents](../snowflake/snowflake-cortex-agents.md), [Snowflake CoWork](../snowflake/snowflake-cowork.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Agent Bricks](../databricks/databricks-agent-bricks.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Agents](../clickhouse/clickhouse-agents.md) (preview) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica AI recipes (Application Integration)](../informatica/informatica-ai-recipes.md), [Informatica AI Agent Engineering](../informatica/informatica-ai-agent-engineering.md) (unconfirmed), [CLAIRE Agents](../informatica/informatica-claire-agents.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Agent Studio](../cloudera/cloudera-agent-studio.md) (preview), [Cloudera AI Studios (RAG, Fine Tuning and Synthetic Data Studios)](../cloudera/cloudera-ai-studios.md) (preview) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database Private Agent Factory](../oracle/oracle-ai-private-agent-factory.md), [Oracle Select AI Agent and Autonomous AI Database MCP Server](../oracle/oracle-select-ai-agent.md), [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule and Joule agents](../sap/sap-joule.md), [SAP Joule Studio](../sap/sap-joule-studio.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise AgentStack](../teradata/teradata-agentstack.md) (preview), [Teradata Tera](../teradata/teradata-tera.md) (preview), [Teradata Enterprise Vector Store](../teradata/teradata-enterprise-vector-store.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Retrieval pipelines](../../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Intelligence](../ibm/confluent-intelligence.md) (preview), [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Chatbot Studio](../palantir/palantir-aip-chatbot-studio.md), [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Agentic AI Accelerator](../sas/sas-agentic-ai-accelerator.md), [SAS Intelligent Decisioning](../sas/sas-intelligent-decisioning.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Visual Agents and Code Agents](../dataiku/dataiku-agents.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [H2O.ai Platform (Driverless AI and h2oGPTe)](../independent/h2o-ai.md), [Redpanda Agentic Data Plane](../independent/redpanda-agentic-data-plane.md) (unconfirmed), [ThoughtSpot Spotter](../independent/thoughtspot-spotter.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
