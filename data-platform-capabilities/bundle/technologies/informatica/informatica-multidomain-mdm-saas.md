---
type: Technology
id: informatica-multidomain-mdm-saas
title: Informatica Multidomain MDM SaaS
description: Cloud MDM service for modelling any business entity, matching and merging records from many sources into golden records with survivorship rules, and managing relationships and hierarchies through the Business 360 Console.
aliases: [MDM SaaS]
platform: platform-informatica
kind: saas
availability: ga
realises: [master-data-management, entity-resolution, survivorship, hierarchy-management]
resource: https://onlinehelp.informatica.com/IICS/prod/mde/en/zz-cloud-helpoverview/Help_for_Other_Services.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Fall 2025 added Adaptive AI Matching and match explainability. Spring 2026 added interactive record-history visualisations, and MDM Workflow Builder entered public preview. Agentic Multidomain MDM and a Data Steward Agent were announced for Q4 2026. Golden records can be published to Salesforce Data 360, Agentforce and Databricks SQL.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Master data management](../../capabilities/master-data/master-data-management.md) (Master and reference data) (primary): Create a single trusted record for entities such as customer, product or supplier from many sources.
- [Entity resolution](../../capabilities/master-data/entity-resolution.md) (Master and reference data): Find and link records that refer to the same real-world entity, even when they do not match exactly.
- [Merge and survivorship](../../capabilities/master-data/survivorship.md) (Master and reference data): Combine matched records into a golden record using rules about which source wins for each attribute.
- [Hierarchy management](../../capabilities/master-data/hierarchy-management.md) (Master and reference data): Maintain hierarchies and relationships such as corporate structures, product taxonomies and organisation charts.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud, Informatica MDM SaaS

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [SAP](../../platforms/platform-sap.md) | [SAP Master Data Governance](../sap/sap-master-data-governance.md) | [Entity resolution](../../capabilities/master-data/entity-resolution.md), [Master data management](../../capabilities/master-data/master-data-management.md), [Merge and survivorship](../../capabilities/master-data/survivorship.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Profisee MDM](../independent/profisee-mdm.md), [Reltio Multidomain MDM](../independent/reltio-multidomain-mdm.md), [Ataccama ONE Master Data Management](../independent/ataccama-one-mdm.md) | [Entity resolution](../../capabilities/master-data/entity-resolution.md), [Hierarchy management](../../capabilities/master-data/hierarchy-management.md), [Master data management](../../capabilities/master-data/master-data-management.md), [Merge and survivorship](../../capabilities/master-data/survivorship.md) |
