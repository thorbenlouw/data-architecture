---
type: Capability
id: api-ingestion
title: API ingestion
description: Collect data from REST, GraphQL or SOAP APIs, handling pagination, authentication and rate limits.
broader: [batch-ingestion]
related: [saas-connectors, custom-connectors, idempotent-loading, data-apis]
depends_on: [secrets-management]
tags: [ingestion-integration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

API ingestion calls a source's web API repeatedly to collect records and deals with the mechanics each API imposes. A job collecting payments from a provider might obtain an OAuth token, request pages of 100 records using the cursor returned with the previous page, back off when it receives HTTP 429 (too many requests), and store the last cursor so the next run continues from there. GraphQL APIs add query cost limits; older SOAP services add XML envelopes and service definitions.

Partner platforms, public data services and internal microservices often expose data only through an API. Unlike database extraction, the caller does not control the query: page sizes, filters and change tracking are whatever the API offers, and many APIs cannot return "what changed since" at all. SaaS connectors package this work for common applications; API ingestion is the general capability for everything else, built as configuration in a connector framework or as custom code.

# Key considerations

- Respect rate limits with backoff and concurrency control. Exceeding them can get credentials suspended for every user of the same account.
- Store raw responses before parsing. Payloads change without notice, and raw copies let you reparse after a fix.
- Prefer cursor or token pagination to page numbers, which skip or repeat records when data changes during a run.
- Handle token expiry and refresh in long runs, and keep secrets out of job code.

# Questions to ask

- Can the API filter by modification time or return changes since a cursor?
- What are the rate limits and quotas, and are they shared with other consumers?
- How are API version changes announced, and how long are old versions supported?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Ingestion and integration](ingestion-integration.md) |
| Broader | [Batch ingestion](batch-ingestion.md) |
| Related | [Custom connector development](custom-connectors.md), [Data APIs](../serving/data-apis.md), [Deduplication and idempotent loading](idempotent-loading.md), [SaaS application connectors](saas-connectors.md) |
| Depends on | [Secrets management](../security/secrets-management.md) |

# Where it appears

- **Maturity tracks:** [Ingestion and integration](../../maturity/track-ingestion.md) (from level 1, Initial)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Application Integration](../../technologies/google-cloud/gcp-application-integration.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake external network access (external access integrations)](../../technologies/snowflake/snowflake-external-access-integrations.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Cloud Application Integration (CAI)](../../technologies/informatica/informatica-cloud-application-integration.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Flow](../../technologies/cloudera/cloudera-data-flow.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Airbyte](../../technologies/open-source/airbyte.md), [Apache NiFi](../../technologies/open-source/apache-nifi.md), [dlt (data load tool)](../../technologies/open-source/dlt.md) |
