---
type: Capability
id: agent-runtime
title: Agent hosting and runtime
description: Deploy and run agents as managed services with identity, durable state, scaling and sandboxed code execution.
aliases: [agent engine, agent sandbox]
broader: [ai-agents]
related:
- container-services
- serverless-compute
- compute-user-isolation
- workflow-orchestration
- genai-observability
tags: [generative-ai]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The runtime is where an agent's loop executes in production. It provides an endpoint or trigger, a service identity, storage for session state so a long task can pause and resume, scaling for many concurrent sessions, and isolated sandboxes where code written by the model runs without reaching other systems. For example, a reconciliation agent started at month end runs for forty minutes, writes Python in a sandbox to compare two files, survives a restart halfway through by resuming from saved state, and posts its results when finished.

Agents run from notebooks or ad hoc services work for demonstrations but leave gaps in identity, recovery, scaling and monitoring. Options include managed agent services on cloud and data platforms, containers or serverless functions running an open-source agent framework, and durable workflow engines that checkpoint each step. Code sandboxes, usually lightweight virtual machines or locked-down containers, are a separate design concern. Unlike model serving, where one request gets one response, agent sessions are long-running and stateful and can take actions part-way through.

# Key considerations

- Long tasks need durable execution. Checkpoint state so a crash or redeploy neither restarts the task nor repeats side effects such as sending an email twice.
- Sandboxes for generated code should deny network and file access by default and set limits on CPU, memory and run time.
- A deployed agent combines a model, prompts, tools and code. Version and release them together, and keep a rollback path.
- Upstream limits such as model quotas and database connections usually cap scale before the runtime does.
- Running agents inside the data platform keeps them close to data and its controls. Running them in an application environment suits customer-facing products. Each choice changes network paths and identity.

# Questions to ask

- How long do agent tasks run, and must they survive restarts?
- Will agents execute code they generate, and against which data?
- How many concurrent sessions are expected at peak?
- Which teams will deploy agents, and do they need self-service?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Generative AI](generative-ai.md) |
| Broader | [AI agents](ai-agents.md) |
| Related | [Container services](../compute/container-services.md), [Generative AI observability](genai-observability.md), [Human oversight of AI](../governance/human-oversight.md), [Serverless compute](../compute/serverless-compute.md), [Shared compute isolation](../security/compute-user-isolation.md), [Workflow orchestration](../orchestration/workflow-orchestration.md) |

# Where it appears

- **Use cases:** [Agentic process automation](../../use-cases/usecase-agentic-automation.md) (requires, level 3)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md)
- **Maturity tracks:** [Generative AI](../../maturity/track-genai.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Bedrock AgentCore](../../technologies/aws/aws-bedrock-agentcore.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Foundry Agent Service](../../technologies/microsoft/azure-foundry-agent-service.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Agent Runtime](../../technologies/google-cloud/gcp-agent-runtime.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Cortex Agents](../../technologies/snowflake/snowflake-cortex-agents.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Agent Runtime and Agent Bricks CLI](../../technologies/databricks/databricks-agent-runtime.md) (preview) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse Agents](../../technologies/clickhouse/clickhouse-agents.md) (preview) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera AI Agent Studio](../../technologies/cloudera/cloudera-agent-studio.md) (preview) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Generative AI (OCI Enterprise AI)](../../technologies/oracle/oracle-oci-generative-ai.md), [Oracle AI Database Private Agent Factory](../../technologies/oracle/oracle-ai-private-agent-factory.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Enterprise AgentStack](../../technologies/teradata/teradata-agentstack.md) (preview), [Teradata Tera](../../technologies/teradata/teradata-tera.md) (preview) |
| [IBM](../../platforms/platform-ibm.md) |  | [Confluent Intelligence](../../technologies/ibm/confluent-intelligence.md) (preview), [IBM watsonx Orchestrate](../../technologies/ibm/ibm-watsonx-orchestrate.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [AIP Chatbot Studio](../../technologies/palantir/palantir-aip-chatbot-studio.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [DataRobot AI Platform](../../technologies/independent/datarobot-ai-platform.md), [LangSmith](../../technologies/independent/langsmith.md), [Redpanda Agentic Data Plane](../../technologies/independent/redpanda-agentic-data-plane.md) (unconfirmed) |
