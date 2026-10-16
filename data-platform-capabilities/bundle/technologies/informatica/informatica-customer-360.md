---
type: Technology
id: informatica-customer-360
title: Informatica Customer 360 SaaS
description: Prebuilt customer master application on MDM SaaS that consolidates customer records, relationships and inferred attributes into one shared view.
aliases: [MDM - Customer 360]
platform: platform-informatica
kind: saas
availability: ga
realises: [master-data-management, entity-resolution]
resource: https://www.informatica.com/products/master-data-management.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A Customer Identification MCP server lets agents look up mastered customers and related records.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Master data management](../../capabilities/master-data/master-data-management.md) (Master and reference data) (primary): Create a single trusted record for entities such as customer, product or supplier from many sources.
- [Entity resolution](../../capabilities/master-data/entity-resolution.md) (Master and reference data): Find and link records that refer to the same real-world entity, even when they do not match exactly.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud, Informatica MDM SaaS

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Entity Resolution](../aws/aws-entity-resolution.md) | [Entity resolution](../../capabilities/master-data/entity-resolution.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Master Data Governance](../sap/sap-master-data-governance.md) | [Entity resolution](../../capabilities/master-data/entity-resolution.md), [Master data management](../../capabilities/master-data/master-data-management.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Ataccama ONE Master Data Management](../independent/ataccama-one-mdm.md), [Semarchy Data Platform](../independent/semarchy-data-platform.md), [Stibo Systems STEP](../independent/stibo-systems-step.md) | [Entity resolution](../../capabilities/master-data/entity-resolution.md), [Master data management](../../capabilities/master-data/master-data-management.md) |
