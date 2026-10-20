---
type: Use Case
id: usecase-application-data-publishing
title: Application data publishing
description: Application teams publish their data to the platform through versioned events and change capture under agreed contracts, so downstream consumers do not break when applications change.
requires:
- {capability: event-streaming, level: 3, why: 'Domain events go to durable, replayable topics that many consumers read independently.'}
- {capability: schema-registry, level: 3, why: 'Every event schema is registered, and incompatible changes are rejected before consumers see them.'}
- {capability: data-contracts, level: 3, why: 'Meaning, quality and service levels are agreed and checked, not only field types.'}
- {capability: change-data-capture, level: 2, why: 'Where events are not emitted, agreed tables are captured from the log with measured load on production.'}
- {capability: schema-change-management, level: 2, why: 'Database changes go through versioned migrations, using expand and contract for anything consumers read.'}
- {capability: impact-analysis, level: 3, why: 'Producers see, before merging, which pipelines, reports and services use a field they want to change.'}
- {capability: ci-cd, level: 3, why: 'Compatibility and contract checks run in the producer''s own build pipeline, not only downstream.'}
- {capability: data-ownership, level: 2, why: Each event and published table has an owning team that answers for it after it leaves the service.}
- {capability: event-api-catalogue, level: 2, why: 'Teams find published events with their owner, schema and consumers instead of asking around.'}
- {capability: streaming-ingestion, level: 2, why: Published events land in platform tables within minutes for analytics and features.}
benefits_from:
- {capability: stream-to-table, why: Exposes topics as tables without a separate loader to run.}
- {capability: bad-data-quarantine, why: Holds events that fail contract checks for replay instead of blocking the stream.}
- {capability: idempotent-loading, why: Replayed or duplicated events are not counted twice.}
- {capability: data-slas, why: Consumers see freshness and availability targets and their history.}
- {capability: behavioural-event-collection, why: Tracking plans validate product events from web and mobile SDKs.}
- {capability: database-replication, why: 'Covers tables nobody models as events, without building capture pipelines.'}
- {capability: column-lineage, why: Narrows impact to the fields actually changed rather than whole tables.}
- {capability: usage-metadata, why: 'Shows which consumers still read old versions, so they can be retired.'}
- {capability: data-product-specification, why: Describes published data as a source-aligned data product where the organisation works that way.}
personas:
- persona-software-engineer
- persona-data-engineer
- persona-data-architect
- persona-data-product-owner
- persona-analytics-engineer
- persona-platform-engineer
patterns: [transactional-outbox, shift-left, data-mesh]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Most of an organisation's data starts in applications such as ordering, billing, mobile apps and customer portals, built by software teams that release weekly or daily. When analytics reads application databases directly or through unannounced extracts, every schema change risks breaking reports and models, and the application team finds out from an incident. Contracted publishing makes the application team the producer of record. It emits domain events, often through a transactional outbox, or allows change capture on agreed tables; registers schemas with compatibility rules; publishes a contract covering meaning, quality and service levels; and checks proposed changes against that contract and against known consumers in its own build pipeline.

Good looks like breaking changes caught in the producer's CI before release, every published event and table listed with an owner and its consumers, schema changes rolled out by expand and contract with a published notice period, and capture adding agreed, measured load to production. Analytics, ML features and other services subscribe to stable interfaces instead of reaching into application internals.

# Non-functional requirements

- Breaking changes to a published interface are blocked in CI unless a new version is released alongside the old one.
- Old versions of an event or table stay available for an agreed notice period, often 30 to 90 days.
- Change capture adds no more than an agreed share of load to production databases, measured and reviewed with the database owner.
- Published events reach platform tables within the latency stated in the contract, typically seconds to minutes.

# Risks

