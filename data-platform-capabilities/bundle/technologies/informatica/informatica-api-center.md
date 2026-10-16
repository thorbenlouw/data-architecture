---
type: Technology
id: informatica-api-center
title: Informatica API Center
description: Designs, publishes, secures with policies, groups and monitors REST APIs, either top-down from an API definition or bottom-up from published Application Integration processes.
platform: platform-informatica
kind: managed-service
availability: ga
realises: [data-apis, application-integration]
resource: https://onlinehelp.informatica.com/IICS/prod/apic/en/aa-introducing-api-center/Introducing_API_Center.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

It supports REST and SOAP protocols.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data APIs](../../capabilities/serving/data-apis.md) (Serving and activation) (primary): Expose datasets through managed REST or GraphQL APIs with authentication, paging and rate limits.
- [Application integration](../../capabilities/ingestion-integration/application-integration.md) (Ingestion and integration): Connect applications through APIs, events and process flows in near real time, outside the analytical data path.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud, Informatica Application Integration

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric API for GraphQL](../microsoft/fabric-api-for-graphql.md), [Azure API Management](../microsoft/azure-api-management.md), [Fabric user data functions](../microsoft/fabric-user-data-functions.md) | [Data APIs](../../capabilities/serving/data-apis.md), [Application integration](../../capabilities/ingestion-integration/application-integration.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Apigee](../google-cloud/gcp-apigee.md) | [Data APIs](../../capabilities/serving/data-apis.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud Query API Endpoints](../clickhouse/clickhouse-query-api-endpoints.md) | [Data APIs](../../capabilities/serving/data-apis.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Integration Suite](../sap/sap-integration-suite.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [Data APIs](../../capabilities/serving/data-apis.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Ontology](../palantir/palantir-ontology.md) | [Data APIs](../../capabilities/serving/data-apis.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Cube Core](../open-source/cube-core.md) | [Data APIs](../../capabilities/serving/data-apis.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [MuleSoft Anypoint Platform](../independent/mulesoft-anypoint-platform.md), [Tinybird](../independent/tinybird.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [Data APIs](../../capabilities/serving/data-apis.md) |
