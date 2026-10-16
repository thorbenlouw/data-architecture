---
type: Technology
id: databricks-agent-runtime
title: Databricks Agent Runtime and Agent Bricks CLI
description: Serverless hosting for code-based agents on Databricks Apps, with durable run state, an authenticated endpoint, a service-principal identity and MLflow tracing, deployed with the agentbricks CLI.
platform: platform-databricks
kind: managed-service
availability: preview
realises: [agent-runtime, agent-memory, agent-identity]
resource: https://docs.databricks.com/aws/en/agents/deploy/agent-runtime
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The Agent Bricks CLI has been in Beta since September 2026. It replaces Model Serving agent deployment and the older agent server templates. Managed agent memory and sessions (Beta, Lakebase-backed) and a Databricks Sandbox tool for running code safely sit alongside it.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md) (Generative AI) (primary): Deploy and run agents as managed services with identity, durable state, scaling and sandboxed code execution.
- [Agent memory](../../capabilities/generative-ai/agent-memory.md) (Generative AI): Store and recall conversation state and long-term facts for agents across sessions, with retention controls.
- [Agent identity and authorisation](../../capabilities/generative-ai/agent-identity.md) (Generative AI): Give each agent its own identity and scoped, short-lived access to data on behalf of named users, enforced at request time.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** preview  
**Product family:** Agent Bricks

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore](../aws/aws-bedrock-agentcore.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent identity and authorisation](../../capabilities/generative-ai/agent-identity.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Foundry Agent Service](../microsoft/azure-foundry-agent-service.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Runtime](../google-cloud/gcp-agent-runtime.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Agents](../snowflake/snowflake-cortex-agents.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Agents](../clickhouse/clickhouse-agents.md) (preview) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Agent Studio](../cloudera/cloudera-agent-studio.md) (preview) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database Private Agent Factory](../oracle/oracle-ai-private-agent-factory.md), [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise AgentStack](../teradata/teradata-agentstack.md) (preview), [Teradata Tera](../teradata/teradata-tera.md) (preview) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Intelligence](../ibm/confluent-intelligence.md) (preview), [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Chatbot Studio](../palantir/palantir-aip-chatbot-studio.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [LangSmith](../independent/langsmith.md), [Redpanda Agentic Data Plane](../independent/redpanda-agentic-data-plane.md) (unconfirmed), [DataRobot AI Platform](../independent/datarobot-ai-platform.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md) |
