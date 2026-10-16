---
type: Persona
id: persona-analytics-engineer
title: Analytics engineer
description: Turns raw data into tested, documented, analysis-ready models.
cares_about:
- transformation-as-code
- sql-transformation
- data-modelling
- data-testing
- semantic-layer
- metric-definitions
- incremental-processing
- version-control
- ci-cd
- ephemeral-environments
- environment-promotion
- column-lineage
- impact-analysis
- data-contracts
- data-catalogue
- data-quality-rules
- data-certification
- usage-metadata
- query-performance-analysis
- materialised-views
- zero-copy-cloning
- asset-based-orchestration
- dashboards-as-code
- ai-context-layer
- semantic-model-interchange
patterns: [dimensional-modelling, elt, medallion-architecture, one-big-table, slowly-changing-dimensions]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Analytics engineers sit between data engineering and analysis. They take data that has already been loaded and build the models that analysts and BI tools use: cleaned staging tables, facts and dimensions, wide tables and metric definitions. They mostly write SQL inside a transformation-as-code framework, with Git, code review, tests and CI, and often belong to an analytics or domain team rather than the central platform team.

Success is a set of models that analysts trust and reuse instead of rebuilding, one agreed calculation for each key metric, documentation that answers most questions, and tests that catch errors before a dashboard shows them.

# Goals

- Publish one trusted, documented model for each business concept.
- Keep metric definitions consistent across dashboards, notebooks and AI tools.
- Catch data and logic errors in CI, not in production.
- Keep models fast and affordable to refresh as data grows.

# Jobs

- Model loaded data into staging, intermediate and mart layers in SQL.
- Write tests and documentation for models, and review pull requests.
- Define metrics and semantic models for BI and AI tools.
- Investigate why a number differs between two reports.
- Make slow or costly models incremental or otherwise cheaper to run.
- Deprecate unused models and tell their consumers.
- Build and check each change in its own isolated environment against production data before merging.
- Find which models cost most to refresh and make them incremental or cheaper.

# Pain points

- Metric logic gets copied into BI workbooks, so the same KPI differs between reports.
- Upstream changes break models without warning.
- Full rebuilds become slow and expensive as tables grow.
- It is hard to see which dashboards depend on a model before changing it.
- CI builds of large projects are slow and costly because each change rebuilds models that did not change.

# Questions they ask

- Should metrics be defined in the semantic layer, the BI tool or the transformation layer?
- Dimensional model, wide tables or both for this domain?
- How do we test changes against production-sized data without copying it?
- How do we expose our models to AI assistants so they answer with the same definitions as our dashboards?
- How do we know what each model costs to refresh, and which to make incremental first?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities they rely on most

