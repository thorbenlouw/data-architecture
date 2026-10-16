---
type: Capability
id: hierarchy-management
title: Hierarchy management
description: Maintain hierarchies and relationships such as corporate structures, product taxonomies and organisation charts.
broader: [master-data-management, reference-data-management]
related: [semantic-layer, enterprise-planning, graph-data, temporal-data]
tags: [master-data]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Hierarchies are the parent-child structures laid over master data: legal entity trees showing which company owns which, product taxonomies from department down to item, sales territories, cost centres, charts of accounts and organisation charts. Each member is linked to its parent, often with effective dates, and the same member can sit in several hierarchies at once, such as a product placed in both a merchandising tree and a financial reporting tree.

Hierarchies drive roll-ups in reports, credit exposure across a corporate group, commission calculations, access rules and planning. They change with reorganisations, acquisitions and reclassification, and reports often need results under both the old and the new structure. Managing them involves versions, approval workflows, checks that every member has a parent and that no loops exist, and publishing to BI and planning tools. Reference data management maintains flat code lists; hierarchies add structure on top, and the two are often managed together.

# Key considerations

- Support ragged hierarchies of uneven depth and alternative hierarchies over the same members.
- Keep effective dates and versions so reports can be restated under old or new structures.
- Validate before publishing: no orphans, no loops, and each member placed exactly once where that is required.
- Publish in a form BI tools and semantic layers can use directly, such as parent-child and flattened level tables.

# Questions to ask

- Which hierarchies drive important reports, and who changes them?
- How often do they change, and must history be reported both ways?
- Which downstream tools need the hierarchies, and in what form?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Master and reference data](master-data.md) |
| Broader | [Master data management](master-data-management.md), [Reference data management](reference-data-management.md) |
| Related | [Bitemporal data](../specialised-data/temporal-data.md), [Graph data](../specialised-data/graph-data.md), [Planning and forecasting](../analytics-bi/enterprise-planning.md), [Product information management](product-information-management.md), [Semantic layer](../analytics-bi/semantic-layer.md) |

# Where it appears

- **Use cases:** [Customer 360](../../use-cases/usecase-customer-360.md) (benefits from) · [Demand forecasting](../../use-cases/usecase-demand-forecasting.md) (requires, level 3) · [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (requires, level 3) · [IoT predictive maintenance](../../use-cases/usecase-iot-predictive-maintenance.md) (requires, level 2) · [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (benefits from)
- **Patterns:** [Dimensional modelling](../../patterns/dimensional-modelling.md)
- **Maturity tracks:** [Master and reference data](../../maturity/track-master-data.md) (from level 3, Defined)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 2 – Data architecture and IT infrastructure; Principle 4 – Completeness · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Reference and Master Data

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Multidomain MDM SaaS](../../technologies/informatica/informatica-multidomain-mdm-saas.md), [Informatica Product 360 SaaS](../../technologies/informatica/informatica-product-360.md), [Informatica Reference 360](../../technologies/informatica/informatica-reference-360.md), [Informatica Supplier 360 SaaS](../../technologies/informatica/informatica-supplier-360.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Precisely EnterWorks](../../technologies/independent/precisely-enterworks.md), [Profisee MDM](../../technologies/independent/profisee-mdm.md), [Reltio Multidomain MDM](../../technologies/independent/reltio-multidomain-mdm.md), [Stibo Systems STEP](../../technologies/independent/stibo-systems-step.md) |
