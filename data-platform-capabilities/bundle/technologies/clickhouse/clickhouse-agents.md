---
type: Technology
id: clickhouse-agents
title: ClickHouse Agents
description: Managed agent service in ClickHouse Cloud with a chat interface, no-code agent builder, skills, memory, sandboxed code execution and MCP tool access, using Claude models by default.
platform: platform-clickhouse
kind: managed-service
availability: preview
realises: [ai-agents, conversational-analytics, agent-tool-access, agent-runtime, agent-memory]
resource: https://clickhouse.com/docs/products/cloud/features/ai-ml/agents
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Public beta from June 2026, governed by Cloud RBAC; extended to Managed Postgres in July 2026, and chats can be traced in Langfuse. It is built on LibreChat, the open-source chat platform ClickHouse acquired in November 2025, which remains available for self-hosting.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI) (primary): Build systems in which models plan, call tools and act over several steps to complete a task.
- [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) (Analytics and BI): Ask questions of data in natural language and get answers, charts or SQL back.
- [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) (Generative AI): Give agents governed access to data and actions through tools and protocols such as MCP.
- [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md) (Generative AI): Deploy and run agents as managed services with identity, durable state, scaling and sandboxed code execution.
- [Agent memory](../../capabilities/generative-ai/agent-memory.md) (Generative AI): Store and recall conversation state and long-term facts for agents across sessions, with retention controls.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** preview  
**Product family:** ClickHouse Cloud, ClickHouse Agentic Data Stack

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore](../aws/aws-bedrock-agentcore.md), [Amazon Quick](../aws/aws-quick.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Foundry Agent Service](../microsoft/azure-foundry-agent-service.md), [Microsoft Agent Framework](../microsoft/azure-agent-framework.md), [Fabric operations agent](../microsoft/fabric-operations-agent.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Agent Development Kit](../google-cloud/gcp-agent-development-kit.md), [BigQuery conversational analytics](../google-cloud/gcp-bigquery-conversational-analytics.md), [Gemini Enterprise](../google-cloud/gcp-gemini-enterprise.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Agents](../snowflake/snowflake-cortex-agents.md), [Snowflake CoWork](../snowflake/snowflake-cowork.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Agent Bricks](../databricks/databricks-agent-bricks.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica AI Agent Engineering](../informatica/informatica-ai-agent-engineering.md) (unconfirmed), [CLAIRE Agents](../informatica/informatica-claire-agents.md), [CLAIRE Data Quality Agent](../informatica/informatica-claire-data-quality-agent.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Agent Studio](../cloudera/cloudera-agent-studio.md) (preview) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Select AI Agent and Autonomous AI Database MCP Server](../oracle/oracle-select-ai-agent.md), [Oracle AI Database Private Agent Factory](../oracle/oracle-ai-private-agent-factory.md), [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule and Joule agents](../sap/sap-joule.md), [SAP Joule Studio](../sap/sap-joule-studio.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise AgentStack](../teradata/teradata-agentstack.md) (preview), [Teradata Tera](../teradata/teradata-tera.md) (preview) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Intelligence](../ibm/confluent-intelligence.md) (preview), [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Chatbot Studio](../palantir/palantir-aip-chatbot-studio.md), [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Agentic AI Accelerator](../sas/sas-agentic-ai-accelerator.md), [SAS Intelligent Decisioning](../sas/sas-intelligent-decisioning.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Visual Agents and Code Agents](../dataiku/dataiku-agents.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [LangGraph](../open-source/langgraph.md), [LangChain](../open-source/langchain.md), [LlamaIndex](../open-source/llamaindex.md) | [Agent memory](../../capabilities/generative-ai/agent-memory.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redpanda Agentic Data Plane](../independent/redpanda-agentic-data-plane.md) (unconfirmed), [Tableau Next](../independent/tableau-next.md), [ThoughtSpot Spotter](../independent/thoughtspot-spotter.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
