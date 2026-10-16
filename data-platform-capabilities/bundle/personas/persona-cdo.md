---
type: Persona
id: persona-cdo
title: Chief data officer
description: Accountable for the organisation's data strategy, value, risk and governance.
cares_about:
- governance-metrics
- data-ownership
- data-domains
- ai-governance
- compliance-evidence
- cost-attribution
- data-quality-scorecards
- critical-data-elements
- data-policy-management
- privacy-management
- metric-definitions
- data-catalogue
- data-classification
- ai-system-discovery
- data-usage-rights
- data-certification
- cost-management
- ai-spend-controls
- external-data-sharing
- data-product-specification
patterns: [data-mesh, data-fabric, shift-left]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Most chief data officers report to the chief executive, chief operating officer or chief financial officer, and many now hold analytics and AI as well as data management. They own the data strategy, chair the governance council and often control the budget for the central platform and data teams. They rarely use the platform themselves. What they know about it comes through scorecards, steering committees, audit findings and conversations with business heads.

Success shows up in a few places: business outcomes that can be credited to data and AI work, audit and regulatory findings closed rather than repeated, platform spend that tracks value, and data that people trust enough to stop keeping private spreadsheets. Their tenure is often short, so they need visible results within the first year or two.

# Goals

- Show measurable business value from data and AI investment, use case by use case.
- Keep regulatory, privacy and AI risk within appetite, with evidence ready for the board and supervisors.
- Get named owners and stewards in place for the data that matters most.
- Bring platform cost into line with the value it supports.
- Make governed AI adoption fast enough that business units do not build around the central team.

# Jobs

- Set and refresh the data and AI strategy and the roadmap of priority use cases.
- Chair the governance council and approve policies, domains and owners.
- Review governance coverage, data quality and cost scorecards monthly or quarterly.
- Sponsor large programmes such as platform modernisation, master data or AI rollout, and decide trade-offs between them.
- Report to the board, audit committee and regulators on data risk, incidents and AI use.
- Approve the risk classification of high-impact AI systems in the AI inventory.

# Pain points

- Value is hard to attribute, because dashboards and models rarely carry a clear link to revenue earned or cost saved.
- Governance is seen as a brake, and ownership and stewardship fade after the launch.
- Platform spend grows faster than anyone can explain, and chargeback disputes take up steering time.
- Shadow AI tools and spreadsheet reporting appear faster than policies can be written.
- Audit evidence is assembled by hand each time, from many teams.

# Questions they ask

- Which capabilities do our top five use cases need, and which do we already have at the right maturity?
- How do we measure governance coverage across the estate in a way the board will accept?
- Where are we exposed under GDPR, the EU AI Act or sector rules, and what would close the gap?
- Should we centralise, federate or adopt data mesh, and what does each cost in people and tooling?
- How do we stop AI projects going around governance without slowing them down?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities they rely on most

