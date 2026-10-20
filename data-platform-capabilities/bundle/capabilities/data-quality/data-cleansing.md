---
type: Capability
id: data-cleansing
title: Data cleansing and standardisation
description: Correct and standardise data values such as addresses, names, dates and codes.
broader: [data-quality]
related:
- entity-resolution
- reference-data-management
- data-enrichment
- data-preparation
- master-data-management
tags: [data-quality]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Typical operations are trimming and normalising case and spacing; parsing a single address field into street, town and postcode; validating addresses against postal reference files; converting dates and phone numbers to standard formats; and mapping free-text entries such as U.K., UK and United Kingdom to one ISO country code. Missing values may be filled from trusted reference data.

Cleansing matters before matching and mastering, where small differences stop records from being linked, and in any report that groups by a messy field. It can be applied at the source, in pipelines or in a master data hub. Fixing at the source is best because every consumer benefits, but it is often outside the data team's control. Because cleansing changes values, keep the original next to the corrected one. Cleansing differs from validation rules, which detect problems, and from enrichment, which adds new attributes.

# Key considerations

- Keep original values beside cleansed ones so corrections can be audited and reversed.
- Feed recurring problems back to source owners. Cleansing the same errors in every load treats the symptom only.
- Address and name standardisation depends on country-specific reference data and rules. Check coverage for the markets you serve.
- Automated fixes can be wrong. Set confidence thresholds and route uncertain cases to people.

# Questions to ask

- Which fields cause the most matching or reporting errors today?
- Can source systems be changed to capture data correctly at entry?
- Which countries and languages must address and name handling support?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data quality and observability](data-quality.md) |
| Broader | [Data quality and observability](data-quality.md) |
| Related | [Master and reference data](../master-data/master-data.md), [Data enrichment](../processing/data-enrichment.md), [Entity resolution](../master-data/entity-resolution.md), [Master data management](../master-data/master-data-management.md), [Merge and survivorship](../master-data/survivorship.md), [Reference data management](../master-data/reference-data-management.md), [Self-service data preparation](../processing/data-preparation.md) |
| Needed by | [Entity resolution](../master-data/entity-resolution.md), [Master data management](../master-data/master-data-management.md) |

# Where it appears

- **Use cases:** [Customer 360](../../use-cases/usecase-customer-360.md) (requires, level 3)
- **Patterns:** [ETL](../../patterns/etl.md)
- **Maturity tracks:** [Data quality and observability](../../maturity/track-data-quality.md) (from level 3, Defined)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Quality · [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 10 – Data and data governance · [GDPR](../../frameworks/framework-gdpr.md): Article 5(1)(d) – Accuracy · [ISO 8000 (data quality)](../../frameworks/framework-iso-8000.md): ISO 8000-61 – Data quality management process reference model; ISO 8000-210 to 8000-230 – Sensor data

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Glue DataBrew](../../technologies/aws/aws-glue-databrew.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery data preparation](../../technologies/google-cloud/gcp-bigquery-data-preparation.md) (preview) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Cloud Data Quality (CDQ)](../../technologies/informatica/informatica-cloud-data-quality.md) |
| [SAS](../../platforms/platform-sas.md) | Quality Knowledge Base | [SAS Data Accelerator](../../technologies/sas/sas-data-accelerator.md), [SAS Data Engineering](../../technologies/sas/sas-data-engineering.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku Flow and visual recipes](../../technologies/dataiku/dataiku-flow-visual-recipes.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Ataccama ONE](../../technologies/independent/ataccama-one.md), [Experian Aperture Data Studio](../../technologies/independent/experian-aperture-data-studio.md), [Precisely Data Integrity Suite](../../technologies/independent/precisely-data-integrity-suite.md), [Tamr](../../technologies/independent/tamr.md) |
