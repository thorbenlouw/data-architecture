---
type: Capability
id: records-of-processing
title: Records of processing
description: Keep a register of personal data processing with purposes, categories, recipients and retention, linked to the data involved.
aliases: [RoPA, GDPR Article 30]
broader: [privacy-management]
related: [data-catalogue, data-lineage, data-retention, data-classification, compliance-evidence]
depends_on: [data-catalogue, data-classification]
tags: [governance]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A record of processing describes one processing activity, such as payroll or marketing analytics, with its purposes, legal basis, categories of people and data, recipients, transfers to other countries, retention periods and security measures. Article 30 of the GDPR requires controllers and processors to keep such records, with limited exemptions, and similar duties exist elsewhere. On a data platform the useful step is linking each activity to the datasets, pipelines and data products that carry it out, so the register reflects what the systems actually do.

Registers kept in spreadsheets drift from reality as pipelines change. Linking them to the catalogue and lineage lets you check that every table holding personal data belongs to at least one recorded activity, spot new uses with no record, and answer regulators and individuals quickly. The register also feeds other controls: retention periods drive deletion jobs, and recorded purposes feed purpose-based access policies. The catalogue describes data assets; the register describes the activities that use them.

# Key considerations

- Agree the level of detail. Too coarse and activities say nothing useful; too fine and nobody maintains them.
- Use the same vocabulary for purposes and data categories in the register, the catalogue and access policies, so they can be checked against each other.
- Generate draft entries from lineage and classification and have privacy staff confirm them, rather than relying on interviews alone.
- Record processors and recipients, including SaaS tools fed by reverse ETL and partners receiving shared data.

# Questions to ask

- Does a register exist, and when was it last checked against the actual systems?
- Can you show which recorded activity each personal-data table supports?
- Who maintains the register, and how do they learn about new pipelines or uses?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Governance and compliance](governance.md) |
| Broader | [Privacy management](privacy-management.md) |
| Related | [Compliance controls and evidence](compliance-evidence.md), [Data catalogue](../metadata/data-catalogue.md), [Data classification](data-classification.md), [Data lineage](../metadata/data-lineage.md), [Privacy impact assessment](privacy-impact-assessment.md), [Retention and disposal](data-retention.md) |
| Depends on | [Data catalogue](../metadata/data-catalogue.md), [Data classification](data-classification.md) |

# Where it appears

- **Use cases:** [Privacy rights handling](../../use-cases/usecase-privacy-rights.md) (requires, level 2)
- **Personas:** [Risk and compliance officer](../../personas/persona-risk-compliance.md) · [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Privacy](../../maturity/track-privacy.md) (from level 2, Managed)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 8 Data Consumption Purpose (Accessibility and usage) · [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 4a – Special categories of personal data for bias detection · [GDPR](../../frameworks/framework-gdpr.md): Article 5(1)(a) – Lawfulness, fairness and transparency; Article 5(1)(b) – Purpose limitation; Article 5(2) – Accountability; Articles 6 and 7 – Lawfulness of processing and conditions for consent; Article 15 – Right of access; Article 19 – Notification to recipients; Article 30 – Records of processing activities; Article 35 – Data protection impact assessment; Articles 44 to 49 – Transfers to third countries

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Independent vendors](../../platforms/platform-independent.md) |  | [Collibra Data Governance](../../technologies/independent/collibra-data-governance.md), [OneTrust Privacy Automation](../../technologies/independent/onetrust-privacy-automation.md), [Securiti DataAI Command Platform](../../technologies/independent/securiti-dataai-command-platform.md) |
