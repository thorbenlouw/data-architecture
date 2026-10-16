---
type: Technology
id: palantir-data-health
title: Palantir Data Health and data expectations
description: Health checks on datasets and builds for freshness, schema, row counts and content, plus expectations declared in pipelines that fail or warn when data breaks rules.
platform: platform-palantir
kind: feature
availability: ga
realises: [data-observability, data-quality-rules, freshness-monitoring, pipeline-monitoring]
resource: https://www.palantir.com/docs/foundry/data-integration/overview/
tags: [palantir]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Checks raise issues and notify owners; expectations are defined in Pipeline Builder or transform code. Recommended checks can be applied in bulk.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data observability](../../capabilities/data-quality/data-observability.md) (Data quality and observability) (primary): Monitor data in production for freshness, volume, schema and distribution problems, and alert owners.
- [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) (Data quality and observability): Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency.
- [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) (Data quality and observability): Detect when data arrives later than expected or misses its freshness target.
- [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md) (Platform operations): Track pipeline runs, failures and durations, and alert the right people.

**Platform:** [Palantir](../../platforms/platform-palantir.md)  
**Availability:** ga  
**Product family:** Palantir Foundry

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data quality](../google-cloud/gcp-knowledge-catalog-data-quality.md) | [Data observability](../../capabilities/data-quality/data-observability.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica data observability](../informatica/informatica-data-observability.md) | [Data observability](../../capabilities/data-quality/data-observability.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
| [IBM](../../platforms/platform-ibm.md) | [Data observability in IBM watsonx.data integration](../ibm/ibm-data-observability.md) | [Data observability](../../capabilities/data-quality/data-observability.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md), [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Monte Carlo Data + AI Observability](../independent/monte-carlo-data-observability.md), [Bigeye AI Trust Platform](../independent/bigeye.md), [Sifflet](../independent/sifflet.md) | [Data observability](../../capabilities/data-quality/data-observability.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
