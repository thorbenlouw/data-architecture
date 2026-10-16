---
type: Capability
id: data-apis
title: Data APIs
description: Expose datasets through managed REST or GraphQL APIs with authentication, paging and rate limits.
aliases: [data services, REST data APIs, GraphQL APIs, query API endpoints, data as a service]
broader: [serving]
related: [low-latency-serving, sql-access, application-integration, access-control, external-data-sharing]
depends_on: [identity-authentication]
tags: [serving]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A data API puts a web interface in front of datasets, so applications, partners and services can request data without database credentials or SQL. A REST endpoint such as `/customers/{id}/orders?from=2025-01-01`, or a GraphQL schema over the same tables, returns JSON. The API layer handles token authentication, authorisation, pagination, filtering, caching, rate limits and usage logging. Some platforms generate these APIs from table definitions; others host hand-written services next to the data.

APIs decouple consumers from storage: tables can be restructured behind a stable, versioned interface, and access is controlled per client and per call. They suit applications, partners and microservices, but not bulk extraction or ad hoc analysis, where SQL access or exports are more efficient. Generated APIs are quick to publish but expose table structures directly; designed APIs take longer but present business-level resources. Response times depend on what sits behind the API, so high-volume lookups usually need a low-latency store.

# Key considerations

- Version APIs and publish deprecation timelines. API consumers are often invisible to the data team.
- Apply the same row and column policies as the underlying data, based on the caller's identity rather than a shared service account.
- Set rate limits and quotas per client so one consumer cannot use up capacity for others.
- Describe APIs with an OpenAPI or GraphQL schema and list them in the catalogue with the datasets they expose.

# Questions to ask

- Who will call the APIs, and do they need single records, filtered sets or bulk data?
- What request rates, latency and availability are expected?
- Will external parties use them, and what authentication and contractual terms apply?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Serving and activation](serving.md) |
| Broader | [Serving and activation](serving.md) |
| Related | [Access control](../security/access-control.md), [Agent tool and data access](../generative-ai/agent-tool-access.md), [API ingestion](../ingestion-integration/api-ingestion.md), [Application integration](../ingestion-integration/application-integration.md), [Embedded analytics](../analytics-bi/embedded-analytics.md), [Event and API catalogue](../metadata/event-api-catalogue.md), [External data sharing](../data-sharing/external-data-sharing.md), [External user and tenant identity](../security/external-identity.md), [Low-latency serving](low-latency-serving.md), [Master data management](../master-data/master-data-management.md), [SQL and programmatic access](sql-access.md) |
| Depends on | [Identity and authentication](../security/identity-authentication.md) |

# Where it appears

- **Use cases:** [Customer 360](../../use-cases/usecase-customer-360.md) (benefits from) · [Customer-facing analytics](../../use-cases/usecase-customer-facing-analytics.md) (benefits from)
- **Personas:** [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Data serving](../../maturity/track-serving.md) (from level 3, Defined)
- **Frameworks:** [EU Data Act](../../frameworks/framework-eu-data-act.md): Chapters II and III – Access to and sharing of connected-product data; Chapter VIII – Interoperability

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure API Management](../../technologies/microsoft/azure-api-management.md), [Fabric API for GraphQL](../../technologies/microsoft/fabric-api-for-graphql.md), [Fabric user data functions](../../technologies/microsoft/fabric-user-data-functions.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Apigee](../../technologies/google-cloud/gcp-apigee.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | Query API Endpoints | [ClickHouse Cloud Query API Endpoints](../../technologies/clickhouse/clickhouse-query-api-endpoints.md) |
| [Informatica](../../platforms/platform-informatica.md) | managed APIs in API Center | [Informatica API Center](../../technologies/informatica/informatica-api-center.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Integration Suite](../../technologies/sap/sap-integration-suite.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Ontology](../../technologies/palantir/palantir-ontology.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Cube Core](../../technologies/open-source/cube-core.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [MuleSoft Anypoint Platform](../../technologies/independent/mulesoft-anypoint-platform.md), [Tinybird](../../technologies/independent/tinybird.md) |
