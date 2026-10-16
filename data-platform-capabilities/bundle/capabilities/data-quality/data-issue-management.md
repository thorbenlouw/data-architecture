---
type: Capability
id: data-issue-management
title: Data issue management
description: Log, assign, track and resolve data quality incidents with their owners.
aliases: [DQ incident management]
broader: [data-quality]
related: [data-observability, impact-analysis, ai-incident-management, data-certification, active-metadata]
depends_on: [data-ownership]
tags: [data-quality]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

An issue is raised from a failed check, an observability alert or a consumer's report, and records the affected assets, severity, owner, status and timeline. The tool assigns it to the data owner or steward, links it to downstream assets found through lineage, notifies affected consumers, and keeps notes on cause and fix. A recurring problem, such as a source sending duplicate customers at every month end, shows up as a pattern rather than a series of one-off fixes.

It matters once several teams produce and consume data and nobody is sure who should fix a problem or whether it is already known. It gives accountability, response times and evidence for governance bodies and regulators. Approaches range from data-specific incident tools to integration with general IT service management. Observability detects problems; issue management covers the human process of triage, resolution and follow-up on root causes.

# Key considerations

- Route issues automatically to the owners recorded in the catalogue. Manual triage becomes a bottleneck.
- Group alerts with one root cause into one incident, or responders drown in duplicates.
- Show open issues on affected assets in the catalogue and BI tools, so consumers know before they use the data.
- Record root causes in a consistent set of categories, so recurring sources of problems can be fixed and reported.

# Questions to ask

- When a consumer finds wrong data, whom do they tell, and how do they know it is being fixed?
- Must data incidents be reported to governance bodies or regulators?
- Should data issues live in the existing IT service management tool or a separate one?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data quality and observability](data-quality.md) |
| Broader | [Data quality and observability](data-quality.md) |
| Related | [Active metadata](../metadata/active-metadata.md), [AI incident management](../governance/ai-incident-management.md), [Bad-data quarantine](bad-data-quarantine.md), [Data anomaly detection](data-anomaly-detection.md), [Data certification](../metadata/data-certification.md), [Data observability](data-observability.md), [Data service levels](../data-products/data-slas.md), [Data trust indicators](../metadata/data-trust-indicators.md), [Impact analysis](../metadata/impact-analysis.md), [Master data management](../master-data/master-data-management.md), [Ownership and stewardship](../governance/data-ownership.md), [Pipeline monitoring and alerting](../platform-operations/pipeline-monitoring.md), [Platform incident management](../platform-operations/platform-incident-management.md), [Stewardship workflows](../governance/stewardship-workflows.md) |
| Depends on | [Ownership and stewardship](../governance/data-ownership.md) |

# Where it appears

- **Use cases:** [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (requires, level 3)
- **Personas:** [Data analyst](../../personas/persona-data-analyst.md) · [Data steward](../../personas/persona-data-steward.md) · [Risk and compliance officer](../../personas/persona-risk-compliance.md)
- **Maturity tracks:** [Data quality and observability](../../maturity/track-data-quality.md) (from level 2, Managed)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 7 – Accuracy (reporting); Principle 13 – Remedial actions and supervisory measures · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Quality · [DCAM v3](../../frameworks/framework-edm-dcam.md): 5 Data Quality Management; 7 Data Management Operations, Risk & Control · [ISO 8000 (data quality)](../../frameworks/framework-iso-8000.md): ISO 8000-61 – Data quality management process reference model · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Service-Level Agreement

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Purview Data Quality](../../technologies/microsoft/purview-data-quality.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks data quality monitoring anomaly detection](../../technologies/databricks/databricks-dqm-anomaly-detection.md) (preview) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Collibra Data Governance](../../technologies/independent/collibra-data-governance.md), [Monte Carlo Data + AI Observability](../../technologies/independent/monte-carlo-data-observability.md), [Sifflet](../../technologies/independent/sifflet.md), [Soda Cloud](../../technologies/independent/soda-cloud.md) |
