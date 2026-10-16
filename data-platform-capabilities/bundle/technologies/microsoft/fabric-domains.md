---
type: Technology
id: fabric-domains
title: Fabric domains
description: Group workspaces by business area, with subdomains, domain admins and delegated settings, to support data mesh operating models.
platform: platform-microsoft
kind: feature
availability: ga
realises: [data-domains, data-ownership]
resource: https://learn.microsoft.com/en-us/fabric/governance/domains
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Domains do not change access; they drive discovery filters and some delegated settings such as default sensitivity labels and certification.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data domains](../../capabilities/governance/data-domains.md) (Governance and compliance) (primary): Group data assets, products and owners into business domains with their own stewardship and policies.
- [Ownership and stewardship](../../capabilities/governance/data-ownership.md) (Governance and compliance): Assign accountable owners and stewards to data and record their responsibilities.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [Data domains](../../capabilities/governance/data-domains.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Discover](../databricks/databricks-discover.md) | [Data domains](../../capabilities/governance/data-domains.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [DataHub](../open-source/datahub.md), [OpenMetadata](../open-source/openmetadata.md) | [Data domains](../../capabilities/governance/data-domains.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Governance](../independent/collibra-data-governance.md), [DataHub Cloud](../independent/datahub-cloud.md), [Atlan](../independent/atlan.md) | [Data domains](../../capabilities/governance/data-domains.md), [Ownership and stewardship](../../capabilities/governance/data-ownership.md) |
