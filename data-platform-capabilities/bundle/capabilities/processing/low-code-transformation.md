---
type: Capability
id: low-code-transformation
title: Low-code transformation
description: Build transformation logic visually from configurable components rather than writing code.
aliases: [visual ETL, no-code pipelines, mapping designer]
broader: [processing]
related: [data-preparation, sql-transformation, platform-migration, application-integration]
tags: [processing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Users assemble pipelines on a canvas from components such as source, filter, join, aggregate, lookup and target, each configured through forms. The tool turns the resulting graph into SQL, Spark code or instructions for its own runtime. For example, an integration developer drags in a CRM extract, joins it to a price list, maps fields to a target schema and schedules the flow without writing a query.

It lowers the skill needed and makes simple flows quick to build and easy for non-programmers to read. It is common in traditional ETL suites and integration teams. The cost shows with complex logic, which becomes a tangle of boxes, and with code review, comparison of versions, testing and reuse, which are all harder than with text-based code. Tools that generate readable code stored in Git narrow the gap. Self-service data preparation is related but different: it serves analysts shaping data for their own analysis, not developers building governed production pipelines.

# Key considerations

- Check whether pipelines are saved as text that Git can compare and merge, or as objects that only the tool can read.
- Generated code can be inefficient. Inspect what actually runs on the engine for large joins.
- Proprietary components create lock-in. Moving hundreds of visual jobs to another tool later is slow, and translation tools only partly help.
- Confirm that parameters, lineage and promotion between environments work as well as they do for code-based pipelines.

# Questions to ask

- Who will build and maintain these pipelines, and can they write SQL or Python?
- Is the typical job field mapping and joins, or multi-step business logic?
- How will visual pipelines be versioned, reviewed and promoted between environments?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Processing and transformation](processing.md) |
| Broader | [Processing and transformation](processing.md) |
| Related | [Application integration](../ingestion-integration/application-integration.md), [Code and SQL translation](../platform-operations/code-translation.md), [Platform migration](../platform-operations/platform-migration.md), [Self-service data preparation](data-preparation.md), [SQL transformation](sql-transformation.md) |

# Where it appears

- **Patterns:** [ETL](../../patterns/etl.md)
- **Maturity tracks:** [Transformation engineering](../../maturity/track-transformation.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Glue ETL](../../technologies/aws/aws-glue-etl.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Dataflow Gen2 (Power Query) | [Azure Data Factory](../../technologies/microsoft/azure-data-factory.md), [Fabric Dataflow Gen2](../../technologies/microsoft/fabric-dataflow-gen2.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery data preparation](../../technologies/google-cloud/gcp-bigquery-data-preparation.md) (preview), [Cloud Data Fusion](../../technologies/google-cloud/gcp-data-fusion.md), [Dataflow templates](../../technologies/google-cloud/gcp-dataflow-templates.md) |
| [Databricks](../../platforms/platform-databricks.md) | Lakeflow Designer | [Lakeflow Designer](../../technologies/databricks/databricks-lakeflow-designer.md) |
| [Informatica](../../platforms/platform-informatica.md) | mappings (Mapping Designer) | [Informatica Cloud Data Integration (CDI)](../../technologies/informatica/informatica-cloud-data-integration.md), [Informatica Cloud Data Integration for PowerCenter (CDI-PC)](../../technologies/informatica/informatica-cdi-pc.md), [Informatica Cloud Data Integration SQL ELT mode](../../technologies/informatica/informatica-cdi-sql-elt-mode.md), [Informatica PowerCenter](../../technologies/informatica/informatica-powercenter.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | Flow Designer (NiFi) | [Cloudera Data Flow](../../technologies/cloudera/cloudera-data-flow.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Data Integration](../../technologies/oracle/oracle-oci-data-integration.md) |
| [SAP](../../platforms/platform-sap.md) | Data flows / transformation flows | [SAP Datasphere](../../technologies/sap/sap-datasphere.md), [SAP Data Intelligence Cloud](../../technologies/sap/sap-data-intelligence-cloud.md) (deprecated) |
| [IBM](../../platforms/platform-ibm.md) | DataStage flows | [IBM watsonx.data integration](../../technologies/ibm/ibm-watsonx-data-integration.md) |
| [Palantir](../../platforms/platform-palantir.md) | Pipeline Builder | [Palantir Pipeline Builder](../../technologies/palantir/palantir-pipeline-builder.md) |
| [SAS](../../platforms/platform-sas.md) | Flows | [SAS Data and AI Studio](../../technologies/sas/sas-data-and-ai-studio.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | Visual recipes | [Dataiku Flow and visual recipes](../../technologies/dataiku/dataiku-flow-visual-recipes.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache NiFi](../../technologies/open-source/apache-nifi.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Alteryx One](../../technologies/independent/alteryx-one.md), [Coalesce Transform](../../technologies/independent/coalesce-transform.md), [Domo](../../technologies/independent/domo.md), [Matillion Maia Foundation](../../technologies/independent/matillion-maia-foundation.md), [Qlik Talend Cloud](../../technologies/independent/qlik-talend-cloud.md) |
