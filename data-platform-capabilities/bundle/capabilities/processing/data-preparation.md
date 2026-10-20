---
type: Capability
id: data-preparation
title: Self-service data preparation
description: Let analysts profile, clean and reshape data interactively without engineering help.
aliases: [data wrangling, Power Query]
broader: [processing, analytics-bi]
related: [data-cleansing, low-code-transformation, ad-hoc-analysis, spreadsheet-integration]
depends_on: [data-profiling]
tags: [processing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Preparation tools show a sample of a dataset in a spreadsheet-like grid with a profile of each column, and let an analyst apply steps such as split, trim, pivot, fill missing values or standardise dates. Each step is saved in a recipe that can be rerun on the full dataset or on fresh data. Many tools suggest steps from patterns they detect, for example offering to parse a text column that holds dates in two formats.

This serves analysts who need data shaped for a particular question and cannot wait for an engineering backlog. It shortens the time to an answer, but creates risk when personal recipes quietly become production pipelines with no tests, owner or lineage. Better tools let a proven recipe be promoted into a governed pipeline. Compared with low-code transformation, preparation is exploratory and usually works on samples. Compared with data cleansing, it is ad hoc rather than a set of standard rules applied across the organisation.

# Key considerations

- Decide where prepared outputs may be written and who may share them, or uncontrolled copies multiply.
- Recipes built on samples miss edge cases that appear only in the full data. Validate on the full set before relying on results.
- Provide a route to promote a recipe into a governed pipeline with an owner and tests.
- Some tools pull data into their own engine. Make sure the platform's access controls and masking still apply there.

# Questions to ask

- How many analysts reshape data themselves today, and with which tools?
- What happens when a prepared dataset becomes important to other people?
- Must prepared data stay inside the platform, or may it be exported to desktops?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Processing and transformation](processing.md) |
| Broader | [Processing and transformation](processing.md), [Analytics and BI](../analytics-bi/analytics-bi.md) |
| Related | [Ad hoc analysis](../analytics-bi/ad-hoc-analysis.md), [Analytical sandboxes](../analytics-bi/analytical-sandboxes.md), [Data cleansing and standardisation](../data-quality/data-cleansing.md), [Data profiling](../data-quality/data-profiling.md), [Low-code transformation](low-code-transformation.md), [Spreadsheet integration](../analytics-bi/spreadsheet-integration.md) |
| Depends on | [Data profiling](../data-quality/data-profiling.md) |

# Where it appears

- **Use cases:** [Self-service BI](../../use-cases/usecase-self-service-bi.md) (benefits from)
- **Personas:** [Data analyst](../../personas/persona-data-analyst.md)
- **Maturity tracks:** [Transformation engineering](../../maturity/track-transformation.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Canvas](../../technologies/aws/aws-sagemaker-canvas.md), [AWS Glue DataBrew](../../technologies/aws/aws-glue-databrew.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric Dataflow Gen2](../../technologies/microsoft/fabric-dataflow-gen2.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery data preparation](../../technologies/google-cloud/gcp-bigquery-data-preparation.md) (preview), [Cloud Data Fusion](../../technologies/google-cloud/gcp-data-fusion.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Lakeflow Designer](../../technologies/databricks/databricks-lakeflow-designer.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Analytics Cloud](../../technologies/oracle/oracle-analytics-cloud.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Contour and Quiver](../../technologies/palantir/palantir-contour-quiver.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS Data Engineering](../../technologies/sas/sas-data-engineering.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | Prepare recipe | [Dataiku Flow and visual recipes](../../technologies/dataiku/dataiku-flow-visual-recipes.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [pandas](../../technologies/open-source/pandas.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Alteryx One](../../technologies/independent/alteryx-one.md), [Tableau Cloud](../../technologies/independent/tableau-cloud.md), [ThoughtSpot Analyst Studio](../../technologies/independent/thoughtspot-analyst-studio.md) |
