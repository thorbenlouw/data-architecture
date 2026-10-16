---
type: Technology
id: semarchy-data-platform
title: Semarchy Data Platform
description: Platform that combines multidomain MDM, reference data management, data quality and governance for publishing mastered entities as data products.
platform: platform-independent
vendor: Semarchy
kind: software
availability: ga
realises:
- master-data-management
- reference-data-management
- entity-resolution
- data-quality-rules
- stewardship-workflows
resource: https://www.semarchy.com/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Grew out of Semarchy xDM. Semarchy now markets "intelligent data products" built on mastered data, and the platform can be deployed as SaaS or self-managed. Data stewards review matches and approve changes through configurable workflows.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Master data management](../../capabilities/master-data/master-data-management.md) (Master and reference data) (primary): Create a single trusted record for entities such as customer, product or supplier from many sources.
- [Reference data management](../../capabilities/master-data/reference-data-management.md) (Master and reference data): Manage shared code lists and mappings, such as country codes and product categories, with versions and approvals.
- [Entity resolution](../../capabilities/master-data/entity-resolution.md) (Master and reference data): Find and link records that refer to the same real-world entity, even when they do not match exactly.
- [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) (Data quality and observability): Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency.
- [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md) (Governance and compliance): Route governance tasks such as term approvals, classification reviews, access approvals and match reviews to the right steward, with queues, deadlines, delegation and a record of each decision.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Customer 360 SaaS](../informatica/informatica-customer-360.md), [Informatica Multidomain MDM SaaS](../informatica/informatica-multidomain-mdm-saas.md), [Informatica Supplier 360 SaaS](../informatica/informatica-supplier-360.md) | [Entity resolution](../../capabilities/master-data/entity-resolution.md), [Master data management](../../capabilities/master-data/master-data-management.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Master Data Governance](../sap/sap-master-data-governance.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Entity resolution](../../capabilities/master-data/entity-resolution.md), [Master data management](../../capabilities/master-data/master-data-management.md), [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md) |
