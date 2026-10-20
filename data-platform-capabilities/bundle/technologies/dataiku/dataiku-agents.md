---
type: Technology
id: dataiku-agents
title: Dataiku Visual Agents and Code Agents
description: Agents built visually or in Python on the LLM Mesh, using managed tools, knowledge banks, semantic models and MCP tools, with human approval steps, tracing, evaluation and MCP and A2A servers for other systems.
aliases: [Visual Agents, Code Agents, Structured Visual Agents, Agent Skills]
platform: platform-dataiku
kind: feature
availability: ga
realises:
- ai-agents
- agent-tool-access
- human-oversight
- genai-observability
- genai-evaluation
- agent-interoperability
resource: https://doc.dataiku.com/dss/latest/agents/index.html
tags: [dataiku]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

Structured Visual Agents, human-in-the-loop approval and calls to external agents arrived in version 14.4, and Agent Skills and an MCP server that exposes agents and tools in 15.0; the A2A server supports versions 0.3 and 1.0 of the protocol. Agent Review and Agent Evaluation test agents against expected answers and, since 15.1, simulated multi-turn users. Agents built on Snowflake Cortex, Databricks, Amazon Bedrock and Google Vertex AI can be called as external agents.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI) (primary): Build systems in which models plan, call tools and act over several steps to complete a task.
- [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) (Generative AI): Give agents governed access to data and actions through tools and protocols such as MCP.
- [Human oversight of AI](../../capabilities/governance/human-oversight.md) (Governance and compliance): Route model and agent decisions to people for review, approval or override, and let them pause or stop a system.
- [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) (Generative AI): Trace model and agent calls with their prompts, responses, latency, cost and user feedback.
- [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) (Generative AI): Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges.
- [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md) (Generative AI): Let agents built on different platforms discover, delegate to and call each other through open protocols.

**Platform:** [Dataiku](../../platforms/platform-dataiku.md)  
**Availability:** ga  
**Product family:** Dataiku Platform for AI Success

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore](../aws/aws-bedrock-agentcore.md), [Amazon Quick](../aws/aws-quick.md) | [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Foundry Agent Service](../microsoft/azure-foundry-agent-service.md), [Microsoft Agent Framework](../microsoft/azure-agent-framework.md), [Fabric operations agent](../microsoft/fabric-operations-agent.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Human oversight of AI](../../capabilities/governance/human-oversight.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Agent Development Kit](../google-cloud/gcp-agent-development-kit.md), [BigQuery conversational analytics](../google-cloud/gcp-bigquery-conversational-analytics.md), [Gemini Enterprise](../google-cloud/gcp-gemini-enterprise.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Agents](../snowflake/snowflake-cortex-agents.md), [Snowflake CoWork](../snowflake/snowflake-cowork.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Agent Bricks](../databricks/databricks-agent-bricks.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Agents](../clickhouse/clickhouse-agents.md) (preview) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica AI Agent Engineering](../informatica/informatica-ai-agent-engineering.md) (unconfirmed), [CLAIRE Agents](../informatica/informatica-claire-agents.md), [CLAIRE Data Quality Agent](../informatica/informatica-claire-data-quality-agent.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Agent Studio](../cloudera/cloudera-agent-studio.md) (preview) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Select AI Agent and Autonomous AI Database MCP Server](../oracle/oracle-select-ai-agent.md), [Oracle AI Database Private Agent Factory](../oracle/oracle-ai-private-agent-factory.md), [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule Studio](../sap/sap-joule-studio.md), [SAP Joule and Joule agents](../sap/sap-joule.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Human oversight of AI](../../capabilities/governance/human-oversight.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise AgentStack](../teradata/teradata-agentstack.md) (preview), [Teradata Tera](../teradata/teradata-tera.md) (preview) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md), [Human oversight of AI](../../capabilities/governance/human-oversight.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md), [Confluent Intelligence](../ibm/confluent-intelligence.md) (preview) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md), [AIP Chatbot Studio](../palantir/palantir-aip-chatbot-studio.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Human oversight of AI](../../capabilities/governance/human-oversight.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Agentic AI Accelerator](../sas/sas-agentic-ai-accelerator.md), [SAS Intelligent Decisioning](../sas/sas-intelligent-decisioning.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [LangGraph](../open-source/langgraph.md), [LangChain](../open-source/langchain.md), [LlamaIndex](../open-source/llamaindex.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Human oversight of AI](../../capabilities/governance/human-oversight.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redpanda Agentic Data Plane](../independent/redpanda-agentic-data-plane.md) (unconfirmed), [LangSmith](../independent/langsmith.md), [Tableau Next](../independent/tableau-next.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
