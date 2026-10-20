---
type: Use Case
id: usecase-marketing-activation
title: Marketing audience activation
description: Build audiences from platform data and sync them to marketing and advertising tools.
aliases: [audience sync, composable CDP]
requires:
- {capability: audience-activation, level: 3, why: Marketers build audiences from platform data and deliver them to channels.}
- {capability: reverse-etl, level: 3, why: Audiences and attributes are synced incrementally to marketing and advertising tools.}
- {capability: consent-management, level: 3, why: 'Customers must only receive marketing they have agreed to, in every channel.'}
- {capability: data-subject-requests, level: 2, why: Erasure requests must also remove the person from audiences already synced to external tools.}
- {capability: entity-resolution, level: 2, why: 'Email addresses, devices and accounts must be linked to the same customer to avoid duplicate or wrong messages.'}
- {capability: sql-transformation, level: 2, why: Segment logic is built on modelled customer and transaction tables.}
- {capability: data-quality-rules, level: 2, why: Bad data in an audience sends wrong offers to real customers.}
- {capability: deidentification, level: 2, why: Identifiers are hashed before they are sent to advertising platforms.}
- {capability: workflow-orchestration, level: 2, why: Audience refreshes run after the data they depend on has loaded.}
- {capability: pipeline-monitoring, level: 2, why: Failed or partial syncs must be caught before a campaign goes out.}
benefits_from:
- {capability: behavioural-event-collection, why: Enables behaviour-triggered audiences such as basket abandonment.}
- {capability: batch-inference, why: Adds propensity and churn scores to audiences.}
- {capability: data-clean-rooms, why: Matches audiences with media partners without exchanging raw customer lists.}
- {capability: master-data-management, why: One customer profile underpins every segment.}
- {capability: change-feeds, why: Sends only customers who entered or left a segment.}
- {capability: saas-connectors, why: Brings campaign responses back for measurement.}
- {capability: freshness-monitoring, why: Stops campaigns going out on stale audiences.}
- {capability: data-enrichment, why: Adds demographic or firmographic attributes for targeting.}
personas:
- persona-business-user
- persona-data-analyst
- persona-analytics-engineer
- persona-data-engineer
- persona-security-officer
patterns: [elt, medallion-architecture]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Marketing teams want to reach the right customers with the right message across email, advertising, social and service channels, using everything the organisation knows about them. Audience activation builds segments such as lapsed high-value customers or people who abandoned a basket from modelled customer data in the platform, then syncs them to marketing and advertising tools, refreshing them as customers move in and out of a segment. Identifiers sent to advertising platforms are usually hashed.

Good looks like marketers building and refreshing audiences without waiting for engineers, segments that use the same customer definitions as reporting, opt-outs and erasure honoured in every destination, and campaign results flowing back so audiences can be measured and improved.

# Non-functional requirements

- Scheduled audiences refresh daily or hourly, and triggered audiences within minutes.
- Opt-outs reach every destination within an agreed time, often 24 hours or less.
- Personal identifiers are hashed or tokenised before leaving the platform.
- Syncs respect destination API rate limits and report failures.

# Risks

