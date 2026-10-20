---
type: Capability
id: ai-agents
title: AI agents
description: Build systems in which models plan, call tools and act over several steps to complete a task.
aliases: [agentic AI, agent builder]
broader: [generative-ai]
related: [ai-guardrails, genai-observability, genai-evaluation, ai-spend-controls, ai-context-layer]
depends_on: [foundation-model-access]
tags: [generative-ai]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

An agent runs a loop: a model receives a goal, chooses a next step, calls a tool such as a search, a SQL query, an API or code execution, reads the result and decides again, until the task is done or a limit is reached. Tools give it reach into data and systems; instructions, permissions and guardrails bound what it may do. For example, a finance agent asked why a cost centre is over budget queries the ledger, compares with last quarter, reads recent purchase orders and drafts an explanation for a controller to review.

Agents suit tasks whose steps vary from case to case and would be hard to script. Designs range from one model calling tools, through workflows where code fixes the sequence and models handle single steps, to multi-agent systems. Fixed workflows are cheaper, faster and easier to test, so open-ended agents are worth it only where flexibility pays. The child capabilities cover the parts needed in production, from tools and runtime to identity and oversight.

# Key considerations

- Errors compound across steps. A step that succeeds 95% of the time gives roughly 60% success over ten steps, so keep tasks short and outputs checkable.
- Agents with write access act at machine speed. Use least privilege, require approval for irreversible actions and cap spend per run.
- An agent that can read private data, take in untrusted content and send data out is the highest-risk combination. Remove at least one of the three where you can.
- Cost and latency vary per run with the number of steps. Set limits on steps, tokens and elapsed time.
- Record every step and tool call so behaviour can be reviewed, reproduced and evaluated.

# Questions to ask

- Which tasks need multi-step judgement rather than a fixed workflow?
- Which actions may an agent take without a person approving them?
- On whose authority does the agent act: its own, or the requesting user's?
- How will success be measured for tasks that can be completed in many valid ways?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Generative AI](generative-ai.md) |
| Broader | [Generative AI](generative-ai.md) |
| Narrower | [Agent and tool registry](agent-registry.md), [Agent hosting and runtime](agent-runtime.md), [Agent identity and authorisation](agent-identity.md), [Agent memory](agent-memory.md), [Agent tool and data access](agent-tool-access.md), [Agent-to-agent interoperability](agent-interoperability.md), [Data engineering agents](../development-lifecycle/data-engineering-agents.md), [Human oversight of AI](../governance/human-oversight.md) |
| Related | [AI context layer](../metadata/ai-context-layer.md), [AI guardrails](ai-guardrails.md), [AI usage and spend controls](../platform-operations/ai-spend-controls.md), [Generative AI evaluation](genai-evaluation.md), [Generative AI observability](genai-observability.md) |
| Depends on | [Foundation model access](foundation-model-access.md) |

# Where it appears

