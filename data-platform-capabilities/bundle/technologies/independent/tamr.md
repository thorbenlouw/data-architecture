---
type: Technology
id: tamr
title: Tamr
description: Machine-learning-led MDM that matches and enriches records with built-in external reference data to produce golden records, made available in real time.
platform: platform-independent
vendor: Tamr
kind: saas
availability: ga
realises: [master-data-management, entity-resolution, survivorship, data-cleansing, data-enrichment]
resource: https://www.tamr.com/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Tamr RealTime serves mastered data to operational systems. Prebuilt data products cover customers, contacts, suppliers, healthcare providers and products, and an MCP connection is available for LLMs. It suits teams that want matching driven more by machine learning than by rules.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Master data management](../../capabilities/master-data/master-data-management.md) (Master and reference data) (primary): Create a single trusted record for entities such as customer, product or supplier from many sources.
- [Entity resolution](../../capabilities/master-data/entity-resolution.md) (Master and reference data): Find and link records that refer to the same real-world entity, even when they do not match exactly.
- [Merge and survivorship](../../capabilities/master-data/survivorship.md) (Master and reference data): Combine matched records into a golden record using rules about which source wins for each attribute.
- [Data cleansing and standardisation](../../capabilities/data-quality/data-cleansing.md) (Data quality and observability): Correct and standardise data values such as addresses, names, dates and codes.
- [Data enrichment](../../capabilities/processing/data-enrichment.md) (Processing and transformation): Add attributes to records from lookup tables or curated third-party reference data.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Multidomain MDM SaaS](../informatica/informatica-multidomain-mdm-saas.md), [Informatica Customer 360 SaaS](../informatica/informatica-customer-360.md), [Informatica Supplier 360 SaaS](../informatica/informatica-supplier-360.md) | [Entity resolution](../../capabilities/master-data/entity-resolution.md), [Master data management](../../capabilities/master-data/master-data-management.md), [Merge and survivorship](../../capabilities/master-data/survivorship.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Master Data Governance](../sap/sap-master-data-governance.md) | [Entity resolution](../../capabilities/master-data/entity-resolution.md), [Master data management](../../capabilities/master-data/master-data-management.md), [Merge and survivorship](../../capabilities/master-data/survivorship.md) |
