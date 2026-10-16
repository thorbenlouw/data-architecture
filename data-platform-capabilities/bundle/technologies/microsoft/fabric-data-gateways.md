---
type: Technology
id: fabric-data-gateways
title: Microsoft on-premises and virtual network data gateways
description: Gateways that let Fabric and Power BI reach data sources inside private or on-premises networks without opening them to the internet.
aliases: [on-premises data gateway, virtual network data gateway, VNet data gateway]
platform: platform-microsoft
kind: software
availability: ga
realises: [network-security, hybrid-data-plane]
resource: https://learn.microsoft.com/en-us/data-integration/gateway/service-gateway-onprem
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The on-premises gateway is software you install and patch; the virtual network gateway is managed by Microsoft and injected into your Azure VNet. Shared across Power BI, Power Platform and Fabric.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Network security](../../capabilities/security/network-security.md) (Security and access) (primary): Keep data traffic on private networks and restrict where the platform can be reached from.
- [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) (Platform operations): Run processing inside your own network or cloud account while the vendor operates the control plane as a service.

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
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud private networking (AWS PrivateLink, GCP Private Service Connect, Azure Private Link)](../clickhouse/clickhouse-private-link.md), [ClickHouse BYOC (Bring Your Own Cloud)](../clickhouse/clickhouse-byoc.md) | [Network security](../../capabilities/security/network-security.md), [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../oracle/oracle-database-multicloud.md) | [Network security](../../capabilities/security/network-security.md) |
