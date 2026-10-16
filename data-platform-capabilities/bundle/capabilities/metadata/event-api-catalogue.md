---
type: Capability
id: event-api-catalogue
title: Event and API catalogue
description: List the event streams and data APIs that systems publish, with owners, schemas, versions and consumers, so teams can find, subscribe to and safely change them.
aliases:
- event catalogue
- stream catalogue
- API catalogue
- event portal
- AsyncAPI catalogue
- developer portal
broader: [data-catalogue]
related: [schema-registry, data-apis, event-streaming, data-contracts, impact-analysis]
tags: [metadata]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data catalogues are built around tables, while application teams exchange data through topics and APIs. An event and API catalogue lists each interface with its owning team, purpose, schema, version history, example payloads and subscribed consumers. Interfaces are usually described in open specifications, AsyncAPI for events and OpenAPI for REST APIs, which the catalogue reads from schema registries, API gateways and code repositories. A payments team that wants to drop a field from `payment.authorised` can see the five services and two pipelines that consume it and which version each reads.

It matters once dozens of teams publish interfaces and nobody can say what exists or who depends on it. Without it, teams create duplicate topics, consumers attach to internal events never meant for reuse, and old versions are never retired. A schema registry enforces compatibility but says little about ownership, meaning or consumers. These catalogues come with streaming platforms, API management products and developer portals, and increasingly feed the main data catalogue so lineage runs from service to dashboard.

# Key considerations

- Generate entries from registries, gateways and specification files in code rather than by hand, or the catalogue drifts from what is deployed.
- Record consumers from actual subscriptions, consumer groups and API keys, not self-declaration, so retirement decisions rest on evidence.
- Mark which interfaces are published for reuse and which are internal, so consumers do not depend on events the producer may change freely.
- Link interfaces to the tables they feed and the contracts that govern them, so impact analysis crosses from applications into the platform.

# Questions to ask

- How many teams publish events or APIs, and how do others find them today?
- Can a producer list every consumer of a topic or API before changing it?
- Are AsyncAPI or OpenAPI specifications maintained, and where are they kept?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Metadata and discovery](metadata.md) |
| Broader | [Data catalogue](data-catalogue.md) |
| Related | [Data APIs](../serving/data-apis.md), [Data contracts](../data-products/data-contracts.md), [Event streaming](../ingestion-integration/event-streaming.md), [Impact analysis](impact-analysis.md), [Schema registry](schema-registry.md) |

# Where it appears

- **Use cases:** [Application data publishing](../../use-cases/usecase-application-data-publishing.md) (requires, level 2)
- **Personas:** [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Data serving](../../maturity/track-serving.md) (from level 3, Defined) · [Real-time and streaming](../../maturity/track-real-time.md) (from level 3, Defined)
- **Frameworks:** [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Infrastructures & Servers

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure API Management](../../technologies/microsoft/azure-api-management.md), [Fabric Real-Time hub](../../technologies/microsoft/fabric-real-time-hub.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Apigee](../../technologies/google-cloud/gcp-apigee.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Integration Suite](../../technologies/sap/sap-integration-suite.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Confluent Cloud](../../technologies/ibm/confluent-cloud.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apicurio Registry](../../technologies/open-source/apicurio-registry.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Kong Konnect](../../technologies/independent/kong-konnect.md), [MuleSoft Anypoint Platform](../../technologies/independent/mulesoft-anypoint-platform.md) |
