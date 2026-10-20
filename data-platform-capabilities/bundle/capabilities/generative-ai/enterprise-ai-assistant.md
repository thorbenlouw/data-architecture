---
type: Capability
id: enterprise-ai-assistant
title: Enterprise AI assistant
description: Give staff a governed, ready-made assistant that answers questions and completes tasks across structured and unstructured enterprise data.
aliases: [AI workspace, workplace assistant, AI copilot, chat assistant, chatbot]
broader: [generative-ai]
related: [conversational-analytics, agent-registry, data-consumer-portal, data-security-posture]
depends_on: [permission-aware-retrieval, foundation-model-access]
tags: [generative-ai]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

This is a ready-made chat and task interface for staff, connected to the organisation's documents, email, collaboration tools and increasingly its data platform. It answers questions with citations, summarises and drafts, runs analyses and calls agents or actions, all under the user's own permissions and the organisation's policies. For example, a project manager asks for open risks across three projects; the assistant searches project documents and tickets, queries the dataset behind a delivery dashboard and drafts a status note.

It is mainly a buy-versus-build decision. An assistant product brings connectors, permission-aware search, an interface, administration and usage reporting that most organisations would otherwise build repeatedly, while specialised workflows still need custom agents. Conversational analytics answers questions about structured data; an enterprise assistant spans documents, applications and data together. Results depend on connector coverage, content quality and access hygiene, because oversharing in source systems quickly becomes visible through search.

# Key considerations

- Fix oversharing in source systems before rollout. An assistant makes everything a user can technically open easy to find.
- Check which connectors are supported and how quickly each one syncs content and permissions.
- Decide how the assistant is extended, through custom agents, MCP tools or plugins, and who may publish them.
- Measure adoption and task outcomes, not only licences assigned.
- Several overlapping assistants from different vendors confuse staff and split governance. Decide which is the default.

# Questions to ask

- Which content sources and applications must the assistant reach?
- Are permissions in those sources accurate enough to expose through search?
- Which tasks beyond answering questions should it perform, such as drafting or updating records?
- Which assistants are already licensed through existing vendors?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Generative AI](generative-ai.md) |
| Broader | [Generative AI](generative-ai.md) |
| Related | [Agent and tool registry](agent-registry.md), [Conversational analytics](../analytics-bi/conversational-analytics.md), [Data consumer portal](../analytics-bi/data-consumer-portal.md), [Data security posture management](../security/data-security-posture.md) |
| Depends on | [Permission-aware retrieval](permission-aware-retrieval.md), [Foundation model access](foundation-model-access.md) |

# Where it appears

- **Use cases:** [Conversational analytics for business users](../../use-cases/usecase-conversational-bi.md) (benefits from) · [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (benefits from)
- **Personas:** [Business user](../../personas/persona-business-user.md)
- **Maturity tracks:** [Generative AI](../../maturity/track-genai.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Quick](../../technologies/aws/aws-quick.md), [Amazon Q Business](../../technologies/aws/aws-q-business.md) (deprecated) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Gemini Enterprise](../../technologies/google-cloud/gcp-gemini-enterprise.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake CoWork](../../technologies/snowflake/snowflake-cowork.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Joule and Joule agents](../../technologies/sap/sap-joule.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx Orchestrate](../../technologies/ibm/ibm-watsonx-orchestrate.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | Agent Hub | [Dataiku Agent Hub](../../technologies/dataiku/dataiku-agent-hub.md) (unconfirmed) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [H2O.ai Platform (Driverless AI and h2oGPTe)](../../technologies/independent/h2o-ai.md), [Qlik Cloud Analytics](../../technologies/independent/qlik-cloud-analytics.md) |
