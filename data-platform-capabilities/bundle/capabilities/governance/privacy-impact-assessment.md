---
type: Capability
id: privacy-impact-assessment
title: Privacy impact assessment
description: Trigger, carry out and record data protection impact assessments for high-risk processing, linked to the data and pipelines concerned.
aliases: [DPIA, PIA]
broader: [privacy-management]
related:
- ai-impact-assessment
- records-of-processing
- data-classification
- data-lineage
- data-product-lifecycle
depends_on: [data-classification, data-lineage]
tags: [governance]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A data protection impact assessment (DPIA) examines planned processing that is likely to pose a high risk to people, such as large-scale profiling, systematic monitoring or processing of health data. It describes the processing, tests whether it is necessary and proportionate, identifies risks to individuals and records the measures that reduce them. Article 35 of the GDPR requires one in such cases. Platform support means prompting an assessment when a new pipeline, data product or model touches sensitive classifications, and linking the finished assessment to the assets it covers.

The value lies in catching problems before data starts flowing, while design changes are cheap. Assessments go stale as processing changes. Links to lineage and metadata let the platform notice when a covered pipeline starts reading new sensitive columns or feeding a new recipient, and ask for a review. A DPIA differs from an AI impact assessment, which covers an AI system's wider effects on people and society; the two are often combined for AI systems that use personal data.

# Key considerations

- Define triggers in metadata terms, such as special-category classifications, new external recipients or automated decisions about people, so screening does not depend on memory.
- Keep the screening step short and do a full assessment only where screening finds high risk, or teams will avoid the process.
- Link each mitigation to an actual control, such as a masking policy or retention rule, so you can show it was put in place.
- Set review triggers for material changes, not only a calendar date.

# Questions to ask

- How do teams know today that a new use of data needs an impact assessment?
- Where are completed assessments stored, and are they linked to the systems they cover?
- Who signs off high-risk processing, and how long does that take?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Governance and compliance](governance.md) |
| Broader | [Privacy management](privacy-management.md) |
| Related | [AI impact assessment](ai-impact-assessment.md), [Bias and fairness assessment](../machine-learning/fairness-assessment.md), [Data classification](data-classification.md), [Data lineage](../metadata/data-lineage.md), [Data product lifecycle management](../data-products/data-product-lifecycle.md), [Records of processing](records-of-processing.md) |
| Depends on | [Data classification](data-classification.md), [Data lineage](../metadata/data-lineage.md) |

# Where it appears

- **Personas:** [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Privacy](../../maturity/track-privacy.md) (from level 2, Managed)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 10 Data Privacy Impact Assessments (Protection and privacy) · [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 27 – Fundamental rights impact assessment · [GDPR](../../frameworks/framework-gdpr.md): Article 35 – Data protection impact assessment · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Annex A.5 – Assessing impacts of AI systems

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Priva](../../technologies/microsoft/purview-priva.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Collibra Data Governance](../../technologies/independent/collibra-data-governance.md), [OneTrust Privacy Automation](../../technologies/independent/onetrust-privacy-automation.md), [Securiti DataAI Command Platform](../../technologies/independent/securiti-dataai-command-platform.md) |
