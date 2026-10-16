---
type: Technology
id: gcp-application-integration
title: Google Cloud Application Integration
description: Integration-platform-as-a-service for building API, event and process integrations visually, using Integration Connectors to reach SaaS and on-premises systems.
aliases: [Integration Connectors]
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [application-integration, saas-connectors, api-ingestion]
resource: https://docs.cloud.google.com/application-integration/docs/overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Integration Connectors (sold separately) provide managed connectors for Salesforce, SAP, ServiceNow, databases and messaging systems that Application Integration and Apigee can call. Gemini can draft integrations.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Application integration](../../capabilities/ingestion-integration/application-integration.md) (Ingestion and integration) (primary): Connect applications through APIs, events and process flows in near real time, outside the analytical data path.
- [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) (Ingestion and integration): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
- [API ingestion](../../capabilities/ingestion-integration/api-ingestion.md) (Ingestion and integration): Collect data from REST, GraphQL or SOAP APIs, handling pagination, authentication and rate limits.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon EventBridge](../aws/aws-eventbridge.md), [AWS Step Functions](../aws/aws-step-functions.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Logic Apps](../microsoft/azure-logic-apps.md), [Azure Event Grid](../microsoft/azure-event-grid.md), [Azure API Management](../microsoft/azure-api-management.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake external network access (external access integrations)](../snowflake/snowflake-external-access-integrations.md) | [API ingestion](../../capabilities/ingestion-integration/api-ingestion.md), [Application integration](../../capabilities/ingestion-integration/application-integration.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Application Integration (CAI)](../informatica/informatica-cloud-application-integration.md), [Informatica API Center](../informatica/informatica-api-center.md) | [API ingestion](../../capabilities/ingestion-integration/api-ingestion.md), [Application integration](../../capabilities/ingestion-integration/application-integration.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Integration Suite](../sap/sap-integration-suite.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Boomi Enterprise Platform](../independent/boomi-enterprise-platform.md), [MuleSoft Anypoint Platform](../independent/mulesoft-anypoint-platform.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md) |
