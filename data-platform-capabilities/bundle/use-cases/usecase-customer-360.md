---
type: Use Case
id: usecase-customer-360
title: Customer 360
description: Give every channel a single, trusted view of each customer.
aliases: [single customer view, golden customer record]
requires:
- {capability: entity-resolution, level: 3, why: 'Records with different identifiers, spellings and addresses must be matched to the same customer.'}
- {capability: master-data-management, level: 3, why: 'The merged golden record needs a managed lifecycle, with merge and unmerge and history.'}
- {capability: survivorship, level: 3, why: 'Rules decide which source wins for each attribute, such as address from billing and email from the app.'}
- {capability: data-cleansing, level: 3, why: 'Names, addresses and phone numbers must be standardised before they can be matched reliably.'}
- {capability: batch-ingestion, level: 3, why: 'Customer data arrives from CRM, billing, e-commerce and service systems.'}
- {capability: change-data-capture, level: 2, why: Profile changes in source systems must reach the 360 view without waiting for a nightly reload.}
- {capability: data-quality-rules, level: 2, why: Invalid or incomplete records must not degrade matches or the profile.}
- {capability: consent-management, level: 3, why: Every channel using the profile must respect what the customer agreed to.}
- {capability: data-classification, level: 3, why: 'A combined profile concentrates personal data, so its fields must be labelled for protection.'}
- {capability: column-masking, level: 3, why: 'Staff in different roles see different parts of the profile, such as partial card or health details.'}
- {capability: low-latency-serving, level: 3, why: Contact centre and web channels look up a profile in milliseconds during a live interaction.}
- {capability: reverse-etl, level: 2, why: The profile must be pushed into CRM and service tools where staff work.}
- {capability: data-ownership, level: 2, why: Someone must own match rules and settle disputed merges between business units.}
benefits_from:
- {capability: data-subject-requests, why: The profile becomes the index for finding a person's data when they exercise their rights.}
- {capability: behavioural-event-collection, why: Adds digital behaviour to the profile and links anonymous and known visits.}
- {capability: hierarchy-management, why: Models households or corporate account structures in business-to-business settings.}
- {capability: data-enrichment, why: Third-party reference data fills gaps and validates addresses and companies.}
- {capability: graph-data, why: 'Shows relationships between people, accounts and households.'}
- {capability: change-feeds, why: Lets channels react to profile changes as they happen.}
- {capability: data-apis, why: 'Gives applications a documented, governed way to read profiles.'}
- {capability: data-quality-scorecards, why: Tracks match and completeness quality over time.}
- {capability: operational-data-store, why: 'Combines the profile with current orders, cases and payments for contact-centre lookups.'}
personas:
- persona-data-architect
- persona-data-steward
- persona-data-engineer
- persona-data-product-owner
- persona-software-engineer
- persona-business-user
- persona-security-officer
patterns: [cqrs-read-models, data-vault, slowly-changing-dimensions, medallion-architecture]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Customers deal with an organisation through stores, websites, apps, contact centres and account managers, and each channel usually holds its own partial record. A customer 360 gathers these records, works out which belong to the same person or business, merges them into one trusted profile with history, consent and key attributes, and serves that profile back to every channel and to analytics and models.

Good looks like a contact centre agent, a marketing campaign and a churn model all seeing the same customer, with duplicates and wrong merges kept below agreed rates, consent applied wherever the profile is used, and profile changes reaching the channels within the agreed time. The hard part is rarely storage. It is matching, survivorship rules and getting each channel to use the result.

# Non-functional requirements

- Profile lookups return in around 100 milliseconds at contact-centre and web concurrency.
- Changes reach channels within the agreed window, from minutes for consent to a day for other attributes.
- Match precision and recall are measured against reviewed samples and have agreed targets.
- Merges and unmerges are recorded with the rule or person responsible.

# Risks

- Over-merging combines different people, which is both a privacy breach and a customer-service failure.
- The programme becomes a multi-year master data project before any channel uses the profile.
- Consent changes made in one channel do not reach the others.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [Entity resolution](../capabilities/master-data/entity-resolution.md) | [Master and reference data](../capabilities/master-data/master-data.md) | 3 (Defined) | Records with different identifiers, spellings and addresses must be matched to the same customer. |
| [Master data management](../capabilities/master-data/master-data-management.md) | [Master and reference data](../capabilities/master-data/master-data.md) | 3 (Defined) | The merged golden record needs a managed lifecycle, with merge and unmerge and history. |
| [Merge and survivorship](../capabilities/master-data/survivorship.md) | [Master and reference data](../capabilities/master-data/master-data.md) | 3 (Defined) | Rules decide which source wins for each attribute, such as address from billing and email from the app. |
| [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | 3 (Defined) | Names, addresses and phone numbers must be standardised before they can be matched reliably. |
| [Batch ingestion](../capabilities/ingestion-integration/batch-ingestion.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 3 (Defined) | Customer data arrives from CRM, billing, e-commerce and service systems. |
| [Change data capture](../capabilities/ingestion-integration/change-data-capture.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 2 (Managed) | Profile changes in source systems must reach the 360 view without waiting for a nightly reload. |
| [Data quality rules](../capabilities/data-quality/data-quality-rules.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | 2 (Managed) | Invalid or incomplete records must not degrade matches or the profile. |
| [Consent and purpose management](../capabilities/governance/consent-management.md) | [Governance and compliance](../capabilities/governance/governance.md) | 3 (Defined) | Every channel using the profile must respect what the customer agreed to. |
| [Data classification](../capabilities/governance/data-classification.md) | [Governance and compliance](../capabilities/governance/governance.md) | 3 (Defined) | A combined profile concentrates personal data, so its fields must be labelled for protection. |
| [Column security and dynamic masking](../capabilities/security/column-masking.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Staff in different roles see different parts of the profile, such as partial card or health details. |
| [Low-latency serving](../capabilities/serving/low-latency-serving.md) | [Serving and activation](../capabilities/serving/serving.md) | 3 (Defined) | Contact centre and web channels look up a profile in milliseconds during a live interaction. |
| [Reverse ETL](../capabilities/serving/reverse-etl.md) | [Serving and activation](../capabilities/serving/serving.md) | 2 (Managed) | The profile must be pushed into CRM and service tools where staff work. |
| [Ownership and stewardship](../capabilities/governance/data-ownership.md) | [Governance and compliance](../capabilities/governance/governance.md) | 2 (Managed) | Someone must own match rules and settle disputed merges between business units. |

# Capabilities that help

| Capability | Why |
|---|---|
| [Data subject requests](../capabilities/governance/data-subject-requests.md) | The profile becomes the index for finding a person's data when they exercise their rights. |
| [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md) | Adds digital behaviour to the profile and links anonymous and known visits. |
| [Hierarchy management](../capabilities/master-data/hierarchy-management.md) | Models households or corporate account structures in business-to-business settings. |
| [Data enrichment](../capabilities/processing/data-enrichment.md) | Third-party reference data fills gaps and validates addresses and companies. |
| [Graph data](../capabilities/specialised-data/graph-data.md) | Shows relationships between people, accounts and households. |
| [Change feeds](../capabilities/serving/change-feeds.md) | Lets channels react to profile changes as they happen. |
| [Data APIs](../capabilities/serving/data-apis.md) | Gives applications a documented, governed way to read profiles. |
| [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md) | Tracks match and completeness quality over time. |
| [Operational data store](../capabilities/serving/operational-data-store.md) | Combines the profile with current orders, cases and payments for contact-centre lookups. |

# Personas

- [Data architect](../personas/persona-data-architect.md): Designs the data platform and how data flows, is modelled and is governed across the organisation.
- [Data steward](../personas/persona-data-steward.md): Looks after the definition, quality and proper use of data in a business domain.
- [Data engineer](../personas/persona-data-engineer.md): Builds and operates the pipelines that ingest, transform and deliver data.
- [Data product owner](../personas/persona-data-product-owner.md): Owns the value, roadmap and consumers of one or more data products.
- [Software engineer](../personas/persona-software-engineer.md): Builds applications that produce data for the platform or consume data from it.
- [Business user](../personas/persona-business-user.md): Uses data, reports and AI assistants to make decisions, without deep technical skills.
- [Security and privacy officer](../personas/persona-security-officer.md): Protects data and makes sure it is used lawfully.

# Patterns

- [Separate read models](../patterns/cqrs-read-models.md)
- [Data Vault](../patterns/data-vault.md)
- [Slowly changing dimensions](../patterns/slowly-changing-dimensions.md)
- [Medallion architecture](../patterns/medallion-architecture.md)

# Frameworks that apply

- [DAMA-DMBOK 2](../frameworks/framework-dama-dmbok.md): The Data Management Body of Knowledge, a reference guide that splits data management into knowledge areas around a central governance function.
- [GDPR](../frameworks/framework-gdpr.md): Regulation (EU) 2016/679, the EU's general law on processing personal data, which sets principles, legal bases, individuals' rights and controller duties.
- [ISO 8000 (data quality)](../frameworks/framework-iso-8000.md): A series of international standards on data quality, covering concepts, quality management processes, profiling, rules, master data exchange and sensor data.

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 10 of 13 | [Merge and survivorship](../capabilities/master-data/survivorship.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md) |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 7 of 13 | [Entity resolution](../capabilities/master-data/entity-resolution.md), [Master data management](../capabilities/master-data/master-data-management.md), [Merge and survivorship](../capabilities/master-data/survivorship.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Reverse ETL](../capabilities/serving/reverse-etl.md) |
| [Google Cloud](../platforms/platform-google-cloud.md) | 8 of 13 (+1 in preview) | [Entity resolution](../capabilities/master-data/entity-resolution.md), [Master data management](../capabilities/master-data/master-data-management.md), [Merge and survivorship](../capabilities/master-data/survivorship.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md) (preview only) |
| [Snowflake](../platforms/platform-snowflake.md) | 6 of 13 | [Entity resolution](../capabilities/master-data/entity-resolution.md), [Master data management](../capabilities/master-data/master-data-management.md), [Merge and survivorship](../capabilities/master-data/survivorship.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md) |
| [Databricks](../platforms/platform-databricks.md) | 6 of 13 | [Entity resolution](../capabilities/master-data/entity-resolution.md), [Master data management](../capabilities/master-data/master-data-management.md), [Merge and survivorship](../capabilities/master-data/survivorship.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 4 of 13 | [Entity resolution](../capabilities/master-data/entity-resolution.md), [Master data management](../capabilities/master-data/master-data-management.md), [Merge and survivorship](../capabilities/master-data/survivorship.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data classification](../capabilities/governance/data-classification.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md) |
| [Informatica](../platforms/platform-informatica.md) | 10 of 13 | [Consent and purpose management](../capabilities/governance/consent-management.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [Low-latency serving](../capabilities/serving/low-latency-serving.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 4 of 13 | [Entity resolution](../capabilities/master-data/entity-resolution.md), [Master data management](../capabilities/master-data/master-data-management.md), [Merge and survivorship](../capabilities/master-data/survivorship.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Change data capture](../capabilities/ingestion-integration/change-data-capture.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md) |
| [Oracle](../platforms/platform-oracle.md) | 4 of 13 | [Entity resolution](../capabilities/master-data/entity-resolution.md), [Master data management](../capabilities/master-data/master-data-management.md), [Merge and survivorship](../capabilities/master-data/survivorship.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Low-latency serving](../capabilities/serving/low-latency-serving.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md) |
| [SAP](../platforms/platform-sap.md) | 7 of 13 | [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data classification](../capabilities/governance/data-classification.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [Low-latency serving](../capabilities/serving/low-latency-serving.md), [Reverse ETL](../capabilities/serving/reverse-etl.md) |
| [Teradata](../platforms/platform-teradata.md) | 0 of 13 | [Entity resolution](../capabilities/master-data/entity-resolution.md), [Master data management](../capabilities/master-data/master-data-management.md), [Merge and survivorship](../capabilities/master-data/survivorship.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Batch ingestion](../capabilities/ingestion-integration/batch-ingestion.md), [Change data capture](../capabilities/ingestion-integration/change-data-capture.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data classification](../capabilities/governance/data-classification.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [Low-latency serving](../capabilities/serving/low-latency-serving.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md) |
| [IBM](../platforms/platform-ibm.md) | 6 of 13 | [Entity resolution](../capabilities/master-data/entity-resolution.md), [Master data management](../capabilities/master-data/master-data-management.md), [Merge and survivorship](../capabilities/master-data/survivorship.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md) |
| [Palantir](../platforms/platform-palantir.md) | 6 of 13 | [Entity resolution](../capabilities/master-data/entity-resolution.md), [Master data management](../capabilities/master-data/master-data-management.md), [Merge and survivorship](../capabilities/master-data/survivorship.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 7 of 13 | [Entity resolution](../capabilities/master-data/entity-resolution.md), [Master data management](../capabilities/master-data/master-data-management.md), [Merge and survivorship](../capabilities/master-data/survivorship.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Reverse ETL](../capabilities/serving/reverse-etl.md) |
| [Independent vendors](../platforms/platform-independent.md) | 13 of 13 |  |
