---
type: Technology
id: sap-master-data-governance
title: SAP Master Data Governance
description: Application for central creation, consolidation and governed maintenance of master data with workflows, validation rules and quality monitoring, on S/4HANA or as a cloud edition on BTP.
aliases: [SAP MDG, MDG]
platform: platform-sap
kind: software
availability: ga
realises:
- master-data-management
- entity-resolution
- survivorship
- data-quality-rules
- data-ownership
- stewardship-workflows
resource: https://www.sap.com/products/data-cloud/master-data-governance.html
tags: [sap]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Supports central governance, consolidation (match and merge) and mass processing. SAP recommends governing master data in MDG and sharing it to analytics through Datasphere or BDC.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Master data management](../../capabilities/master-data/master-data-management.md) (Master and reference data) (primary): Create a single trusted record for entities such as customer, product or supplier from many sources.
- [Entity resolution](../../capabilities/master-data/entity-resolution.md) (Master and reference data): Find and link records that refer to the same real-world entity, even when they do not match exactly.
- [Merge and survivorship](../../capabilities/master-data/survivorship.md) (Master and reference data): Combine matched records into a golden record using rules about which source wins for each attribute.
- [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) (Data quality and observability): Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency.
- [Ownership and stewardship](../../capabilities/governance/data-ownership.md) (Governance and compliance): Assign accountable owners and stewards to data and record their responsibilities.
- [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md) (Governance and compliance): Route governance tasks such as term approvals, classification reviews, access approvals and match reviews to the right steward, with queues, deadlines, delegation and a record of each decision.

**Platform:** [SAP](../../platforms/platform-sap.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Multidomain MDM SaaS](../informatica/informatica-multidomain-mdm-saas.md), [Informatica Customer 360 SaaS](../informatica/informatica-customer-360.md), [Informatica Supplier 360 SaaS](../informatica/informatica-supplier-360.md) | [Entity resolution](../../capabilities/master-data/entity-resolution.md), [Master data management](../../capabilities/master-data/master-data-management.md), [Merge and survivorship](../../capabilities/master-data/survivorship.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Ataccama ONE Master Data Management](../independent/ataccama-one-mdm.md), [Semarchy Data Platform](../independent/semarchy-data-platform.md), [Profisee MDM](../independent/profisee-mdm.md) | [Entity resolution](../../capabilities/master-data/entity-resolution.md), [Master data management](../../capabilities/master-data/master-data-management.md), [Merge and survivorship](../../capabilities/master-data/survivorship.md), [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md) |
