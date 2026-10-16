---
type: Technology
id: sap-databricks
title: SAP Databricks
description: SAP-sold and SAP-managed Databricks workspace embedded in BDC, for notebooks, Spark pipelines, serverless SQL and ML over SAP data products shared with Delta Sharing.
platform: platform-sap
kind: managed-service
availability: ga
realises: [distributed-processing, notebooks, model-training, ad-hoc-analysis, internal-data-sharing]
distribution_of: platform-databricks
resource: https://www.sap.com/products/data-cloud/databricks.html
tags: [sap]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Generally available since 2025. It is a scoped Databricks offering inside the BDC tenant; customers with an existing Databricks estate typically use BDC Connect for Databricks instead.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Distributed processing](../../capabilities/processing/distributed-processing.md) (Processing and transformation) (primary): Process large datasets in parallel across a cluster of machines.
- [Notebooks](../../capabilities/development-lifecycle/notebooks.md) (Development and DataOps): Develop interactively with code, results and narrative together, with collaboration and scheduling.
- [Model training](../../capabilities/machine-learning/model-training.md) (Machine learning development): Train models on platform data at the scale required, from single machines to GPU clusters.
- [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) (Analytics and BI): Explore data freely with SQL editors, pivots and visual exploration to answer one-off questions.
- [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) (Data sharing and collaboration): Share live data between teams, accounts and workspaces without copying it.

**Platform:** [SAP](../../platforms/platform-sap.md)  
**Availability:** ga  
**Product family:** SAP Business Data Cloud  
**Distribution of:** [Databricks](../../platforms/platform-databricks.md). It is not counted in SAP's coverage.
