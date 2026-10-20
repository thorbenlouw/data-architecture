---
type: Technology
id: aws-bedrock-agentcore
title: Amazon Bedrock AgentCore
description: Platform for hosting and operating AI agents built with any framework or model, providing isolated runtime sessions, memory, identity, code and browser tools and tracing.
aliases: [AgentCore, AgentCore Runtime, AgentCore Memory, AgentCore Identity]
platform: platform-aws
kind: managed-service
availability: ga
realises:
- ai-agents
- genai-observability
- agent-runtime
- agent-memory
- agent-identity
- agent-interoperability
resource: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA since October 2025. The managed harness (GA June 2026) defines an agent declaratively from a model, prompt and tools; Runtime hosts custom code in microVMs, and since August 2026 can run on EC2 capacity in your account. AgentCore Identity handles OAuth and on-behalf-of access to downstream systems. Observability emits OpenTelemetry traces to CloudWatch.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI) (primary): Build systems in which models plan, call tools and act over several steps to complete a task.
- [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) (Generative AI): Trace model and agent calls with their prompts, responses, latency, cost and user feedback.
- [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md) (Generative AI): Deploy and run agents as managed services with identity, durable state, scaling and sandboxed code execution.
- [Agent memory](../../capabilities/generative-ai/agent-memory.md) (Generative AI): Store and recall conversation state and long-term facts for agents across sessions, with retention controls.
- [Agent identity and authorisation](../../capabilities/generative-ai/agent-identity.md) (Generative AI): Give each agent its own identity and scoped, short-lived access to data on behalf of named users, enforced at request time.
- [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md) (Generative AI): Let agents built on different platforms discover, delegate to and call each other through open protocols.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon Bedrock AgentCore

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Foundry Agent Service](../microsoft/azure-foundry-agent-service.md), [Microsoft Agent Framework](../microsoft/azure-agent-framework.md), [Fabric operations agent](../microsoft/fabric-operations-agent.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md), [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Agent Development Kit](../google-cloud/gcp-agent-development-kit.md), [BigQuery conversational analytics](../google-cloud/gcp-bigquery-conversational-analytics.md), [Gemini Enterprise](../google-cloud/gcp-gemini-enterprise.md) | [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Agents](../snowflake/snowflake-cortex-agents.md), [Snowflake CoWork](../snowflake/snowflake-cowork.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Agent Bricks](../databricks/databricks-agent-bricks.md), [Databricks Agent Runtime and Agent Bricks CLI](../databricks/databricks-agent-runtime.md) (preview) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent identity and authorisation](../../capabilities/generative-ai/agent-identity.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Agents](../clickhouse/clickhouse-agents.md) (preview) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE Agents](../informatica/informatica-claire-agents.md), [Informatica AI Agent Engineering](../informatica/informatica-ai-agent-engineering.md) (unconfirmed), [CLAIRE Data Quality Agent](../informatica/informatica-claire-data-quality-agent.md) | [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Agent Studio](../cloudera/cloudera-agent-studio.md) (preview) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database Private Agent Factory](../oracle/oracle-ai-private-agent-factory.md), [Oracle Select AI Agent and Autonomous AI Database MCP Server](../oracle/oracle-select-ai-agent.md), [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule and Joule agents](../sap/sap-joule.md), [SAP Joule Studio](../sap/sap-joule-studio.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise AgentStack](../teradata/teradata-agentstack.md) (preview), [Teradata Tera](../teradata/teradata-tera.md) (preview) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md), [Confluent Intelligence](../ibm/confluent-intelligence.md) (preview) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Chatbot Studio](../palantir/palantir-aip-chatbot-studio.md), [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Agentic AI Accelerator](../sas/sas-agentic-ai-accelerator.md), [SAS Intelligent Decisioning](../sas/sas-intelligent-decisioning.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Visual Agents and Code Agents](../dataiku/dataiku-agents.md) | [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [LangGraph](../open-source/langgraph.md), [LangChain](../open-source/langchain.md), [LlamaIndex](../open-source/llamaindex.md) | [Agent memory](../../capabilities/generative-ai/agent-memory.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [LangSmith](../independent/langsmith.md), [Redpanda Agentic Data Plane](../independent/redpanda-agentic-data-plane.md) (unconfirmed), [DataRobot AI Platform](../independent/datarobot-ai-platform.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
