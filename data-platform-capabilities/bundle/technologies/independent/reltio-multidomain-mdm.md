---
type: Technology
id: reltio-multidomain-mdm
title: Reltio Multidomain MDM
description: Cloud-native multidomain MDM that resolves entities with rules and machine learning, merges them into profiles and serves them to applications through real-time APIs.
aliases: [Reltio, Reltio Context Intelligence Platform]
formerly: [Reltio Connected Data Platform]
platform: platform-independent
vendor: Reltio (SAP)
kind: saas
availability: ga
realises:
- master-data-management
- entity-resolution
- survivorship
- hierarchy-management
- low-latency-serving
- stewardship-workflows
resource: https://www.reltio.com/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

SAP announced the purchase in March 2026 and completed it by May 2026. Reltio is becoming a core part of SAP Business Data Cloud but is still sold on its own. The wider offer is branded the Reltio Context Intelligence Platform, with Reltio Intelligent 360 (unified profiles) and AgentFlow (AI agents for stewardship).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Master data management](../../capabilities/master-data/master-data-management.md) (Master and reference data) (primary): Create a single trusted record for entities such as customer, product or supplier from many sources.
- [Entity resolution](../../capabilities/master-data/entity-resolution.md) (Master and reference data): Find and link records that refer to the same real-world entity, even when they do not match exactly.
- [Merge and survivorship](../../capabilities/master-data/survivorship.md) (Master and reference data): Combine matched records into a golden record using rules about which source wins for each attribute.
- [Hierarchy management](../../capabilities/master-data/hierarchy-management.md) (Master and reference data): Maintain hierarchies and relationships such as corporate structures, product taxonomies and organisation charts.
- [Low-latency serving](../../capabilities/serving/low-latency-serving.md) (Serving and activation): Serve individual records or small result sets to applications in milliseconds.
- [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md) (Governance and compliance): Route governance tasks such as term approvals, classification reviews, access approvals and match reviews to the right steward, with queues, deadlines, delegation and a record of each decision.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Multidomain MDM SaaS](../informatica/informatica-multidomain-mdm-saas.md), [Informatica Customer 360 SaaS](../informatica/informatica-customer-360.md), [Informatica Supplier 360 SaaS](../informatica/informatica-supplier-360.md) | [Entity resolution](../../capabilities/master-data/entity-resolution.md), [Hierarchy management](../../capabilities/master-data/hierarchy-management.md), [Master data management](../../capabilities/master-data/master-data-management.md), [Merge and survivorship](../../capabilities/master-data/survivorship.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Master Data Governance](../sap/sap-master-data-governance.md) | [Entity resolution](../../capabilities/master-data/entity-resolution.md), [Master data management](../../capabilities/master-data/master-data-management.md), [Merge and survivorship](../../capabilities/master-data/survivorship.md), [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md) |
