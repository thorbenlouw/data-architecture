---
type: Technology
id: solidatus
title: Solidatus
description: Lineage modelling tool that combines automatically harvested technical lineage with business process lineage in versioned, bi-temporal models.
platform: platform-independent
vendor: Solidatus
kind: saas
availability: ga
realises: [cross-system-lineage, impact-analysis, compliance-evidence, data-ownership]
resource: https://www.solidatus.com/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Often used by banks for regulatory traceability (for example BCBS 239), from risk reports back to source systems. It has an AI lineage assistant, a Microsoft Purview integration and OpenLineage support. Citi is a strategic investor.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) (Metadata and discovery) (primary): Stitch lineage across ingestion tools, platforms and BI tools into one connected view.
- [Impact analysis](../../capabilities/metadata/impact-analysis.md) (Metadata and discovery): Use lineage to find everything affected by a proposed change or a data incident.
- [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) (Governance and compliance): Map regulatory requirements to platform controls and produce evidence for auditors.
- [Ownership and stewardship](../../capabilities/governance/data-ownership.md) (Governance and compliance): Assign accountable owners and stewards to data and record their responsibilities.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog data lineage](../aws/aws-sagemaker-catalog-lineage.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data lineage in Microsoft Purview](../microsoft/purview-lineage.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data lineage](../google-cloud/gcp-knowledge-catalog-data-lineage.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake external lineage](../snowflake/snowflake-external-lineage.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog data lineage](../databricks/databricks-unity-catalog-lineage.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica CDGC lineage](../informatica/informatica-cdgc-lineage.md), [Informatica Data 360 Connector and Scanner](../informatica/informatica-data-360-connector-and-scanner.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Lineage](../cloudera/cloudera-data-lineage.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Manta Data Lineage](../ibm/ibm-manta-data-lineage.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenLineage](../open-source/openlineage.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) |
