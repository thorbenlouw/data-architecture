---
type: Technology
id: sap-joule-studio
title: SAP Joule Studio
description: Capability in SAP Build for building Joule skills and custom agents, from no-code to pro-code, with model choice, tool access and connection to MCP servers.
aliases: [Joule Studio, Joule Studio in SAP Build]
platform: platform-sap
kind: feature
availability: ga
realises: [ai-agents, agent-tool-access, prompt-management, human-oversight]
resource: https://www.sap.com/products/artificial-intelligence/joule-studio.html
tags: [sap]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The skill builder became generally available in July 2025 and the agent builder by January 2026. Agents can be grounded in BDC data, documents and SAP Knowledge Graph, and can ask a person to approve actions.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI) (primary): Build systems in which models plan, call tools and act over several steps to complete a task.
- [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) (Generative AI): Give agents governed access to data and actions through tools and protocols such as MCP.
- [Prompt management](../../capabilities/generative-ai/prompt-management.md) (Generative AI): Version, test and reuse prompts and model configurations.
- [Human oversight of AI](../../capabilities/governance/human-oversight.md) (Governance and compliance): Route model and agent decisions to people for review, approval or override, and let them pause or stop a system.

**Platform:** [SAP](../../platforms/platform-sap.md)  
**Availability:** ga  
**Product family:** SAP Joule, SAP Business AI Platform, SAP Business Technology Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore](../aws/aws-bedrock-agentcore.md), [Amazon Quick](../aws/aws-quick.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric operations agent](../microsoft/fabric-operations-agent.md), [Foundry Agent Service](../microsoft/azure-foundry-agent-service.md), [Microsoft Agent Framework](../microsoft/azure-agent-framework.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Human oversight of AI](../../capabilities/governance/human-oversight.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Agent Development Kit](../google-cloud/gcp-agent-development-kit.md), [BigQuery conversational analytics](../google-cloud/gcp-bigquery-conversational-analytics.md), [Gemini Enterprise](../google-cloud/gcp-gemini-enterprise.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Agents](../snowflake/snowflake-cortex-agents.md), [Snowflake CoWork](../snowflake/snowflake-cowork.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Agent Bricks](../databricks/databricks-agent-bricks.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Agents](../clickhouse/clickhouse-agents.md) (preview) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica AI Agent Engineering](../informatica/informatica-ai-agent-engineering.md) (unconfirmed), [CLAIRE Agents](../informatica/informatica-claire-agents.md), [CLAIRE Data Quality Agent](../informatica/informatica-claire-data-quality-agent.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Agent Studio](../cloudera/cloudera-agent-studio.md) (preview) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Select AI Agent and Autonomous AI Database MCP Server](../oracle/oracle-select-ai-agent.md), [Oracle AI Database Private Agent Factory](../oracle/oracle-ai-private-agent-factory.md), [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise AgentStack](../teradata/teradata-agentstack.md) (preview), [Teradata Tera](../teradata/teradata-tera.md) (preview) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Human oversight of AI](../../capabilities/governance/human-oversight.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Intelligence](../ibm/confluent-intelligence.md) (preview), [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md), [AIP Chatbot Studio](../palantir/palantir-aip-chatbot-studio.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Human oversight of AI](../../capabilities/governance/human-oversight.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Agentic AI Accelerator](../sas/sas-agentic-ai-accelerator.md), [SAS Intelligent Decisioning](../sas/sas-intelligent-decisioning.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Visual Agents and Code Agents](../dataiku/dataiku-agents.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Human oversight of AI](../../capabilities/governance/human-oversight.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [LangGraph](../open-source/langgraph.md), [LangChain](../open-source/langchain.md), [LlamaIndex](../open-source/llamaindex.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Human oversight of AI](../../capabilities/governance/human-oversight.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redpanda Agentic Data Plane](../independent/redpanda-agentic-data-plane.md) (unconfirmed), [Tableau Next](../independent/tableau-next.md), [Boomi Enterprise Platform](../independent/boomi-enterprise-platform.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI agents](../../capabilities/generative-ai/ai-agents.md) |
