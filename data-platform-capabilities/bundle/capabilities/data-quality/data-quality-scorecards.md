---
type: Capability
id: data-quality-scorecards
title: Data quality scorecards
description: Track quality results over time and report them by dataset, domain and quality dimension.
aliases: [DQ dashboards]
broader: [data-quality]
related: [critical-data-elements, governance-metrics, data-certification, data-catalogue, data-slas]
depends_on: [data-quality-rules]
tags: [data-quality]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Each check result is assigned to a quality dimension, such as completeness or validity, and rolls up from columns to datasets, products and domains. A steward might see that the customer domain scores 97% on validity but has fallen from 92% to 81% on completeness this quarter, mostly because one source stopped sending email addresses. Scores are often weighted by the importance of each field or rule.

Scorecards turn individual results into management information: they show trends, compare domains, guide remediation and give evidence to governance committees and regulators. They typically appear in the catalogue next to each asset, in dashboards for stewards, and in reports on critical data elements. A score is only as meaningful as the checks behind it. A high score over a few trivial rules says little, so coverage should be reported alongside it.

# Key considerations

- Report coverage with each score, such as the share of critical fields that have checks, so a high score is not mistaken for good data.
- Weight scores by business impact, or many minor rules will hide one critical failure.
- Keep check results in queryable tables with dataset, rule, dimension and time, so scorecards can be built with ordinary BI tools.
- Show scores where consumers choose data, such as the catalogue, not only in a steward's dashboard.

# Questions to ask

- Who needs to see data quality results, and at what level of detail?
- Are there regulatory requirements to evidence the quality of specific data elements?
- How will scores drive action: targets, reviews or funding?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data quality and observability](data-quality.md) |
| Broader | [Data quality and observability](data-quality.md) |
| Related | [Critical data elements](../governance/critical-data-elements.md), [Data catalogue](../metadata/data-catalogue.md), [Data certification](../metadata/data-certification.md), [Data service levels](../data-products/data-slas.md), [Data trust indicators](../metadata/data-trust-indicators.md), [Governance coverage metrics](../governance/governance-metrics.md), [Master data management](../master-data/master-data-management.md), [Product information management](../master-data/product-information-management.md) |
| Depends on | [Data quality rules](data-quality-rules.md) |

# Where it appears

- **Use cases:** [Customer 360](../../use-cases/usecase-customer-360.md) (benefits from) · [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (benefits from) · [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (benefits from)
- **Personas:** [Chief data officer](../../personas/persona-cdo.md) · [Data product owner](../../personas/persona-data-product-owner.md) · [Data steward](../../personas/persona-data-steward.md) · [Risk and compliance officer](../../personas/persona-risk-compliance.md)
- **Maturity tracks:** [Data quality and observability](../../maturity/track-data-quality.md) (from level 4, Measured)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 4 – Completeness · [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 11 Data Quality Measurement (Data lifecycle) · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Quality · [DCAM v3](../../frameworks/framework-edm-dcam.md): 5 Data Quality Management · [ISO 8000 (data quality)](../../frameworks/framework-iso-8000.md): ISO 8000-8 – Concepts and measuring; ISO 8000-61 – Data quality management process reference model; ISO 8000-62 to 8000-65 – Process maturity assessment and measurement; ISO 8000-130 and 8000-140 – Accuracy and completeness

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Purview Data Quality](../../technologies/microsoft/purview-data-quality.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Knowledge Catalog data quality](../../technologies/google-cloud/gcp-knowledge-catalog-data-quality.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake data quality monitoring (data metric functions)](../../technologies/snowflake/snowflake-data-quality-monitoring.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Cloud Data Governance and Catalog (CDGC)](../../technologies/informatica/informatica-cloud-data-governance-and-catalog.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Data quality in IBM watsonx.data intelligence](../../technologies/ibm/ibm-watsonx-data-intelligence-quality.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Collibra Data Quality & Observability](../../technologies/independent/collibra-data-quality-observability.md), [Experian Aperture Data Studio](../../technologies/independent/experian-aperture-data-studio.md), [GX Cloud](../../technologies/independent/gx-cloud.md) |
