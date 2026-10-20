---
type: Technology
id: databricks-lakeguard
title: Lakeguard
description: Isolation technology that sandboxes each user's code and UDFs away from the Spark engine and from other users, so shared compute can enforce Unity Catalog row filters and column masks.
platform: platform-databricks
kind: feature
availability: ga
realises: [compute-user-isolation, row-level-security, column-masking]
resource: https://docs.databricks.com/aws/en/compute/lakeguard
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Lakeguard underpins standard access mode, serverless compute and SQL warehouses and is built on Spark Connect. Dedicated clusters hand fine-grained filtering off to serverless compute.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Shared compute isolation](../../capabilities/security/compute-user-isolation.md) (Security and access) (primary): Sandbox each user's code on shared compute so nobody can bypass access controls or affect other users.
- [Row-level security](../../capabilities/security/row-level-security.md) (Security and access): Restrict which rows each user sees based on who they are.
- [Column security and dynamic masking](../../capabilities/security/column-masking.md) (Security and access): Hide or mask sensitive columns depending on who is querying.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Databricks compute

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift row-level security and dynamic data masking](../aws/aws-redshift-fine-grained-security.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake security](../microsoft/fabric-onelake-security.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database security features](../oracle/oracle-database-security.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku DSS](../dataiku/dataiku.md) | [Shared compute isolation](../../capabilities/security/compute-user-isolation.md) |
