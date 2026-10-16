---
type: Reference
id: application-read-paths
title: Read paths for applications
description: How an application should read data from the platform, or publish data to it, compared by latency, concurrency, freshness, consistency and coupling.
order: 6
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

This page is for software engineers whose application reads data, scores or features from the platform, or publishes its own data to it. Analytical engines are built to scan large volumes for a modest number of users. An application usually needs the opposite: small answers, many times a second, with predictable latency and someone on call when it fails. Pointing an application straight at warehouse tables is the commonest mistake, so choose a read path deliberately and agree its targets before go-live.

# Ways to read from the platform

Figures are typical orders of magnitude, not guarantees. They depend on the product, the data and how much compute is paid for.

| Read path | Latency | Concurrency | Freshness | Consistency | Coupling | Typical use |
|---|---|---|---|---|---|---|
| [SQL and programmatic access](../capabilities/serving/sql-access.md) | Hundreds of milliseconds to minutes | Tens of concurrent queries per compute cluster; more means more compute | As fresh as the tables read | Each query sees one committed snapshot | High: depends on table names, schemas and SQL dialect | Internal tools, data science, bulk and ad hoc reads |
| [Data APIs](../capabilities/serving/data-apis.md) | Set by the store behind it: milliseconds from a cache or serving store, seconds from a warehouse | Controlled per client by rate limits | As fresh as the store behind it | Per request; paging over changing data can skip or repeat rows | Low: a versioned interface hides storage | Partners, microservices and applications with fixed, predictable requests |
| [Read-optimised views](../capabilities/serving/read-optimised-views.md) | Tens of milliseconds to seconds | Moderate; small precomputed tables are cheap to read | As of the last refresh, minutes to a day | Consistent as of the refresh, behind the sources | Medium: the view's shape becomes a published interface | In-app summaries and dashboards with known query shapes |
| [Low-latency serving](../capabilities/serving/low-latency-serving.md) | Single-digit to tens of milliseconds | Thousands of requests a second or more | As of the last push: seconds from a stream, hours from batch | Per key; eventually consistent with the platform | Low to medium, by key or through an API | Personalisation, pricing, profile and score lookups |
| [Operational data store](../capabilities/serving/operational-data-store.md) | Milliseconds to under a second for lookups | Moderate to high | Usually minutes behind the source systems | Current values; sources can briefly disagree | Medium: an integrated schema across systems | Contact-centre and operational views across several systems |
| [Operational database integration](../capabilities/serving/operational-database.md) | Milliseconds | High, as for any transactional database | Current for the application's own writes | Transactional for its own writes; analytical copies lag | High: the application owns and depends on the schema | Data applications that write as well as read, such as approvals or price setting |
| [Change feeds](../capabilities/serving/change-feeds.md) | Seconds to minutes after each commit | A few consumers, each reading in order | Incremental, as changes commit | Ordered by commit; the consumer tracks its position and must handle replays | Medium to high: row-level table schema | Keeping caches, search indexes or application copies in step with platform tables |
| [Reverse ETL](../capabilities/serving/reverse-etl.md) | Minutes to hours, on the sync schedule | Bounded by the destination's API limits | The sync interval | Eventually consistent; rejected rows need handling | Low for the tool, which sees its own objects | Scores and attributes in CRM, marketing and support tools |
| [Event streaming](../capabilities/ingestion-integration/event-streaming.md) | Milliseconds to seconds | Many independent consumer groups | As soon as events are published | Ordered per key within a partition; at-least-once delivery by default | Low: producer and consumers share only the event schema | Reacting to scores, alerts or changes the platform publishes |

For model features at request time, the [Online feature store](../capabilities/machine-learning/online-feature-store.md) is the specialised form of low-latency serving. For aggregates over very fresh data at high concurrency, such as analytics inside a product, a [Real-time analytical database](../capabilities/compute/real-time-analytics.md) database sits between read-optimised views and low-latency serving.

# Choosing a read path

Work down the questions and stop at the first yes.

