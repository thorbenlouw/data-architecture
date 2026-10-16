---
type: Technology
id: informatica-data-observability
title: Informatica data observability
description: Learns normal trends in scanned source data, raises events for sudden deviations, grouped by metric and severity, and improves its alerts from how users respond to them.
platform: platform-informatica
kind: feature
availability: ga
realises: [data-observability, data-anomaly-detection, freshness-monitoring]
resource: https://onlinehelp.informatica.com/IICS/prod/DGC/en/af-data-quality/Data_observability.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

It is enabled per catalog source in [Metadata Command Center](informatica-metadata-command-center.md), and its events are reviewed in [Cloud Data Governance and Catalog](informatica-cloud-data-governance-and-catalog.md). Informatica describes it as covering freshness, volume, distribution and schema changes.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data observability](../../capabilities/data-quality/data-observability.md) (Data quality and observability) (primary): Monitor data in production for freshness, volume, schema and distribution problems, and alert owners.
- [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md) (Data quality and observability): Learn normal patterns in data and alert on unexpected changes without hand-written rules.
- [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) (Data quality and observability): Detect when data arrives later than expected or misses its freshness target.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud, Informatica Data Quality and Observability, Cloud Data Governance and Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data quality](../google-cloud/gcp-knowledge-catalog-data-quality.md) | [Data observability](../../capabilities/data-quality/data-observability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake data quality monitoring (data metric functions)](../snowflake/snowflake-data-quality-monitoring.md) | [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks data quality monitoring anomaly detection](../databricks/databricks-dqm-anomaly-detection.md) (preview) | [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
| [IBM](../../platforms/platform-ibm.md) | [Data observability in IBM watsonx.data integration](../ibm/ibm-data-observability.md) | [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md), [Data observability](../../capabilities/data-quality/data-observability.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Health and data expectations](../palantir/palantir-data-health.md) | [Data observability](../../capabilities/data-quality/data-observability.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Monte Carlo Data + AI Observability](../independent/monte-carlo-data-observability.md), [Bigeye AI Trust Platform](../independent/bigeye.md), [Sifflet](../independent/sifflet.md) | [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md), [Data observability](../../capabilities/data-quality/data-observability.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
