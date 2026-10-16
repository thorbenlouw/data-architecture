---
type: Capability
id: survivorship
title: Merge and survivorship
description: Combine matched records into a golden record using rules about which source wins for each attribute.
broader: [master-data-management]
related: [data-quality-rules, data-ownership, column-lineage, data-cleansing]
depends_on: [entity-resolution]
tags: [master-data]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Once records are matched, survivorship builds the golden record by choosing, attribute by attribute, which value to keep. Rules may prefer a trusted source (the HR system wins for job title), the most recent update, the most complete value, the most common value, or a value that passes validation. A customer's legal name might come from the identity-checked onboarding system, their email address from the most recently updated marketing record, and their phone number from whichever source verified it.

Without explicit rules, merged records take arbitrary values that change each time data loads. Good survivorship records where each surviving value came from and which alternatives were rejected, lets stewards override values without the next load overwriting them, and allows recomputation when rules change. Some attributes are combined rather than chosen, such as keeping every known address. Matching decides which records belong together; survivorship decides what the combined record says.

# Key considerations

- Agree rules for each attribute with business owners, and record why each source is trusted.
- Protect steward overrides from being overwritten by later automated loads.
- Keep all contributing values and their sources, not only the winner, for audit and recomputation.
- Recency rules need reliable update timestamps in every source. Check that they exist and mean the same thing.

# Questions to ask

- Which system is most trusted for each important attribute, and do the business owners agree?
- Do consumers need to see where each value came from?
- How should manual corrections interact with automated merges?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Master and reference data](master-data.md) |
| Broader | [Master data management](master-data-management.md) |
| Related | [Column-level lineage](../metadata/column-lineage.md), [Data cleansing and standardisation](../data-quality/data-cleansing.md), [Data quality rules](../data-quality/data-quality-rules.md), [Ownership and stewardship](../governance/data-ownership.md) |
| Depends on | [Entity resolution](entity-resolution.md) |

# Where it appears

- **Use cases:** [Customer 360](../../use-cases/usecase-customer-360.md) (requires, level 3)
- **Personas:** [Data steward](../../personas/persona-data-steward.md)
- **Maturity tracks:** [Master and reference data](../../maturity/track-master-data.md) (from level 3, Defined)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Reference and Master Data · [ISO 8000 (data quality)](../../frameworks/framework-iso-8000.md): ISO 8000-120 – Provenance

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Multidomain MDM SaaS](../../technologies/informatica/informatica-multidomain-mdm-saas.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Master Data Governance](../../technologies/sap/sap-master-data-governance.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Ataccama ONE Master Data Management](../../technologies/independent/ataccama-one-mdm.md), [Profisee MDM](../../technologies/independent/profisee-mdm.md), [Reltio Multidomain MDM](../../technologies/independent/reltio-multidomain-mdm.md), [Tamr](../../technologies/independent/tamr.md) |
