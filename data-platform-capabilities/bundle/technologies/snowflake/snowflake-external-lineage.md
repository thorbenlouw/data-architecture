---
type: Technology
id: snowflake-external-lineage
title: Snowflake external lineage
description: Accepts OpenLineage COMPLETE events through a REST endpoint, so tools such as dbt and Airflow can add lineage from outside Snowflake to the lineage graph.
platform: platform-snowflake
kind: feature
availability: ga
realises: [cross-system-lineage, metadata-interoperability]
resource: https://docs.snowflake.com/en/user-guide/external-lineage
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA since September 2026. Requires Enterprise Edition. OpenLineage version 2 is not supported.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) (Metadata and discovery) (primary): Stitch lineage across ingestion tools, platforms and BI tools into one connected view.
- [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) (Metadata and discovery): Exchange metadata between tools through open APIs and standards.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake Horizon Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog data lineage](../aws/aws-sagemaker-catalog-lineage.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data lineage in Microsoft Purview](../microsoft/purview-lineage.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data lineage](../google-cloud/gcp-knowledge-catalog-data-lineage.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog data lineage](../databricks/databricks-unity-catalog-lineage.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica CDGC lineage](../informatica/informatica-cdgc-lineage.md), [Informatica Data 360 Connector and Scanner](../informatica/informatica-data-360-connector-and-scanner.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Lineage](../cloudera/cloudera-data-lineage.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Manta Data Lineage](../ibm/ibm-manta-data-lineage.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenLineage](../open-source/openlineage.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Lineage](../independent/collibra-data-lineage.md), [Solidatus](../independent/solidatus.md), [Bigeye AI Trust Platform](../independent/bigeye.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) |
