---
type: Technology
id: dlt
title: dlt (data load tool)
description: Python library for writing extract-and-load pipelines that infer and evolve schemas, load incrementally and write to warehouses, lakes and lakehouse tables.
aliases: [dltHub]
platform: platform-open-source
kind: open-source
availability: ga
realises: [api-ingestion, database-extraction, custom-connectors, schema-evolution, idempotent-loading]
resource: https://dlthub.com/docs/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, company-led by dltHub. Runs anywhere Python runs, for example inside Airflow or Dagster tasks, with no server. A declarative REST API source covers many APIs without custom code.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [API ingestion](../../capabilities/ingestion-integration/api-ingestion.md) (Ingestion and integration) (primary): Collect data from REST, GraphQL or SOAP APIs, handling pagination, authentication and rate limits.
- [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) (Ingestion and integration): Extract full or incremental snapshots from relational and NoSQL databases using queries or bulk export.
- [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md) (Ingestion and integration): Build and run connectors for sources with no prebuilt option, using an SDK or framework.
- [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md) (Storage and table management): Reject data that does not match a table's schema, and change schemas safely over time.
- [Deduplication and idempotent loading](../../capabilities/ingestion-integration/idempotent-loading.md) (Ingestion and integration): Make loads safe to retry or replay by removing duplicates on write so nothing is counted twice.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Application Integration](../google-cloud/gcp-application-integration.md) | [API ingestion](../../capabilities/ingestion-integration/api-ingestion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake external network access (external access integrations)](../snowflake/snowflake-external-access-integrations.md) | [API ingestion](../../capabilities/ingestion-integration/api-ingestion.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Application Integration (CAI)](../informatica/informatica-cloud-application-integration.md) | [API ingestion](../../capabilities/ingestion-integration/api-ingestion.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [API ingestion](../../capabilities/ingestion-integration/api-ingestion.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
