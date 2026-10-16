---
type: Capability
id: privacy-management
title: Privacy management
description: Meet privacy obligations such as purpose limitation, consent and individuals' rights over their data.
broader: [governance]
related: [data-classification, data-lineage, data-retention, master-data-management, access-control]
depends_on: [data-classification, data-lineage]
tags: [governance]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Privacy management turns the obligations attached to personal data into platform behaviour. Privacy laws such as the EU and UK GDPR generally expect a lawful basis for each use, use limited to stated purposes, no more data than needed, deletion once data is no longer needed, and responses when individuals exercise rights over their data. On the platform this means knowing where personal data is, recording which purposes each dataset serves, and being able to restrict, export or erase one person's records on request.

The capabilities in this area work together. Records of processing and impact assessments document what is done and why. Consent and purpose management restrict use to what is permitted. Data subject requests act on individuals' rights. De-identification and privacy-enhancing technologies reduce risk so data can be used more widely. All of them rely on classification and lineage to find personal data. Privacy differs from security: security stops unauthorised access, while privacy also limits what authorised users may do with the data.

# Key considerations

- Design for erasure and restriction from the start. Immutable storage, backups, logs and model training sets make deletion hard to add later.
- Link purposes to datasets and pipelines in metadata, so a use outside the recorded purpose can be detected.
- Keep a stable internal identifier for each person across systems, or finding and deleting their data becomes a manual search.
- Requirements differ by jurisdiction. Model the common obligations once and configure the local differences.
- Design controls with the data protection officer or privacy team, so platform behaviour matches how the organisation interprets the law.

# Questions to ask

- Which privacy laws apply, given where customers, employees and processing are located?
- Can you list every system and table that holds a given person's data?
- How are data subject requests handled today, and how long do they take?
- Are purposes recorded per dataset, and does anything stop data being used for a different purpose?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Governance and compliance](governance.md) |
| Broader | [Governance and compliance](governance.md) |
| Narrower | [Consent and purpose management](consent-management.md), [Data breach response](../security/data-breach-response.md), [Data subject requests](data-subject-requests.md), [De-identification](deidentification.md), [Privacy impact assessment](privacy-impact-assessment.md), [Privacy-enhancing technologies](privacy-enhancing-technologies.md), [Records of processing](records-of-processing.md) |
| Related | [Access control](../security/access-control.md), [Data classification](data-classification.md), [Data lineage](../metadata/data-lineage.md), [Master data management](../master-data/master-data-management.md), [Retention and disposal](data-retention.md) |
| Depends on | [Data classification](data-classification.md), [Data lineage](../metadata/data-lineage.md) |

# Where it appears

- **Personas:** [Chief data officer](../../personas/persona-cdo.md) · [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Privacy](../../maturity/track-privacy.md)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Handling Ethics · [GDPR](../../frameworks/framework-gdpr.md): Article 5(1)(a) – Lawfulness, fairness and transparency

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Priva](../../technologies/microsoft/purview-priva.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Foundry security controls](../../technologies/palantir/palantir-security-controls.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [OneTrust Privacy Automation](../../technologies/independent/onetrust-privacy-automation.md) |

Narrower capabilities are realised by a further 40 technologies; see their pages.
