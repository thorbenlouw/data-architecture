---
type: Technology
id: onetrust-data-use-governance
title: OneTrust Data Use Governance
description: Turns privacy and purpose rules into data access and masking policies and applies them on cloud data platforms.
platform: platform-independent
vendor: OneTrust
kind: saas
availability: ga
realises: [data-policy-management, consent-management, attribute-based-access]
resource: https://www.onetrust.com/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

OneTrust's bridge between privacy obligations and platform access control. It overlaps with Immuta and Collibra Data Access, so decide which tool owns enforcement.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Policy management](../../capabilities/governance/data-policy-management.md) (Governance and compliance) (primary): Define data policies centrally and apply them consistently across platforms and tools.
- [Consent and purpose management](../../capabilities/governance/consent-management.md) (Governance and compliance): Record what each person agreed to and restrict use of their data to permitted purposes.
- [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md) (Security and access): Grant or deny access based on attributes of the user and tags on the data.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Intent-Driven Governance](../snowflake/snowflake-intent-driven-governance.md) (preview), [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md) | [Policy management](../../capabilities/governance/data-policy-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog attribute-based access control (ABAC)](../databricks/databricks-abac.md), [Databricks governed tags](../databricks/databricks-governed-tags.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Policy management](../../capabilities/governance/data-policy-management.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Access Management (CDAM)](../informatica/informatica-cloud-data-access-management.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Policy management](../../capabilities/governance/data-policy-management.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [Policy management](../../capabilities/governance/data-policy-management.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Open Policy Agent (OPA)](../open-source/open-policy-agent.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Policy management](../../capabilities/governance/data-policy-management.md) |
