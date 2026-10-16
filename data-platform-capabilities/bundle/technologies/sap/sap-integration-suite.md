---
type: Technology
id: sap-integration-suite
title: SAP Integration Suite
description: SAP BTP integration platform for process integration, API management, B2B and EDI exchange and event brokering between SAP and third-party applications.
aliases: [SAP Cloud Integration, SAP API Management]
platform: platform-sap
kind: saas
availability: ga
realises:
- application-integration
- data-apis
- managed-file-transfer
- event-streaming
- b2b-edi-integration
- message-queuing
- event-api-catalogue
resource: https://www.sap.com/products/technology-platform/integration-suite.html
tags: [sap]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Provides prebuilt integration content for SAP applications and AI-assisted flow design. Event brokering uses SAP Event Mesh or Advanced Event Mesh. Sits outside the analytical path but is often the source of events.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Application integration](../../capabilities/ingestion-integration/application-integration.md) (Ingestion and integration) (primary): Connect applications through APIs, events and process flows in near real time, outside the analytical data path.
- [Data APIs](../../capabilities/serving/data-apis.md) (Serving and activation): Expose datasets through managed REST or GraphQL APIs with authentication, paging and rate limits.
- [Managed file transfer](../../capabilities/ingestion-integration/managed-file-transfer.md) (Ingestion and integration): Exchange files securely with partners over SFTP, FTPS or AS2, with tracking and retries.
- [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) (Ingestion and integration): Publish and subscribe to durable, ordered and replayable streams of events between systems.
- [B2B and EDI integration](../../capabilities/ingestion-integration/b2b-edi-integration.md) (Ingestion and integration): Exchange structured business documents such as orders and invoices with trading partners using EDI standards.
- [Message queuing](../../capabilities/ingestion-integration/message-queuing.md) (Ingestion and integration): Distribute messages to competing consumers with per-message acknowledgement and redelivery.
- [Event and API catalogue](../../capabilities/metadata/event-api-catalogue.md) (Metadata and discovery): List the event streams and data APIs that systems publish, with owners, schemas, versions and consumers, so teams can find, subscribe to and safely change them.

**Platform:** [SAP](../../platforms/platform-sap.md)  
**Availability:** ga  
**Product family:** SAP Business Technology Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon EventBridge](../aws/aws-eventbridge.md), [AWS Step Functions](../aws/aws-step-functions.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Logic Apps](../microsoft/azure-logic-apps.md), [Azure API Management](../microsoft/azure-api-management.md), [Azure Event Grid](../microsoft/azure-event-grid.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [B2B and EDI integration](../../capabilities/ingestion-integration/b2b-edi-integration.md), [Managed file transfer](../../capabilities/ingestion-integration/managed-file-transfer.md), [Data APIs](../../capabilities/serving/data-apis.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Application Integration](../google-cloud/gcp-application-integration.md), [Eventarc](../google-cloud/gcp-eventarc.md), [Google Cloud Workflows](../google-cloud/gcp-workflows.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake external network access (external access integrations)](../snowflake/snowflake-external-access-integrations.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Application Integration (CAI)](../informatica/informatica-cloud-application-integration.md), [Informatica API Center](../informatica/informatica-api-center.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [Data APIs](../../capabilities/serving/data-apis.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [MuleSoft Anypoint Platform](../independent/mulesoft-anypoint-platform.md), [Boomi Enterprise Platform](../independent/boomi-enterprise-platform.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [B2B and EDI integration](../../capabilities/ingestion-integration/b2b-edi-integration.md), [Data APIs](../../capabilities/serving/data-apis.md), [Event and API catalogue](../../capabilities/metadata/event-api-catalogue.md) |
