---
type: Technology
id: mulesoft-anypoint-platform
title: MuleSoft Anypoint Platform
description: Integration and API management platform for building Mule applications, APIs and event flows that connect systems in near real time.
aliases: [MuleSoft, Anypoint Platform, MuleSoft Agent Fabric]
platform: platform-independent
vendor: MuleSoft (Salesforce)
kind: saas
availability: ga
realises:
- application-integration
- data-apis
- document-processing
- agent-tool-access
- agent-registry
- agent-interoperability
- b2b-edi-integration
- message-queuing
- event-api-catalogue
resource: https://docs.mulesoft.com/general/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

MuleSoft Agent Fabric governs and orchestrates AI agents. MuleSoft supports MCP and offers Intelligent Document Processing and RPA. It sits outside the analytical path, although Salesforce now places it beside Informatica and Data 360.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Application integration](../../capabilities/ingestion-integration/application-integration.md) (Ingestion and integration) (primary): Connect applications through APIs, events and process flows in near real time, outside the analytical data path.
- [Data APIs](../../capabilities/serving/data-apis.md) (Serving and activation): Expose datasets through managed REST or GraphQL APIs with authentication, paging and rate limits.
- [Document processing](../../capabilities/processing/document-processing.md) (Processing and transformation): Extract text, tables and fields from documents such as PDFs, scans and images.
- [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) (Generative AI): Give agents governed access to data and actions through tools and protocols such as MCP.
- [Agent and tool registry](../../capabilities/generative-ai/agent-registry.md) (Generative AI): Keep a governed inventory of agents, tools and MCP servers with owners and permissions so they can be found, approved and controlled.
- [Agent-to-agent interoperability](../../capabilities/generative-ai/agent-interoperability.md) (Generative AI): Let agents built on different platforms discover, delegate to and call each other through open protocols.
- [B2B and EDI integration](../../capabilities/ingestion-integration/b2b-edi-integration.md) (Ingestion and integration): Exchange structured business documents such as orders and invoices with trading partners using EDI standards.
- [Message queuing](../../capabilities/ingestion-integration/message-queuing.md) (Ingestion and integration): Distribute messages to competing consumers with per-message acknowledgement and redelivery.
- [Event and API catalogue](../../capabilities/metadata/event-api-catalogue.md) (Metadata and discovery): List the event streams and data APIs that systems publish, with owners, schemas, versions and consumers, so teams can find, subscribe to and safely change them.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon EventBridge](../aws/aws-eventbridge.md), [AWS Step Functions](../aws/aws-step-functions.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Logic Apps](../microsoft/azure-logic-apps.md), [Azure API Management](../microsoft/azure-api-management.md), [Azure Event Grid](../microsoft/azure-event-grid.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [B2B and EDI integration](../../capabilities/ingestion-integration/b2b-edi-integration.md), [Data APIs](../../capabilities/serving/data-apis.md), [Event and API catalogue](../../capabilities/metadata/event-api-catalogue.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Application Integration](../google-cloud/gcp-application-integration.md), [Eventarc](../google-cloud/gcp-eventarc.md), [Google Cloud Workflows](../google-cloud/gcp-workflows.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake external network access (external access integrations)](../snowflake/snowflake-external-access-integrations.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Application Integration (CAI)](../informatica/informatica-cloud-application-integration.md), [Informatica API Center](../informatica/informatica-api-center.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [Data APIs](../../capabilities/serving/data-apis.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Integration Suite](../sap/sap-integration-suite.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [B2B and EDI integration](../../capabilities/ingestion-integration/b2b-edi-integration.md), [Data APIs](../../capabilities/serving/data-apis.md), [Event and API catalogue](../../capabilities/metadata/event-api-catalogue.md) |
