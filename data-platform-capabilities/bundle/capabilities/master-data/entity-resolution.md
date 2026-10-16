---
type: Capability
id: entity-resolution
title: Entity resolution
description: Find and link records that refer to the same real-world entity, even when they do not match exactly.
aliases: [matching, record linkage, record matching]
broader: [master-data-management]
related: [graph-data, data-labelling, privacy-enhancing-technologies, data-clean-rooms, data-enrichment]
depends_on: [data-cleansing]
tags: [master-data]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Entity resolution decides which records refer to the same real-world entity when no shared key exists. Records are first standardised (names, addresses, phone numbers), then grouped by inexpensive blocking keys, such as postcode plus surname initial, so that not every record is compared with every other. Candidate pairs are scored by comparing fields with fuzzy measures such as edit distance and phonetic codes, using deterministic rules, probabilistic models or machine learning trained on labelled pairs. Matching pairs are linked into clusters, one per entity.

It is needed for single customer views, fraud and anti-money-laundering investigation, removing duplicates, joining third-party data and, with privacy-preserving techniques, linking records across organisations. Scores are usually split into automatic matches, automatic non-matches and an uncertain middle band for people to review. Thresholds trade false merges, which mix two people's data, against missed matches, which leave duplicates. Entity resolution produces links; master data management decides what to do with them over time.

# Key considerations

- False merges are usually worse than missed matches, especially for people. Set thresholds for each use case.
- Blocking keys determine both speed and how many true matches are found. A key that is often empty causes silent misses.
- Keep match decisions and scores so links can be explained, reviewed and undone.
- Resolve again as data changes. A new record can join two existing clusters or split one.
- Matching works on personal data. Limit who can see candidate pairs and why.

# Questions to ask

- Is there any identifier shared across sources, and how reliable is it?
- What does a wrong merge cost compared with a missed match?
- How many records are involved, and must matching run in batch, at the moment of entry, or both?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Master and reference data](master-data.md) |
| Broader | [Master data management](master-data-management.md) |
| Related | [Behavioural event collection](../ingestion-integration/behavioural-event-collection.md), [Data breach response](../security/data-breach-response.md), [Data clean rooms](../data-sharing/data-clean-rooms.md), [Data cleansing and standardisation](../data-quality/data-cleansing.md), [Data enrichment](../processing/data-enrichment.md), [Data labelling](../machine-learning/data-labelling.md), [Data subject requests](../governance/data-subject-requests.md), [Deduplication and idempotent loading](../ingestion-integration/idempotent-loading.md), [Graph data](../specialised-data/graph-data.md), [Operational data store](../serving/operational-data-store.md), [Privacy-enhancing technologies](../governance/privacy-enhancing-technologies.md) |
| Depends on | [Data cleansing and standardisation](../data-quality/data-cleansing.md) |
| Needed by | [Audience building and activation](../serving/audience-activation.md), [Consent and purpose management](../governance/consent-management.md), [Knowledge graphs](../specialised-data/knowledge-graphs.md), [Merge and survivorship](survivorship.md) |

# Where it appears

- **Use cases:** [Credit decisioning](../../use-cases/usecase-credit-decisioning.md) (benefits from) · [Customer 360](../../use-cases/usecase-customer-360.md) (requires, level 3) · [Document data extraction](../../use-cases/usecase-document-extraction.md) (benefits from) · [Marketing audience activation](../../use-cases/usecase-marketing-activation.md) (requires, level 2) · [Privacy rights handling](../../use-cases/usecase-privacy-rights.md) (requires, level 2) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (benefits from)
- **Personas:** [Data steward](../../personas/persona-data-steward.md)
- **Maturity tracks:** [Master and reference data](../../maturity/track-master-data.md) (from level 2, Managed)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 2 – Data architecture and IT infrastructure · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Reference and Master Data · [ISO 8000 (data quality)](../../frameworks/framework-iso-8000.md): ISO 8000-115 to 8000-119 – Quality identifiers

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Entity Resolution](../../technologies/aws/aws-entity-resolution.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Cloud Data Quality (CDQ)](../../technologies/informatica/informatica-cloud-data-quality.md), [Informatica Customer 360 SaaS](../../technologies/informatica/informatica-customer-360.md), [Informatica Multidomain MDM SaaS](../../technologies/informatica/informatica-multidomain-mdm-saas.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Master Data Governance](../../technologies/sap/sap-master-data-governance.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Ataccama ONE Master Data Management](../../technologies/independent/ataccama-one-mdm.md), [Experian Aperture Data Studio](../../technologies/independent/experian-aperture-data-studio.md), [Hightouch](../../technologies/independent/hightouch.md), [mParticle](../../technologies/independent/mparticle.md), [Profisee MDM](../../technologies/independent/profisee-mdm.md), [Reltio Multidomain MDM](../../technologies/independent/reltio-multidomain-mdm.md), [Semarchy Data Platform](../../technologies/independent/semarchy-data-platform.md), [Stibo Systems STEP](../../technologies/independent/stibo-systems-step.md), [Tamr](../../technologies/independent/tamr.md), [Twilio Segment](../../technologies/independent/twilio-segment.md) |