- Customers who opted out are contacted, which brings complaints and regulatory fines.
- Identity mismatches send offers to the wrong people.
- Destination tools keep stale copies of audiences and personal data after their purpose ends.
- Each team defines the same segment differently.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [Audience building and activation](../capabilities/serving/audience-activation.md) | [Serving and activation](../capabilities/serving/serving.md) | 3 (Defined) | Marketers build audiences from platform data and deliver them to channels. |
| [Reverse ETL](../capabilities/serving/reverse-etl.md) | [Serving and activation](../capabilities/serving/serving.md) | 3 (Defined) | Audiences and attributes are synced incrementally to marketing and advertising tools. |
| [Consent and purpose management](../capabilities/governance/consent-management.md) | [Governance and compliance](../capabilities/governance/governance.md) | 3 (Defined) | Customers must only receive marketing they have agreed to, in every channel. |
| [Data subject requests](../capabilities/governance/data-subject-requests.md) | [Governance and compliance](../capabilities/governance/governance.md) | 2 (Managed) | Erasure requests must also remove the person from audiences already synced to external tools. |
| [Entity resolution](../capabilities/master-data/entity-resolution.md) | [Master and reference data](../capabilities/master-data/master-data.md) | 2 (Managed) | Email addresses, devices and accounts must be linked to the same customer to avoid duplicate or wrong messages. |
| [SQL transformation](../capabilities/processing/sql-transformation.md) | [Processing and transformation](../capabilities/processing/processing.md) | 2 (Managed) | Segment logic is built on modelled customer and transaction tables. |
| [Data quality rules](../capabilities/data-quality/data-quality-rules.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | 2 (Managed) | Bad data in an audience sends wrong offers to real customers. |
| [De-identification](../capabilities/governance/deidentification.md) | [Governance and compliance](../capabilities/governance/governance.md) | 2 (Managed) | Identifiers are hashed before they are sent to advertising platforms. |
| [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md) | [Orchestration](../capabilities/orchestration/orchestration.md) | 2 (Managed) | Audience refreshes run after the data they depend on has loaded. |
| [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | 2 (Managed) | Failed or partial syncs must be caught before a campaign goes out. |

# Capabilities that help

| Capability | Why |
|---|---|
| [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md) | Enables behaviour-triggered audiences such as basket abandonment. |
| [Batch inference](../capabilities/mlops/batch-inference.md) | Adds propensity and churn scores to audiences. |
| [Data clean rooms](../capabilities/data-sharing/data-clean-rooms.md) | Matches audiences with media partners without exchanging raw customer lists. |
| [Master data management](../capabilities/master-data/master-data-management.md) | One customer profile underpins every segment. |
| [Change feeds](../capabilities/serving/change-feeds.md) | Sends only customers who entered or left a segment. |
| [SaaS application connectors](../capabilities/ingestion-integration/saas-connectors.md) | Brings campaign responses back for measurement. |
| [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md) | Stops campaigns going out on stale audiences. |
| [Data enrichment](../capabilities/processing/data-enrichment.md) | Adds demographic or firmographic attributes for targeting. |

# Personas

- [Business user](../personas/persona-business-user.md): Uses data, reports and AI assistants to make decisions, without deep technical skills.
- [Data analyst](../personas/persona-data-analyst.md): Answers business questions through analysis, dashboards and reports.
- [Analytics engineer](../personas/persona-analytics-engineer.md): Turns raw data into tested, documented, analysis-ready models.
- [Data engineer](../personas/persona-data-engineer.md): Builds and operates the pipelines that ingest, transform and deliver data.
- [Security and privacy officer](../personas/persona-security-officer.md): Protects data and makes sure it is used lawfully.

# Patterns

- [ELT](../patterns/elt.md)
- [Medallion architecture](../patterns/medallion-architecture.md)

# Frameworks that apply

- [GDPR](../frameworks/framework-gdpr.md): Regulation (EU) 2016/679, the EU's general law on processing personal data, which sets principles, legal bases, individuals' rights and controller duties.

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 8 of 10 | [Audience building and activation](../capabilities/serving/audience-activation.md), [Consent and purpose management](../capabilities/governance/consent-management.md) |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 6 of 10 | [Audience building and activation](../capabilities/serving/audience-activation.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Entity resolution](../capabilities/master-data/entity-resolution.md) |
| [Google Cloud](../platforms/platform-google-cloud.md) | 7 of 10 | [Audience building and activation](../capabilities/serving/audience-activation.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Entity resolution](../capabilities/master-data/entity-resolution.md) |
| [Snowflake](../platforms/platform-snowflake.md) | 5 of 10 | [Audience building and activation](../capabilities/serving/audience-activation.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [Entity resolution](../capabilities/master-data/entity-resolution.md) |
| [Databricks](../platforms/platform-databricks.md) | 5 of 10 | [Audience building and activation](../capabilities/serving/audience-activation.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [Entity resolution](../capabilities/master-data/entity-resolution.md) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 2 of 10 | [Audience building and activation](../capabilities/serving/audience-activation.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [De-identification](../capabilities/governance/deidentification.md), [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md) |
| [Informatica](../platforms/platform-informatica.md) | 7 of 10 | [Audience building and activation](../capabilities/serving/audience-activation.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 2 of 10 | [Audience building and activation](../capabilities/serving/audience-activation.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [SQL transformation](../capabilities/processing/sql-transformation.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [De-identification](../capabilities/governance/deidentification.md) |
| [Oracle](../platforms/platform-oracle.md) | 2 of 10 | [Audience building and activation](../capabilities/serving/audience-activation.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [SQL transformation](../capabilities/processing/sql-transformation.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md) |
| [SAP](../platforms/platform-sap.md) | 4 of 10 | [Audience building and activation](../capabilities/serving/audience-activation.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [De-identification](../capabilities/governance/deidentification.md), [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md) |
| [Teradata](../platforms/platform-teradata.md) | 0 of 10 | [Audience building and activation](../capabilities/serving/audience-activation.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [SQL transformation](../capabilities/processing/sql-transformation.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [De-identification](../capabilities/governance/deidentification.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md) |
| [IBM](../platforms/platform-ibm.md) | 3 of 10 | [Audience building and activation](../capabilities/serving/audience-activation.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [SQL transformation](../capabilities/processing/sql-transformation.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md) |
| [Palantir](../platforms/platform-palantir.md) | 4 of 10 | [Audience building and activation](../capabilities/serving/audience-activation.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md) |
| [SAS](../platforms/platform-sas.md) | 2 of 10 | [Audience building and activation](../capabilities/serving/audience-activation.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [De-identification](../capabilities/governance/deidentification.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md) |
| [Dataiku](../platforms/platform-dataiku.md) | 3 of 10 | [Audience building and activation](../capabilities/serving/audience-activation.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [De-identification](../capabilities/governance/deidentification.md), [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 5 of 10 | [Audience building and activation](../capabilities/serving/audience-activation.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [Entity resolution](../capabilities/master-data/entity-resolution.md) |
| [Independent vendors](../platforms/platform-independent.md) | 10 of 10 |  |
