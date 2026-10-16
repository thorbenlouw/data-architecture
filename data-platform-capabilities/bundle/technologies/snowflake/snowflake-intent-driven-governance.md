---
type: Technology
id: snowflake-intent-driven-governance
title: Snowflake Intent-Driven Governance
description: A review-first CoCo workflow that turns a governance goal stated in plain language into a scope, a governance specification and SQL for tags and protections, which a person approves before it runs.
platform: platform-snowflake
kind: feature
availability: preview
realises: [data-policy-management, data-classification]
resource: https://docs.snowflake.com/user-guide/intent-driven-governance
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Policy management](../../capabilities/governance/data-policy-management.md) (Governance and compliance) (primary): Define data policies centrally and apply them consistently across platforms and tools.
- [Data classification](../../capabilities/governance/data-classification.md) (Governance and compliance): Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** preview  
**Product family:** Snowflake Horizon Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Databricks](../../platforms/platform-databricks.md) | [Databricks governed tags](../databricks/databricks-governed-tags.md), [Unity Catalog attribute-based access control (ABAC)](../databricks/databricks-abac.md) | [Data classification](../../capabilities/governance/data-classification.md), [Policy management](../../capabilities/governance/data-policy-management.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Access Management (CDAM)](../informatica/informatica-cloud-data-access-management.md) | [Policy management](../../capabilities/governance/data-policy-management.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [Data classification](../../capabilities/governance/data-classification.md), [Policy management](../../capabilities/governance/data-policy-management.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Open Policy Agent (OPA)](../open-source/open-policy-agent.md) | [Policy management](../../capabilities/governance/data-policy-management.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [OneTrust Data Use Governance](../independent/onetrust-data-use-governance.md), [Privacera](../independent/privacera.md), [Collibra Data Access](../independent/collibra-data-access.md) | [Policy management](../../capabilities/governance/data-policy-management.md), [Data classification](../../capabilities/governance/data-classification.md) |
