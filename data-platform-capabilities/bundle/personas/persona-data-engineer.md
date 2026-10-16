---
type: Persona
id: persona-data-engineer
title: Data engineer
description: Builds and operates the pipelines that ingest, transform and deliver data.
cares_about:
- workflow-orchestration
- batch-ingestion
- change-data-capture
- sql-transformation
- dataframe-apis
- transformation-as-code
- incremental-processing
- idempotent-loading
- backfill-replay
- data-quality-rules
- pipeline-monitoring
- data-testing
- ci-cd
- environment-promotion
- version-control
- schema-evolution
- open-table-formats
- table-maintenance
- distributed-processing
- single-node-processing
- streaming-ingestion
- stream-processing
- event-streaming
- event-driven-triggering
- saas-connectors
- bad-data-quarantine
- freshness-monitoring
- data-contracts
- query-performance-analysis
- runtime-management
- secrets-management
- table-lineage
patterns: [elt, medallion-architecture, write-audit-publish, kappa-architecture, shift-left]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data engineers work in a central data team or are embedded in a domain or product team. Their days go on writing ingestion and transformation code, reviewing colleagues' changes, investigating failed or late runs and negotiating with source system owners about extract windows and schema changes. Many share an on-call rota for production pipelines.

Success is data that lands on time and complete, pipelines that recover from failure without losing or duplicating records, and changes that can be released without breaking consumers. They tend to be noticed only when something goes wrong: a late report, a broken dashboard or a source change that nobody announced.

# Goals

- Deliver complete data on time against agreed service levels.
- Make every pipeline safe to rerun, backfill and change.
- Spend less time on hand-built connectors and firefighting, and more on new sources and consumers.
- Catch quality and schema problems before consumers do.

# Jobs

- Build ingestion from databases, SaaS applications, files, APIs and event streams.
- Write and test transformations in SQL or DataFrame code, and review colleagues' changes.
- Schedule pipelines, set their dependencies and retries, and keep them running.
- Investigate failures and late data, then rerun or backfill the affected periods.
- Add quality checks and quarantine rules, and agree contracts with source teams.
- Handle schema changes from sources and maintain tables through compaction and partitioning.
- Tune slow or expensive jobs.
- Choose single-node, distributed or streaming processing for each pipeline, and size its compute.
- Upgrade pipelines to new runtime and library versions, and check that their outputs do not change.
- Take part in the on-call rota and keep runbooks for production pipelines up to date.

# Pain points

- Source systems change schemas without notice and pipelines fail overnight.
- Noisy alerts with no clear owner make on-call tiring.
- Retries and replays leave duplicate or missing rows, especially in change capture and streaming.
- Waiting for access to sources, credentials and environments delays new work.
- Tests, documentation and lineage are the first things cut under deadline pressure.
- Runtime and library upgrades break jobs that have run unchanged for years.
- Development environments hold little realistic data, so changes are effectively tested in production.

# Questions they ask

- Batch extraction, change data capture or streaming for this source, given the freshness consumers actually need?
- Should we build this connector ourselves or use a managed one?
- How do we make loads idempotent so that replays and backfills are safe?
- Should quality checks sit at ingestion, during transformation or at publication, or at all three?
- What testing and promotion path must every pipeline follow before it reaches production?
- Does this job need a cluster, or would a single-node engine do it faster and cheaper?
- What should this pipeline cost per run, and how will we know when that drifts?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities they rely on most

