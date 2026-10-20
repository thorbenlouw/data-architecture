---
type: Technology
id: databricks-agent-bricks
title: Agent Bricks
description: Databricks' platform for developing agents. It brings together agent hosting, sandboxed code execution, memory, MCP tools, retrieval, tracing, evaluation and governed model access.
platform: platform-databricks
kind: managed-service
availability: ga
realises: [ai-agents]
resource: https://docs.databricks.com/aws/en/generative-ai/agent-bricks/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Since March 2026 the Agent Bricks name has covered all Databricks AI tooling that used to carry the Mosaic AI brand, such as Agent Framework, [Model Serving](databricks-model-serving.md), [AI Search](databricks-ai-search.md) and [Agent Evaluation](databricks-agent-evaluation.md). Its no-code [Knowledge Assistant and Supervisor Agent](databricks-knowledge-assistant-supervisor-agent.md) became legacy in October 2026, and Databricks now points to [Genie Agents](databricks-genie-agents.md) for no-code agents and the [Agent Bricks CLI](databricks-agent-runtime.md) for code. Release stages vary by component.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI) (primary): Build systems in which models plan, call tools and act over several steps to complete a task.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Agent Bricks

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore](../aws/aws-bedrock-agentcore.md), [Amazon Quick](../aws/aws-quick.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Agent Framework](../microsoft/azure-agent-framework.md), [Fabric operations agent](../microsoft/fabric-operations-agent.md), [Foundry Agent Service](../microsoft/azure-foundry-agent-service.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Agent Development Kit](../google-cloud/gcp-agent-development-kit.md), [BigQuery conversational analytics](../google-cloud/gcp-bigquery-conversational-analytics.md), [Gemini Enterprise](../google-cloud/gcp-gemini-enterprise.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Agents](../snowflake/snowflake-cortex-agents.md), [Snowflake CoWork](../snowflake/snowflake-cowork.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Agents](../clickhouse/clickhouse-agents.md) (preview) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica AI Agent Engineering](../informatica/informatica-ai-agent-engineering.md) (unconfirmed), [CLAIRE Agents](../informatica/informatica-claire-agents.md), [CLAIRE Data Quality Agent](../informatica/informatica-claire-data-quality-agent.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Agent Studio](../cloudera/cloudera-agent-studio.md) (preview) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Select AI Agent and Autonomous AI Database MCP Server](../oracle/oracle-select-ai-agent.md), [Oracle AI Database Private Agent Factory](../oracle/oracle-ai-private-agent-factory.md), [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule and Joule agents](../sap/sap-joule.md), [SAP Joule Studio](../sap/sap-joule-studio.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise AgentStack](../teradata/teradata-agentstack.md) (preview), [Teradata Tera](../teradata/teradata-tera.md) (preview) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Intelligence](../ibm/confluent-intelligence.md) (preview), [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Chatbot Studio](../palantir/palantir-aip-chatbot-studio.md), [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Agentic AI Accelerator](../sas/sas-agentic-ai-accelerator.md), [SAS Intelligent Decisioning](../sas/sas-intelligent-decisioning.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Visual Agents and Code Agents](../dataiku/dataiku-agents.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [LangChain](../open-source/langchain.md), [LangGraph](../open-source/langgraph.md), [LlamaIndex](../open-source/llamaindex.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redpanda Agentic Data Plane](../independent/redpanda-agentic-data-plane.md) (unconfirmed), [ThoughtSpot Spotter](../independent/thoughtspot-spotter.md), [Alteryx One](../independent/alteryx-one.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
