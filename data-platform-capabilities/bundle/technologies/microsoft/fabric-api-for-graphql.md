---
type: Technology
id: fabric-api-for-graphql
title: Fabric API for GraphQL
description: Generates a GraphQL API over warehouses, SQL databases, lakehouse and mirrored database endpoints so applications can query and change data.
platform: platform-microsoft
kind: feature
availability: ga
realises: [data-apis]
resource: https://learn.microsoft.com/en-us/fabric/data-engineering/api-graphql-overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Every exposed table or view needs a primary key. Custom authorisation through user data functions is preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data APIs](../../capabilities/serving/data-apis.md) (Serving and activation) (primary): Expose datasets through managed REST or GraphQL APIs with authentication, paging and rate limits.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Apigee](../google-cloud/gcp-apigee.md) | [Data APIs](../../capabilities/serving/data-apis.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud Query API Endpoints](../clickhouse/clickhouse-query-api-endpoints.md) | [Data APIs](../../capabilities/serving/data-apis.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica API Center](../informatica/informatica-api-center.md) | [Data APIs](../../capabilities/serving/data-apis.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Integration Suite](../sap/sap-integration-suite.md) | [Data APIs](../../capabilities/serving/data-apis.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Ontology](../palantir/palantir-ontology.md) | [Data APIs](../../capabilities/serving/data-apis.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Cube Core](../open-source/cube-core.md) | [Data APIs](../../capabilities/serving/data-apis.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Tinybird](../independent/tinybird.md), [MuleSoft Anypoint Platform](../independent/mulesoft-anypoint-platform.md) | [Data APIs](../../capabilities/serving/data-apis.md) |
