---
type: Technology
id: aws-q-business
title: Amazon Q Business
description: Generative AI assistant for employees that answered questions and ran Q Apps over indexed enterprise content.
platform: platform-aws
kind: saas
availability: deprecated
realises: [enterprise-ai-assistant, retrieval-augmented-generation, ai-agents, permission-aware-retrieval]
resource: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html
tags: [aws]
status: deprecated
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

In maintenance since 30 June 2026 and closed to new customers from 30 July 2026. AWS recommends migrating to Amazon Quick; Q Apps must be rebuilt as Quick Flows.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md) (Generative AI) (primary): Give staff a governed, ready-made assistant that answers questions and completes tasks across structured and unstructured enterprise data.
- [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) (Generative AI): Ground model answers in your own content by retrieving relevant passages at query time.
- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI): Build systems in which models plan, call tools and act over several steps to complete a task.
- [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md) (Generative AI): Filter retrieved content by each user's permissions in the source systems so AI answers never reveal what the user could not open.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** deprecated  
Not counted in platform coverage because it is deprecated.

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Gemini Enterprise](../google-cloud/gcp-gemini-enterprise.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md), [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake CoWork](../snowflake/snowflake-cowork.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica AI recipes (Application Integration)](../informatica/informatica-ai-recipes.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database Private Agent Factory](../oracle/oracle-ai-private-agent-factory.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule and Joule agents](../sap/sap-joule.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Chatbot Studio](../palantir/palantir-aip-chatbot-studio.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Permission-aware retrieval](../../capabilities/generative-ai/permission-aware-retrieval.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Agent Hub](../dataiku/dataiku-agent-hub.md) (unconfirmed) | [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [LangChain](../open-source/langchain.md), [LlamaIndex](../open-source/llamaindex.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [H2O.ai Platform (Driverless AI and h2oGPTe)](../independent/h2o-ai.md), [Qlik Cloud Analytics](../independent/qlik-cloud-analytics.md) | [AI agents](../../capabilities/generative-ai/ai-agents.md), [Enterprise AI assistant](../../capabilities/generative-ai/enterprise-ai-assistant.md), [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) |
