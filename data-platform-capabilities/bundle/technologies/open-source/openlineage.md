---
type: Technology
id: openlineage
title: OpenLineage
description: Open specification and client libraries for emitting lineage events about jobs, runs and datasets, with extensible facets such as column-level lineage.
platform: platform-open-source
kind: open-standard
availability: ga
realises: [metadata-interoperability, cross-system-lineage, column-lineage]
resource: https://openlineage.io/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, an LF AI & Data project. Integrations exist for Spark, Airflow (provider package), Flink, dbt and others, and many catalogues (DataHub, OpenMetadata, Marquez, and commercial ones) consume its events.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) (Metadata and discovery) (primary): Exchange metadata between tools through open APIs and standards.
- [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) (Metadata and discovery): Stitch lineage across ingestion tools, platforms and BI tools into one connected view.
- [Column-level lineage](../../capabilities/metadata/column-lineage.md) (Metadata and discovery): Track how each column is derived from source columns.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog data lineage](../aws/aws-sagemaker-catalog-lineage.md), [AWS Glue Data Catalog](../aws/aws-glue-data-catalog.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Data Map](../microsoft/purview-data-map.md), [Data lineage in Microsoft Purview](../microsoft/purview-lineage.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data lineage](../google-cloud/gcp-knowledge-catalog-data-lineage.md), [Google Cloud Lakehouse runtime catalog](../google-cloud/gcp-lakehouse-runtime-catalog.md), [Knowledge Catalog](../google-cloud/gcp-knowledge-catalog.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake external lineage](../snowflake/snowflake-external-lineage.md), [Snowflake Horizon Iceberg REST Catalog API](../snowflake/snowflake-horizon-iceberg-rest-catalog.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks catalog federation](../databricks/databricks-catalog-federation.md), [Unity Catalog Iceberg REST Catalog API](../databricks/databricks-iceberg-rest-catalog.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Metadata Command Center (MCC)](../informatica/informatica-metadata-command-center.md), [Informatica CDGC lineage](../informatica/informatica-cdgc-lineage.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Iceberg REST Catalog](../cloudera/cloudera-iceberg-rest-catalog.md), [Cloudera Data Lineage](../cloudera/cloudera-data-lineage.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud Connect](../sap/sap-bdc-connect.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Manta Data Lineage](../ibm/ibm-manta-data-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Atlan](../independent/atlan.md), [Collibra Data Lineage](../independent/collibra-data-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) |
