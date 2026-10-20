---
type: Technology
id: gcp-gemini-enterprise
title: Gemini Enterprise
description: Employee-facing agent platform that combines enterprise search over connected applications, prebuilt and custom agents and Gemini chat under company permissions.
formerly: [Google Agentspace]
platform: platform-google-cloud
kind: saas
availability: ga
realises: [enterprise-ai-assistant, ai-agents, conversational-analytics, permission-aware-retrieval]
resource: https://docs.cloud.google.com/gemini/enterprise/docs
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Connectors cover SharePoint, Confluence, Jira, ServiceNow and Google Workspace. BigQuery and Looker data agents can be published into it, which makes it the main consumption surface for conversational analytics. Editions include Business, Standard, Plus and Frontline.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md) (Generative AI) (primary): Give staff a governed, ready-made assistant that answers questions and completes tasks across structured and unstructured enterprise data.
- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI): Build systems in which models plan, call tools and act over several steps to complete a task.
- [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) (Analytics and BI): Ask questions of data in natural language and get answers, charts or SQL back.
- [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md) (Generative AI): Filter retrieved content by each user's permissions in the source systems so AI answers never reveal what the user could not open.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick](../aws/aws-quick.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md), [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake CoWork](../snowflake/snowflake-cowork.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule and Joule agents](../sap/sap-joule.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Agent Hub](../dataiku/dataiku-agent-hub.md) (unconfirmed) | [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [H2O.ai Platform (Driverless AI and h2oGPTe)](../independent/h2o-ai.md), [Qlik Cloud Analytics](../independent/qlik-cloud-analytics.md), [ThoughtSpot Spotter](../independent/thoughtspot-spotter.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
