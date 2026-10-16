---
type: Persona
id: persona-software-engineer
title: Software engineer
description: Builds applications that produce data for the platform or consume data from it.
cares_about:
- event-streaming
- schema-registry
- data-contracts
- change-data-capture
- impact-analysis
- event-api-catalogue
- data-apis
- low-latency-serving
- read-optimised-views
- change-feeds
- schema-change-management
- operational-database
- operational-data-store
- application-integration
- message-queuing
- behavioural-event-collection
- real-time-inference
- online-feature-store
- data-slas
- embedded-analytics
- external-identity
- ci-cd
- identity-authentication
- real-time-analytics
- sql-access
patterns: [transactional-outbox, cqrs-read-models, shift-left, kappa-architecture]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Software engineers build the applications that produce most of an organisation's data, such as ordering, billing, mobile apps and customer portals, and increasingly the applications that read data and predictions back from the platform. They are measured on features and service reliability, so the data platform matters to them when it asks them to publish events, allow change capture on their database, honour a data contract or answer within their latency budget.

Success is integrating with the platform through stable, documented interfaces such as events, change feeds and APIs, without being blamed for analytics breakages they had no way to see coming.

# Goals

- Publish data from their services without slowing their own release cadence.
- Read data and predictions from the platform with predictable latency and availability.
- Know what depends on their schemas before they change them.

# Jobs

- Emit domain events and maintain their schemas.
- Agree data contracts with the data teams that consume their data.
- Expose their databases for change capture or replication without harming production.
- Call data APIs, feature endpoints and prediction endpoints from applications.
- Embed analytics and AI features in products.
- Change database schemas through versioned migrations.
- Register the events and APIs their service publishes, with an owner, a schema and a deprecation policy.
- Run compatibility and contract checks for their published interfaces in their own build pipeline.

# Pain points

- Analytics pipelines break on schema changes they did not know anyone depended on.
- Change capture and bulk extracts add load to production databases.
- Analytical data is too slow or too unreliable to serve from an application.
- Ownership of events is unclear once they leave the service.
- They cannot tell who consumes an event or API, so old versions are never retired.

# Questions they ask

- Events, change data capture or an API for getting our data to the platform?
- Which compatibility rules apply to our event schemas, and how are they enforced?
- What latency and availability can the platform guarantee if our application reads from it?
- How do we test our changes against downstream contracts in our own build pipeline?
- Where do we register our events and APIs so other teams can find them and we can see who uses them?
- Should our application read from a read-optimised view, a data API or an operational data store, and who supports it out of hours?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities they rely on most

