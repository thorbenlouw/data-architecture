---
type: Capability
id: agent-memory
title: Agent memory
description: Store and recall conversation state and long-term facts for agents across sessions, with retention controls.
broader: [ai-agents]
related:
- data-retention
- data-subject-requests
- low-latency-serving
- vector-search
- permission-aware-retrieval
tags: [generative-ai]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Models keep nothing between calls, so a memory layer stores what an agent needs later. Short-term memory is the state of the current session: messages, tool results and plans, often summarised to fit the model's context. Long-term memory holds facts and preferences drawn from past sessions and retrieved when relevant. For example, a sales assistant remembers that a user covers the Nordic region and wants figures in euros, and applies this next week without being told again.

Memory gives continuity and saves users repeating themselves, but it is also a growing store of personal and possibly sensitive information. Implementations include session stores keyed by conversation, vector stores of extracted memories, structured user profiles and graph-based memory. The agent may decide what to save during a session, or a background process may extract memories afterwards. Retrieval-augmented generation draws on shared, curated documents; memory is specific to a user or agent and is written by the agent itself, which is why visibility, retention and deletion need explicit design.

# Key considerations

- Memories can contain personal data, so privacy obligations apply, including deletion when a person asks.
- Scope memory strictly by user and tenant. Shared memory can pass one user's information to another.
- Wrong or outdated memories persist and mislead. Let users see, correct and delete them, and expire old entries.
- Memories written from untrusted content can carry injected instructions into future sessions. Treat stored memories as untrusted input.
- Decide what is kept word for word and what is summarised. Summaries lose detail that audit or dispute handling may need.

# Questions to ask

- Which tasks benefit from continuity across sessions?
- What retention periods and deletion rights apply to conversation data?
- Should users be able to view and edit what an agent remembers about them?
- Is memory shared between agents, or private to each one?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Generative AI](generative-ai.md) |
| Broader | [AI agents](ai-agents.md) |
| Related | [Data subject requests](../governance/data-subject-requests.md), [Low-latency serving](../serving/low-latency-serving.md), [Permission-aware retrieval](permission-aware-retrieval.md), [Retention and disposal](../governance/data-retention.md), [Vector search](vector-search.md) |

# Where it appears

- **Use cases:** [Agentic process automation](../../use-cases/usecase-agentic-automation.md) (benefits from)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md)
- **Maturity tracks:** [Generative AI](../../maturity/track-genai.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Bedrock AgentCore](../../technologies/aws/aws-bedrock-agentcore.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Foundry Agent Service](../../technologies/microsoft/azure-foundry-agent-service.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Agent Runtime](../../technologies/google-cloud/gcp-agent-runtime.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Agent Runtime and Agent Bricks CLI](../../technologies/databricks/databricks-agent-runtime.md) (preview) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse Agents](../../technologies/clickhouse/clickhouse-agents.md) (preview) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Enterprise AgentStack](../../technologies/teradata/teradata-agentstack.md) (preview) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [LangGraph](../../technologies/open-source/langgraph.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [LangSmith](../../technologies/independent/langsmith.md) |
