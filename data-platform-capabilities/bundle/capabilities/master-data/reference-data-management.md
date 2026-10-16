---
type: Capability
id: reference-data-management
title: Reference data management
description: Manage shared code lists and mappings, such as country codes and product categories, with versions and approvals.
broader: [master-data]
related: [data-enrichment, data-quality-rules, business-glossary, critical-data-elements]
tags: [master-data]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Reference data is the set of permitted values used to classify other data: country and currency codes, units of measure, industry classifications, product categories, status codes and internal codes such as business lines. Each code list is held with its values, descriptions and effective dates. Mappings link each system's local codes to the enterprise standard, so "UK", "GBR" and "826" all resolve to one country. Changes go through versioning and approval before they are published to consumers.

Inconsistent codes break joins and totals quietly: revenue by region differs between two reports because their source systems group countries differently. External standards such as ISO 3166 for countries and ISO 4217 for currencies change too, and regulators publish their own lists. Reference data is smaller and more stable than master data but used everywhere, so a wrong change spreads fast. Many organisations start with spreadsheets; managing it properly adds history, approvals, distribution as tables and APIs, and lineage to the reports that use it.

# Key considerations

- Track changes to external standards and plan how updates reach consumers.
- Version code lists and mappings with effective dates so historical reports stay consistent.
- Publish code lists in one place that consumers join to, rather than copying them into each pipeline.
- Validate incoming data against the code lists and route unknown codes for review.

# Questions to ask

- Which code lists are used across many systems or reports, and who maintains them now?
- How do each system's local codes map to a standard, and is that mapping written down?
- How often do code lists change, and who must approve a change?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Master and reference data](master-data.md) |
| Broader | [Master and reference data](master-data.md) |
| Narrower | [Hierarchy management](hierarchy-management.md) |
| Related | [Business glossary](../metadata/business-glossary.md), [Critical data elements](../governance/critical-data-elements.md), [Data cleansing and standardisation](../data-quality/data-cleansing.md), [Data enrichment](../processing/data-enrichment.md), [Data entry and write-back](../analytics-bi/data-writeback.md), [Data quality rules](../data-quality/data-quality-rules.md), [Product information management](product-information-management.md) |

# Where it appears

- **Use cases:** [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (requires, level 2) · [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (requires, level 3)
- **Personas:** [Data steward](../../personas/persona-data-steward.md)
- **Maturity tracks:** [Master and reference data](../../maturity/track-master-data.md) (from level 2, Managed)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 2 – Data architecture and IT infrastructure · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Reference and Master Data · [EU Data Act](../../frameworks/framework-eu-data-act.md): Chapter VIII – Interoperability · [ISO 8000 (data quality)](../../frameworks/framework-iso-8000.md): ISO 8000-100 and 8000-110 – Master data exchange and conformance to data specification; ISO 8000-115 to 8000-119 – Quality identifiers

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Informatica](../../platforms/platform-informatica.md) | Reference 360 | [Informatica Reference 360](../../technologies/informatica/informatica-reference-360.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Ataccama ONE Master Data Management](../../technologies/independent/ataccama-one-mdm.md), [Collibra Data Governance](../../technologies/independent/collibra-data-governance.md), [Profisee MDM](../../technologies/independent/profisee-mdm.md), [Semarchy Data Platform](../../technologies/independent/semarchy-data-platform.md) |

Narrower capabilities are realised by a further 8 technologies; see their pages.
