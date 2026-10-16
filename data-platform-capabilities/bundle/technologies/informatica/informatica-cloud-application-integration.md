---
type: Technology
id: informatica-cloud-application-integration
title: Informatica Cloud Application Integration (CAI)
description: Designs and runs event-driven and API-driven processes and service connectors that integrate applications in near real time, including over Kafka, JMS, AMQP, Azure Service Bus, Amazon SQS/SNS and Google Pub/Sub.
aliases: [CAI]
platform: platform-informatica
kind: managed-service
availability: ga
realises: [application-integration, event-driven-triggering, api-ingestion]
resource: https://onlinehelp.informatica.com/IICS/prod/CAI/en/index.htm
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Processes published from CAI become APIs that API Center manages, and also tools behind composite MCP servers in AI Agent Engineering. Within Salesforce it overlaps with MuleSoft. The separate Integration Hub service offers publish-subscribe data distribution.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Application integration](../../capabilities/ingestion-integration/application-integration.md) (Ingestion and integration) (primary): Connect applications through APIs, events and process flows in near real time, outside the analytical data path.
- [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) (Orchestration): Start pipelines when something happens, such as a file arriving, a table changing or a message being published.
- [API ingestion](../../capabilities/ingestion-integration/api-ingestion.md) (Ingestion and integration): Collect data from REST, GraphQL or SOAP APIs, handling pagination, authentication and rate limits.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud, Informatica Application Integration

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon EventBridge](../aws/aws-eventbridge.md), [AWS Step Functions](../aws/aws-step-functions.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Event Grid](../microsoft/azure-event-grid.md), [Azure Logic Apps](../microsoft/azure-logic-apps.md), [Azure API Management](../microsoft/azure-api-management.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Application Integration](../google-cloud/gcp-application-integration.md), [Eventarc](../google-cloud/gcp-eventarc.md), [Google Cloud Workflows](../google-cloud/gcp-workflows.md) | [API ingestion](../../capabilities/ingestion-integration/api-ingestion.md), [Application integration](../../capabilities/ingestion-integration/application-integration.md), [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake external network access (external access integrations)](../snowflake/snowflake-external-access-integrations.md) | [API ingestion](../../capabilities/ingestion-integration/api-ingestion.md), [Application integration](../../capabilities/ingestion-integration/application-integration.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Integration Suite](../sap/sap-integration-suite.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Boomi Enterprise Platform](../independent/boomi-enterprise-platform.md), [MuleSoft Anypoint Platform](../independent/mulesoft-anypoint-platform.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md) |
