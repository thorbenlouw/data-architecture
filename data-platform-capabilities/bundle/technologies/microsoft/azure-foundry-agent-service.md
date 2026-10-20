---
type: Technology
id: azure-foundry-agent-service
title: Foundry Agent Service
description: A managed runtime for prompt-based and hosted code agents with tools, MCP connections, threads and publishing to Teams and Microsoft 365 Copilot.
formerly: [Azure AI Agent Service, Azure AI Foundry Agent Service]
platform: platform-microsoft
kind: managed-service
availability: ga
realises: [ai-agents, agent-tool-access, agent-runtime, agent-memory, agent-interoperability]
resource: https://learn.microsoft.com/en-us/azure/foundry/concepts/general-availability
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Core agents are GA; memory, toolboxes and routines are preview. Foundry workflows are preview and will be retired on 1 December 2026 in favour of Microsoft Agent Framework.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI) (primary): Build systems in which models plan, call tools and act over several steps to complete a task.
- [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) (Generative AI): Give agents governed access to data and actions through tools and protocols such as MCP.
- [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md) (Generative AI): Deploy and run agents as managed services with identity, durable state, scaling and sandboxed code execution.
- [Agent memory](../../capabilities/generative-ai/agent-memory.md) (Generative AI): Store and recall conversation state and long-term facts for agents across sessions, with retention controls.
- [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md) (Generative AI): Let agents built on different platforms discover, delegate to and call each other through open protocols.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Microsoft Foundry

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore](../aws/aws-bedrock-agentcore.md), [Amazon Quick](../aws/aws-quick.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md), [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Agent Development Kit](../google-cloud/gcp-agent-development-kit.md), [BigQuery conversational analytics](../google-cloud/gcp-bigquery-conversational-analytics.md), [Gemini Enterprise](../google-cloud/gcp-gemini-enterprise.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Agents](../snowflake/snowflake-cortex-agents.md), [Snowflake CoWork](../snowflake/snowflake-cowork.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Agent Bricks](../databricks/databricks-agent-bricks.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Agents](../clickhouse/clickhouse-agents.md) (preview) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica AI Agent Engineering](../informatica/informatica-ai-agent-engineering.md) (unconfirmed), [CLAIRE Agents](../informatica/informatica-claire-agents.md), [CLAIRE Data Quality Agent](../informatica/informatica-claire-data-quality-agent.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Agent Studio](../cloudera/cloudera-agent-studio.md) (preview) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Select AI Agent and Autonomous AI Database MCP Server](../oracle/oracle-select-ai-agent.md), [Oracle AI Database Private Agent Factory](../oracle/oracle-ai-private-agent-factory.md), [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule Studio](../sap/sap-joule-studio.md), [SAP Joule and Joule agents](../sap/sap-joule.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise AgentStack](../teradata/teradata-agentstack.md) (preview), [Teradata Tera](../teradata/teradata-tera.md) (preview) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md), [Confluent Intelligence](../ibm/confluent-intelligence.md) (preview) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Chatbot Studio](../palantir/palantir-aip-chatbot-studio.md), [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Agentic AI Accelerator](../sas/sas-agentic-ai-accelerator.md), [SAS Intelligent Decisioning](../sas/sas-intelligent-decisioning.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Visual Agents and Code Agents](../dataiku/dataiku-agents.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [LangGraph](../open-source/langgraph.md), [LangChain](../open-source/langchain.md), [LlamaIndex](../open-source/llamaindex.md) | [Agent memory](../../capabilities/generative-ai/agent-memory.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redpanda Agentic Data Plane](../independent/redpanda-agentic-data-plane.md) (unconfirmed), [LangSmith](../independent/langsmith.md), [Tableau Next](../independent/tableau-next.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md) |