| Capability | Domain | What it does |
|---|---|---|
| [Event streaming](../capabilities/ingestion-integration/event-streaming.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | Publish and subscribe to durable, ordered and replayable streams of events between systems. |
| [Schema registry](../capabilities/metadata/schema-registry.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Store and version schemas for events and messages, and enforce compatibility between producers and consumers. |
| [Data contracts](../capabilities/data-products/data-contracts.md) | [Data products](../capabilities/data-products/data-products.md) | Agree and enforce a dataset's schema, meaning, quality and service levels between producers and consumers. |
| [Change data capture](../capabilities/ingestion-integration/change-data-capture.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency. |
| [Impact analysis](../capabilities/metadata/impact-analysis.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Use lineage to find everything affected by a proposed change or a data incident. |
| [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | List the event streams and data APIs that systems publish, with owners, schemas, versions and consumers, so teams can find, subscribe to and safely change them. |
| [Data APIs](../capabilities/serving/data-apis.md) | [Serving and activation](../capabilities/serving/serving.md) | Expose datasets through managed REST or GraphQL APIs with authentication, paging and rate limits. |
| [Low-latency serving](../capabilities/serving/low-latency-serving.md) | [Serving and activation](../capabilities/serving/serving.md) | Serve individual records or small result sets to applications in milliseconds. |
| [Read-optimised views](../capabilities/serving/read-optimised-views.md) | [Serving and activation](../capabilities/serving/serving.md) | Precompute tables in the shape consumers read them, such as pre-joined or pre-aggregated tables, and keep them current with pipelines so reads are fast and cheap. |
| [Change feeds](../capabilities/serving/change-feeds.md) | [Serving and activation](../capabilities/serving/serving.md) | Expose row-level changes to tables as a stream that downstream consumers can process incrementally. |
| [Schema change management](../capabilities/development-lifecycle/schema-change-management.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | Version and apply database schema changes through controlled migrations. |
| [Operational database integration](../capabilities/serving/operational-database.md) | [Serving and activation](../capabilities/serving/serving.md) | Run transactional databases as part of the platform, with data flowing to and from analytical storage without separate pipelines. |
| [Operational data store](../capabilities/serving/operational-data-store.md) | [Serving and activation](../capabilities/serving/serving.md) | Hold a current, integrated view of data from several operational systems for operational reporting and lookups. |
| [Application integration](../capabilities/ingestion-integration/application-integration.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | Connect applications through APIs, events and process flows in near real time, outside the analytical data path. |
| [Message queuing](../capabilities/ingestion-integration/message-queuing.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | Distribute messages to competing consumers with per-message acknowledgement and redelivery. |
| [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | Collect clickstream and product events from web, mobile and server SDKs and validate them against a tracking plan. |
| [Real-time inference](../capabilities/mlops/real-time-inference.md) | [ML operations](../capabilities/mlops/mlops.md) | Serve predictions through low-latency endpoints. |
| [Online feature store](../capabilities/machine-learning/online-feature-store.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | Serve the latest feature values to models in milliseconds. |
| [Data service levels](../capabilities/data-products/data-slas.md) | [Data products](../capabilities/data-products/data-products.md) | Set and track service levels for data products, such as freshness, availability and quality. |
| [Embedded analytics](../capabilities/analytics-bi/embedded-analytics.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Put dashboards and analytics inside other applications and portals, often for external customers. |
| [External user and tenant identity](../capabilities/security/external-identity.md) | [Security and access](../capabilities/security/security.md) | Manage identities, tenants and permissions for customers and partners who use data products or embedded analytics. |
| [CI/CD](../capabilities/development-lifecycle/ci-cd.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | Build, test and deploy pipelines, models and infrastructure automatically on every change. |
| [Identity and authentication](../capabilities/security/identity-authentication.md) | [Security and access](../capabilities/security/security.md) | Authenticate people and services through central identity, single sign-on and short-lived credentials. |
| [Real-time analytical database](../capabilities/compute/real-time-analytics.md) | [Query and compute](../capabilities/compute/compute.md) | Answer analytical queries in milliseconds over fresh, high-volume data, often for user-facing applications. |
| [SQL and programmatic access](../capabilities/serving/sql-access.md) | [Serving and activation](../capabilities/serving/serving.md) | Connect tools and code to the platform through standard drivers and protocols. |

# Patterns

- [Transactional outbox](../patterns/transactional-outbox.md)
- [Separate read models](../patterns/cqrs-read-models.md)
- [Shift-left data quality and governance](../patterns/shift-left.md)
- [Kappa architecture](../patterns/kappa-architecture.md)

# Use cases they take part in

- [Agentic process automation](../use-cases/usecase-agentic-automation.md): AI agents complete multi-step business tasks using enterprise data and tools under controls.
- [Application data publishing](../use-cases/usecase-application-data-publishing.md): Application teams publish their data to the platform through versioned events and change capture under agreed contracts, so downstream consumers do not break when applications change.
- [Customer 360](../use-cases/usecase-customer-360.md): Give every channel a single, trusted view of each customer.
- [Customer-facing analytics](../use-cases/usecase-customer-facing-analytics.md): Give external customers fast, secure analytics inside a product.
- [Document data extraction](../use-cases/usecase-document-extraction.md): Extract fields and tables from invoices, claims, contracts and forms into business systems, with people reviewing uncertain results.
- [Operational reporting](../use-cases/usecase-operational-reporting.md): Report on current operations within minutes of events happening.
- [Personalised recommendations](../use-cases/usecase-recommendations.md): Recommend products or content to each user in real time.
- [Privacy rights handling](../use-cases/usecase-privacy-rights.md): Find, report and erase an individual's data across the estate within legal deadlines.
- [Real-time fraud detection](../use-cases/usecase-fraud-detection.md): Score transactions in milliseconds and block or flag suspicious ones.
- [Security and log analytics](../use-cases/usecase-security-log-analytics.md): Collect and analyse large volumes of logs to detect threats and investigate incidents.

# Frameworks they work with

- [Open Data Contract Standard (ODCS)](../frameworks/framework-bitol-odcs.md): An open YAML standard for describing a data contract, covering schema, quality, service levels, roles, pricing and where the data is served.
