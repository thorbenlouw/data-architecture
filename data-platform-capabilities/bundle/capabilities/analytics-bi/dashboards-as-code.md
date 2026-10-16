---
type: Capability
id: dashboards-as-code
title: Dashboards as code
description: Define dashboards in version-controlled files that are reviewed and tested alongside the models they use.
aliases: [BI as code]
broader: [dashboards-reports]
related: [transformation-as-code, ci-cd, environment-promotion, impact-analysis, data-testing]
depends_on: [version-control]
tags: [analytics-bi]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

With dashboards as code, each dashboard's queries, charts, layout and filters are held as text files, usually YAML, JSON, Markdown or a small domain language, in a Git repository. Changes go through pull requests, a CI pipeline checks that every referenced column and metric exists, and deployment publishes the dashboard to each environment. If a model change renames a column, the build fails before a broken dashboard reaches users.

It suits teams that already manage transformations as code and want BI to follow the same review, testing and promotion. Dashboards become reproducible across environments and easy to restore. The trade-off is that business users who build by dragging and dropping are left out unless the tool keeps visual editing and files in step. Some tools generate files from visual edits; others are code-first. Exporting a dashboard definition is not the same thing: it gives a backup, but not reviewed and tested change.

# Key considerations

- Check whether visual edits and file edits stay in sync, or whether one silently overwrites the other.
- Run tests against the real models, so an upstream schema change fails the dashboard build rather than the live dashboard.
- Keep environment-specific settings, such as connections and schema names, out of dashboard files so the same file promotes unchanged.
- Code-first tools suit engineers and analysts. Plan how business users will request or make changes.

# Questions to ask

- Do dashboards break after upstream changes, and does that cause incidents today?
- Who builds dashboards: engineers and analysts comfortable with Git, or business users?
- Must dashboards pass through test environments for audit or regulatory reasons?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Analytics and BI](analytics-bi.md) |
| Broader | [Dashboards and interactive reports](dashboards-reports.md) |
| Related | [CI/CD](../development-lifecycle/ci-cd.md), [Data pipeline testing](../development-lifecycle/data-testing.md), [Environment promotion](../development-lifecycle/environment-promotion.md), [Impact analysis](../metadata/impact-analysis.md), [Transformation as code](../processing/transformation-as-code.md), [Version control integration](../development-lifecycle/version-control.md) |
| Depends on | [Version control integration](../development-lifecycle/version-control.md) |

# Where it appears

- **Use cases:** [Customer-facing analytics](../../use-cases/usecase-customer-facing-analytics.md) (benefits from)
- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md)
- **Maturity tracks:** [Analytics and BI](../../maturity/track-analytics-bi.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Power BI reports and dashboards](../../technologies/microsoft/powerbi-reports.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [LookML](../../technologies/google-cloud/gcp-lookml.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks AI/BI dashboards](../../technologies/databricks/databricks-ai-bi-dashboards.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Lightdash](../../technologies/open-source/lightdash.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [dbt Charts](../../technologies/independent/dbt-charts.md) (unconfirmed) |