- Contracts are imposed by consumers and ignored by producers under delivery pressure.
- Compatibility checks pass while meaning changes, such as an amount moving from gross to net.
- Versions multiply because nobody knows when consumers have moved off old ones.
- Personal data is published in events and copied into many consumers before classification catches up.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [Event streaming](../capabilities/ingestion-integration/event-streaming.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 3 (Defined) | Domain events go to durable, replayable topics that many consumers read independently. |
| [Schema registry](../capabilities/metadata/schema-registry.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | 3 (Defined) | Every event schema is registered, and incompatible changes are rejected before consumers see them. |
| [Data contracts](../capabilities/data-products/data-contracts.md) | [Data products](../capabilities/data-products/data-products.md) | 3 (Defined) | Meaning, quality and service levels are agreed and checked, not only field types. |
| [Change data capture](../capabilities/ingestion-integration/change-data-capture.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 2 (Managed) | Where events are not emitted, agreed tables are captured from the log with measured load on production. |
| [Schema change management](../capabilities/development-lifecycle/schema-change-management.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 2 (Managed) | Database changes go through versioned migrations, using expand and contract for anything consumers read. |
| [Impact analysis](../capabilities/metadata/impact-analysis.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | 3 (Defined) | Producers see, before merging, which pipelines, reports and services use a field they want to change. |
| [CI/CD](../capabilities/development-lifecycle/ci-cd.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 3 (Defined) | Compatibility and contract checks run in the producer's own build pipeline, not only downstream. |
| [Ownership and stewardship](../capabilities/governance/data-ownership.md) | [Governance and compliance](../capabilities/governance/governance.md) | 2 (Managed) | Each event and published table has an owning team that answers for it after it leaves the service. |
| [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | 2 (Managed) | Teams find published events with their owner, schema and consumers instead of asking around. |
| [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 2 (Managed) | Published events land in platform tables within minutes for analytics and features. |

# Capabilities that help

| Capability | Why |
|---|---|
| [Stream-to-table materialisation](../capabilities/ingestion-integration/stream-to-table.md) | Exposes topics as tables without a separate loader to run. |
| [Bad-data quarantine](../capabilities/data-quality/bad-data-quarantine.md) | Holds events that fail contract checks for replay instead of blocking the stream. |
| [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md) | Replayed or duplicated events are not counted twice. |
| [Data service levels](../capabilities/data-products/data-slas.md) | Consumers see freshness and availability targets and their history. |
| [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md) | Tracking plans validate product events from web and mobile SDKs. |
| [Database replication and mirroring](../capabilities/ingestion-integration/database-replication.md) | Covers tables nobody models as events, without building capture pipelines. |
| [Column-level lineage](../capabilities/metadata/column-lineage.md) | Narrows impact to the fields actually changed rather than whole tables. |
| [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md) | Shows which consumers still read old versions, so they can be retired. |
| [Data product specification](../capabilities/data-products/data-product-specification.md) | Describes published data as a source-aligned data product where the organisation works that way. |

# Personas

- [Software engineer](../personas/persona-software-engineer.md): Builds applications that produce data for the platform or consume data from it.
- [Data engineer](../personas/persona-data-engineer.md): Builds and operates the pipelines that ingest, transform and deliver data.
- [Data architect](../personas/persona-data-architect.md): Designs the data platform and how data flows, is modelled and is governed across the organisation.
- [Data product owner](../personas/persona-data-product-owner.md): Owns the value, roadmap and consumers of one or more data products.
- [Analytics engineer](../personas/persona-analytics-engineer.md): Turns raw data into tested, documented, analysis-ready models.
- [Data platform engineer](../personas/persona-platform-engineer.md): Builds and runs the shared data platform and its self-service tooling.

# Patterns

- [Transactional outbox](../patterns/transactional-outbox.md)
- [Shift-left data quality and governance](../patterns/shift-left.md)
- [Data mesh](../patterns/data-mesh.md)

# Frameworks that apply

- [Data mesh principles](../frameworks/framework-data-mesh.md): Four principles for decentralising analytical data ownership to business domains while keeping data interoperable and governed.
- [Open Data Contract Standard (ODCS)](../frameworks/framework-bitol-odcs.md): An open YAML standard for describing a data contract, covering schema, quality, service levels, roles, pricing and where the data is served.

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 6 of 10 | [Data contracts](../capabilities/data-products/data-contracts.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md) |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 8 of 10 | [Data contracts](../capabilities/data-products/data-contracts.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md) |
| [Google Cloud](../platforms/platform-google-cloud.md) | 9 of 10 | [Schema change management](../capabilities/development-lifecycle/schema-change-management.md) |
| [Snowflake](../platforms/platform-snowflake.md) | 5 of 10 | [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Schema registry](../capabilities/metadata/schema-registry.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md) |
| [Databricks](../platforms/platform-databricks.md) | 4 of 10 | [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Schema registry](../capabilities/metadata/schema-registry.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 2 of 10 | [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Schema registry](../capabilities/metadata/schema-registry.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Impact analysis](../capabilities/metadata/impact-analysis.md), [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md) |
| [Informatica](../platforms/platform-informatica.md) | 4 of 10 | [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Schema registry](../capabilities/metadata/schema-registry.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 4 of 10 | [Data contracts](../capabilities/data-products/data-contracts.md), [Change data capture](../capabilities/ingestion-integration/change-data-capture.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md) |
| [Oracle](../platforms/platform-oracle.md) | 3 of 10 | [Schema registry](../capabilities/metadata/schema-registry.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Impact analysis](../capabilities/metadata/impact-analysis.md), [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md) |
| [SAP](../platforms/platform-sap.md) | 4 of 10 | [Schema registry](../capabilities/metadata/schema-registry.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Impact analysis](../capabilities/metadata/impact-analysis.md), [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Teradata](../platforms/platform-teradata.md) | 0 of 10 | [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Schema registry](../capabilities/metadata/schema-registry.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Change data capture](../capabilities/ingestion-integration/change-data-capture.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Impact analysis](../capabilities/metadata/impact-analysis.md), [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md), [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md) |
| [IBM](../platforms/platform-ibm.md) | 7 of 10 | [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md) |
| [Palantir](../platforms/platform-palantir.md) | 4 of 10 | [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Schema registry](../capabilities/metadata/schema-registry.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md) |
| [SAS](../platforms/platform-sas.md) | 3 of 10 | [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Schema registry](../capabilities/metadata/schema-registry.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Change data capture](../capabilities/ingestion-integration/change-data-capture.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md) |
| [Dataiku](../platforms/platform-dataiku.md) | 2 of 10 | [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Schema registry](../capabilities/metadata/schema-registry.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Change data capture](../capabilities/ingestion-integration/change-data-capture.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md), [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 9 of 10 | [Impact analysis](../capabilities/metadata/impact-analysis.md) |
| [Independent vendors](../platforms/platform-independent.md) | 8 of 10 | [Schema registry](../capabilities/metadata/schema-registry.md), [Schema change management](../capabilities/development-lifecycle/schema-change-management.md) |
