---
type: Capability
id: data-enrichment
title: Data enrichment
description: Add attributes to records from lookup tables or curated third-party reference data.
aliases: [lookups, dictionaries, third-party enrichment]
broader: [processing]
related: [reference-data-management, entity-resolution, data-cleansing, data-usage-rights, data-marketplace]
tags: [processing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Enrichment adds attributes that the source system never captured. Examples are deriving region and time zone from a postcode, adding a company's industry code and size from a business information dataset, attaching the weather for the date and place of each sale, or assigning customers to segments from a lookup table. It works by joining on shared keys, by matching on names and addresses, by calling an enrichment service, or by using a model to infer an attribute.

It makes data more useful for segmentation, risk assessment and analysis without changing source systems. Results depend on where the reference data comes from, how many records match, and how current the reference set is. Third-party data comes with licence terms that can restrict use, sharing and retention. Enrichment adds new attributes, whereas data cleansing corrects existing ones. When records lack a shared key, enrichment depends on entity resolution; when it uses code lists, it depends on reference data management.

# Key considerations

- Measure and report match rates. Records that fail to match are often the ones that matter most.
- Record the source and version of each enriched attribute so results can be explained and refreshed.
- Check licence terms before using third-party attributes in models, shared data products or exports.
- Enriching at load time makes reads fast; enriching at query time keeps attributes current. Choose per attribute.

# Questions to ask

- Which attributes do analysts or models need that source systems do not hold?
- Is third-party reference data already licensed, and on what terms?
- How often does the reference data change, and must its history be kept?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Processing and transformation](processing.md) |
| Broader | [Processing and transformation](processing.md) |
| Related | [Data cleansing and standardisation](../data-quality/data-cleansing.md), [Data licensing and usage rights](../governance/data-usage-rights.md), [Data marketplace](../data-sharing/data-marketplace.md), [Entity resolution](../master-data/entity-resolution.md), [Geospatial data](../specialised-data/geospatial-data.md), [Reference data management](../master-data/reference-data-management.md) |

# Where it appears

- **Use cases:** [Customer 360](../../use-cases/usecase-customer-360.md) (benefits from) · [Demand forecasting](../../use-cases/usecase-demand-forecasting.md) (benefits from) · [Marketing audience activation](../../use-cases/usecase-marketing-activation.md) (benefits from) · [Security and log analytics](../../use-cases/usecase-security-log-analytics.md) (requires, level 2)
- **Maturity tracks:** [Transformation engineering](../../maturity/track-transformation.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Stream Analytics](../../technologies/microsoft/azure-stream-analytics.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Dataflow](../../technologies/google-cloud/gcp-dataflow.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse dictionaries](../../technologies/clickhouse/clickhouse-dictionaries.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Cloud Data Quality (CDQ)](../../technologies/informatica/informatica-cloud-data-quality.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Beam](../../technologies/open-source/apache-beam.md), [Apache Druid](../../technologies/open-source/apache-druid.md), [Apache Flink](../../technologies/open-source/apache-flink.md), [Apache NiFi](../../technologies/open-source/apache-nifi.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Experian Aperture Data Studio](../../technologies/independent/experian-aperture-data-studio.md), [Precisely Data Integrity Suite](../../technologies/independent/precisely-data-integrity-suite.md), [Tamr](../../technologies/independent/tamr.md) |
