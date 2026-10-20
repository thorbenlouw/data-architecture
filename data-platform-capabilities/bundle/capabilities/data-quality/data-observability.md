---
type: Capability
id: data-observability
title: Data observability
description: Monitor data in production for freshness, volume, schema and distribution problems, and alert owners.
broader: [data-quality]
related: [pipeline-monitoring, impact-analysis, data-lineage, data-issue-management, active-metadata]
depends_on: [metadata-harvesting]
tags: [data-quality]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

For each monitored table, an observability tool tracks a few standard signals: freshness (when it last updated), volume (rows per load), schema (columns added, removed or retyped), distributions (null rates, ranges, value frequencies) and lineage. If a nightly load arrives with 40% fewer rows than usual and one column has turned null, the owner gets an alert, and lineage shows which downstream reports are affected.

It matters because rules catch only the problems someone anticipated, and many failures come from upstream changes nobody announced. Tools collect metadata and statistics broadly, often from query logs and system tables rather than full scans, to keep costs down. Observability differs from pipeline monitoring, which reports whether jobs succeeded; a job can succeed while loading wrong or partial data. Its alerts feed incident management, impact analysis and service level reporting.

# Key considerations

- Broad, shallow coverage often finds more than deep checks on a few tables. Start with freshness, volume and schema on everything important.
- Alert fatigue kills adoption. Route alerts to named owners, group related alerts into one incident, and tune sensitivity.
- Check how monitoring reads data. Metadata and query logs are cheap; distribution checks may scan tables and cost compute.
- Without lineage, alerts lack context. Pair monitoring with lineage so owners can see causes upstream and impact downstream.

# Questions to ask

- How do you find out about data problems today, and how long after they start?
- Which tables and products would cause the most harm if wrong or late?
- Who receives and acts on data alerts, and during which hours?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data quality and observability](data-quality.md) |
| Broader | [Data quality and observability](data-quality.md) |
| Narrower | [Data anomaly detection](data-anomaly-detection.md), [Freshness monitoring](freshness-monitoring.md) |
| Related | [Data products](../data-products/data-products.md), [Development and DataOps](../development-lifecycle/development-lifecycle.md), [Active metadata](../metadata/active-metadata.md), [Data issue management](data-issue-management.md), [Data lineage](../metadata/data-lineage.md), [Data service levels](../data-products/data-slas.md), [Impact analysis](../metadata/impact-analysis.md), [Model monitoring](../mlops/model-monitoring.md), [Pipeline monitoring and alerting](../platform-operations/pipeline-monitoring.md), [Platform observability](../platform-operations/platform-observability.md) |
| Depends on | [Metadata harvesting](../metadata/metadata-harvesting.md) |

# Where it appears

- **Maturity tracks:** [Data quality and observability](../../maturity/track-data-quality.md) (from level 3, Defined)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 11 Data Quality Measurement (Data lifecycle) · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Quality · [DCAM v3](../../frameworks/framework-edm-dcam.md): 5 Data Quality Management · [ISO 8000 (data quality)](../../frameworks/framework-iso-8000.md): ISO 8000-61 – Data quality management process reference model · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Data Quality · [Open Data Product Standard (ODPS)](../../frameworks/framework-bitol-odps.md): Management Ports

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Knowledge Catalog data quality](../../technologies/google-cloud/gcp-knowledge-catalog-data-quality.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica data observability](../../technologies/informatica/informatica-data-observability.md) |
| [IBM](../../platforms/platform-ibm.md) | Data observability (Databand) | [Data observability in IBM watsonx.data integration](../../technologies/ibm/ibm-data-observability.md) |
| [Palantir](../../platforms/platform-palantir.md) | Data Health | [Palantir Data Health and data expectations](../../technologies/palantir/palantir-data-health.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Anomalo](../../technologies/independent/anomalo.md), [Ataccama ONE](../../technologies/independent/ataccama-one.md), [Bigeye AI Trust Platform](../../technologies/independent/bigeye.md), [Collibra Data Quality & Observability](../../technologies/independent/collibra-data-quality-observability.md), [DataHub Cloud](../../technologies/independent/datahub-cloud.md), [Monte Carlo Data + AI Observability](../../technologies/independent/monte-carlo-data-observability.md), [Precisely Data Integrity Suite](../../technologies/independent/precisely-data-integrity-suite.md), [Secoda](../../technologies/independent/secoda.md), [Sifflet](../../technologies/independent/sifflet.md), [Soda Cloud](../../technologies/independent/soda-cloud.md) |

Narrower capabilities are realised by a further 17 technologies; see their pages.
