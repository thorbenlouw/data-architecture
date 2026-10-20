---
type: Technology
id: marquez
title: Marquez
description: Metadata service that collects OpenLineage events and shows dataset and job lineage and run history through an API and web UI.
platform: platform-open-source
kind: open-source
availability: ga
realises: [table-lineage, pipeline-monitoring]
resource: https://marquezproject.ai/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, an LF AI & Data project and the reference implementation of OpenLineage. Lighter than a full catalogue; often used for development or as a lineage back end.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Table-level lineage](../../capabilities/metadata/table-lineage.md) (Metadata and discovery) (primary): Track dependencies between datasets, tables and views.
- [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md) (Platform operations): Track pipeline runs, failures and durations, and alert the right people.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog data lineage](../aws/aws-sagemaker-catalog-lineage.md) | [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data lineage in Microsoft Purview](../microsoft/purview-lineage.md), [Fabric materialized lake views](../microsoft/fabric-materialized-lake-views.md) | [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data lineage](../google-cloud/gcp-knowledge-catalog-data-lineage.md) | [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake data lineage (Snowsight lineage)](../snowflake/snowflake-data-lineage.md) | [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog data lineage](../databricks/databricks-unity-catalog-lineage.md) | [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica CDGC lineage](../informatica/informatica-cdgc-lineage.md) | [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Lineage](../palantir/palantir-data-lineage.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Lineage](../independent/collibra-data-lineage.md), [dbt Catalog](../independent/dbt-catalog.md) | [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
