---
type: Technology
id: informatica-cloud-data-access-management
title: Informatica Cloud Data Access Management (CDAM)
description: Defines data filter, access control and de-identification policies once, driven by catalogue metadata, and enforces them by pushing them into data platforms or by applying them inside Informatica pipelines and marketplace deliveries.
aliases: [CDAM, Data Access Management]
platform: platform-informatica
kind: managed-service
availability: ga
realises: [data-policy-management, attribute-based-access, row-level-security, deidentification]
resource: https://onlinehelp.informatica.com/IICS/prod/DGC/en/ae-data-accessmanagement/Data_access_policy_enforcement_methods.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Pushdown targets include Snowflake, Databricks, Google BigQuery, Amazon Redshift, Amazon S3, Microsoft Fabric, Power BI and Tableau. De-identification is enforced only through the Access Policy transformation in Data Integration and Ingestion and Replication, or through Marketplace orders, not by pushdown. CDAM builds on technology Informatica gained when it bought Privitar in 2023.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Policy management](../../capabilities/governance/data-policy-management.md) (Governance and compliance) (primary): Define data policies centrally and apply them consistently across platforms and tools.
- [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md) (Security and access): Grant or deny access based on attributes of the user and tags on the data.
- [Row-level security](../../capabilities/security/row-level-security.md) (Security and access): Restrict which rows each user sees based on who they are.
- [De-identification](../../capabilities/governance/deidentification.md) (Governance and compliance): Pseudonymise, tokenise or anonymise data so it can be used with less privacy risk.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Intent-Driven Governance](../snowflake/snowflake-intent-driven-governance.md) (preview), [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md), [Snowflake row access policies](../snowflake/snowflake-row-access-policies.md) | [Policy management](../../capabilities/governance/data-policy-management.md), [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog attribute-based access control (ABAC)](../databricks/databricks-abac.md), [Databricks governed tags](../databricks/databricks-governed-tags.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Policy management](../../capabilities/governance/data-policy-management.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [Policy management](../../capabilities/governance/data-policy-management.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Policy management](../../capabilities/governance/data-policy-management.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Open Policy Agent (OPA)](../open-source/open-policy-agent.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Policy management](../../capabilities/governance/data-policy-management.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [OneTrust Data Use Governance](../independent/onetrust-data-use-governance.md), [Collibra Data Access](../independent/collibra-data-access.md), [Immuta Data Authorization Platform](../independent/immuta-data-authorization-platform.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Policy management](../../capabilities/governance/data-policy-management.md), [Row-level security](../../capabilities/security/row-level-security.md) |
