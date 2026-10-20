---
type: Technology
id: gcp-remote-mcp-servers
title: Google Cloud remote MCP servers
description: Google-hosted Model Context Protocol endpoints that let AI agents query and manage BigQuery, Spanner, AlloyDB, Cloud SQL, Bigtable, Firestore, Knowledge Catalog, Dataform, Pub/Sub and other services under IAM.
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [agent-tool-access]
resource: https://docs.cloud.google.com/mcp/supported-products
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Most data servers (for example BigQuery, Spanner, AlloyDB, Pub/Sub, Managed Kafka) are GA; data lineage, Datastream and Database Migration Service servers are in preview. Looker has its own managed MCP server in preview. Model Armor screening and IAM deny policies (for example blocking write tools) are the recommended controls.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) (Generative AI) (primary): Give agents governed access to data and actions through tools and protocols such as MCP.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore Gateway](../aws/aws-bedrock-agentcore-gateway.md), [Amazon Bedrock AgentCore Policy](../aws/aws-bedrock-agentcore-policy.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric MCP server](../microsoft/fabric-mcp-server.md), [Fabric data agent](../microsoft/fabric-data-agent.md), [Fabric IQ ontology](../microsoft/fabric-iq-ontology.md) (preview) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake-managed MCP server](../snowflake/snowflake-managed-mcp-server.md), [Snowflake Cortex Agents](../snowflake/snowflake-cortex-agents.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks managed MCP servers](../databricks/databricks-managed-mcp-servers.md) (preview), [Unity Gateway](../databricks/databricks-unity-gateway.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse MCP server (open-source and Remote MCP in Cloud)](../clickhouse/clickhouse-mcp-server.md), [ClickHouse Agents](../clickhouse/clickhouse-agents.md) (preview) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Headless Data Management (Informatica MCP servers)](../informatica/informatica-headless-data-management.md), [Informatica AI Agent Engineering](../informatica/informatica-ai-agent-engineering.md) (unconfirmed) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Agent Studio](../cloudera/cloudera-agent-studio.md) (preview) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Select AI Agent and Autonomous AI Database MCP Server](../oracle/oracle-select-ai-agent.md), [Oracle Analytics Cloud AI Assistant, AI Data Agents and MCP Server](../oracle/oracle-analytics-cloud-ai.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule Studio](../sap/sap-joule-studio.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise MCP](../teradata/teradata-enterprise-mcp.md), [Teradata Enterprise AgentStack](../teradata/teradata-agentstack.md) (preview) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Intelligence](../ibm/confluent-intelligence.md) (preview), [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir MCP and Ontology MCP](../palantir/palantir-mcp.md), [AIP Chatbot Studio](../palantir/palantir-aip-chatbot-studio.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Viya MCP Server](../sas/sas-viya-mcp-server.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Visual Agents and Code Agents](../dataiku/dataiku-agents.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Model Context Protocol (MCP)](../open-source/model-context-protocol.md), [LangGraph](../open-source/langgraph.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Airbyte Agents](../independent/airbyte-agents.md) (unconfirmed), [AtScale](../independent/atscale.md), [dbt Semantic Layer](../independent/dbt-semantic-layer.md) | [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) |
