---
type: Technology
id: fabric-private-links
title: Private links for Microsoft Fabric
description: Restricts inbound access to a Fabric tenant or to individual workspaces through Azure Private Link, with managed virtual networks for Spark.
platform: platform-microsoft
kind: feature
availability: ga
realises: [network-security]
resource: https://learn.microsoft.com/en-us/fabric/security/security-private-links-overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Tenant-level private link affects the whole tenant and disables some features; workspace-level private links are more granular, but item support varies (Power BI is excluded). Managed private endpoints give Spark private access to Azure sources.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Network security](../../capabilities/security/network-security.md) (Security and access) (primary): Keep data traffic on private networks and restrict where the platform can be reached from.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS PrivateLink](../aws/aws-privatelink.md) | [Network security](../../capabilities/security/network-security.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [VPC Service Controls](../google-cloud/gcp-vpc-service-controls.md), [Google Cloud Agent Gateway](../google-cloud/gcp-agent-gateway.md) | [Network security](../../capabilities/security/network-security.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake network policies and network rules](../snowflake/snowflake-network-policies.md), [Snowflake private connectivity (AWS PrivateLink, Azure Private Link, Google Cloud Private Service Connect)](../snowflake/snowflake-private-connectivity.md) | [Network security](../../capabilities/security/network-security.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Private Link for Databricks](../databricks/databricks-private-link.md), [Databricks serverless egress control](../databricks/databricks-serverless-egress-control.md) | [Network security](../../capabilities/security/network-security.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud private networking (AWS PrivateLink, GCP Private Service Connect, Azure Private Link)](../clickhouse/clickhouse-private-link.md), [ClickHouse BYOC (Bring Your Own Cloud)](../clickhouse/clickhouse-byoc.md) | [Network security](../../capabilities/security/network-security.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../oracle/oracle-database-multicloud.md) | [Network security](../../capabilities/security/network-security.md) |
