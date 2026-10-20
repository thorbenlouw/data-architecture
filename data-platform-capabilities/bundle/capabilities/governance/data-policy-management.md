---
type: Capability
id: data-policy-management
title: Policy management
description: Define data policies centrally and apply them consistently across platforms and tools.
aliases: [policy as code]
broader: [governance]
related: [attribute-based-access, column-masking, row-level-security, data-retention, infrastructure-as-code]
depends_on: [data-classification, access-control]
tags: [governance]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A policy states a rule about data in a form systems can apply, for example "columns tagged `personal.email` are masked for everyone outside customer service" or "finance tables are deleted seven years after the end of the financial year". Policy management stores such rules in one place, with an owner, history and approval, and pushes them to the systems that enforce them. Rules are usually written against classifications, domains and user attributes rather than named tables, so one policy covers every matching asset.

Most organisations run several engines and tools, each with its own permission model, and writing the same rule in each by hand leaves gaps and contradictions. Central management helps only as far as each target can enforce the rule; elsewhere the policy becomes a control checked by review. Approaches range from one platform's native policy features, to separate policy engines that translate rules into each system's grants, to policy as code in Git. Access control enforces rules; policy management is where they are written and governed.

# Key considerations

- Check which policy types each target system can enforce natively, such as masking, row filters or retention, and what happens to policies it cannot.
- Treat policies as code: review them, test them against sample users and data, and keep history. A wrong policy can expose or block a whole domain at once.
- Define how conflicting policies are resolved, for example deny overrides allow, before many teams start writing them.
- For high-risk rules, separate the people who write policies from those who approve them.
- Policies are only as good as the tags they refer to. Classification coverage limits what policy can enforce.

# Questions to ask

- How many engines and tools must enforce the same rules, and does each have its own permission model?
- Which policies exist only as documents today, and which are enforced in systems?
- Who may create or change a data policy, and who approves it?
- How would you test a policy change before it takes effect in production?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Governance and compliance](governance.md) |
| Broader | [Governance and compliance](governance.md) |
| Related | [Access control](../security/access-control.md), [Active metadata](../metadata/active-metadata.md), [Attribute- and tag-based access control](../security/attribute-based-access.md), [Catalogue federation](../storage/catalogue-federation.md), [Column security and dynamic masking](../security/column-masking.md), [Infrastructure as code](../platform-operations/infrastructure-as-code.md), [Retention and disposal](data-retention.md), [Row-level security](../security/row-level-security.md) |
| Depends on | [Data classification](data-classification.md), [Access control](../security/access-control.md) |

# Where it appears

- **Use cases:** [Sensitive data protection](../../use-cases/usecase-sensitive-data-protection.md) (requires, level 3)
- **Patterns:** [Data fabric](../../patterns/data-fabric.md) · [Data mesh](../../patterns/data-mesh.md)
- **Personas:** [Chief data officer](../../personas/persona-cdo.md) · [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Governance operating model](../../maturity/track-governance.md) (from level 3, Defined)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 1 – Governance · [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 4 Data Sovereignty and Cross-Border Movement (Governance and accountability) · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Governance · [Data mesh principles](../../frameworks/framework-data-mesh.md): Federated computational governance · [DCAM v3](../../frameworks/framework-edm-dcam.md): 1 Data Strategy, DMS & Business Case; 6 Govern Data & DMP · [GDPR](../../frameworks/framework-gdpr.md): Article 5(1)(b) – Purpose limitation · [ISO 8000 (data quality)](../../frameworks/framework-iso-8000.md): ISO 8000-51 – Exchange of data policy statements · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Clause 5 – Leadership; Annex A.2 – Policies related to AI · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): GOVERN 1 – Policies, processes and practices

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Horizon Catalog](../../technologies/snowflake/snowflake-horizon-catalog.md), [Snowflake Intent-Driven Governance](../../technologies/snowflake/snowflake-intent-driven-governance.md) (preview) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks governed tags](../../technologies/databricks/databricks-governed-tags.md), [Unity Catalog attribute-based access control (ABAC)](../../technologies/databricks/databricks-abac.md) |
| [Informatica](../../platforms/platform-informatica.md) | Data Access Management policies | [Informatica Cloud Data Access Management (CDAM)](../../technologies/informatica/informatica-cloud-data-access-management.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.data intelligence](../../technologies/ibm/ibm-watsonx-data-intelligence.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS Data Governance](../../technologies/sas/sas-data-governance.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Open Policy Agent (OPA)](../../technologies/open-source/open-policy-agent.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Collibra Data Access](../../technologies/independent/collibra-data-access.md), [Collibra Data Governance](../../technologies/independent/collibra-data-governance.md), [Immuta Data Authorization Platform](../../technologies/independent/immuta-data-authorization-platform.md), [OneTrust Data Use Governance](../../technologies/independent/onetrust-data-use-governance.md), [Privacera](../../technologies/independent/privacera.md) |
