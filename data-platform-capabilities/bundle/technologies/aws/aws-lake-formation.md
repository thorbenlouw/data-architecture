---
type: Technology
id: aws-lake-formation
title: AWS Lake Formation
description: Permission layer over the Glue Data Catalog that grants database, table, column, row and cell access and shares data across accounts.
aliases: [LF-Tags]
platform: platform-aws
kind: managed-service
availability: ga
realises:
- access-control
- attribute-based-access
- row-level-security
- column-masking
- internal-data-sharing
- credential-vending
resource: https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

LF-Tags provide tag-based access control and data filters provide row and cell security; it hides columns rather than applying dynamic masks. Enforced by Athena, Redshift Spectrum, EMR and Glue. Hybrid access mode allows a gradual move from IAM-only policies. Access is logged in CloudTrail.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Access control](../../capabilities/security/access-control.md) (Security and access) (primary): Decide who can see and change which data, at every level from account down to individual values.
- [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md) (Security and access): Grant or deny access based on attributes of the user and tags on the data.
- [Row-level security](../../capabilities/security/row-level-security.md) (Security and access): Restrict which rows each user sees based on who they are.
- [Column security and dynamic masking](../../capabilities/security/column-masking.md) (Security and access): Hide or mask sensitive columns depending on who is querying.
- [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) (Data sharing and collaboration): Share live data between teams, accounts and workspaces without copying it.
- [Storage credential vending](../../capabilities/storage/credential-vending.md) (Storage and table management): Have the catalogue issue short-lived, table-scoped storage credentials to engines so they never hold broad storage access.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake security](../microsoft/fabric-onelake-security.md) | [Access control](../../capabilities/security/access-control.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog attribute-based access control (ABAC)](../databricks/databricks-abac.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Ranger](../open-source/apache-ranger.md), [Unity Catalog (open source)](../open-source/unity-catalog.md), [Apache Gravitino](../open-source/apache-gravitino.md) | [Access control](../../capabilities/security/access-control.md), [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
