---
type: Capability
id: governance-metrics
title: Governance coverage metrics
description: Measure how much of the estate is owned, described, classified, monitored and access-controlled, and track improvement.
aliases: [governance health]
broader: [governance]
related: [usage-metadata, data-quality-scorecards, data-catalogue, system-telemetry, compliance-evidence]
depends_on: [data-catalogue]
tags: [governance]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Governance coverage metrics count how much of the data estate meets basic governance expectations: the share of assets with an owner, a description and a classification, covered by quality checks or monitoring, protected by policies rather than direct grants, and linked into lineage. They are calculated from catalogue, policy and monitoring metadata, broken down by domain, platform and sensitivity, and tracked over time. For example, a report might show that 92% of finance tables have an owner but only 40% of their personal-data columns have a masking policy.

Metrics turn governance from intentions into a programme with measurable progress. They show where to focus, let domains compare themselves and give leaders evidence that investment works. They are most useful weighted by importance: coverage of sensitive, heavily used or critical assets matters more than coverage of abandoned scratch tables. Data quality scorecards measure the data itself and compliance evidence proves specific controls operated; coverage metrics measure how widely governance practices are applied.

# Key considerations

- Compute metrics automatically from system metadata. Manually reported figures go out of date and are easy to game.
- Weight by usage and sensitivity, and exclude or report separately temporary and abandoned assets.
- Pick a few metrics tied to actions, such as orphaned assets to reassign, rather than a long list nobody acts on.
- Watch for box-ticking: a one-word description counts as documented. Sample quality as well as presence.

# Questions to ask

- Which governance outcomes does leadership want to see improve, and how are they measured today?
- Can coverage be calculated automatically from catalogue and policy metadata?
- Which domains or platforms are behind, and why?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Governance and compliance](governance.md) |
| Broader | [Governance and compliance](governance.md) |
| Related | [Compliance controls and evidence](compliance-evidence.md), [Data catalogue](../metadata/data-catalogue.md), [Data quality scorecards](../data-quality/data-quality-scorecards.md), [Data security posture management](../security/data-security-posture.md), [Usage and popularity metadata](../metadata/usage-metadata.md), [Usage and system telemetry](../platform-operations/system-telemetry.md) |
| Depends on | [Data catalogue](../metadata/data-catalogue.md) |

# Where it appears

- **Use cases:** [Sensitive data protection](../../use-cases/usecase-sensitive-data-protection.md) (benefits from)
- **Personas:** [Chief data officer](../../personas/persona-cdo.md) · [Data steward](../../personas/persona-data-steward.md) · [Risk and compliance officer](../../personas/persona-risk-compliance.md)
- **Maturity tracks:** [Governance operating model](../../maturity/track-governance.md) (from level 4, Measured)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 1 – Governance; Principle 13 – Remedial actions and supervisory measures · [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 1 Data Control Compliance (Governance and accountability); 2 Ownership Field (Governance and accountability) · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Governance · [Data mesh principles](../../frameworks/framework-data-mesh.md): Federated computational governance · [DCAM v3](../../frameworks/framework-edm-dcam.md): 1 Data Strategy, DMS & Business Case; 2 Data Management Program & Funding; 6 Govern Data & DMP · [ISO 8000 (data quality)](../../frameworks/framework-iso-8000.md): ISO 8000-62 to 8000-65 – Process maturity assessment and measurement · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Clause 9 – Performance evaluation

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Purview Unified Catalog](../../technologies/microsoft/purview-unified-catalog.md), [OneLake catalog](../../technologies/microsoft/fabric-onelake-catalog.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Governance Hub](../../technologies/databricks/databricks-governance-hub.md) (preview) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [OpenMetadata](../../technologies/open-source/openmetadata.md) |
