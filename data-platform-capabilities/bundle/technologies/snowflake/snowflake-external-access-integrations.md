---
type: Technology
id: snowflake-external-access-integrations
title: Snowflake external network access (external access integrations)
description: Lets UDFs, procedures and container services call approved external endpoints over the network, using network rules and secrets, for example to pull data from REST APIs.
platform: platform-snowflake
kind: feature
availability: ga
realises: [api-ingestion, application-integration]
resource: https://docs.snowflake.com/en/developer-guide/external-network-access/external-network-access-overview
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [API ingestion](../../capabilities/ingestion-integration/api-ingestion.md) (Ingestion and integration) (primary): Collect data from REST, GraphQL or SOAP APIs, handling pagination, authentication and rate limits.
- [Application integration](../../capabilities/ingestion-integration/application-integration.md) (Ingestion and integration): Connect applications through APIs, events and process flows in near real time, outside the analytical data path.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Application Integration](../google-cloud/gcp-application-integration.md) | [API ingestion](../../capabilities/ingestion-integration/api-ingestion.md), [Application integration](../../capabilities/ingestion-integration/application-integration.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Application Integration (CAI)](../informatica/informatica-cloud-application-integration.md) | [API ingestion](../../capabilities/ingestion-integration/api-ingestion.md), [Application integration](../../capabilities/ingestion-integration/application-integration.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [API ingestion](../../capabilities/ingestion-integration/api-ingestion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [dlt (data load tool)](../open-source/dlt.md), [Airbyte](../open-source/airbyte.md), [Apache NiFi](../open-source/apache-nifi.md) | [API ingestion](../../capabilities/ingestion-integration/api-ingestion.md) |
