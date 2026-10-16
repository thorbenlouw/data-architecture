---
type: Capability
id: attribute-based-access
title: Attribute- and tag-based access control
description: Grant or deny access based on attributes of the user and tags on the data.
aliases: [ABAC, tag-based policies]
broader: [access-control]
related: [data-classification, data-policy-management, consent-management, role-based-access, column-masking]
depends_on: [data-classification, identity-authentication]
tags: [security]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Attribute-based access control (ABAC) decides access from properties of the user and the data instead of from explicit grants on each object. Data carries tags such as `sensitivity=restricted` or `domain=hr`; users carry attributes such as department, region or clearance. A policy then says, for example, "users may read columns tagged `personal` only if their `pii_approved` attribute is true; otherwise the values are masked". On data platforms the usual form is tag-based access control, where policies attach to classification tags and apply to every table or column carrying them.

ABAC scales where roles do not: one policy covers thousands of tables, and new data is protected as soon as it is tagged. It also expresses rules roles handle badly, such as limits by region or purpose. The cost is dependence on accurate tags and attributes, and access decisions that are harder to explain. Open Policy Agent and the XACML standard follow the general model; data platforms usually build narrower tag-based policies into the catalogue.

# Key considerations

- Tag quality becomes a security control. Restrict who can set and remove sensitive tags as carefully as who can grant access.
- Provide a way to explain a decision, showing which policy and attributes allowed or denied access, for users and auditors.
- Decide the default for untagged data. Default-deny is safer but blocks new data until it is classified.
- Source user attributes from an authoritative system and sync them automatically, rather than maintaining them by hand in the platform.

# Questions to ask

- Are sensitive columns tagged consistently enough to base access on tags?
- Which user attributes, such as department, region or clearance, are available from the identity provider?
- Do access rules depend on purpose, location or other conditions that roles handle poorly?
- How would a user or auditor find out why access was denied?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Security and access](security.md) |
| Broader | [Access control](access-control.md) |
| Related | [Active metadata](../metadata/active-metadata.md), [Column security and dynamic masking](column-masking.md), [Consent and purpose management](../governance/consent-management.md), [Data classification](../governance/data-classification.md), [Data licensing and usage rights](../governance/data-usage-rights.md), [Permission-aware retrieval](../generative-ai/permission-aware-retrieval.md), [Policy management](../governance/data-policy-management.md), [Role-based access control](role-based-access.md), [Row-level security](row-level-security.md) |
| Depends on | [Data classification](../governance/data-classification.md), [Identity and authentication](identity-authentication.md) |

# Where it appears

- **Use cases:** [Sensitive data protection](../../use-cases/usecase-sensitive-data-protection.md) (requires, level 3)
- **Patterns:** [Data fabric](../../patterns/data-fabric.md)
- **Personas:** [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Security and access control](../../maturity/track-security.md) (from level 3, Defined)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 7 Entitlements and Access for Sensitive Data (Accessibility and usage) · [Data mesh principles](../../frameworks/framework-data-mesh.md): Federated computational governance · [GDPR](../../frameworks/framework-gdpr.md): Article 5(1)(b) – Purpose limitation; Article 9 – Special categories of personal data; Article 18 – Right to restriction of processing

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | LF-Tags (Lake Formation tag-based access control) | [AWS Identity and Access Management](../../technologies/aws/aws-iam.md), [AWS Lake Formation](../../technologies/aws/aws-lake-formation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | policy tags; IAM Conditions; data governance tags | [BigQuery policy tags](../../technologies/google-cloud/gcp-bigquery-policy-tags.md), [Google Cloud Identity and Access Management](../../technologies/google-cloud/gcp-iam.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | tag-based masking policies | [Snowflake masking policies](../../technologies/snowflake/snowflake-masking-policies.md), [Snowflake object tagging](../../technologies/snowflake/snowflake-object-tagging.md), [Snowflake row access policies](../../technologies/snowflake/snowflake-row-access-policies.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Unity Catalog attribute-based access control (ABAC)](../../technologies/databricks/databricks-abac.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Cloud Data Access Management (CDAM)](../../technologies/informatica/informatica-cloud-data-access-management.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Shared Data Experience (SDX)](../../technologies/cloudera/cloudera-sdx.md) |
| [Palantir](../../platforms/platform-palantir.md) | Markings | [Palantir Foundry security controls](../../technologies/palantir/palantir-security-controls.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Ranger](../../technologies/open-source/apache-ranger.md), [Open Policy Agent (OPA)](../../technologies/open-source/open-policy-agent.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Collibra Data Access](../../technologies/independent/collibra-data-access.md), [Immuta Data Authorization Platform](../../technologies/independent/immuta-data-authorization-platform.md), [OneTrust Data Use Governance](../../technologies/independent/onetrust-data-use-governance.md), [Privacera](../../technologies/independent/privacera.md), [Starburst Galaxy](../../technologies/independent/starburst-galaxy.md) |
