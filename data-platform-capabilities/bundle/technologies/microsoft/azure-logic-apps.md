---
type: Technology
id: azure-logic-apps
title: Azure Logic Apps
description: Low-code workflow service with hundreds of connectors for application integration, including SFTP and B2B protocols such as AS2 and EDI.
platform: platform-microsoft
kind: managed-service
availability: ga
realises: [application-integration, managed-file-transfer, saas-connectors, b2b-edi-integration]
resource: https://learn.microsoft.com/en-us/azure/logic-apps/logic-apps-overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Application integration](../../capabilities/ingestion-integration/application-integration.md) (Ingestion and integration) (primary): Connect applications through APIs, events and process flows in near real time, outside the analytical data path.
- [Managed file transfer](../../capabilities/ingestion-integration/managed-file-transfer.md) (Ingestion and integration): Exchange files securely with partners over SFTP, FTPS or AS2, with tracking and retries.
- [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) (Ingestion and integration): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
- [B2B and EDI integration](../../capabilities/ingestion-integration/b2b-edi-integration.md) (Ingestion and integration): Exchange structured business documents such as orders and invoices with trading partners using EDI standards.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon EventBridge](../aws/aws-eventbridge.md), [AWS Step Functions](../aws/aws-step-functions.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Application Integration](../google-cloud/gcp-application-integration.md), [Eventarc](../google-cloud/gcp-eventarc.md), [Google Cloud Workflows](../google-cloud/gcp-workflows.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake external network access (external access integrations)](../snowflake/snowflake-external-access-integrations.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Application Integration (CAI)](../informatica/informatica-cloud-application-integration.md), [Informatica API Center](../informatica/informatica-api-center.md), [Informatica B2B Gateway](../informatica/informatica-b2b-gateway.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [B2B and EDI integration](../../capabilities/ingestion-integration/b2b-edi-integration.md), [Managed file transfer](../../capabilities/ingestion-integration/managed-file-transfer.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Integration Suite](../sap/sap-integration-suite.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [B2B and EDI integration](../../capabilities/ingestion-integration/b2b-edi-integration.md), [Managed file transfer](../../capabilities/ingestion-integration/managed-file-transfer.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Boomi Enterprise Platform](../independent/boomi-enterprise-platform.md), [MuleSoft Anypoint Platform](../independent/mulesoft-anypoint-platform.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [B2B and EDI integration](../../capabilities/ingestion-integration/b2b-edi-integration.md), [Managed file transfer](../../capabilities/ingestion-integration/managed-file-transfer.md) |
