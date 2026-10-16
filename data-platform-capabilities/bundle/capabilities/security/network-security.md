---
type: Capability
id: network-security
title: Network security
description: Keep data traffic on private networks and restrict where the platform can be reached from.
aliases: [private endpoints, PrivateLink, VPC Service Controls, IP allowlists]
broader: [security]
related: [data-loss-prevention, hybrid-data-plane, infrastructure-as-code, data-residency, ai-gateway]
tags: [security]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Network security controls the paths by which users, tools and services reach the platform, and by which the platform reaches out. Private connectivity keeps traffic between your networks and the platform's endpoints on private links rather than the public internet. IP allow lists and network policies restrict where connections may come from. Egress controls limit which external destinations platform compute, notebooks and functions may call. For example, a bank may allow access only through private endpoints from its corporate network and let pipelines call only a short list of approved APIs.

Network controls add a layer that still holds when credentials are stolen, because an attacker must also be on an approved network path. Outbound control matters as much as inbound: unrestricted egress lets compromised code or careless users send data anywhere. Serverless and managed services complicate this because their compute runs in the provider's network. Network controls complement identity-based controls; they do not replace them.

# Key considerations

- Cover every surface: web interface, SQL endpoints, APIs, storage, and serverless and AI services, which often have separate network settings.
- Restrict outbound traffic from compute to approved destinations, including model APIs and package repositories.
- Private connectivity adds DNS, routing and cost complexity, especially across several clouds and regions. Design it centrally.
- Keep network rules in infrastructure as code and log denied connections, so changes are reviewed and blocked traffic is visible.

# Questions to ask

- Must the platform be unreachable from the public internet?
- Which external services do pipelines, notebooks and agents need to call?
- Do serverless compute and AI features support the same private networking as provisioned compute?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Security and access](security.md) |
| Broader | [Security and access](security.md) |
| Related | [AI gateway](../generative-ai/ai-gateway.md), [AI system discovery](../governance/ai-system-discovery.md), [Container services](../compute/container-services.md), [Cryptographic agility](cryptographic-agility.md), [Customer-hosted data plane](../platform-operations/hybrid-data-plane.md), [Data loss prevention](data-loss-prevention.md), [Data residency and sovereignty](../governance/data-residency.md), [Encryption](encryption.md), [Hybrid and multi-cloud deployment](../platform-operations/deployment-options.md), [Infrastructure as code](../platform-operations/infrastructure-as-code.md), [Managed file transfer](../ingestion-integration/managed-file-transfer.md), [Object storage](../storage/object-storage.md) |
| Needed by | [Customer-hosted data plane](../platform-operations/hybrid-data-plane.md), [Foundation model access](../generative-ai/foundation-model-access.md) |

# Where it appears

- **Use cases:** [IoT predictive maintenance](../../use-cases/usecase-iot-predictive-maintenance.md) (requires, level 3) · [Legacy warehouse migration](../../use-cases/usecase-platform-modernisation.md) (requires, level 2) · [Self-service domain onboarding](../../use-cases/usecase-domain-onboarding.md) (requires, level 3)
- **Personas:** [Data platform engineer](../../personas/persona-platform-engineer.md) · [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Security and access control](../../maturity/track-security.md) (from level 2, Managed)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 9 Appropriate Security Controls (Protection and privacy) · [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Article 9 – Protection and prevention; Chapter IV – Digital operational resilience testing (Articles 24 to 27) · [GDPR](../../frameworks/framework-gdpr.md): Article 5(1)(f) – Integrity and confidentiality

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS PrivateLink](../../technologies/aws/aws-privatelink.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Private Link](../../technologies/microsoft/azure-private-link.md), [Fabric workspace outbound access protection](../../technologies/microsoft/fabric-outbound-access-protection.md), [Microsoft on-premises and virtual network data gateways](../../technologies/microsoft/fabric-data-gateways.md), [Private links for Microsoft Fabric](../../technologies/microsoft/fabric-private-links.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Agent Gateway](../../technologies/google-cloud/gcp-agent-gateway.md), [VPC Service Controls](../../technologies/google-cloud/gcp-vpc-service-controls.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake network policies and network rules](../../technologies/snowflake/snowflake-network-policies.md), [Snowflake private connectivity (AWS PrivateLink, Azure Private Link, Google Cloud Private Service Connect)](../../technologies/snowflake/snowflake-private-connectivity.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks serverless egress control](../../technologies/databricks/databricks-serverless-egress-control.md), [Private Link for Databricks](../../technologies/databricks/databricks-private-link.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse BYOC (Bring Your Own Cloud)](../../technologies/clickhouse/clickhouse-byoc.md), [ClickHouse Cloud private networking (AWS PrivateLink, GCP Private Service Connect, Azure Private Link)](../../technologies/clickhouse/clickhouse-private-link.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../../technologies/oracle/oracle-database-multicloud.md) |