| Capability | Domain | What it does |
|---|---|---|
| [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md) | [Orchestration](../capabilities/orchestration/orchestration.md) | Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts. |
| [Batch ingestion](../capabilities/ingestion-integration/batch-ingestion.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | Load data from sources on a schedule or on demand, in bulk or incrementally. |
| [Change data capture](../capabilities/ingestion-integration/change-data-capture.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency. |
| [SQL transformation](../capabilities/processing/sql-transformation.md) | [Processing and transformation](../capabilities/processing/processing.md) | Transform data inside the platform using SQL, typically after it has been loaded. |
| [DataFrame APIs](../capabilities/processing/dataframe-apis.md) | [Processing and transformation](../capabilities/processing/processing.md) | Express transformations in Python, Scala or other languages through DataFrame interfaces that run in the engine. |
| [Transformation as code](../capabilities/processing/transformation-as-code.md) | [Processing and transformation](../capabilities/processing/processing.md) | Define transformations as version-controlled, tested, modular code whose dependencies are resolved automatically. |
| [Incremental processing](../capabilities/processing/incremental-processing.md) | [Processing and transformation](../capabilities/processing/processing.md) | Process only new or changed data instead of recomputing everything each run. |
| [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | Make loads safe to retry or replay by removing duplicates on write so nothing is counted twice. |
| [Backfill and reprocessing](../capabilities/orchestration/backfill-replay.md) | [Orchestration](../capabilities/orchestration/orchestration.md) | Rerun pipelines over historical periods or replay events to correct or rebuild data. |
| [Data quality rules](../capabilities/data-quality/data-quality-rules.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency. |
| [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Track pipeline runs, failures and durations, and alert the right people. |
| [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | Test transformation logic and data with unit, integration and regression tests before release. |
| [CI/CD](../capabilities/development-lifecycle/ci-cd.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | Build, test and deploy pipelines, models and infrastructure automatically on every change. |
| [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | Promote the same artefacts through development, test and production with environment-specific configuration. |
| [Version control integration](../capabilities/development-lifecycle/version-control.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | Keep code and configuration in Git and work with branches from inside the platform. |
| [Schema enforcement and evolution](../capabilities/storage/schema-evolution.md) | [Storage and table management](../capabilities/storage/storage.md) | Reject data that does not match a table's schema, and change schemas safely over time. |
| [Open table formats](../capabilities/storage/open-table-formats.md) | [Storage and table management](../capabilities/storage/storage.md) | Manage collections of files as transactional tables with a defined schema, history and metadata. |
| [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md) | [Storage and table management](../capabilities/storage/storage.md) | Compact small files, remove obsolete files and reorganise data so tables stay fast and cheap. |
| [Distributed processing](../capabilities/processing/distributed-processing.md) | [Processing and transformation](../capabilities/processing/processing.md) | Process large datasets in parallel across a cluster of machines. |
| [Single-node processing](../capabilities/processing/single-node-processing.md) | [Processing and transformation](../capabilities/processing/processing.md) | Process small to medium datasets quickly on one machine using in-process engines. |
| [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency. |
| [Stream processing](../capabilities/processing/stream-processing.md) | [Processing and transformation](../capabilities/processing/processing.md) | Transform, join and aggregate events continuously as they arrive, keeping state across events. |
| [Event streaming](../capabilities/ingestion-integration/event-streaming.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | Publish and subscribe to durable, ordered and replayable streams of events between systems. |
| [Event-driven triggering](../capabilities/orchestration/event-driven-triggering.md) | [Orchestration](../capabilities/orchestration/orchestration.md) | Start pipelines when something happens, such as a file arriving, a table changing or a message being published. |
| [SaaS application connectors](../capabilities/ingestion-integration/saas-connectors.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors. |
| [Bad-data quarantine](../capabilities/data-quality/bad-data-quarantine.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | Route records that fail checks to a holding area for inspection and replay instead of failing or loading them. |
| [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | Detect when data arrives later than expected or misses its freshness target. |
| [Data contracts](../capabilities/data-products/data-contracts.md) | [Data products](../capabilities/data-products/data-products.md) | Agree and enforce a dataset's schema, meaning, quality and service levels between producers and consumers. |
| [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Inspect query plans, job stages, run history and bottlenecks to tune performance and cost. |
| [Runtime and environment management](../capabilities/development-lifecycle/runtime-management.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | Define, version and upgrade the engine runtimes, libraries and images that notebooks, jobs and model serving run on, so code reruns the same way and upgrades do not break it. |
| [Secrets management](../capabilities/security/secrets-management.md) | [Security and access](../capabilities/security/security.md) | Store and rotate the credentials and keys used by pipelines and tools without putting them in code. |
| [Table-level lineage](../capabilities/metadata/table-lineage.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Track dependencies between datasets, tables and views. |

# Patterns

- [ELT](../patterns/elt.md)
- [Medallion architecture](../patterns/medallion-architecture.md)
- [Write-audit-publish](../patterns/write-audit-publish.md)
- [Kappa architecture](../patterns/kappa-architecture.md)
- [Shift-left data quality and governance](../patterns/shift-left.md)

# Use cases they take part in

- [Application data publishing](../use-cases/usecase-application-data-publishing.md): Application teams publish their data to the platform through versioned events and change capture under agreed contracts, so downstream consumers do not break when applications change.
- [Churn prediction](../use-cases/usecase-churn-prediction.md): Score customers regularly by likelihood to leave so teams can act before they do.
- [Credit decisioning](../use-cases/usecase-credit-decisioning.md): Score credit applications and decide to approve, decline or refer them, with reasons, fairness checks and model risk controls.
- [Customer 360](../use-cases/usecase-customer-360.md): Give every channel a single, trusted view of each customer.
- [Customer-facing analytics](../use-cases/usecase-customer-facing-analytics.md): Give external customers fast, secure analytics inside a product.
- [Data sharing and monetisation](../use-cases/usecase-data-monetisation.md): Share or sell data products to partners and customers under agreed terms.
- [Demand forecasting](../use-cases/usecase-demand-forecasting.md): Forecast demand by product, location and time to plan stock, staff and supply.
- [Document data extraction](../use-cases/usecase-document-extraction.md): Extract fields and tables from invoices, claims, contracts and forms into business systems, with people reviewing uncertain results.
- [Enterprise management reporting](../use-cases/usecase-enterprise-reporting.md): Produce trusted, consistent KPIs and management reports across the organisation.
- [IoT predictive maintenance](../use-cases/usecase-iot-predictive-maintenance.md): Analyse sensor telemetry to predict equipment failures before they happen.
- [Knowledge assistant](../use-cases/usecase-rag-assistant.md): A generative AI assistant that answers questions from internal documents, with citations.
- [Legacy warehouse migration](../use-cases/usecase-platform-modernisation.md): Move from an on-premises warehouse or Hadoop estate to a cloud data platform.
- [Marketing audience activation](../use-cases/usecase-marketing-activation.md): Build audiences from platform data and sync them to marketing and advertising tools.
- [Operational reporting](../use-cases/usecase-operational-reporting.md): Report on current operations within minutes of events happening.
- [Personalised recommendations](../use-cases/usecase-recommendations.md): Recommend products or content to each user in real time.
- [Platform cost management and chargeback](../use-cases/usecase-platform-cost-management.md): Attribute, forecast and control what the data platform costs, and recover it from the teams and products that use it.
- [Privacy rights handling](../use-cases/usecase-privacy-rights.md): Find, report and erase an individual's data across the estate within legal deadlines.
- [Real-time fraud detection](../use-cases/usecase-fraud-detection.md): Score transactions in milliseconds and block or flag suspicious ones.
- [Regulatory reporting](../use-cases/usecase-regulatory-reporting.md): Produce accurate, auditable and reproducible submissions to regulators.
- [Security and log analytics](../use-cases/usecase-security-log-analytics.md): Collect and analyse large volumes of logs to detect threats and investigate incidents.
- [Self-service BI](../use-cases/usecase-self-service-bi.md): Analysts and business users explore governed data and build their own reports with trusted metrics.
- [Self-service domain onboarding](../use-cases/usecase-domain-onboarding.md): Give a new domain or product team a governed workspace, path to live and budget on the shared platform within a day.
- [Sensitive data protection](../use-cases/usecase-sensitive-data-protection.md): Know where sensitive and personal data is across the platform, control who can reach it through one set of policies, and prove it to auditors.

# Frameworks they work with

- [Open Data Contract Standard (ODCS)](../frameworks/framework-bitol-odcs.md): An open YAML standard for describing a data contract, covering schema, quality, service levels, roles, pricing and where the data is served.
