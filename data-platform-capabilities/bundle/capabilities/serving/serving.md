---
type: Capability
id: serving
title: Serving and activation
description: Deliver data to the applications, people and processes that use it, at the latency and volume they need.
aliases: [data consumption, data delivery]
broader: []
related: [analytics-bi, semantic-layer, data-sharing, data-contracts, access-control]
depends_on: [storage]
order: 6
tags: [serving]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Serving is the last step: getting data from the platform to whoever uses it, in the form, latency and volume they need. Consumers vary widely. A finance analyst runs SQL from a BI tool; a mobile app looks up one customer's offers in a few milliseconds; a CRM needs account scores refreshed nightly; a regulator wants a monthly file; another team wants every change to a table as it happens. No single storage layout suits all of them, so serving usually means reshaping or copying data for particular access patterns.

The capabilities group by consumer. For people and tools, SQL and programmatic access and read-optimised views give fast, governed queries. For applications, low-latency serving, data APIs and operational data stores provide record lookups and a current integrated view, and operational database integration runs transactional stores beside the platform. For other systems, change feeds stream table changes, reverse ETL and audience activation push modelled data into business tools, and data export delivers files in bulk.

Each serving path is in effect a contract with its consumers, with its own latency, availability and security expectations. Analytical engines are built for large scans, not thousands of small concurrent lookups, so application-facing serving usually needs a separate store, cache or API. Every copy made for serving adds sync logic and another place where access control must hold, so the number of paths should be a deliberate choice.

# Key considerations

- Classify consumers by latency, concurrency and volume before choosing serving paths. One path rarely fits all of them.
- Give every serving copy a defined sync method and freshness target. Stale copies cause more support incidents than slow queries.
- Apply the same access policies to serving stores, APIs and exports as to the source tables, or serving becomes the weak point.
- Application-facing paths need operational service levels, on-call cover and capacity planning that analytics teams may not be used to providing.

# Questions to ask

- Who consumes the data: people, applications, business tools or external parties?
- What response time and how many concurrent requests does each consumer need?
- What happens to the business if a serving path is unavailable for an hour?
- Which consumers need updates pushed to them rather than pulling data themselves?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Narrower | [Change feeds](change-feeds.md), [Data APIs](data-apis.md), [Data application hosting](../development-lifecycle/data-applications.md), [Data export](data-export.md), [Decision management](decision-management.md), [Low-latency serving](low-latency-serving.md), [Operational data store](operational-data-store.md), [Operational database integration](operational-database.md), [Read-optimised views](read-optimised-views.md), [Real-time analytical database](../compute/real-time-analytics.md), [Regulatory submission](regulatory-submission.md), [Reverse ETL](reverse-etl.md), [SQL and programmatic access](sql-access.md) |
| Related | [Analytics and BI](../analytics-bi/analytics-bi.md), [Data sharing and collaboration](../data-sharing/data-sharing.md), [Access control](../security/access-control.md), [Data contracts](../data-products/data-contracts.md), [Semantic layer](../analytics-bi/semantic-layer.md) |
| Depends on | [Storage and table management](../storage/storage.md) |

# Where it appears

- **Maturity tracks:** [Data serving](../../maturity/track-serving.md)

# How platforms provide it

No technology in this bundle realises this capability directly yet.

Narrower capabilities are realised by a further 118 technologies; see their pages.
