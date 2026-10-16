---
type: Technology
id: databricks-private-link
title: Private Link for Databricks
description: AWS PrivateLink, Azure Private Link and Private Service Connect connectivity for front-end access, classic compute to the control plane, and inbound access to serverless services such as Lakebase and Zerobus Ingest.
platform: platform-databricks
kind: feature
availability: ga
realises: [network-security]
resource: https://docs.databricks.com/aws/en/security/network/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Inbound Private Link for performance-intensive services became GA in June 2026. Context-based ingress policies (GA October 2026) and IP access lists restrict where workspaces can be reached from. A private network gateway is in Private Preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Network security](../../capabilities/security/network-security.md) (Security and access) (primary): Keep data traffic on private networks and restrict where the platform can be reached from.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS PrivateLink](../aws/aws-privatelink.md) | [Network security](../../capabilities/security/network-security.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Private Link](../microsoft/azure-private-link.md), [Private links for Microsoft Fabric](../microsoft/fabric-private-links.md), [Fabric workspace outbound access protection](../microsoft/fabric-outbound-access-protection.md) | [Network security](../../capabilities/security/network-security.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [VPC Service Controls](../google-cloud/gcp-vpc-service-controls.md), [Google Cloud Agent Gateway](../google-cloud/gcp-agent-gateway.md) | [Network security](../../capabilities/security/network-security.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake network policies and network rules](../snowflake/snowflake-network-policies.md), [Snowflake private connectivity (AWS PrivateLink, Azure Private Link, Google Cloud Private Service Connect)](../snowflake/snowflake-private-connectivity.md) | [Network security](../../capabilities/security/network-security.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud private networking (AWS PrivateLink, GCP Private Service Connect, Azure Private Link)](../clickhouse/clickhouse-private-link.md), [ClickHouse BYOC (Bring Your Own Cloud)](../clickhouse/clickhouse-byoc.md) | [Network security](../../capabilities/security/network-security.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../oracle/oracle-database-multicloud.md) | [Network security](../../capabilities/security/network-security.md) |
