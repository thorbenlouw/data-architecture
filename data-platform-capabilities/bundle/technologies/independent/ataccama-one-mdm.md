---
type: Technology
id: ataccama-one-mdm
title: Ataccama ONE Master Data Management
description: Multidomain master data and reference data management module of Ataccama ONE, with matching, merging and stewardship built on the platform's data quality engine.
aliases: [Ataccama MDM]
platform: platform-independent
vendor: Ataccama
kind: software
availability: ga
realises:
- master-data-management
- reference-data-management
- entity-resolution
- survivorship
- stewardship-workflows
resource: https://www.ataccama.com/platform
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A good fit when quality and MDM are bought together. It shares rules and metadata with the data quality and catalogue modules.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Master data management](../../capabilities/master-data/master-data-management.md) (Master and reference data) (primary): Create a single trusted record for entities such as customer, product or supplier from many sources.
- [Reference data management](../../capabilities/master-data/reference-data-management.md) (Master and reference data): Manage shared code lists and mappings, such as country codes and product categories, with versions and approvals.
- [Entity resolution](../../capabilities/master-data/entity-resolution.md) (Master and reference data): Find and link records that refer to the same real-world entity, even when they do not match exactly.
- [Merge and survivorship](../../capabilities/master-data/survivorship.md) (Master and reference data): Combine matched records into a golden record using rules about which source wins for each attribute.
- [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md) (Governance and compliance): Route governance tasks such as term approvals, classification reviews, access approvals and match reviews to the right steward, with queues, deadlines, delegation and a record of each decision.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Multidomain MDM SaaS](../informatica/informatica-multidomain-mdm-saas.md), [Informatica Customer 360 SaaS](../informatica/informatica-customer-360.md), [Informatica Supplier 360 SaaS](../informatica/informatica-supplier-360.md) | [Entity resolution](../../capabilities/master-data/entity-resolution.md), [Master data management](../../capabilities/master-data/master-data-management.md), [Merge and survivorship](../../capabilities/master-data/survivorship.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Master Data Governance](../sap/sap-master-data-governance.md) | [Entity resolution](../../capabilities/master-data/entity-resolution.md), [Master data management](../../capabilities/master-data/master-data-management.md), [Merge and survivorship](../../capabilities/master-data/survivorship.md), [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md) |
