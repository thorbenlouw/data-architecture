---
type: Technology
id: fabric-operations-agent
title: Fabric operations agent
description: An agent that monitors Eventhouse or ontology data against goals and rules, and recommends or runs actions through Teams with approval.
platform: platform-microsoft
kind: feature
availability: ga
realises: [ai-agents, data-alerting, human-oversight, agent-identity]
resource: https://learn.microsoft.com/en-us/fabric/real-time-intelligence/operations-agent
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Runs with an Entra Agent ID on behalf of its creator, so approved actions use the creator's permissions. Requires paid capacity and Copilot to be enabled.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI) (primary): Build systems in which models plan, call tools and act over several steps to complete a task.
- [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) (Analytics and BI): Notify people when data crosses thresholds, or deliver reports to them on a schedule.
- [Human oversight of AI](../../capabilities/governance/human-oversight.md) (Governance and compliance): Route model and agent decisions to people for review, approval or override, and let them pause or stop a system.
- [Agent identity and authorisation](../../capabilities/generative-ai/agent-identity.md) (Generative AI): Give each agent its own identity and scoped, short-lived access to data on behalf of named users, enforced at request time.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Fabric IQ

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore](../aws/aws-bedrock-agentcore.md), [Amazon Quick](../aws/aws-quick.md) | [Agent identity and authorisation](../../capabilities/generative-ai/agent-identity.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Agent Development Kit](../google-cloud/gcp-agent-development-kit.md), [BigQuery conversational analytics](../google-cloud/gcp-bigquery-conversational-analytics.md), [Gemini Enterprise](../google-cloud/gcp-gemini-enterprise.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Agents](../snowflake/snowflake-cortex-agents.md), [Snowflake CoWork](../snowflake/snowflake-cowork.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Agent Bricks](../databricks/databricks-agent-bricks.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Agents](../clickhouse/clickhouse-agents.md) (preview) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica AI Agent Engineering](../informatica/informatica-ai-agent-engineering.md) (unconfirmed), [CLAIRE Agents](../informatica/informatica-claire-agents.md), [CLAIRE Data Quality Agent](../informatica/informatica-claire-data-quality-agent.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Agent Studio](../cloudera/cloudera-agent-studio.md) (preview) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Select AI Agent and Autonomous AI Database MCP Server](../oracle/oracle-select-ai-agent.md), [Oracle AI Database Private Agent Factory](../oracle/oracle-ai-private-agent-factory.md), [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule Studio](../sap/sap-joule-studio.md), [SAP Joule and Joule agents](../sap/sap-joule.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Human oversight of AI](../../capabilities/governance/human-oversight.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise AgentStack](../teradata/teradata-agentstack.md) (preview), [Teradata Tera](../teradata/teradata-tera.md) (preview) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Human oversight of AI](../../capabilities/governance/human-oversight.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Intelligence](../ibm/confluent-intelligence.md) (preview), [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md), [AIP Chatbot Studio](../palantir/palantir-aip-chatbot-studio.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Human oversight of AI](../../capabilities/governance/human-oversight.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Agentic AI Accelerator](../sas/sas-agentic-ai-accelerator.md), [SAS Intelligent Decisioning](../sas/sas-intelligent-decisioning.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Visual Agents and Code Agents](../dataiku/dataiku-agents.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Human oversight of AI](../../capabilities/governance/human-oversight.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [LangGraph](../open-source/langgraph.md), [LangChain](../open-source/langchain.md), [LlamaIndex](../open-source/llamaindex.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Human oversight of AI](../../capabilities/governance/human-oversight.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redpanda Agentic Data Plane](../independent/redpanda-agentic-data-plane.md) (unconfirmed), [ThoughtSpot Spotter](../independent/thoughtspot-spotter.md), [Alteryx One](../independent/alteryx-one.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
