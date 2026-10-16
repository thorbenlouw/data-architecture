---
type: Technology
id: clickhouse-private-link
title: ClickHouse Cloud private networking (AWS PrivateLink, GCP Private Service Connect, Azure Private Link)
description: Connects ClickHouse Cloud services and ClickPipes to customer virtual networks over the cloud providers' private endpoint services, and restricts public access with IP filters.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [network-security]
resource: https://clickhouse.com/docs/cloud/security/private-link-overview
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Scale and Enterprise tiers only. Cross-region AWS PrivateLink became GA in August 2025; ClickPipes supports reverse private endpoints to reach private sources. API keys can also carry IP filters.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Network security](../../capabilities/security/network-security.md) (Security and access) (primary): Keep data traffic on private networks and restrict where the platform can be reached from.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga  
**Product family:** ClickHouse Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS PrivateLink](../aws/aws-privatelink.md) | [Network security](../../capabilities/security/network-security.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Private Link](../microsoft/azure-private-link.md), [Private links for Microsoft Fabric](../microsoft/fabric-private-links.md), [Fabric workspace outbound access protection](../microsoft/fabric-outbound-access-protection.md) | [Network security](../../capabilities/security/network-security.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [VPC Service Controls](../google-cloud/gcp-vpc-service-controls.md), [Google Cloud Agent Gateway](../google-cloud/gcp-agent-gateway.md) | [Network security](../../capabilities/security/network-security.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake network policies and network rules](../snowflake/snowflake-network-policies.md), [Snowflake private connectivity (AWS PrivateLink, Azure Private Link, Google Cloud Private Service Connect)](../snowflake/snowflake-private-connectivity.md) | [Network security](../../capabilities/security/network-security.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Private Link for Databricks](../databricks/databricks-private-link.md), [Databricks serverless egress control](../databricks/databricks-serverless-egress-control.md) | [Network security](../../capabilities/security/network-security.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../oracle/oracle-database-multicloud.md) | [Network security](../../capabilities/security/network-security.md) |