| Capability | Domain | What it does |
|---|---|---|
| [Governance coverage metrics](../capabilities/governance/governance-metrics.md) | [Governance and compliance](../capabilities/governance/governance.md) | Measure how much of the estate is owned, described, classified, monitored and access-controlled, and track improvement. |
| [Ownership and stewardship](../capabilities/governance/data-ownership.md) | [Governance and compliance](../capabilities/governance/governance.md) | Assign accountable owners and stewards to data and record their responsibilities. |
| [Data domains](../capabilities/governance/data-domains.md) | [Governance and compliance](../capabilities/governance/governance.md) | Group data assets, products and owners into business domains with their own stewardship and policies. |
| [AI governance](../capabilities/governance/ai-governance.md) | [Governance and compliance](../capabilities/governance/governance.md) | Inventory AI systems and govern their risk, approval, documentation and use in line with regulation. |
| [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) | [Governance and compliance](../capabilities/governance/governance.md) | Map regulatory requirements to platform controls and produce evidence for auditors. |
| [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Attribute spend to teams, products and workloads using tags and usage data. |
| [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | Track quality results over time and report them by dataset, domain and quality dimension. |
| [Critical data elements](../capabilities/governance/critical-data-elements.md) | [Governance and compliance](../capabilities/governance/governance.md) | Identify the data items that matter most for regulatory, risk and financial reporting and apply stricter controls to them. |
| [Policy management](../capabilities/governance/data-policy-management.md) | [Governance and compliance](../capabilities/governance/governance.md) | Define data policies centrally and apply them consistently across platforms and tools. |
| [Privacy management](../capabilities/governance/privacy-management.md) | [Governance and compliance](../capabilities/governance/governance.md) | Meet privacy obligations such as purpose limitation, consent and individuals' rights over their data. |
| [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Define, certify and version key business metrics with owners and calculation logic. |
| [Data catalogue](../capabilities/metadata/data-catalogue.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Provide a searchable inventory of data assets with descriptions, owners, quality and usage. |
| [Data classification](../capabilities/governance/data-classification.md) | [Governance and compliance](../capabilities/governance/governance.md) | Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically. |
| [AI system discovery](../capabilities/governance/ai-system-discovery.md) | [Governance and compliance](../capabilities/governance/governance.md) | Find the AI models, agents and services in use, including unapproved ones, to build and maintain the AI inventory. |
| [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md) | [Governance and compliance](../capabilities/governance/governance.md) | Record licence terms and permitted uses of datasets and check use against them, including for model training. |
| [Data certification](../capabilities/metadata/data-certification.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Mark assets as trusted, deprecated or under review so consumers know what to rely on. |
| [Cost management](../capabilities/platform-operations/cost-management.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Understand, allocate and control what the platform costs. |
| [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Limit, prioritise and attribute model and agent consumption per user, team or application. |
| [External data sharing](../capabilities/data-sharing/external-data-sharing.md) | [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md) | Share live data with customers, partners and suppliers under agreed terms. |
| [Data product specification](../capabilities/data-products/data-product-specification.md) | [Data products](../capabilities/data-products/data-products.md) | Describe a data product's purpose, outputs, owners and terms of use in a standard, machine-readable form. |

# Patterns

- [Data mesh](../patterns/data-mesh.md)
- [Data fabric](../patterns/data-fabric.md)
- [Shift-left data quality and governance](../patterns/shift-left.md)

# Use cases they take part in

- [Data sharing and monetisation](../use-cases/usecase-data-monetisation.md): Share or sell data products to partners and customers under agreed terms.
- [Enterprise management reporting](../use-cases/usecase-enterprise-reporting.md): Produce trusted, consistent KPIs and management reports across the organisation.
- [Legacy warehouse migration](../use-cases/usecase-platform-modernisation.md): Move from an on-premises warehouse or Hadoop estate to a cloud data platform.
- [Platform cost management and chargeback](../use-cases/usecase-platform-cost-management.md): Attribute, forecast and control what the data platform costs, and recover it from the teams and products that use it.
- [Regulatory reporting](../use-cases/usecase-regulatory-reporting.md): Produce accurate, auditable and reproducible submissions to regulators.

# Frameworks they work with

- [BCBS 239](../frameworks/framework-bcbs-239.md): Fourteen principles for how banks aggregate risk data and produce risk reports, in normal times and under stress.
- [CDMC (Cloud Data Management Capabilities)](../frameworks/framework-edm-cdmc.md): A framework of fourteen key controls for managing sensitive data in cloud and hybrid environments, with certification for cloud platforms and tools.
- [DAMA-DMBOK 2](../frameworks/framework-dama-dmbok.md): The Data Management Body of Knowledge, a reference guide that splits data management into knowledge areas around a central governance function.
- [DCAM v3](../frameworks/framework-edm-dcam.md): The Data Management Capability Assessment Model, an evidence-based framework for scoring how mature an organisation's data management programme is.
- [EU AI Act](../frameworks/framework-eu-ai-act.md): Regulation (EU) 2024/1689, which sets risk-based rules for placing AI systems and general-purpose AI models on the EU market and using them.
- [ISO 8000 (data quality)](../frameworks/framework-iso-8000.md): A series of international standards on data quality, covering concepts, quality management processes, profiling, rules, master data exchange and sensor data.
- [ISO/IEC 42001:2023](../frameworks/framework-iso-iec-42001.md): The international standard for an AI management system, setting requirements for governing AI responsibly within an organisation.
