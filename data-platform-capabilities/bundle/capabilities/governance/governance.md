---
type: Capability
id: governance
title: Governance and compliance
description: Set and enforce the rules, roles and controls for how data is managed and used.
aliases: [data governance]
broader: []
related: [data-catalogue, data-lineage, data-quality, access-control, data-products]
depends_on: [data-catalogue]
order: 14
tags: [governance]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Governance decides who answers for data, which rules apply to it and how the organisation shows those rules are followed. On a data platform it appears as specific mechanisms: owners and stewards recorded against datasets, sensitivity labels on tables and columns, policies that turn those labels into access and retention behaviour, and logs and reports that prove what happened. Without these mechanisms governance stays a set of documents the platform ignores.

The domain has three layers. Foundations say what the data is and who is accountable: ownership and stewardship, data domains, classification and critical data elements. Policy capabilities say what may be done with it: policy management, retention and disposal, residency, usage rights and the privacy controls for personal data. Assurance capabilities show the rules work: compliance evidence and governance coverage metrics. AI governance and model governance apply the same structure to models and agents, adding impact assessment, incident handling and an inventory of AI systems.

Governance relies on other domains for enforcement. The catalogue and lineage supply the inventory and the paths data takes; security turns policies into grants, masks and filters; data quality measures fitness for use. A practical test of maturity is whether a label or policy, once set, changes what the platform does without further manual work, and whether you can show an auditor that it did.

# Key considerations

- Start with the data and decisions that carry real risk, such as personal data, regulatory reporting and external sharing, rather than governing every table equally.
- Write policies against classifications and domains, not individual tables, so new data is covered as soon as it is labelled.
- Decide which controls the platform enforces and which rely on people following a process. Process-only controls need regular sampling to show they still work.
- Keep governance metadata in the catalogue behind an open API, so security, quality and AI tooling can read it, rather than in spreadsheets.
- Governance that adds weeks to getting access or publishing data gets bypassed. Measure lead times as well as coverage.

# Questions to ask

- Which regulations, audits or internal policies must the platform satisfy, and who signs off compliance today?
- Is accountability for data assigned by business domain, by system or not at all?
- Which governance rules does the platform enforce automatically, and which depend on people following a process?
- How would you show an auditor who could see a given dataset last quarter, and why?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Narrower | [AI governance](ai-governance.md), [Compliance controls and evidence](compliance-evidence.md), [Critical data elements](critical-data-elements.md), [Data classification](data-classification.md), [Data domains](data-domains.md), [Data licensing and usage rights](data-usage-rights.md), [Data residency and sovereignty](data-residency.md), [Governance coverage metrics](governance-metrics.md), [Model governance](../mlops/model-governance.md), [Ownership and stewardship](data-ownership.md), [Policy management](data-policy-management.md), [Privacy management](privacy-management.md), [Regulatory submission](../serving/regulatory-submission.md), [Retention and disposal](data-retention.md), [Stewardship workflows](stewardship-workflows.md) |
| Related | [Metadata and discovery](../metadata/metadata.md), [Data quality and observability](../data-quality/data-quality.md), [Security and access](../security/security.md), [Data products](../data-products/data-products.md), [Platform operations](../platform-operations/platform-operations.md), [Access control](../security/access-control.md), [Data catalogue](../metadata/data-catalogue.md), [Data lineage](../metadata/data-lineage.md) |
| Depends on | [Data catalogue](../metadata/data-catalogue.md) |

# How platforms provide it

No technology in this bundle realises this capability directly yet.

Narrower capabilities are realised by a further 151 technologies; see their pages.
