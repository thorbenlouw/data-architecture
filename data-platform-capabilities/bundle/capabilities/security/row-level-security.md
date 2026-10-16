---
type: Capability
id: row-level-security
title: Row-level security
description: Restrict which rows each user sees based on who they are.
aliases: [row filters, row access policies]
broader: [access-control]
related: [column-masking, attribute-based-access, multi-tenancy, embedded-analytics, data-policy-management]
depends_on: [identity-authentication]
tags: [security]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Row-level security attaches a filter to a table so each query returns only the rows the user is entitled to see. The filter is a condition evaluated on every query, usually based on the current user or their groups and a mapping table, for example `region IN (SELECT region FROM user_regions WHERE user_name = current_user())`. Sales managers in France and Germany run the same query on the same table and see different rows, with no copies or separate views to maintain.

It suits any dataset that serves audiences with different scope: regions, business units, clients of a multi-tenant product, or the cases assigned to each caseworker. Enforced in the engine, it applies to every tool that queries the table; enforced only in a BI tool, it leaves the underlying data open to anyone with direct access. Performance is the main technical cost, since filters with subqueries run on every query, and filters interact with caching, materialised views and extracts.

# Key considerations

- Enforce filters in the engine or catalogue rather than in each BI tool, so direct SQL access is covered too.
- Govern and audit the entitlement mapping table, since changing it changes who sees what.
- Test performance at production scale. Filters that join large mapping tables slow every query on the table.
- Check how row filters behave with result caches, materialised views, exports and shared copies, which may not apply them.

# Questions to ask

- Do different users need to see different subsets of the same table, and by what rule?
- Where are the entitlement rules held today, and who maintains them?
- Is row filtering applied only in the BI tool, or in the data platform as well?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Security and access](security.md) |
| Broader | [Access control](access-control.md) |
| Related | [Analytics and BI](../analytics-bi/analytics-bi.md), [Attribute- and tag-based access control](attribute-based-access.md), [Column security and dynamic masking](column-masking.md), [Dashboards and interactive reports](../analytics-bi/dashboards-reports.md), [Embedded analytics](../analytics-bi/embedded-analytics.md), [External data sharing](../data-sharing/external-data-sharing.md), [External user and tenant identity](external-identity.md), [Multi-tenancy and workspace isolation](../platform-operations/multi-tenancy.md), [Paginated reports](../analytics-bi/paginated-reports.md), [Permission-aware retrieval](../generative-ai/permission-aware-retrieval.md), [Policy management](../governance/data-policy-management.md), [Result caching](../compute/result-caching.md), [Shared compute isolation](compute-user-isolation.md), [Storage credential vending](../storage/credential-vending.md) |
| Depends on | [Identity and authentication](identity-authentication.md) |
| Needed by | [Embedded analytics](../analytics-bi/embedded-analytics.md) |

# Where it appears

- **Use cases:** [Conversational analytics for business users](../../use-cases/usecase-conversational-bi.md) (requires, level 3) · [Customer-facing analytics](../../use-cases/usecase-customer-facing-analytics.md) (requires, level 4) · [Data sharing and monetisation](../../use-cases/usecase-data-monetisation.md) (requires, level 3) · [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (requires, level 2) · [Operational reporting](../../use-cases/usecase-operational-reporting.md) (requires, level 2) · [Self-service BI](../../use-cases/usecase-self-service-bi.md) (requires, level 3) · [Sensitive data protection](../../use-cases/usecase-sensitive-data-protection.md) (requires, level 2)
- **Patterns:** [Data marts](../../patterns/data-marts.md)
- **Personas:** [Business user](../../personas/persona-business-user.md) · [Data analyst](../../personas/persona-data-analyst.md) · [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Security and access control](../../maturity/track-security.md) (from level 3, Defined)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 11 – Distribution · [GDPR](../../frameworks/framework-gdpr.md): Article 18 – Right to restriction of processing

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Lake Formation data filters; Redshift RLS policies | [Amazon Redshift row-level security and dynamic data masking](../../technologies/aws/aws-redshift-fine-grained-security.md), [AWS Lake Formation](../../technologies/aws/aws-lake-formation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [OneLake security](../../technologies/microsoft/fabric-onelake-security.md), [Power BI semantic models](../../technologies/microsoft/powerbi-semantic-models.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery row-level security](../../technologies/google-cloud/gcp-bigquery-row-level-security.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | row access policies | [Snowflake row access policies](../../technologies/snowflake/snowflake-row-access-policies.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Lakeguard](../../technologies/databricks/databricks-lakeguard.md), [Unity Catalog attribute-based access control (ABAC)](../../technologies/databricks/databricks-abac.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | Row policies | [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../../technologies/clickhouse/clickhouse-access-control.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Cloud Data Access Management (CDAM)](../../technologies/informatica/informatica-cloud-data-access-management.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Shared Data Experience (SDX)](../../technologies/cloudera/cloudera-sdx.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Database security features](../../technologies/oracle/oracle-database-security.md) |
| [SAP](../../platforms/platform-sap.md) | Data access controls | [SAP Datasphere](../../technologies/sap/sap-datasphere.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Database security (roles, row-level security, encryption)](../../technologies/teradata/teradata-security.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Foundry security controls](../../technologies/palantir/palantir-security-controls.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Ranger](../../technologies/open-source/apache-ranger.md), [PostgreSQL](../../technologies/open-source/postgresql.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Collibra Data Access](../../technologies/independent/collibra-data-access.md), [Immuta Data Authorization Platform](../../technologies/independent/immuta-data-authorization-platform.md) |
