---
type: Use Case
id: usecase-security-log-analytics
title: Security and log analytics
description: Collect and analyse large volumes of logs to detect threats and investigate incidents.
aliases: [SIEM, threat hunting]
requires:
- {capability: streaming-ingestion, level: 3, why: Logs arrive continuously at terabytes a day from many collectors.}
- {capability: observability-analytics, level: 3, why: 'Logs, metrics and traces are stored and analysed at scale with search, dashboards and alerts.'}
- {capability: semi-structured-data, level: 3, why: 'Log records are nested and vary by source, and must be queried without flattening first.'}
- {capability: full-text-search, level: 3, why: 'Investigators search free text such as hostnames, hashes and user names across huge volumes.'}
- {capability: stream-processing, level: 2, why: Detection rules run continuously over incoming events.}
- {capability: data-enrichment, level: 2, why: 'Events are enriched with asset, identity and threat-intelligence context for triage.'}
- {capability: object-storage, level: 3, why: Petabytes of history must be kept affordably.}
- {capability: storage-tiering, level: 3, why: Recent logs stay in fast storage while older logs move to cheaper tiers automatically.}
- {capability: data-retention, level: 3, why: Retention periods set by regulation and policy must be applied by log type.}
- {capability: audit-logging, level: 3, why: 'Security logs must be tamper-evident, and access to them recorded.'}
- {capability: role-based-access, level: 3, why: Logs contain sensitive data and only security staff should search them.}
- {capability: elastic-scaling, level: 2, why: Investigations create sudden bursts of heavy queries.}
- {capability: application-integration, level: 2, why: Detections must open cases in incident response and ticketing tools.}
benefits_from:
- {capability: open-table-formats, why: Lets several tools query one copy of log data and reduces SIEM lock-in.}
- {capability: decoupled-storage-compute, why: Allows long retention without paying for idle compute.}
- {capability: data-threat-detection, why: Adds detection of abnormal access to the data platform itself.}
- {capability: graph-data, why: 'Traces attack paths across users, hosts and resources.'}
- {capability: ai-agents, why: Helps analysts triage alerts and gather context faster.}
- {capability: approximate-query-processing, why: Speeds up counts over very large volumes during hunting.}
- {capability: immutable-backups, why: Protects evidence from attackers who try to delete it.}
- {capability: deidentification, why: Masks personal data in logs where full detail is not needed.}
- {capability: cost-attribution, why: Shows which sources drive ingestion and storage cost.}
- {capability: cost-forecasting, why: 'Projects ingestion and retention cost as log sources are added, so sources are not dropped mid-year to fit the budget.'}
personas:
- persona-security-officer
- persona-platform-engineer
- persona-data-engineer
- persona-software-engineer
- persona-risk-compliance
- persona-finops-practitioner
patterns: [data-lake, lakehouse, kappa-architecture]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Security teams collect logs from endpoints, networks, identity providers, cloud services and applications to detect attacks and investigate incidents. Volumes run to terabytes a day, formats vary, and detection rules must run within minutes while investigators may need to search a year or more of history. Logs are shipped continuously, normalised to a common schema, enriched with asset, identity and threat information, checked against detection rules, and kept in hot storage for fast search and cheaper storage for long retention.

Good looks like high-value log sources all collected, detections firing within minutes, investigators searching months of history in seconds or minutes, and a cost per gigabyte low enough that sources do not have to be dropped to fit the budget. Using a security data lake in open formats alongside or behind a traditional SIEM is a common way to control that cost.

# Non-functional requirements

- Ingestion of terabytes a day with bursts during incidents, without dropping events.
- Detection latency of seconds to minutes from event to alert.
- Search over the most recent 30 to 90 days returns in seconds to minutes.
- Retention of at least a year searchable, longer in archive where regulation requires.
- Logs are tamper-evident and access to them is restricted and recorded.

# Risks