- **Use cases:** [Security and log analytics](../../use-cases/usecase-security-log-analytics.md) (benefits from)
- **Maturity tracks:** [Generative AI](../../maturity/track-genai.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Bedrock AgentCore (harness and Runtime) | [Amazon Bedrock AgentCore](../../technologies/aws/aws-bedrock-agentcore.md), [Amazon Quick](../../technologies/aws/aws-quick.md), [Amazon Bedrock Agents Classic](../../technologies/aws/aws-bedrock-agents-classic.md) (deprecated), [Amazon Q Business](../../technologies/aws/aws-q-business.md) (deprecated) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric operations agent](../../technologies/microsoft/fabric-operations-agent.md), [Foundry Agent Service](../../technologies/microsoft/azure-foundry-agent-service.md), [Microsoft Agent Framework](../../technologies/microsoft/azure-agent-framework.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Agent Development Kit and Agent Runtime (formerly Agent Engine) | [BigQuery conversational analytics](../../technologies/google-cloud/gcp-bigquery-conversational-analytics.md), [Gemini Enterprise](../../technologies/google-cloud/gcp-gemini-enterprise.md), [Google Agent Development Kit](../../technologies/google-cloud/gcp-agent-development-kit.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Cortex Agents](../../technologies/snowflake/snowflake-cortex-agents.md), [Snowflake CoWork](../../technologies/snowflake/snowflake-cowork.md) |
| [Databricks](../../platforms/platform-databricks.md) | Agent Bricks | [Agent Bricks](../../technologies/databricks/databricks-agent-bricks.md), [Agent Bricks Knowledge Assistant and Supervisor Agent](../../technologies/databricks/databricks-knowledge-assistant-supervisor-agent.md) (deprecated) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse Agents](../../technologies/clickhouse/clickhouse-agents.md) (preview) |
| [Informatica](../../platforms/platform-informatica.md) | CLAIRE Agents and AI Agent Engineering | [CLAIRE Agents](../../technologies/informatica/informatica-claire-agents.md), [CLAIRE Data Quality Agent](../../technologies/informatica/informatica-claire-data-quality-agent.md), [Informatica AI Agent Engineering](../../technologies/informatica/informatica-ai-agent-engineering.md) (unconfirmed), [Informatica AI recipes (Application Integration)](../../technologies/informatica/informatica-ai-recipes.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera AI Agent Studio](../../technologies/cloudera/cloudera-agent-studio.md) (preview) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Generative AI (OCI Enterprise AI)](../../technologies/oracle/oracle-oci-generative-ai.md), [Oracle AI Database Private Agent Factory](../../technologies/oracle/oracle-ai-private-agent-factory.md), [Oracle Select AI Agent and Autonomous AI Database MCP Server](../../technologies/oracle/oracle-select-ai-agent.md) |
| [SAP](../../platforms/platform-sap.md) | Joule Agents / Joule Assistants | [SAP Joule and Joule agents](../../technologies/sap/sap-joule.md), [SAP Joule Studio](../../technologies/sap/sap-joule-studio.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Enterprise AgentStack](../../technologies/teradata/teradata-agentstack.md) (preview), [Teradata Tera](../../technologies/teradata/teradata-tera.md) (preview) |
| [IBM](../../platforms/platform-ibm.md) | watsonx Orchestrate | [Confluent Intelligence](../../technologies/ibm/confluent-intelligence.md) (preview), [IBM watsonx Orchestrate](../../technologies/ibm/ibm-watsonx-orchestrate.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [AIP Chatbot Studio](../../technologies/palantir/palantir-aip-chatbot-studio.md), [AIP Logic and AIP Evals](../../technologies/palantir/palantir-aip-logic.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS Agentic AI Accelerator](../../technologies/sas/sas-agentic-ai-accelerator.md), [SAS Intelligent Decisioning](../../technologies/sas/sas-intelligent-decisioning.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku Visual Agents and Code Agents](../../technologies/dataiku/dataiku-agents.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [LangChain](../../technologies/open-source/langchain.md), [LangGraph](../../technologies/open-source/langgraph.md), [LlamaIndex](../../technologies/open-source/llamaindex.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Alteryx One](../../technologies/independent/alteryx-one.md), [Boomi Enterprise Platform](../../technologies/independent/boomi-enterprise-platform.md), [DataRobot AI Platform](../../technologies/independent/datarobot-ai-platform.md), [Elastic Cloud](../../technologies/independent/elastic-cloud.md), [H2O.ai Platform (Driverless AI and h2oGPTe)](../../technologies/independent/h2o-ai.md), [LangSmith](../../technologies/independent/langsmith.md), [Redpanda Agentic Data Plane](../../technologies/independent/redpanda-agentic-data-plane.md) (unconfirmed), [Tableau Next](../../technologies/independent/tableau-next.md), [ThoughtSpot Spotter](../../technologies/independent/thoughtspot-spotter.md) |

Narrower capabilities are realised by a further 82 technologies; see their pages.
