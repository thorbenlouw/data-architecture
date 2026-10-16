---
type: Capability
id: master-data
title: Master and reference data
description: Create and maintain consistent, trusted versions of core business entities and shared code lists.
broader: []
related: [data-quality-rules, data-cleansing, data-modelling, critical-data-elements, data-domains]
depends_on: [data-ownership]
order: 13
tags: [master-data]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Master data describes the core things a business deals with: customers, products, suppliers, employees, locations and assets. Reference data is the shared code lists used to classify them and their transactions, such as country codes, currencies, units of measure and product categories. Both change slowly compared with transactions, are used by many systems, and cause errors everywhere when systems disagree, for example one supplier held under three identifiers or two definitions of a sales region.

Master data management brings the records about each entity together into one trusted record. It relies on entity resolution to find records that match, survivorship rules to choose which values win, and hierarchy management to maintain structures such as corporate ownership and product taxonomies. Reference data management maintains code lists, their versions and the mappings between each system's local codes and the standard. Product information management is a specialised form for the product content published to sales channels.

The domain sits between operational systems and analytics. Approaches range from a registry that only links source identifiers, through consolidated golden records for analytics, to a central hub that creates master data and sends it back to operational systems. Analytics-only approaches deliver faster; operational ones fix problems at source but need process change. None stays accurate without named owners and stewards.

# Key considerations

- Choose the implementation style per entity: registry, consolidation, coexistence or central hub. Customer and product often need different styles.
- Master data programmes fail more often on ownership and process than on technology. Name accountable owners and stewards first.
- Start with the entities and attributes that cause measurable problems, not a complete enterprise model.
- Plan how golden records and code mappings reach consumers: shared tables, APIs, events or sync back to sources.

# Questions to ask

- Which entities cause the most errors or rework when systems disagree?
- Is mastered data needed only for analytics, or must it flow back to operational systems?
- Who will own and steward each master data domain?
- How many systems hold each entity, and how do their identifiers relate?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Narrower | [Master data management](master-data-management.md), [Product information management](product-information-management.md), [Reference data management](reference-data-management.md) |
| Related | [Critical data elements](../governance/critical-data-elements.md), [Data cleansing and standardisation](../data-quality/data-cleansing.md), [Data domains](../governance/data-domains.md), [Data modelling and design](../development-lifecycle/data-modelling.md), [Data quality rules](../data-quality/data-quality-rules.md) |
| Depends on | [Ownership and stewardship](../governance/data-ownership.md) |

# Where it appears

- **Maturity tracks:** [Master and reference data](../../maturity/track-master-data.md)

# How platforms provide it

No technology in this bundle realises this capability directly yet.

Narrower capabilities are realised by a further 22 technologies; see their pages.
