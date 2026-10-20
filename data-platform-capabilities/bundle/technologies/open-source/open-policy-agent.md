---
type: Technology
id: open-policy-agent
title: Open Policy Agent (OPA)
description: General-purpose policy engine that evaluates policies written in Rego to make authorisation and compliance decisions for applications, APIs, Kubernetes and pipelines.
aliases: [OPA, Rego]
platform: platform-open-source
kind: open-source
availability: ga
realises: [data-policy-management, attribute-based-access, configuration-guardrails]
resource: https://www.openpolicyagent.org/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, a CNCF graduated project. In 2025 the core maintainers moved from Styra to Apple; the project stays under CNCF governance. Used as a policy-as-code layer, for example for Trino access control or checking infrastructure plans in CI.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Policy management](../../capabilities/governance/data-policy-management.md) (Governance and compliance) (primary): Define data policies centrally and apply them consistently across platforms and tools.
- [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md) (Security and access): Grant or deny access based on attributes of the user and tags on the data.
- [Resource configuration guardrails](../../capabilities/platform-operations/configuration-guardrails.md) (Platform operations): Restrict which platform resources can be created and how they are configured, such as allowed sizes, regions, tags and network settings, and report anything that breaks the rules.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Intent-Driven Governance](../snowflake/snowflake-intent-driven-governance.md) (preview), [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md) | [Policy management](../../capabilities/governance/data-policy-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog attribute-based access control (ABAC)](../databricks/databricks-abac.md), [Databricks governed tags](../databricks/databricks-governed-tags.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Policy management](../../capabilities/governance/data-policy-management.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Access Management (CDAM)](../informatica/informatica-cloud-data-access-management.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Policy management](../../capabilities/governance/data-policy-management.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [Policy management](../../capabilities/governance/data-policy-management.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Policy management](../../capabilities/governance/data-policy-management.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [OneTrust Data Use Governance](../independent/onetrust-data-use-governance.md), [Collibra Data Access](../independent/collibra-data-access.md), [Immuta Data Authorization Platform](../independent/immuta-data-authorization-platform.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Policy management](../../capabilities/governance/data-policy-management.md) |
