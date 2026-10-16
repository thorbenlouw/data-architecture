---
type: Capability
id: credential-vending
title: Storage credential vending
description: Have the catalogue issue short-lived, table-scoped storage credentials to engines so they never hold broad storage access.
aliases: [vended credentials]
broader: [table-catalogue, access-control]
related: [audit-logging, engine-interoperability, row-level-security, external-data-sharing, object-storage]
depends_on: [identity-authentication]
tags: [storage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Instead of giving each engine a long-lived key that opens a whole bucket, the engine asks the catalogue for a table. The catalogue checks the user's permissions and returns, with the table metadata, a temporary storage credential limited to that table's files, typically valid for an hour or less and read-only if the user may only read. The engine then reads or writes the files directly with it. The Iceberg REST catalogue specification defines how such credentials are returned; cloud token services issue the scoped tokens underneath.

Without vending, every engine and user needs broad storage permissions, so anyone can bypass the catalogue's table-level grants by reading files directly. Vending makes the catalogue the single gate to the data and lets third-party engines take part without being trusted with whole buckets. It does not replace finer controls. A vended credential grants access to files, so row filters and column masks still need an engine that enforces them.

# Key considerations

- Vended credentials cover files, not rows or columns. Tables with row filters or masks need a trusted engine or a separate serving path.
- Remove standing storage permissions once vending is in place, or the old path remains a way round the catalogue.
- Long-running jobs must renew credentials. Check that engines refresh tokens before they expire mid-query.
- Log every credential issued, with user, engine and table, so storage access can be traced back to a person.

# Questions to ask

- Which engines and users hold direct storage permissions today?
- Will engines outside your control, such as partners' or vendors', need to read tables?
- Do any tables carry row or column policies that file-level access would bypass?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Storage and table management](storage.md) |
| Broader | [Table catalogue](table-catalogue.md), [Access control](../security/access-control.md) |
| Related | [Audit logging](../security/audit-logging.md), [External data sharing](../data-sharing/external-data-sharing.md), [Identity and authentication](../security/identity-authentication.md), [Multi-engine interoperability](../compute/engine-interoperability.md), [Object storage](object-storage.md), [Open-protocol sharing](../data-sharing/open-protocol-sharing.md), [Row-level security](../security/row-level-security.md), [Secrets management](../security/secrets-management.md), [Shared compute isolation](../security/compute-user-isolation.md), [Single-node processing](../processing/single-node-processing.md) |
| Depends on | [Identity and authentication](../security/identity-authentication.md) |

# Where it appears

- **Use cases:** [Sensitive data protection](../../use-cases/usecase-sensitive-data-protection.md) (benefits from)
- **Patterns:** [Lakehouse](../../patterns/lakehouse.md)
- **Personas:** [Data platform engineer](../../personas/persona-platform-engineer.md)
- **Maturity tracks:** [Security and access control](../../maturity/track-security.md) (from level 3, Defined) · [Storage and table management](../../maturity/track-storage.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Glue Data Catalog](../../technologies/aws/aws-glue-data-catalog.md), [AWS Lake Formation](../../technologies/aws/aws-lake-formation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Lakehouse runtime catalog](../../technologies/google-cloud/gcp-lakehouse-runtime-catalog.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Horizon Iceberg REST Catalog API](../../technologies/snowflake/snowflake-horizon-iceberg-rest-catalog.md), [Snowflake Open Catalog](../../technologies/snowflake/snowflake-open-catalog.md) (deprecated) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Unity Catalog Iceberg REST Catalog API](../../technologies/databricks/databricks-iceberg-rest-catalog.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Iceberg REST Catalog](../../technologies/cloudera/cloudera-iceberg-rest-catalog.md) |
| [SAP](../../platforms/platform-sap.md) |  | [Dremio Cloud](../../technologies/sap/dremio-cloud.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Gravitino](../../technologies/open-source/apache-gravitino.md), [Apache Polaris](../../technologies/open-source/apache-polaris.md), [Iceberg REST Catalog specification](../../technologies/open-source/apache-iceberg-rest-catalog-spec.md), [Unity Catalog (open source)](../../technologies/open-source/unity-catalog.md) |