1. **Does the application write data with transactions, not only read it?** Use an [Operational database integration](../capabilities/serving/operational-database.md) on or beside the platform. For people correcting or adding figures in analytics tools, see [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md).
2. **Is the consumer a business tool such as a CRM or marketing platform?** Use [Reverse ETL](../capabilities/serving/reverse-etl.md), so the tool receives records in its own objects.
3. **Must the application react to changes, or keep its own copy in step?** Subscribe to [Event streaming](../capabilities/ingestion-integration/event-streaming.md) topics where the platform publishes designed events, such as scores or alerts. Read [Change feeds](../capabilities/serving/change-feeds.md) where row changes to a platform table are what matters.
4. **Does each request need one record or a small set within tens of milliseconds, at high request rates?** Load the data into [Low-latency serving](../capabilities/serving/low-latency-serving.md), usually behind a [data API](../capabilities/serving/data-apis.md). Use the [Online feature store](../capabilities/machine-learning/online-feature-store.md) for model features.
5. **Does it need aggregates over fresh, high-volume data for many concurrent users?** Use a [Real-time analytical database](../capabilities/compute/real-time-analytics.md) database. If data minutes or hours old is acceptable, [Read-optimised views](../capabilities/serving/read-optimised-views.md) are simpler and cheaper.
6. **Does it need one current view across several operational systems?** Use an [Operational data store](../capabilities/serving/operational-data-store.md).
7. **Is the consumer another team's service, a partner or an external customer?** Put a [data API](../capabilities/serving/data-apis.md) in front of whichever store the earlier questions led to, rather than handing out SQL credentials.
8. **Otherwise** (internal tools, flexible or bulk reads, modest concurrency), use [SQL and programmatic access](../capabilities/serving/sql-access.md), preferably against read-optimised views rather than detailed tables.

Several paths often combine. A customer portal might read profile data from low-latency serving through an API, show account summaries from read-optimised views, and receive alerts from an event stream.

# Before go-live

- **Targets and support.** Agree latency, availability and freshness targets as [data service levels](../capabilities/data-products/data-slas.md), and who answers out of hours. Analytical platforms are often supported in business hours only.
- **Isolation.** Run application traffic on its own compute through [Workload isolation](../capabilities/compute/workload-isolation.md), so a heavy report cannot slow the application.
- **Identity.** Give the application its own service identity with only the access it needs ([Identity and authentication](../capabilities/security/identity-authentication.md)). Customers and partners need [External user and tenant identity](../capabilities/security/external-identity.md), not shared accounts.
- **Visibility.** Treat the read path as a published interface. Version it, list it in the [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md), and make sure [Impact analysis](../capabilities/metadata/impact-analysis.md) shows the application as a consumer, so table owners see it before they change anything.
- **Failure.** Decide what the application does when the platform is unavailable or stale, such as serving last-known values or hiding a feature, and test it.

The [Separate read models](../patterns/cqrs-read-models.md) pattern describes the general approach of keeping read models separate from the systems that write the data.

# Publishing data to the platform

Most of an organisation's data starts in applications. When analytics reads application databases directly or through unannounced extracts, every schema change risks breaking reports and models. The mechanisms below run from least to most deliberate.

| Mechanism | What the application team does | What consumers depend on | Main risk | Use when |
|---|---|---|---|---|
| [Change data capture](../capabilities/ingestion-integration/change-data-capture.md), or [Database replication and mirroring](../capabilities/ingestion-integration/database-replication.md) as a managed service | Allows log-based capture on agreed tables | Internal table structure | Schema changes break consumers, and meaning must be inferred from tables | Tables nobody models as events, or systems the team cannot change |
| [Transactional outbox](../patterns/transactional-outbox.md) | Writes a designed event to an outbox table in the same transaction as the business change; change data capture or a relay publishes it | A designed event schema | Delivery is at least once, so consumers must deduplicate; the outbox needs pruning | Services that can change and must publish events that match committed data |
| [Event streaming](../capabilities/ingestion-integration/event-streaming.md) with a [Schema registry](../capabilities/metadata/schema-registry.md) | Produces events straight to topics, with registered schemas and compatibility rules | A registered event schema | Writing to the database and the topic separately can leave them disagreeing; the outbox avoids this | Events that are not database changes, such as clicks or telemetry, or event-sourced services |
| [Data contracts](../capabilities/data-products/data-contracts.md), on top of any of the above | Publishes meaning, quality rules and service levels for each interface and checks them in its own build | Contracted promises, not only a schema | Contracts imposed by consumers and ignored by producers under delivery pressure | Every interface that crosses a team boundary |

In practice:

- Prefer designed events through an outbox for data meant for other teams. Use change data capture on agreed tables where events do not exist. Avoid scheduled query extraction against production databases.
- Register every event schema, set a compatibility rule (backward compatibility is a common default) and run the check in the producer's build, not only downstream.
- Change schemas by expand and contract through [Schema change management](../capabilities/development-lifecycle/schema-change-management.md): add the new field, move consumers, and remove the old field after an agreed notice period.
- List each published event and table in the [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md) with its owner and consumers, and check [Impact analysis](../capabilities/metadata/impact-analysis.md) before changing it.
- Expect duplicates and replays. Consumers need [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md).
- Classify personal data before it is published ([Data classification](../capabilities/governance/data-classification.md)). Once events reach many consumers, it is copied everywhere.

The [Application data publishing](../use-cases/usecase-application-data-publishing.md) use case lists the capabilities and minimum levels this needs, and [Shift-left data quality and governance](../patterns/shift-left.md) describes the wider approach of moving checks to producers.