| Capability | Domain | What it does |
|---|---|---|
| [Transformation as code](../capabilities/processing/transformation-as-code.md) | [Processing and transformation](../capabilities/processing/processing.md) | Define transformations as version-controlled, tested, modular code whose dependencies are resolved automatically. |
| [SQL transformation](../capabilities/processing/sql-transformation.md) | [Processing and transformation](../capabilities/processing/processing.md) | Transform data inside the platform using SQL, typically after it has been loaded. |
| [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | Design and document conceptual, logical and physical data models, and keep them in step with what is deployed. |
| [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | Test transformation logic and data with unit, integration and regression tests before release. |
| [Semantic layer](../capabilities/analytics-bi/semantic-layer.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Define business entities, measures and relationships once so every tool calculates them the same way. |
| [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Define, certify and version key business metrics with owners and calculation logic. |
| [Incremental processing](../capabilities/processing/incremental-processing.md) | [Processing and transformation](../capabilities/processing/processing.md) | Process only new or changed data instead of recomputing everything each run. |
| [Version control integration](../capabilities/development-lifecycle/version-control.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | Keep code and configuration in Git and work with branches from inside the platform. |
| [CI/CD](../capabilities/development-lifecycle/ci-cd.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | Build, test and deploy pipelines, models and infrastructure automatically on every change. |
| [Ephemeral development environments](../capabilities/development-lifecycle/ephemeral-environments.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | Create a short-lived, isolated environment for each developer or change, reusing production data and unchanged objects, and remove it when the work is merged. |
| [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | Promote the same artefacts through development, test and production with environment-specific configuration. |
| [Column-level lineage](../capabilities/metadata/column-lineage.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Track how each column is derived from source columns. |
| [Impact analysis](../capabilities/metadata/impact-analysis.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Use lineage to find everything affected by a proposed change or a data incident. |
| [Data contracts](../capabilities/data-products/data-contracts.md) | [Data products](../capabilities/data-products/data-products.md) | Agree and enforce a dataset's schema, meaning, quality and service levels between producers and consumers. |
| [Data catalogue](../capabilities/metadata/data-catalogue.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Provide a searchable inventory of data assets with descriptions, owners, quality and usage. |
| [Data quality rules](../capabilities/data-quality/data-quality-rules.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency. |
| [Data certification](../capabilities/metadata/data-certification.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Mark assets as trusted, deprecated or under review so consumers know what to rely on. |
| [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Show who uses which data, how often and how, to guide discovery and clean-up. |
| [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Inspect query plans, job stages, run history and bottlenecks to tune performance and cost. |
| [Materialised views](../capabilities/compute/materialised-views.md) | [Query and compute](../capabilities/compute/compute.md) | Have the query engine store a query's result, refresh it as sources change and optionally use it to answer other queries. |
| [Zero-copy cloning](../capabilities/storage/zero-copy-cloning.md) | [Storage and table management](../capabilities/storage/storage.md) | Create an instant copy of a table, schema or database that shares storage with the original until either changes. |
| [Data-aware orchestration](../capabilities/orchestration/asset-based-orchestration.md) | [Orchestration](../capabilities/orchestration/orchestration.md) | Schedule work based on the freshness and dependencies of data assets rather than fixed times. |
| [Dashboards as code](../capabilities/analytics-bi/dashboards-as-code.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Define dashboards in version-controlled files that are reviewed and tested alongside the models they use. |
| [AI context layer](../capabilities/metadata/ai-context-layer.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly. |
| [Semantic model interchange](../capabilities/analytics-bi/semantic-model-interchange.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Exchange semantic models and metric definitions between BI tools, semantic layers and AI tools in a standard format. |

# Patterns

- [Dimensional modelling](../patterns/dimensional-modelling.md)
- [ELT](../patterns/elt.md)
- [Medallion architecture](../patterns/medallion-architecture.md)
- [One big table](../patterns/one-big-table.md)
- [Slowly changing dimensions](../patterns/slowly-changing-dimensions.md)

# Use cases they take part in

- [Application data publishing](../use-cases/usecase-application-data-publishing.md): Application teams publish their data to the platform through versioned events and change capture under agreed contracts, so downstream consumers do not break when applications change.
- [Conversational analytics for business users](../use-cases/usecase-conversational-bi.md): Business users ask questions of governed data in plain language and get trustworthy answers.
- [Customer-facing analytics](../use-cases/usecase-customer-facing-analytics.md): Give external customers fast, secure analytics inside a product.
- [Enterprise management reporting](../use-cases/usecase-enterprise-reporting.md): Produce trusted, consistent KPIs and management reports across the organisation.
- [Legacy warehouse migration](../use-cases/usecase-platform-modernisation.md): Move from an on-premises warehouse or Hadoop estate to a cloud data platform.
- [Marketing audience activation](../use-cases/usecase-marketing-activation.md): Build audiences from platform data and sync them to marketing and advertising tools.
- [Platform cost management and chargeback](../use-cases/usecase-platform-cost-management.md): Attribute, forecast and control what the data platform costs, and recover it from the teams and products that use it.
- [Self-service BI](../use-cases/usecase-self-service-bi.md): Analysts and business users explore governed data and build their own reports with trusted metrics.
- [Self-service domain onboarding](../use-cases/usecase-domain-onboarding.md): Give a new domain or product team a governed workspace, path to live and budget on the shared platform within a day.
