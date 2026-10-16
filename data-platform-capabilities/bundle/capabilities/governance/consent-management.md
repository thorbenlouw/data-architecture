---
type: Capability
id: consent-management
title: Consent and purpose management
description: Record what each person agreed to and restrict use of their data to permitted purposes.
broader: [privacy-management]
related: [audience-activation, reverse-etl, attribute-based-access, change-data-capture, data-usage-rights]
depends_on: [entity-resolution]
tags: [governance]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

For each person, the platform keeps a record of what they agreed to or objected to, such as marketing email, personalised advertising, research use or sharing with partners, with the time, source and version of the wording they saw. Pipelines and queries check that record before data is used for a purpose. For example, an email campaign audience excludes everyone who withdrew marketing consent yesterday, and a training job drops records of people who objected to profiling.

Consent is only one legal basis for processing under laws such as the GDPR, so the wider need is purpose management: tagging datasets and jobs with the purposes they serve and allowing use only where a basis exists for that purpose. Preferences change constantly and must take effect quickly, including in downstream copies and activation tools. Implementations range from a consent table joined into pipelines, to purpose tags enforced by access policies, to dedicated consent platforms that send changes to the data platform as events or through change data capture.

# Key considerations

- Store consent as a history of events, not a single current flag, so you can show what was permitted at the time data was used.
- Withdrawals must reach downstream copies quickly, including feature stores, audience tools and partner shares.
- Enforce purpose at access time where possible, for example through policies on purpose tags, rather than relying on every pipeline to filter correctly.
- Agree with the privacy team a default, by purpose and jurisdiction, for people with no recorded preference.

# Questions to ask

- Where is consent captured today, and how quickly do changes reach the data platform?
- Which uses of personal data rely on consent and which on another legal basis?
- Do datasets and jobs record the purposes they serve?
- Could you show, for a past campaign or model, that everyone included had a valid basis?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Governance and compliance](governance.md) |
| Broader | [Privacy management](privacy-management.md) |
| Related | [Attribute- and tag-based access control](../security/attribute-based-access.md), [Audience building and activation](../serving/audience-activation.md), [Behavioural event collection](../ingestion-integration/behavioural-event-collection.md), [Change data capture](../ingestion-integration/change-data-capture.md), [Data clean rooms](../data-sharing/data-clean-rooms.md), [Data licensing and usage rights](data-usage-rights.md), [Reverse ETL](../serving/reverse-etl.md) |
| Depends on | [Entity resolution](../master-data/entity-resolution.md) |
| Needed by | [Audience building and activation](../serving/audience-activation.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (requires, level 2) · [Customer 360](../../use-cases/usecase-customer-360.md) (requires, level 3) · [Data sharing and monetisation](../../use-cases/usecase-data-monetisation.md) (requires, level 3) · [Marketing audience activation](../../use-cases/usecase-marketing-activation.md) (requires, level 3) · [Personalised recommendations](../../use-cases/usecase-recommendations.md) (requires, level 2) · [Privacy rights handling](../../use-cases/usecase-privacy-rights.md) (benefits from)
- **Personas:** [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Privacy](../../maturity/track-privacy.md) (from level 3, Defined)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 8 Data Consumption Purpose (Accessibility and usage) · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Handling Ethics · [GDPR](../../frameworks/framework-gdpr.md): Article 5(1)(a) – Lawfulness, fairness and transparency; Article 5(1)(b) – Purpose limitation; Articles 6 and 7 – Lawfulness of processing and conditions for consent; Article 21 – Right to object

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Independent vendors](../../platforms/platform-independent.md) |  | [OneTrust Data Use Governance](../../technologies/independent/onetrust-data-use-governance.md), [OneTrust Privacy Automation](../../technologies/independent/onetrust-privacy-automation.md), [Securiti DataAI Command Platform](../../technologies/independent/securiti-dataai-command-platform.md) |
