---
type: Technology
id: profisee-mdm
title: Profisee MDM
description: Multidomain MDM for matching, merging, stewardship and hierarchy management, closely integrated with Microsoft Azure, Purview and Fabric.
aliases: [Profisee]
platform: platform-independent
vendor: Profisee
kind: software
availability: ga
realises:
- master-data-management
- entity-resolution
- survivorship
- hierarchy-management
- reference-data-management
- stewardship-workflows
resource: https://profisee.com/news/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Profisee Anywhere (September 2026) lets customers manage master data directly in Microsoft Fabric OneLake. The 2026.R2 release added the Aisey AI agent for setup and an MCP server. It is the usual choice for MDM on Microsoft-centred platforms.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Master data management](../../capabilities/master-data/master-data-management.md) (Master and reference data) (primary): Create a single trusted record for entities such as customer, product or supplier from many sources.
- [Entity resolution](../../capabilities/master-data/entity-resolution.md) (Master and reference data): Find and link records that refer to the same real-world entity, even when they do not match exactly.
- [Merge and survivorship](../../capabilities/master-data/survivorship.md) (Master and reference data): Combine matched records into a golden record using rules about which source wins for each attribute.
- [Hierarchy management](../../capabilities/master-data/hierarchy-management.md) (Master and reference data): Maintain hierarchies and relationships such as corporate structures, product taxonomies and organisation charts.
- [Reference data management](../../capabilities/master-data/reference-data-management.md) (Master and reference data): Manage shared code lists and mappings, such as country codes and product categories, with versions and approvals.
- [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md) (Governance and compliance): Route governance tasks such as term approvals, classification reviews, access approvals and match reviews to the right steward, with queues, deadlines, delegation and a record of each decision.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Multidomain MDM SaaS](../informatica/informatica-multidomain-mdm-saas.md), [Informatica Customer 360 SaaS](../informatica/informatica-customer-360.md), [Informatica Supplier 360 SaaS](../informatica/informatica-supplier-360.md) | [Entity resolution](../../capabilities/master-data/entity-resolution.md), [Hierarchy management](../../capabilities/master-data/hierarchy-management.md), [Master data management](../../capabilities/master-data/master-data-management.md), [Merge and survivorship](../../capabilities/master-data/survivorship.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Master Data Governance](../sap/sap-master-data-governance.md) | [Entity resolution](../../capabilities/master-data/entity-resolution.md), [Master data management](../../capabilities/master-data/master-data-management.md), [Merge and survivorship](../../capabilities/master-data/survivorship.md), [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md) |
