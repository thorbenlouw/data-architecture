---
type: Technology
id: clickhouse-query-api-endpoints
title: ClickHouse Cloud Query API Endpoints
description: Turns a saved, parameterised SQL query in the Cloud console into an authenticated HTTP endpoint that returns results in any ClickHouse format.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [data-apis, low-latency-serving]
resource: https://clickhouse.com/docs/cloud/get-started/query-endpoints
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Authenticated with Cloud API keys and a chosen database role, with CORS controls; version 2 adds streaming and all output formats. Useful for simple application back ends without running an API tier.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data APIs](../../capabilities/serving/data-apis.md) (Serving and activation) (primary): Expose datasets through managed REST or GraphQL APIs with authentication, paging and rate limits.
- [Low-latency serving](../../capabilities/serving/low-latency-serving.md) (Serving and activation): Serve individual records or small result sets to applications in milliseconds.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga  
**Product family:** ClickHouse Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric API for GraphQL](../microsoft/fabric-api-for-graphql.md), [Fabric user data functions](../microsoft/fabric-user-data-functions.md), [Azure API Management](../microsoft/azure-api-management.md) | [Data APIs](../../capabilities/serving/data-apis.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Apigee](../google-cloud/gcp-apigee.md) | [Data APIs](../../capabilities/serving/data-apis.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica API Center](../informatica/informatica-api-center.md) | [Data APIs](../../capabilities/serving/data-apis.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Integration Suite](../sap/sap-integration-suite.md) | [Data APIs](../../capabilities/serving/data-apis.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Ontology](../palantir/palantir-ontology.md) | [Data APIs](../../capabilities/serving/data-apis.md), [Low-latency serving](../../capabilities/serving/low-latency-serving.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Cube Core](../open-source/cube-core.md) | [Data APIs](../../capabilities/serving/data-apis.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Tinybird](../independent/tinybird.md), [MuleSoft Anypoint Platform](../independent/mulesoft-anypoint-platform.md) | [Data APIs](../../capabilities/serving/data-apis.md) |
