---
type: Technology
id: boomi-enterprise-platform
title: Boomi Enterprise Platform
description: Integration platform as a service covering application integration, API management, event streams, B2B/EDI, managed file transfer and AI agent building.
aliases: [Boomi]
formerly: [Boomi AtomSphere]
platform: platform-independent
vendor: Boomi
kind: saas
availability: ga
realises:
- application-integration
- event-streaming
- managed-file-transfer
- ai-agents
- agent-tool-access
- b2b-edi-integration
- agent-registry
resource: https://boomi.com/platform/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Agentstudio and the Agent Control Plane build and govern agents, and API Management can publish APIs as MCP tools. Boomi also sells Boomi Data Hub for master data management, and Boomi Data Integration (formerly Rivery) for ELT.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Application integration](../../capabilities/ingestion-integration/application-integration.md) (Ingestion and integration) (primary): Connect applications through APIs, events and process flows in near real time, outside the analytical data path.
- [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) (Ingestion and integration): Publish and subscribe to durable, ordered and replayable streams of events between systems.
- [Managed file transfer](../../capabilities/ingestion-integration/managed-file-transfer.md) (Ingestion and integration): Exchange files securely with partners over SFTP, FTPS or AS2, with tracking and retries.
- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI): Build systems in which models plan, call tools and act over several steps to complete a task.
- [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) (Generative AI): Give agents governed access to data and actions through tools and protocols such as MCP.
- [B2B and EDI integration](../../capabilities/ingestion-integration/b2b-edi-integration.md) (Ingestion and integration): Exchange structured business documents such as orders and invoices with trading partners using EDI standards.
- [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) (Generative AI): Keep a governed inventory of agents, tools and MCP servers with owners and permissions so they can be found, approved and controlled.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon EventBridge](../aws/aws-eventbridge.md), [AWS Step Functions](../aws/aws-step-functions.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Logic Apps](../microsoft/azure-logic-apps.md), [Azure Event Grid](../microsoft/azure-event-grid.md), [Azure API Management](../microsoft/azure-api-management.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [B2B and EDI integration](../../capabilities/ingestion-integration/b2b-edi-integration.md), [Managed file transfer](../../capabilities/ingestion-integration/managed-file-transfer.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Application Integration](../google-cloud/gcp-application-integration.md), [Eventarc](../google-cloud/gcp-eventarc.md), [Google Cloud Workflows](../google-cloud/gcp-workflows.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake external network access (external access integrations)](../snowflake/snowflake-external-access-integrations.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Application Integration (CAI)](../informatica/informatica-cloud-application-integration.md), [Informatica API Center](../informatica/informatica-api-center.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Integration Suite](../sap/sap-integration-suite.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [B2B and EDI integration](../../capabilities/ingestion-integration/b2b-edi-integration.md), [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Managed file transfer](../../capabilities/ingestion-integration/managed-file-transfer.md) |