- Ingestion cost forces teams to drop log sources, leaving blind spots.
- Inconsistent log schemas break detection rules without anyone noticing.
- Too many low-value alerts bury real incidents.
- Retention is too short for incidents discovered months after they started.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 3 (Defined) | Logs arrive continuously at terabytes a day from many collectors. |
| [Observability data analytics](../capabilities/specialised-data/observability-analytics.md) | [Specialised data types](../capabilities/specialised-data/specialised-data.md) | 3 (Defined) | Logs, metrics and traces are stored and analysed at scale with search, dashboards and alerts. |
| [Semi-structured data](../capabilities/storage/semi-structured-data.md) | [Storage and table management](../capabilities/storage/storage.md) | 3 (Defined) | Log records are nested and vary by source, and must be queried without flattening first. |
| [Full-text search](../capabilities/specialised-data/full-text-search.md) | [Specialised data types](../capabilities/specialised-data/specialised-data.md) | 3 (Defined) | Investigators search free text such as hostnames, hashes and user names across huge volumes. |
| [Stream processing](../capabilities/processing/stream-processing.md) | [Processing and transformation](../capabilities/processing/processing.md) | 2 (Managed) | Detection rules run continuously over incoming events. |
| [Data enrichment](../capabilities/processing/data-enrichment.md) | [Processing and transformation](../capabilities/processing/processing.md) | 2 (Managed) | Events are enriched with asset, identity and threat-intelligence context for triage. |
| [Object storage](../capabilities/storage/object-storage.md) | [Storage and table management](../capabilities/storage/storage.md) | 3 (Defined) | Petabytes of history must be kept affordably. |
| [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md) | [Storage and table management](../capabilities/storage/storage.md) | 3 (Defined) | Recent logs stay in fast storage while older logs move to cheaper tiers automatically. |
| [Retention and disposal](../capabilities/governance/data-retention.md) | [Governance and compliance](../capabilities/governance/governance.md) | 3 (Defined) | Retention periods set by regulation and policy must be applied by log type. |
| [Audit logging](../capabilities/security/audit-logging.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Security logs must be tamper-evident, and access to them recorded. |
| [Role-based access control](../capabilities/security/role-based-access.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Logs contain sensitive data and only security staff should search them. |
| [Elastic scaling](../capabilities/compute/elastic-scaling.md) | [Query and compute](../capabilities/compute/compute.md) | 2 (Managed) | Investigations create sudden bursts of heavy queries. |
| [Application integration](../capabilities/ingestion-integration/application-integration.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 2 (Managed) | Detections must open cases in incident response and ticketing tools. |

# Capabilities that help

| Capability | Why |
|---|---|
| [Open table formats](../capabilities/storage/open-table-formats.md) | Lets several tools query one copy of log data and reduces SIEM lock-in. |
| [Decoupled storage and compute](../capabilities/compute/decoupled-storage-compute.md) | Allows long retention without paying for idle compute. |
| [Data threat detection](../capabilities/security/data-threat-detection.md) | Adds detection of abnormal access to the data platform itself. |
| [Graph data](../capabilities/specialised-data/graph-data.md) | Traces attack paths across users, hosts and resources. |
| [AI agents](../capabilities/generative-ai/ai-agents.md) | Helps analysts triage alerts and gather context faster. |
| [Approximate query processing](../capabilities/compute/approximate-query-processing.md) | Speeds up counts over very large volumes during hunting. |
| [Immutable backups](../capabilities/platform-operations/immutable-backups.md) | Protects evidence from attackers who try to delete it. |
| [De-identification](../capabilities/governance/deidentification.md) | Masks personal data in logs where full detail is not needed. |
| [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md) | Shows which sources drive ingestion and storage cost. |
| [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md) | Projects ingestion and retention cost as log sources are added, so sources are not dropped mid-year to fit the budget. |

# Personas

- [Security and privacy officer](../personas/persona-security-officer.md): Protects data and makes sure it is used lawfully.
- [Data platform engineer](../personas/persona-platform-engineer.md): Builds and runs the shared data platform and its self-service tooling.
- [Data engineer](../personas/persona-data-engineer.md): Builds and operates the pipelines that ingest, transform and deliver data.
- [Software engineer](../personas/persona-software-engineer.md): Builds applications that produce data for the platform or consume data from it.
- [Risk and compliance officer](../personas/persona-risk-compliance.md): Needs assurance, with evidence, that data controls meet regulatory and internal requirements.
- [FinOps practitioner](../personas/persona-finops-practitioner.md): Tracks, allocates and optimises what the data platform costs.

# Patterns

- [Data lake](../patterns/data-lake.md)
- [Lakehouse](../patterns/lakehouse.md)
- [Kappa architecture](../patterns/kappa-architecture.md)

# Frameworks that apply

- [DORA (Digital Operational Resilience Act)](../frameworks/framework-eu-dora.md): Regulation (EU) 2022/2554, which sets ICT risk, incident, resilience testing and third-party requirements for EU financial entities.

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 12 of 13 | [Data enrichment](../capabilities/processing/data-enrichment.md) |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 13 of 13 |  |
| [Google Cloud](../platforms/platform-google-cloud.md) | 13 of 13 |  |
| [Snowflake](../platforms/platform-snowflake.md) | 11 of 13 | [Stream processing](../capabilities/processing/stream-processing.md), [Data enrichment](../capabilities/processing/data-enrichment.md) |
| [Databricks](../platforms/platform-databricks.md) | 8 of 13 | [Observability data analytics](../capabilities/specialised-data/observability-analytics.md), [Data enrichment](../capabilities/processing/data-enrichment.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Application integration](../capabilities/ingestion-integration/application-integration.md) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 11 of 13 | [Stream processing](../capabilities/processing/stream-processing.md), [Application integration](../capabilities/ingestion-integration/application-integration.md) |
| [Informatica](../platforms/platform-informatica.md) | 7 of 13 | [Observability data analytics](../capabilities/specialised-data/observability-analytics.md), [Full-text search](../capabilities/specialised-data/full-text-search.md), [Stream processing](../capabilities/processing/stream-processing.md), [Object storage](../capabilities/storage/object-storage.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Retention and disposal](../capabilities/governance/data-retention.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 6 of 13 | [Observability data analytics](../capabilities/specialised-data/observability-analytics.md), [Semi-structured data](../capabilities/storage/semi-structured-data.md), [Full-text search](../capabilities/specialised-data/full-text-search.md), [Data enrichment](../capabilities/processing/data-enrichment.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Application integration](../capabilities/ingestion-integration/application-integration.md) |
| [Oracle](../platforms/platform-oracle.md) | 6 of 13 | [Observability data analytics](../capabilities/specialised-data/observability-analytics.md), [Data enrichment](../capabilities/processing/data-enrichment.md), [Object storage](../capabilities/storage/object-storage.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Role-based access control](../capabilities/security/role-based-access.md), [Application integration](../capabilities/ingestion-integration/application-integration.md) |
| [SAP](../platforms/platform-sap.md) | 4 of 13 | [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md), [Observability data analytics](../capabilities/specialised-data/observability-analytics.md), [Full-text search](../capabilities/specialised-data/full-text-search.md), [Stream processing](../capabilities/processing/stream-processing.md), [Data enrichment](../capabilities/processing/data-enrichment.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Audit logging](../capabilities/security/audit-logging.md), [Role-based access control](../capabilities/security/role-based-access.md), [Elastic scaling](../capabilities/compute/elastic-scaling.md) |
| [Teradata](../platforms/platform-teradata.md) | 5 of 13 | [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md), [Observability data analytics](../capabilities/specialised-data/observability-analytics.md), [Full-text search](../capabilities/specialised-data/full-text-search.md), [Stream processing](../capabilities/processing/stream-processing.md), [Data enrichment](../capabilities/processing/data-enrichment.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Application integration](../capabilities/ingestion-integration/application-integration.md) |
| [IBM](../platforms/platform-ibm.md) | 5 of 13 | [Observability data analytics](../capabilities/specialised-data/observability-analytics.md), [Semi-structured data](../capabilities/storage/semi-structured-data.md), [Data enrichment](../capabilities/processing/data-enrichment.md), [Object storage](../capabilities/storage/object-storage.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Role-based access control](../capabilities/security/role-based-access.md), [Elastic scaling](../capabilities/compute/elastic-scaling.md), [Application integration](../capabilities/ingestion-integration/application-integration.md) |
| [Palantir](../platforms/platform-palantir.md) | 4 of 13 | [Observability data analytics](../capabilities/specialised-data/observability-analytics.md), [Semi-structured data](../capabilities/storage/semi-structured-data.md), [Full-text search](../capabilities/specialised-data/full-text-search.md), [Data enrichment](../capabilities/processing/data-enrichment.md), [Object storage](../capabilities/storage/object-storage.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Elastic scaling](../capabilities/compute/elastic-scaling.md), [Application integration](../capabilities/ingestion-integration/application-integration.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 10 of 13 | [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Application integration](../capabilities/ingestion-integration/application-integration.md) |
| [Independent vendors](../platforms/platform-independent.md) | 9 of 13 | [Object storage](../capabilities/storage/object-storage.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Role-based access control](../capabilities/security/role-based-access.md), [Elastic scaling](../capabilities/compute/elastic-scaling.md) |
