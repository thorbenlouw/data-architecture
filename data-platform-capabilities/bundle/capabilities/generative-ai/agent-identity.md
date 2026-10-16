---
type: Capability
id: agent-identity
title: Agent identity and authorisation
description: Give each agent its own identity and scoped, short-lived access to data on behalf of named users, enforced at request time.
aliases: [on-behalf-of access, agent permissions]
broader: [ai-agents, access-control]
related: [permission-aware-retrieval, audit-logging, secrets-management, agent-tool-access, agent-registry]
depends_on: [identity-authentication]
tags: [generative-ai]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Each agent gets its own identity, separate from human users and from shared service accounts. When it acts for a person, it obtains a token that names both the agent and that user, carries only the scopes the task needs and expires quickly. Downstream systems then grant the overlap of the user's permissions and the agent's. For example, an expenses agent acting for an employee can read that employee's receipts and submit a claim, but cannot read colleagues' claims even though the same agent serves everyone. OAuth delegation and token exchange are the usual mechanisms, and MCP authorisation builds on OAuth.

Shared service accounts make every agent a route to privilege escalation, and audit records show only a generic bot. Two modes are common: acting for a signed-in user, and running unattended with a tightly scoped identity of its own. Agents differ from other workloads in being numerous, short-lived and acting for others through chains of calls, so delegation must pass through each hop without widening.

# Key considerations

- Decide per agent whether it acts as the user, as itself, or as the overlap of both. Unattended agents need their own narrowly scoped identity.
- Use short-lived tokens. Never place long-lived credentials in prompts, agent memory or code.
- Users should be able to see and revoke what an agent may do on their behalf.
- When agents call other agents or tools, pass the delegation along without widening its scopes.
- Audit records must show both the agent and the person it acted for.

# Questions to ask

- Do agents act for specific users, run unattended, or both?
- Can the identity provider issue scoped, delegated tokens to non-human identities?
- Can downstream systems enforce each user's permissions on requests made by an agent?
- What must audit records show for regulators or internal review?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Generative AI](generative-ai.md) |
| Broader | [AI agents](ai-agents.md), [Access control](../security/access-control.md) |
| Related | [Agent and tool registry](agent-registry.md), [Agent tool and data access](agent-tool-access.md), [Audit logging](../security/audit-logging.md), [Data engineering agents](../development-lifecycle/data-engineering-agents.md), [Identity and authentication](../security/identity-authentication.md), [Permission-aware retrieval](permission-aware-retrieval.md), [Secrets management](../security/secrets-management.md) |
| Depends on | [Identity and authentication](../security/identity-authentication.md) |
| Needed by | [Agent-to-agent interoperability](agent-interoperability.md) |

# Where it appears

- **Use cases:** [Agentic process automation](../../use-cases/usecase-agentic-automation.md) (requires, level 3)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md) · [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Generative AI](../../maturity/track-genai.md) (from level 4, Measured) · [Security and access control](../../maturity/track-security.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Bedrock AgentCore](../../technologies/aws/aws-bedrock-agentcore.md), [Amazon Bedrock AgentCore Policy](../../technologies/aws/aws-bedrock-agentcore-policy.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric operations agent](../../technologies/microsoft/fabric-operations-agent.md), [Microsoft Entra ID](../../technologies/microsoft/azure-entra-id.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Agent Gateway](../../technologies/google-cloud/gcp-agent-gateway.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Agent Runtime and Agent Bricks CLI](../../technologies/databricks/databricks-agent-runtime.md) (preview) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Cyera DSPM](../../technologies/independent/cyera-dspm.md), [Immuta Data Authorization Platform](../../technologies/independent/immuta-data-authorization-platform.md), [Privacera](../../technologies/independent/privacera.md) |
