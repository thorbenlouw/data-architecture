---
type: Capability
id: column-masking
title: Column security and dynamic masking
description: Hide or mask sensitive columns depending on who is querying.
aliases: [dynamic data masking, column-level security]
broader: [access-control]
related:
- deidentification
- attribute-based-access
- data-classification
- row-level-security
- test-data-management
depends_on: [data-classification]
tags: [security]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Column security hides whole columns from users without permission; dynamic masking returns a transformed value instead of the real one, depending on who is querying. A masking policy is a function attached to a column or a tag. For example, a support agent sees `****-****-****-4321` for a card number, an analyst sees a hash that still supports joins and counts, and the fraud team sees the full value. The stored data does not change; the engine applies the function as it returns results.

Masking lets one table serve users with different rights without copies, and lets analysts work with sensitive tables for purposes that do not need the sensitive values. Common masks are full redaction, partial display, hashing, rounding or generalisation, and returning NULL. Static masking and de-identification differ because they change the stored data, which suits test data and sharing. Masking does not stop inference: deterministic hashes can be matched against known values, and unmasked columns such as postcode and birth date may still identify a person.

# Key considerations

- Attach masking policies to classification tags rather than individual columns, so new sensitive columns are masked as soon as they are tagged.
- Deterministic masks such as hashes keep joins working but can be reversed for guessable values. Use keyed hashes where that matters.
- Check that masks apply consistently in views, materialised views, exports, caches and data shares.
- Decide whether masked columns may be used in filters and joins, and test what users can infer from the results.

# Questions to ask

- Which columns need different visibility for different users, and what should each group see?
- Do analysts need to join or count on sensitive columns without seeing the values?
- Is masking applied in the platform, in each tool, or by keeping separate copies today?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Security and access](security.md) |
| Broader | [Access control](access-control.md) |
| Related | [Attribute- and tag-based access control](attribute-based-access.md), [Data classification](../governance/data-classification.md), [De-identification](../governance/deidentification.md), [Policy management](../governance/data-policy-management.md), [Row-level security](row-level-security.md), [Shared compute isolation](compute-user-isolation.md), [Spreadsheet integration](../analytics-bi/spreadsheet-integration.md), [Test data management](../development-lifecycle/test-data-management.md) |
| Depends on | [Data classification](../governance/data-classification.md) |

# Where it appears

- **Use cases:** [Conversational analytics for business users](../../use-cases/usecase-conversational-bi.md) (requires, level 3) · [Customer 360](../../use-cases/usecase-customer-360.md) (requires, level 3) · [Self-service BI](../../use-cases/usecase-self-service-bi.md) (requires, level 2) · [Sensitive data protection](../../use-cases/usecase-sensitive-data-protection.md) (requires, level 3)
- **Patterns:** [ELT](../../patterns/elt.md)
- **Personas:** [Data analyst](../../personas/persona-data-analyst.md) · [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Security and access control](../../maturity/track-security.md) (from level 3, Defined)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 9 Appropriate Security Controls (Protection and privacy) · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Security · [GDPR](../../frameworks/framework-gdpr.md): Article 5(1)(c) – Data minimisation; Article 9 – Special categories of personal data; Article 25 – Data protection by design and by default

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Redshift dynamic data masking | [Amazon Redshift row-level security and dynamic data masking](../../technologies/aws/aws-redshift-fine-grained-security.md), [AWS Lake Formation](../../technologies/aws/aws-lake-formation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [OneLake security](../../technologies/microsoft/fabric-onelake-security.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | data masking with data policies | [BigQuery data masking](../../technologies/google-cloud/gcp-bigquery-data-masking.md), [BigQuery policy tags](../../technologies/google-cloud/gcp-bigquery-policy-tags.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | masking policies | [Snowflake masking policies](../../technologies/snowflake/snowflake-masking-policies.md), [Snowflake projection policies](../../technologies/snowflake/snowflake-projection-policies.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Lakeguard](../../technologies/databricks/databricks-lakeguard.md), [Unity Catalog attribute-based access control (ABAC)](../../technologies/databricks/databricks-abac.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | Masking policies | [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../../technologies/clickhouse/clickhouse-access-control.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Shared Data Experience (SDX)](../../technologies/cloudera/cloudera-sdx.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Database security features](../../technologies/oracle/oracle-database-security.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.data intelligence](../../technologies/ibm/ibm-watsonx-data-intelligence.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Foundry security controls](../../technologies/palantir/palantir-security-controls.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Ranger](../../technologies/open-source/apache-ranger.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Collibra Data Access](../../technologies/independent/collibra-data-access.md), [Immuta Data Authorization Platform](../../technologies/independent/immuta-data-authorization-platform.md), [Privacera](../../technologies/independent/privacera.md), [Protegrity Data Security Platform](../../technologies/independent/protegrity-data-security-platform.md), [Skyflow Data Privacy Vault](../../technologies/independent/skyflow-data-privacy-vault.md) |
