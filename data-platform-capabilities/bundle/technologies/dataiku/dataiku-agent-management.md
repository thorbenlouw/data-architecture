---
type: Technology
id: dataiku-agent-management
title: Dataiku Agent Management
description: Standalone product that finds AI agents running on Dataiku and other vendors' platforms, maps the tools and models they use, and tracks their performance, risk and certification status.
platform: platform-dataiku
kind: software
availability: preview
realises: [ai-system-discovery, agent-registry, genai-observability]
resource: https://www.dataiku.com/company/news/dataiku-agent-management-general-availability
tags: [dataiku]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

Connects to agents on Amazon Bedrock, Databricks, Google Vertex AI (Gemini Enterprise Agent Platform), Microsoft Copilot Studio and Azure AI Foundry, Salesforce Agentforce, Snowflake Cortex and Dataiku, and to agents on other frameworks through OpenTelemetry; the depth of integration varies by platform. An early access programme opened in March 2026, and in September 2026 Dataiku announced general availability for October 2026. Priced per instance per year, with monitoring metered per agent.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI system discovery](../../capabilities/governance/ai-system-discovery.md) (Governance and compliance) (primary): Find the AI models, agents and services in use, including unapproved ones, to build and maintain the AI inventory.
- [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) (Generative AI): Keep a governed inventory of agents, tools and MCP servers with owners and permissions so they can be found, approved and controlled.
- [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) (Generative AI): Trace model and agent calls with their prompts, responses, latency, cost and user feedback.

**Platform:** [Dataiku](../../platforms/platform-dataiku.md)  
**Availability:** preview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Agent Registry](../aws/aws-agent-registry.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI system discovery](../../capabilities/governance/ai-system-discovery.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Data Security Posture Management](../microsoft/purview-dspm.md), [Foundry Control Plane](../microsoft/azure-foundry-control-plane.md) (preview) | [AI system discovery](../../capabilities/governance/ai-system-discovery.md), [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Security Command Center](../google-cloud/gcp-security-command-center.md) | [AI system discovery](../../capabilities/governance/ai-system-discovery.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica CDGC AI governance](../informatica/informatica-cdgc-ai-governance.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI system discovery](../../capabilities/governance/ai-system-discovery.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Agent Hub](../sap/sap-ai-agent-hub.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI system discovery](../../capabilities/governance/ai-system-discovery.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Guardium Data Security Center](../ibm/ibm-guardium-data-security-center.md), [IBM watsonx.governance](../ibm/ibm-watsonx-governance.md) | [AI system discovery](../../capabilities/governance/ai-system-discovery.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Credo AI Governance Platform](../independent/credo-ai-governance-platform.md), [BigID Next](../independent/bigid-next.md), [Holistic AI Governance Platform](../independent/holistic-ai-governance-platform.md) | [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md), [AI system discovery](../../capabilities/governance/ai-system-discovery.md) |
