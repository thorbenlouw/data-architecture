---
type: Technology
id: gcp-assured-workloads
title: Assured Workloads
description: Applies controls for data location, personnel access and supported services to folders so workloads meet regulatory regimes such as FedRAMP, CJIS and EU sovereignty requirements.
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [data-residency, compliance-evidence, configuration-guardrails]
resource: https://docs.cloud.google.com/assured-workloads/docs/overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

BigQuery Enterprise Plus is required for Assured Workloads controls in BigQuery. Google Distributed Cloud air-gapped is the option where a fully disconnected deployment is needed.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data residency and sovereignty](../../capabilities/governance/data-residency.md) (Governance and compliance) (primary): Keep data and its processing in approved jurisdictions and prove that you have.
- [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) (Governance and compliance): Map regulatory requirements to platform controls and produce evidence for auditors.
- [Resource configuration guardrails](../../capabilities/platform-operations/configuration-guardrails.md) (Platform operations): Restrict which platform resources can be created and how they are configured, such as allowed sizes, regions, tags and network settings, and report anything that breaks the rules.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Outposts](../aws/aws-outposts.md), [AWS Config](../aws/aws-config.md) | [Data residency and sovereignty](../../capabilities/governance/data-residency.md), [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md), [Resource configuration guardrails](../../capabilities/platform-operations/configuration-guardrails.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Policy](../microsoft/azure-policy.md) | [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md), [Data residency and sovereignty](../../capabilities/governance/data-residency.md), [Resource configuration guardrails](../../capabilities/platform-operations/configuration-guardrails.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks compliance security profile](../databricks/databricks-compliance-security-profile.md) | [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md), [Data residency and sovereignty](../../capabilities/governance/data-residency.md), [Resource configuration guardrails](../../capabilities/platform-operations/configuration-guardrails.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse BYOC (Bring Your Own Cloud)](../clickhouse/clickhouse-byoc.md) | [Data residency and sovereignty](../../capabilities/governance/data-residency.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Intelligent Data Management Cloud (IDMC)](../informatica/informatica-idmc.md) | [Data residency and sovereignty](../../capabilities/governance/data-residency.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Skyflow Data Privacy Vault](../independent/skyflow-data-privacy-vault.md) | [Data residency and sovereignty](../../capabilities/governance/data-residency.md) |
