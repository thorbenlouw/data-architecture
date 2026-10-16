---
type: Capability
id: data-profiling
title: Data profiling
description: Analyse data to understand its structure, distributions, completeness and anomalies.
broader: [data-quality]
related:
- data-anomaly-detection
- data-classification
- data-preparation
- metadata-harvesting
- platform-migration
tags: [data-quality]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Profiling scans a dataset and reports, for each column, the data type, share of nulls, number of distinct values, minimum and maximum, most frequent values, and length and pattern distributions; for tables, it suggests candidate keys and relationships with other tables. Profiling a supplier table might show that 12% of postcodes are blank, that a country column mixes codes and full names, and that supplier ID is unique apart from 40 duplicates.

It is the first step when taking on a new source, planning a migration, writing quality rules or designing a model, because it replaces assumptions with evidence. It can run once on demand, on a sample for speed, or continuously, storing statistics over time so that changes become visible. Continuous profiling is the base for learned anomaly detection. Profiling describes data; quality rules judge it against requirements.

# Key considerations

- Sampling is fast but misses rare values and duplicates. Profile full data when checking keys and edge cases.
- Profiles expose sensitive values, such as the most frequent names or card numbers. Apply the same access controls as the data and mask outputs.
- Keep profiles over time rather than discarding them. The history is what makes drift and anomaly detection possible.
- Use profiles to suggest candidate rules, then have owners confirm them, rather than accepting every generated rule.

# Questions to ask

- How well do teams understand new sources before building on them?
- Are profiles needed once, for migration or design, or continuously?
- Who may see profile results that include sample values?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data quality and observability](data-quality.md) |
| Broader | [Data quality and observability](data-quality.md) |
| Related | [Data anomaly detection](data-anomaly-detection.md), [Data classification](../governance/data-classification.md), [Drift detection](../mlops/drift-detection.md), [Metadata harvesting](../metadata/metadata-harvesting.md), [Platform migration](../platform-operations/platform-migration.md), [Self-service data preparation](../processing/data-preparation.md) |
| Needed by | [Data anomaly detection](data-anomaly-detection.md), [Data classification](../governance/data-classification.md), [Self-service data preparation](../processing/data-preparation.md) |

# Where it appears

- **Personas:** [Data scientist](../../personas/persona-data-scientist.md) · [Data steward](../../personas/persona-data-steward.md)
- **Maturity tracks:** [Data quality and observability](../../maturity/track-data-quality.md) (from level 2, Managed)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Quality · [DCAM v3](../../frameworks/framework-edm-dcam.md): 5 Data Quality Management · [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 10 – Data and data governance · [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Data validation · [ISO 8000 (data quality)](../../frameworks/framework-iso-8000.md): ISO 8000-8 – Concepts and measuring; ISO/TS 8000-81 – Data profiling; ISO/CD TR 8000-320 – AI training data quality (in development) · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Annex A.7 – Data for AI systems

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Glue Data Quality](../../technologies/aws/aws-glue-data-quality.md), [AWS Glue DataBrew](../../technologies/aws/aws-glue-databrew.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Purview Data Quality](../../technologies/microsoft/purview-data-quality.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Knowledge Catalog data profiling](../../technologies/google-cloud/gcp-knowledge-catalog-data-profiling.md) |
| [Databricks](../../platforms/platform-databricks.md) | Data profiling (formerly Lakehouse Monitoring) | [Databricks data profiling](../../technologies/databricks/databricks-data-profiling.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Data Profiling](../../technologies/informatica/informatica-data-profiling.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Catalog](../../technologies/cloudera/cloudera-data-catalog.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Data quality in IBM watsonx.data intelligence](../../technologies/ibm/ibm-watsonx-data-intelligence-quality.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Evidently](../../technologies/open-source/evidently.md), [GX Core (Great Expectations)](../../technologies/open-source/great-expectations.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Ataccama ONE](../../technologies/independent/ataccama-one.md), [Collibra Data Quality & Observability](../../technologies/independent/collibra-data-quality-observability.md), [Experian Aperture Data Studio](../../technologies/independent/experian-aperture-data-studio.md), [GX Cloud](../../technologies/independent/gx-cloud.md) |
