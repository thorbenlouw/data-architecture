---
type: Capability
id: application-integration
title: Application integration
description: Connect applications through APIs, events and process flows in near real time, outside the analytical data path.
aliases: [iPaaS, EAI]
broader: [ingestion-integration]
related: [event-streaming, message-queuing, reverse-etl, data-apis, b2b-edi-integration]
tags: [ingestion-integration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Application integration links operational systems so that a change in one triggers work in another, usually within seconds. When an order is placed, an integration flow might call the warehouse system to reserve stock, publish an event for billing and update the customer record in the CRM, translating formats between each step and retrying calls that fail. Tools range from API gateways and message brokers to integration platforms with visual flow designers and libraries of application adapters.

It is easily confused with ingestion because both move data between systems. The difference is purpose: application integration carries individual transactions to keep business processes running, while ingestion moves data in bulk or continuously so it can be analysed. They overlap through shared infrastructure such as event streams, and integration flows are a good source of business events for analytics. Using analytical pipelines for process flows, or the reverse, tends to fail on latency, error handling or volume.

# Key considerations

- Keep operational flows and analytical pipelines separately owned and monitored, even when they share a broker.
- Publish business events from integration flows to an event stream, so analytics can consume them without new point-to-point calls.
- Design for partial failure. Multi-step flows need compensating actions, as in the saga pattern, when a later step fails.
- Point-to-point connections multiply quickly. A shared event backbone or API layer reduces the number to maintain.

# Questions to ask

- Which business processes depend on data moving between applications in real time?
- Is there an existing integration platform or enterprise service bus, and who owns it?
- Which integration events would also be useful for analytics?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Ingestion and integration](ingestion-integration.md) |
| Broader | [Ingestion and integration](ingestion-integration.md) |
| Related | [Agent-to-agent interoperability](../generative-ai/agent-interoperability.md), [B2B and EDI integration](b2b-edi-integration.md), [Data APIs](../serving/data-apis.md), [Event streaming](event-streaming.md), [Low-code transformation](../processing/low-code-transformation.md), [Message queuing](message-queuing.md), [Reverse ETL](../serving/reverse-etl.md) |

# Where it appears

- **Use cases:** [Document data extraction](../../use-cases/usecase-document-extraction.md) (requires, level 2) · [IoT predictive maintenance](../../use-cases/usecase-iot-predictive-maintenance.md) (requires, level 2) · [Security and log analytics](../../use-cases/usecase-security-log-analytics.md) (requires, level 2)
- **Personas:** [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Ingestion and integration](../../maturity/track-ingestion.md) (from level 4, Measured)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Integration and Interoperability

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon EventBridge](../../technologies/aws/aws-eventbridge.md), [AWS Step Functions](../../technologies/aws/aws-step-functions.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure API Management](../../technologies/microsoft/azure-api-management.md), [Azure Event Grid](../../technologies/microsoft/azure-event-grid.md), [Azure Logic Apps](../../technologies/microsoft/azure-logic-apps.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Eventarc](../../technologies/google-cloud/gcp-eventarc.md), [Google Cloud Application Integration](../../technologies/google-cloud/gcp-application-integration.md), [Google Cloud Workflows](../../technologies/google-cloud/gcp-workflows.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake external network access (external access integrations)](../../technologies/snowflake/snowflake-external-access-integrations.md) |
| [Informatica](../../platforms/platform-informatica.md) | Application Integration processes | [Informatica API Center](../../technologies/informatica/informatica-api-center.md), [Informatica Cloud Application Integration (CAI)](../../technologies/informatica/informatica-cloud-application-integration.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Integration Suite](../../technologies/sap/sap-integration-suite.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Boomi Enterprise Platform](../../technologies/independent/boomi-enterprise-platform.md), [MuleSoft Anypoint Platform](../../technologies/independent/mulesoft-anypoint-platform.md) |
