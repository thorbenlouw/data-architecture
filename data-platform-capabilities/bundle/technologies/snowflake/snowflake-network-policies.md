---
type: Technology
id: snowflake-network-policies
title: Snowflake network policies and network rules
description: Restrict which IP ranges, VPC endpoints or private endpoints can reach an account or user, and which external destinations workloads can reach.
platform: platform-snowflake
kind: feature
availability: ga
realises: [network-security]
resource: https://docs.snowflake.com/en/user-guide/network-policies
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Network security](../../capabilities/security/network-security.md) (Security and access) (primary): Keep data traffic on private networks and restrict where the platform can be reached from.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS PrivateLink](../aws/aws-privatelink.md) | [Network security](../../capabilities/security/network-security.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Private Link](../microsoft/azure-private-link.md), [Private links for Microsoft Fabric](../microsoft/fabric-private-links.md), [Fabric workspace outbound access protection](../microsoft/fabric-outbound-access-protection.md) | [Network security](../../capabilities/security/network-security.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [VPC Service Controls](../google-cloud/gcp-vpc-service-controls.md), [Google Cloud Agent Gateway](../google-cloud/gcp-agent-gateway.md) | [Network security](../../capabilities/security/network-security.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Private Link for Databricks](../databricks/databricks-private-link.md), [Databricks serverless egress control](../databricks/databricks-serverless-egress-control.md) | [Network security](../../capabilities/security/network-security.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud private networking (AWS PrivateLink, GCP Private Service Connect, Azure Private Link)](../clickhouse/clickhouse-private-link.md), [ClickHouse BYOC (Bring Your Own Cloud)](../clickhouse/clickhouse-byoc.md) | [Network security](../../capabilities/security/network-security.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../oracle/oracle-database-multicloud.md) | [Network security](../../capabilities/security/network-security.md) |
