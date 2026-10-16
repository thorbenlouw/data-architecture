---
type: Technology
id: fabric-onelake-security
title: OneLake security
description: Role-based access rules defined once on OneLake data, down to table, folder, row and column, and enforced across Fabric engines.
formerly: [OneLake data access roles]
platform: platform-microsoft
kind: feature
availability: ga
realises: [access-control, role-based-access, row-level-security, column-masking]
resource: https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/OneLake-security-Generally-Available/ba-p/5176756
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Became GA in May 2026. Enforced in Spark, Power BI (Direct Lake), data agents and Excel among others; column security hides columns rather than masking values. Check per-engine support before relying on it as the single enforcement point.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Access control](../../capabilities/security/access-control.md) (Security and access) (primary): Decide who can see and change which data, at every level from account down to individual values.
- [Role-based access control](../../capabilities/security/role-based-access.md) (Security and access): Grant permissions to roles and assign roles to people and groups.
- [Row-level security](../../capabilities/security/row-level-security.md) (Security and access): Restrict which rows each user sees based on who they are.
- [Column security and dynamic masking](../../capabilities/security/column-masking.md) (Security and access): Hide or mask sensitive columns depending on who is querying.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** OneLake

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Lake Formation](../aws/aws-lake-formation.md), [Amazon Redshift row-level security and dynamic data masking](../aws/aws-redshift-fine-grained-security.md), [Amazon S3](../aws/aws-s3.md) | [Access control](../../capabilities/security/access-control.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeguard](../databricks/databricks-lakeguard.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../clickhouse/clickhouse-access-control.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Shared Data Experience (SDX)](../cloudera/cloudera-sdx.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry security controls](../palantir/palantir-security-controls.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Ranger](../open-source/apache-ranger.md), [Unity Catalog (open source)](../open-source/unity-catalog.md), [Apache Gravitino](../open-source/apache-gravitino.md) | [Access control](../../capabilities/security/access-control.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
