---
type: Technology
id: teradata-agentstack
title: Teradata Enterprise AgentStack
description: Suite for building, running and governing AI agents on Teradata, made up of AgentBuilder, Enterprise MCP, AgentEngine and AgentOps.
platform: platform-teradata
kind: software
availability: preview
realises:
- ai-agents
- genai-observability
- ai-guardrails
- agent-tool-access
- agent-runtime
- agent-memory
- human-oversight
resource: https://www.teradata.com/platform/agent-stack
tags: [teradata]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Launched in January 2026 and now part of AI Studio. AgentBuilder (no-code and pro-code, based on Flowise and supporting CrewAI and LangGraph) was released as a private preview; AgentEngine runs agents with memory on Kubernetes or Docker; AgentOps traces reasoning and tool calls, enforces policy and adds human approval steps. [Teradata Enterprise MCP](teradata-enterprise-mcp.md) provides governed data access. Needs Teradata Database 17.20 or later.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI) (primary): Build systems in which models plan, call tools and act over several steps to complete a task.
- [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) (Generative AI): Trace model and agent calls with their prompts, responses, latency, cost and user feedback.
- [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) (Generative AI): Check model inputs, outputs and agent tool calls against policy to block harmful content, data leakage, prompt injection and disallowed actions.
- [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) (Generative AI): Give agents governed access to data and actions through tools and protocols such as MCP.
- [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md) (Generative AI): Deploy and run agents as managed services with identity, durable state, scaling and sandboxed code execution.
- [Agent memory](../../capabilities/generative-ai/agent-memory.md) (Generative AI): Store and recall conversation state and long-term facts for agents across sessions, with retention controls.
- [Human oversight of AI](../../capabilities/governance/human-oversight.md) (Governance and compliance): Route model and agent decisions to people for review, approval or override, and let them pause or stop a system.

**Platform:** [Teradata](../../platforms/platform-teradata.md)  
**Availability:** preview  
**Product family:** Teradata AI Studio, Teradata Enterprise AgentStack

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore](../aws/aws-bedrock-agentcore.md), [Amazon Quick](../aws/aws-quick.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Foundry Agent Service](../microsoft/azure-foundry-agent-service.md), [Fabric operations agent](../microsoft/fabric-operations-agent.md), [Microsoft Agent Framework](../microsoft/azure-agent-framework.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Agent Development Kit](../google-cloud/gcp-agent-development-kit.md), [BigQuery conversational analytics](../google-cloud/gcp-bigquery-conversational-analytics.md), [Gemini Enterprise](../google-cloud/gcp-gemini-enterprise.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Agents](../snowflake/snowflake-cortex-agents.md), [Snowflake CoWork](../snowflake/snowflake-cowork.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Agent Bricks](../databricks/databricks-agent-bricks.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Agents](../clickhouse/clickhouse-agents.md) (preview) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica AI Agent Engineering](../informatica/informatica-ai-agent-engineering.md) (unconfirmed), [CLAIRE Agents](../informatica/informatica-claire-agents.md), [CLAIRE Data Quality Agent](../informatica/informatica-claire-data-quality-agent.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Agent Studio](../cloudera/cloudera-agent-studio.md) (preview) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Select AI Agent and Autonomous AI Database MCP Server](../oracle/oracle-select-ai-agent.md), [Oracle AI Database Private Agent Factory](../oracle/oracle-ai-private-agent-factory.md), [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule Studio](../sap/sap-joule-studio.md), [SAP Joule and Joule agents](../sap/sap-joule.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Human oversight of AI](../../capabilities/governance/human-oversight.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md), [Confluent Intelligence](../ibm/confluent-intelligence.md) (preview) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Chatbot Studio](../palantir/palantir-aip-chatbot-studio.md), [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Human oversight of AI](../../capabilities/governance/human-oversight.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Agentic AI Accelerator](../sas/sas-agentic-ai-accelerator.md), [SAS Intelligent Decisioning](../sas/sas-intelligent-decisioning.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Visual Agents and Code Agents](../dataiku/dataiku-agents.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md), [Human oversight of AI](../../capabilities/governance/human-oversight.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [LangGraph](../open-source/langgraph.md), [LangChain](../open-source/langchain.md), [LlamaIndex](../open-source/llamaindex.md) | [Agent memory](../../capabilities/generative-ai/agent-memory.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Human oversight of AI](../../capabilities/governance/human-oversight.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redpanda Agentic Data Plane](../independent/redpanda-agentic-data-plane.md) (unconfirmed), [LangSmith](../independent/langsmith.md), [Tableau Next](../independent/tableau-next.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md) |
