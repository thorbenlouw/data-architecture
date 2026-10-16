---
type: Technology
id: gcp-apigee
title: Apigee
description: API management platform for publishing, securing, rate-limiting and monitoring APIs, including APIs that expose data products and LLM endpoints.
aliases: [Apigee X, Apigee API hub]
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [data-apis, ai-gateway, ai-spend-controls, data-product-metering, event-api-catalogue]
resource: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apigee can act as an AI gateway for model traffic with token quotas, semantic caching and Model Armor policies. API hub catalogues APIs across gateways.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data APIs](../../capabilities/serving/data-apis.md) (Serving and activation) (primary): Expose datasets through managed REST or GraphQL APIs with authentication, paging and rate limits.
- [AI gateway](../../capabilities/generative-ai/ai-gateway.md) (Generative AI): Route, secure, rate-limit and track model calls across providers from one place.
- [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) (Platform operations): Limit, prioritise and attribute model and agent consumption per user, team or application.
- [Data product usage metering](../../capabilities/data-products/data-product-metering.md) (Data products): Measure how much each consumer uses a data product so it can be billed, charged back or capped.
- [Event and API catalogue](../../capabilities/metadata/event-api-catalogue.md) (Metadata and discovery): List the event streams and data APIs that systems publish, with owners, schemas, versions and consumers, so teams can find, subscribe to and safely change them.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure API Management](../microsoft/azure-api-management.md), [Fabric API for GraphQL](../microsoft/fabric-api-for-graphql.md), [Fabric user data functions](../microsoft/fabric-user-data-functions.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md), [Data APIs](../../capabilities/serving/data-apis.md), [Event and API catalogue](../../capabilities/metadata/event-api-catalogue.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud Query API Endpoints](../clickhouse/clickhouse-query-api-endpoints.md) | [Data APIs](../../capabilities/serving/data-apis.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica API Center](../informatica/informatica-api-center.md) | [Data APIs](../../capabilities/serving/data-apis.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Integration Suite](../sap/sap-integration-suite.md) | [Data APIs](../../capabilities/serving/data-apis.md), [Event and API catalogue](../../capabilities/metadata/event-api-catalogue.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Ontology](../palantir/palantir-ontology.md) | [Data APIs](../../capabilities/serving/data-apis.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Cube Core](../open-source/cube-core.md), [LiteLLM](../open-source/litellm.md) | [Data APIs](../../capabilities/serving/data-apis.md), [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [MuleSoft Anypoint Platform](../independent/mulesoft-anypoint-platform.md), [Tinybird](../independent/tinybird.md), [Kong Konnect](../independent/kong-konnect.md) | [Data APIs](../../capabilities/serving/data-apis.md), [Event and API catalogue](../../capabilities/metadata/event-api-catalogue.md), [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
