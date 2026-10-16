---
type: Technology
id: aws-quick
title: Amazon Quick
description: Workplace AI service combining chat agents, deep research, workflow automation, BI and generated apps over company data and connected applications.
aliases: [Quick Index, Quick Flows, Quick Research, Quick Automate]
formerly: [Amazon Quick Suite]
platform: platform-aws
kind: saas
availability: ga
realises:
- enterprise-ai-assistant
- ai-agents
- data-applications
- data-consumer-portal
- permission-aware-retrieval
resource: https://docs.aws.amazon.com/quick/latest/userguide/what-is.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Components are Quick Sight (BI), Quick Index (grounding on company documents), Quick Research, Quick Flows, Quick Automate and Apps. Connects to tools through action connectors, MCP and OpenAPI, and runs in Slack, Teams, Microsoft 365 and Chrome. It replaces Amazon Q Business, whose indexes can be brought into Quick during migration.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md) (Generative AI) (primary): Give staff a governed, ready-made assistant that answers questions and completes tasks across structured and unstructured enterprise data.
- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI): Build systems in which models plan, call tools and act over several steps to complete a task.
- [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) (Development and DataOps): Build and host interactive data applications next to the data, under platform security.
- [Data consumer portal](../../capabilities/analytics-bi/data-consumer-portal.md) (Analytics and BI): Give business users one place to find the dashboards, apps and AI agents shared with them, without engineering tools.
- [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md) (Generative AI): Filter retrieved content by each user's permissions in the source systems so AI answers never reveal what the user could not open.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon Quick

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Gemini Enterprise](../google-cloud/gcp-gemini-enterprise.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md), [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake CoWork](../snowflake/snowflake-cowork.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule and Joule agents](../sap/sap-joule.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [H2O.ai Platform (Driverless AI and h2oGPTe)](../independent/h2o-ai.md), [Qlik Cloud Analytics](../independent/qlik-cloud-analytics.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md) |
