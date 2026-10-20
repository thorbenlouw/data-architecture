---
type: Technology
id: informatica-claire-agents
title: CLAIRE Agents
description: Prebuilt AI agents that plan and carry out multi-step data management work such as discovering trusted data, exploring MDM data, building ELT pipelines and writing data quality rules.
platform: platform-informatica
kind: feature
availability: ga
realises: [ai-agents, data-engineering-agents, agent-interoperability]
resource: https://www.informatica.com/blogs/new-informatica-capabilities-clear-the-path-to-ai-ready-data.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The Enterprise Discovery, Data Exploration, Data Integration (ELT) and Product Help agents became GA in Fall 2025, and the Data Quality Agent in Spring 2026. A Metadata Enrichment Agent and a Data Steward Agent were announced for Q4 2026. Support for the A2A protocol (for example with Gemini Enterprise) comes with the Fall 2026 release, and agent skills are in preview on AWS Agent Registry and Amazon Quick.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI) (primary): Build systems in which models plan, call tools and act over several steps to complete a task.
- [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) (Development and DataOps): Use AI agents that plan, build, test and repair pipelines and models from goals, under platform governance.
- [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md) (Generative AI): Let agents built on different platforms discover, delegate to and call each other through open protocols.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud, CLAIRE

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore](../aws/aws-bedrock-agentcore.md), [Amazon Quick](../aws/aws-quick.md) | [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Agent Framework](../microsoft/azure-agent-framework.md), [Foundry Agent Service](../microsoft/azure-foundry-agent-service.md), [Fabric operations agent](../microsoft/fabric-operations-agent.md) | [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Agent Development Kit](../google-cloud/gcp-agent-development-kit.md), [BigQuery conversational analytics](../google-cloud/gcp-bigquery-conversational-analytics.md), [BigQuery Data Engineering Agent](../google-cloud/gcp-bigquery-data-engineering-agent.md) | [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Agents](../snowflake/snowflake-cortex-agents.md), [Snowflake CoWork](../snowflake/snowflake-cowork.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Agent Bricks](../databricks/databricks-agent-bricks.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Agents](../clickhouse/clickhouse-agents.md) (preview) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Agent Studio](../cloudera/cloudera-agent-studio.md) (preview) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Select AI Agent and Autonomous AI Database MCP Server](../oracle/oracle-select-ai-agent.md), [Oracle AI Database Private Agent Factory](../oracle/oracle-ai-private-agent-factory.md), [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule and Joule agents](../sap/sap-joule.md), [SAP Joule Studio](../sap/sap-joule-studio.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise AgentStack](../teradata/teradata-agentstack.md) (preview), [Teradata Tera](../teradata/teradata-tera.md) (preview) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md), [Confluent Intelligence](../ibm/confluent-intelligence.md) (preview) | [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Chatbot Studio](../palantir/palantir-aip-chatbot-studio.md), [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Agentic AI Accelerator](../sas/sas-agentic-ai-accelerator.md), [SAS Intelligent Decisioning](../sas/sas-intelligent-decisioning.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Visual Agents and Code Agents](../dataiku/dataiku-agents.md) | [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [LangChain](../open-source/langchain.md), [LangGraph](../open-source/langgraph.md), [LlamaIndex](../open-source/llamaindex.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redpanda Agentic Data Plane](../independent/redpanda-agentic-data-plane.md) (unconfirmed), [ThoughtSpot Spotter](../independent/thoughtspot-spotter.md), [Alteryx One](../independent/alteryx-one.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
