---
type: Technology
id: fabric-workspace-identity
title: Fabric workspace identity
description: A Microsoft Entra identity managed by Fabric for a workspace, used to authenticate to ADLS, Event Hubs and other sources without stored secrets.
platform: platform-microsoft
kind: feature
availability: ga
realises: [identity-authentication]
resource: https://learn.microsoft.com/en-us/fabric/security/workspace-identity
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Identity and authentication](../../capabilities/security/identity-authentication.md) (Security and access) (primary): Authenticate people and services through central identity, single sign-on and short-lived credentials.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS IAM Identity Center](../aws/aws-iam-identity-center.md), [AWS Identity and Access Management](../aws/aws-iam.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Identity and Access Management](../google-cloud/gcp-iam.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake authentication (SSO, OAuth, key pair, PATs, workload identity federation)](../snowflake/snowflake-authentication.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks automatic identity management](../databricks/databricks-automatic-identity-management.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud](../clickhouse/clickhouse-cloud.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md) |
| [Informatica](../../platforms/platform-informatica.md) | [IDMC Administrator](../informatica/informatica-administrator.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Viya security controls](../sas/sas-viya-security.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Keycloak](../open-source/keycloak.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md) |
